from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from API.API_APP import router as solar_router


app = FastAPI(
    title="API de Energia Solar",
    description="API de energia solar con cinco patrones de diseño GoF."
)

app.include_router(solar_router)

app.mount(
    "/",
    StaticFiles(
        directory=Path(__file__).resolve().parent / "static",
        html=True,
    ),
    name="static",
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)