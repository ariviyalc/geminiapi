from fastapi import FastAPI
from fastapi.responses import JSONResponse
import google.generativeai as genai

app = FastAPI()

@app.get("/")
async def root():
    return {
        "status": "online",
        "message": "Gemini API is working",
        "developer": "https://pro_xbots.t.me",
        "endpoint": "/gemini?key=YOUR_KEY&text=YOUR_QUERY"
    }

@app.get("/gemini")
async def gemini_query(key: str = None, text: str = None):
    # Validate that both parameters are provided
    if not key or not text:
        return JSONResponse(
            content={
                "status_code": 400,
                "message": "The parameters key and text are required"
            },
            status_code=400
        )

    try:
        # Configure Gemini with the API key
        genai.configure(api_key=key)

        # Use the Gemini 2.5 Flash-Lite model
        model = genai.GenerativeModel("gemini-2.5-flash-lite")

        # Generate response
        response = model.generate_content(text)

        return JSONResponse(
            content={
                "status_code": 200,
                "message": response.text
            },
            status_code=200
        )

    except Exception as e:
        return JSONResponse(
            content={
                "status_code": 400,
                "message": f"Error: {str(e)}"
            },
            status_code=400
        )