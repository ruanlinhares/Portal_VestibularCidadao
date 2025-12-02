import os
from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.core.google_client import client
import tempfile
import shutil
import mimetypes

router = APIRouter()

@router.post("/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    
    print(f"\n[DEBUG 1] Iniciando upload de: {file.filename}")
    mime_type, _ = mimetypes.guess_type(file.filename)
    
    if mime_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Apenas arquivos PDF são permitidos")

    
    tmp_path: str | None = None
    
    # 1. Salva temporariamente
    try:
      
        await file.seek(0)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            shutil.copyfileobj(file.file, tmp)
            tmp_path = tmp.name
        
        print(f"[DEBUG 2] Arquivo temporário salvo em: {tmp_path}")

    except Exception as e:
        print(f"[DEBUG ERRO] Falha ao salvar arquivo temporário: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Erro ao salvar arquivo temporariamente: {str(e)}")

   
    try:
        print(f"[DEBUG 3] Abrindo o arquivo temporário para leitura binária e upload...")
        
        with open(tmp_path, "rb") as f:
            uploaded = client.files.upload(
                file=f,
                mime_type=mime_type, # <--- ESSA LINHA CORRIGE O ERRO ATUAL
                config={"display_name": file.filename}
            )
        
        print(f"[DEBUG 4] SUCESSO! Upload concluído. File ID: {uploaded.name}")

        return {
            "file_id": uploaded.name,
            "filename": file.filename
        }
        
    except Exception as e:
        print(f"[DEBUG ERRO] FALHA no upload para Gemini: {str(e)}")
        # Re-lança a exceção para o cliente
        raise HTTPException(status_code=500, detail=f"Erro ao enviar arquivo: {str(e)}")

    finally:
        # 3. GARANTE que o arquivo temporário seja excluído, mesmo se houver erro
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)
            print(f"[DEBUG 5] Arquivo temporário removido: {tmp_path}")

# @router.post("/upload_pdf")
# async def upload_pdf(file: UploadFile = File(...)):

#     # 1️⃣ Validar MIME type pelo nome do arquivo
#     mime_type, _ = mimetypes.guess_type(file.filename)
#     if mime_type != "application/pdf":
#         raise HTTPException(status_code=400, detail="Apenas arquivos PDF são permitidos")

#     tmp_path = None
#     try:
#         # 2️⃣ Salvar temporariamente
#         await file.seek(0)
#         with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
#             shutil.copyfileobj(file.file, tmp)
#             tmp_path = tmp.name

#         # 3️⃣ Abrir o arquivo temporário para envio
#         with open(tmp_path, "rb") as f:
#             # Agora o Google consegue inferir o tipo
#             uploaded = client.files.upload(file=f)

#         return {"file_id": uploaded.name, "filename": file.filename}

#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Erro ao enviar arquivo: {str(e)}")

#     finally:
#         # 4️⃣ Limpeza do temporário
#         if tmp_path and os.path.exists(tmp_path):
#             os.remove(tmp_path)


@router.get("/ask")
async def ask(question: str, file_id: str):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=question,
        config={
            "search": {
                "files": [file_id]
            }
        }
    )

    return {"answer": response.text}