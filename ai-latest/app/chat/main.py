from fastapi import FastAPI

from app.chat.adapter.inbound.web.chat_controller import router as chat_router
from app.chat.adapter.inbound.web.text_controller import router as text_router

app = FastAPI()

app.include_router(text_router)
app.include_router(chat_router)