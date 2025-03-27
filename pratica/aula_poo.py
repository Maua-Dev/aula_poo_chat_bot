from typing import List
from openai import OpenAI


class Message:
    """Classe base para representar uma mensagem no chat."""

    def __init__(self, role: str, text: str):
        # Implemente aqui
        pass

    def to_openai(self):
        # Método para converter para formato da API
        pass


class UserMessage(Message):
    """Mensagem enviada pelo usuário."""

    def __init__(self, text: str):
        # Implemente aqui
        pass


class BotMessage(Message):
    """Mensagem enviada pelo bot."""

    def __init__(self, text: str):
        # Implemente aqui
        pass


class SystemMessage(Message):
    """Mensagem de sistema com instruções."""

    def __init__(self, text: str):
        # Implemente aqui
        pass


class Bot:
    """Assistente virtual que gera respostas."""

    def __init__(self, name: str, instructions: str, llm):
        # Implemente aqui
        pass

    def invoke(self, messages):
        # Gere uma resposta
        pass

    def _get_prompt(self):
        # Método privado para formatar instruções
        pass


class Chat:
    """Gerencia a conversa entre usuário e bot."""

    def __init__(self, bot):
        # Implemente aqui
        pass

    def generate_response(self):
        # Solicite uma resposta ao bot
        pass

    def add_message(self, message):
        # Adicione a mensagem ao histórico
        pass

    def get_messages(self):
        # Retorne todas as mensagens
        pass


# ============== EXEMPLO DE USO ==============

def exemplo_uso():
    """
    Exemplo de como usar as classes implementadas.
    """
    # Importa a biblioteca necessária
    from openai import OpenAI

    # Criando uma instância do bot
    bot = Bot(
        name="Assistente POO",
        instructions="Você é um assistente que ajuda a explicar conceitos de Programação Orientada a Objetos.",
        llm=OpenAI()
    )

    # Criando uma instância do chat (composição)
    chat = Chat(bot=bot)

    # Exibindo a mensagem de boas-vindas
    print(chat.messages[0].text)

    # Loop de interação
    while True:
        # Obtendo input do usuário
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            break

        # Adicionando mensagem do usuário ao chat
        chat.add_message(UserMessage(user_input))

        # Gerando resposta do bot
        response = chat.generate_response()
        chat.add_message(response)

        # Exibindo a resposta
        print(f"{bot.name}: {response.text}")
