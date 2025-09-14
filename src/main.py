from fastapi import FastAPI

from link_shortener.router import router as link_shortener_router


app = FastAPI()

app.include_router(link_shortener_router, prefix="/api", tags=["link_shortener"])