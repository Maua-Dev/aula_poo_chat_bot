import uuid
import uvicorn
from typing import Dict
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI, Request, Body
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse

from pratica.aula_poo_resolvido import UserMessage, chat as chatbot, Chat

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Armazenamento de sessões
sessions: Dict[str, Chat] = {}


@app.get("/", response_class=HTMLResponse)
async def root():
    """Redireciona para a página do chat"""
    return RedirectResponse(url="/chat")


@app.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request):
    """Renderiza a página do chat"""
    session_id = str(uuid.uuid4())
    sessions[session_id] = chatbot
    return templates.TemplateResponse(
        "chat.html",
        {"request": request, "session_id": session_id, "bot_name": chatbot.bot.name}
    )


@app.post("/send_message/{session_id}")
async def send_message(session_id: str, message: dict = Body(...)):
    """
    Endpoint para processar mensagens e retornar respostas de forma síncrona
    """
    if session_id not in sessions:
        return JSONResponse(status_code=404, content={"error": "Sessão não encontrada"})

    chat = sessions[session_id]

    # Adiciona a mensagem do usuário ao chat
    user_message = UserMessage(message["content"])
    chat.add_message(user_message)

    # Gera uma resposta (de forma síncrona)
    bot_response = chat.generate_response()
    chat.add_message(bot_response)

    return {
        "response": bot_response.text
    }


@app.get("/{path:path}")
async def catch_all(path: str):
    """Redireciona qualquer caminho indefinido para a página do chat"""
    return RedirectResponse(url="/chat")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
