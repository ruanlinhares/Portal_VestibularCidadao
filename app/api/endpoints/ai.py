import os
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
import google.generativeai as genai
import tempfile
import shutil
from PyPDF2 import PdfReader
from app.core.config import settings

router = APIRouter()

genai.configure(api_key=settings.google_api_key)


# @router.post("/upload_pdf")
# async def upload_pdf(file: UploadFile = File(...)):
    
#     print(f"\n[DEBUG 1] Iniciando upload de: {file.filename}")

#     tmp_path: str | None = None
    
#     try:
      
#         await file.seek(0)

#         with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
#             shutil.copyfileobj(file.file, tmp)
#             tmp_path = tmp.name
        
#         print(f"[DEBUG 2] Arquivo temporário salvo em: {tmp_path}")

#     except Exception as e:
#         print(f"[DEBUG ERRO] Falha ao salvar arquivo temporário: {str(e)}")
#         raise HTTPException(status_code=500, detail=f"Erro ao salvar arquivo temporariamente: {str(e)}")

   
#     try:
#         print(f"[DEBUG 3] Abrindo o arquivo temporário para leitura binária e upload...")
        
        
#         uploaded = genai.upload_file(
#             path=tmp_path,
#             display_name=file.filename 
#         )
        
#         print(f"[DEBUG 4] SUCESSO! Upload concluído. File ID: {uploaded.name}")

#         return {
#             "file_id": uploaded.name,
#             "filename": file.filename
#         }
        
#     except Exception as e:
#         print(f"[DEBUG ERRO] FALHA no upload para Gemini: {str(e)}")
#         # Re-lança a exceção para o cliente
#         raise HTTPException(status_code=500, detail=f"Erro ao enviar arquivo: {str(e)}")

#     finally:
#         # 3. GARANTE que o arquivo temporário seja excluído, mesmo se houver erro
#         if tmp_path and os.path.exists(tmp_path):
#             os.remove(tmp_path)
#             print(f"[DEBUG 5] Arquivo temporário removido: {tmp_path}")


# @router.get("/ask")
# async def ask(question: str, file_id: str):
#     try:
#         model = genai.GenerativeModel("gemini-2.0-flash")  # ou "gemini-2.0-flash"

#         prompt = f"Leia o arquivo com ID {file_id} e responda à pergunta: {question}"
#         response = model.generate_content(
#             prompt
#         )

#         return {"answer": response.text}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Erro ao consultar arquivo: {str(e)}")

pdf_texts: dict[str, str] = {} 

def extract_text(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text


@router.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Apenas arquivos PDF são permitidos")

    tmp_path = None
    try:
        # Salva PDF temporariamente
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name

        text = extract_text(tmp_path)

        # Cria ID simples (pode usar UUID para produção)
        file_id = f"{file.filename}_{len(pdf_texts)+1}"
        pdf_texts[file_id] = text

        return {"file_id": file_id, "filename": file.filename}

    finally:
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)

@router.get("/ask")
async def ask(question: str, file_id: str):
    
    if file_id not in pdf_texts:
        raise HTTPException(status_code=404, detail="Arquivo não encontrado")

    text = pdf_texts[file_id]

    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        prompt = f"Use o seguinte texto como base para responder à pergunta:\n\n{text}\n\nPergunta: {question}"

        response = model.generate_content(prompt)

        return {"answer": response.text} 

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao consultar arquivo: {str(e)}")
