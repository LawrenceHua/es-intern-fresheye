"""
FreshEye - Produce Freshness Scanner API

TODO: Build out the API endpoints below using FastAPI.
Use GitHub Copilot to help you! Try writing a comment describing
what each endpoint should do, then let Copilot complete it.
"""

from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI(title="FreshEye - Produce Freshness Scanner")

# Serve static files (HTML, CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home():
    """Serve the main upload page."""
    with open("static/index.html") as f:
        return f.read()


@app.post("/api/classify")
async def classify_produce(file: UploadFile = File(...)):
    """
    TODO: Accept an uploaded image file and return freshness classification.

    Steps:
    1. Read the uploaded image
    2. Preprocess it for the model (resize, normalize)
    3. Run inference with the classifier
    4. Return: {"item": "apple", "freshness": "Fresh", "confidence": 0.92, "tips": "..."}
    """
    # YOUR CODE HERE — use Copilot to help!
    return {
        "item": "unknown",
        "freshness": "Not implemented yet",
        "confidence": 0.0,
        "tips": "Implement the classifier first!"
    }


@app.get("/api/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy", "model_loaded": False}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
