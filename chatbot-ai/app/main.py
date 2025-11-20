from fastapi import FastAPI
from app.chat.adapter.inbound.web.chat_controller import router as chat_router
app = FastAPI()

app.include_router(chat_router)

