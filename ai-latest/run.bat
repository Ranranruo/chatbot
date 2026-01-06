@echo off
call venv/Scripts/activate
uvicorn app.chat.main:app --reload
pause