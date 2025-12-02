import os
from google import genai
from app.core.config import settings



try:
    client = genai.Client(api_key=settings.google_api_key) 
    print("Sucesso: Cliente Gemini inicializado.")
    # Se você não vir esta mensagem, sua chave está incorreta ou ausente.
except Exception as e:
    print(f"ERRO DE CHAVE DE API/INICIALIZAÇÃO: {e}")