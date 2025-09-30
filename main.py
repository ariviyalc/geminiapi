from fastapi import FastAPI
from fastapi.responses import JSONResponse
import google.generativeai as genai

app = FastAPI()

@app.get("/")
async def root():
    return {
        "status": "online",
        "message": "API de Gemini funcionando",
        "developer": "El Impaciente",
        "endpoint": "/gemini?key=YOUR_KEY&text=YOUR_QUERY"
    }

@app.get("/gemini")
async def gemini_query(key: str = None, text: str = None):
    # Validar que ambos parámetros estén presentes
    if not key or not text:
        return JSONResponse(
            content={
                "status_code": 400,
                "developer": "El Impaciente",
                "message": "Se requieren los parámetros key y text"
            },
            status_code=400
        )
    
    try:
        # Configurar Gemini con la API key
        genai.configure(api_key=key)
        
        # Usar el modelo Gemini Pro
        model = genai.GenerativeModel('gemini-pro')
        
        # Generar respuesta
        response = model.generate_content(text)
        
        return JSONResponse(
            content={
                "status_code": 200,
                "developer": "El Impaciente",
                "message": response.text
            },
            status_code=200
        )
        
    except Exception as e:
        return JSONResponse(
            content={
                "status_code": 400,
                "developer": "El Impaciente",
                "message": f"Error: {str(e)}"
            },
            status_code=400
        )