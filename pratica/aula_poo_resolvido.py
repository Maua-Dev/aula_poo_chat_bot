import os
from typing import List
from openai import OpenAI


# ============== ETAPA 1: Classe Message e suas derivadas ==============

class Message:
    """
    Classe base para representar uma mensagem no chat.
    
    Esta classe demonstra encapsulamento ao conter os dados da mensagem
    e fornecer métodos para acessá-los de forma controlada.
    """

    def __init__(self, role: str, text: str):
        # Encapsulamento: atributos da classe
        self.role = role
        self.text = text

    def to_openai(self):
        """
        Converte a mensagem para o formato esperado pela API da OpenAI.
        Este método será herdado ou sobrescrito pelas subclasses.
        """
        return {
            "role": self.role,
            "content": self.text
        }


class UserMessage(Message):
    """
    Representa uma mensagem enviada pelo usuário.
    
    Demonstra herança ao estender a classe Message e
    especializar seu comportamento.
    """

    def __init__(self, text: str):
        # Herança: chama o construtor da classe pai
        super().__init__("user", text)


class BotMessage(Message):
    """
    Representa uma mensagem enviada pelo bot.
    
    Outro exemplo de herança a partir da classe Message.
    """

    def __init__(self, text: str):
        # Herança: chama o construtor da classe pai
        super().__init__("assistant", text)


class SystemMessage(Message):
    """
    Representa uma mensagem de sistema com instruções.
    
    Mais um exemplo de herança da classe Message.
    """

    def __init__(self, text: str):
        # Herança: chama o construtor da classe pai
        super().__init__("system", text)


# ============== ETAPA 2: Classe Bot ==============

class Bot:
    """
    Representa o assistente virtual que gera respostas.
    
    Demonstra encapsulamento ao esconder a complexidade da geração
    de respostas e expor apenas métodos de alto nível.
    """

    def __init__(self, name: str, instructions: str, llm: OpenAI):
        # Encapsulamento: atributos da classe
        self.name = name
        self.instructions = instructions
        self.llm = llm
        # Inicializa a mensagem de boas-vindas do bot
        self.started_message = BotMessage(f"Olá! Eu sou o {self.name}. Como posso ajudar você hoje?")

    def invoke(self, messages: List[Message]) -> BotMessage:
        """
        Gera uma resposta do bot com base nas mensagens anteriores.
        
        Demonstra abstração ao esconder a complexidade da interação com a API.
        """
        # Adiciona o prompt do sistema às mensagens
        messages = [self._get_prompt()] + messages
        # Converte as mensagens para o formato da OpenAI
        # Polimorfismo: chama o mesmo método em diferentes objetos
        messages = [message.to_openai() for message in messages]

        # Chama a API para gerar uma resposta
        response = self.llm.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )

        # Retorna a resposta como um objeto BotMessage
        return BotMessage(response.choices[0].message.content)

    def _get_prompt(self) -> SystemMessage:
        """
        Método privado para gerar o prompt do sistema.
        
        Encapsulamento: método interno, não destinado a ser chamado diretamente de fora.
        O prefixo '_' é uma convenção para indicar que o método é privado.
        """
        return SystemMessage(f"{self.instructions}\nSeu nome é {self.name}")


# ============== ETAPA 3: Classe Chat ==============

class Chat:
    """
    Gerencia a conversa entre o usuário e o bot.
    
    Demonstra composição, pois um Chat contém um Bot e uma coleção de Messages.
    """

    def __init__(self, bot: Bot):
        # Composição: um Chat contém um Bot
        self.bot = bot
        # Composição: um Chat contém várias Messages
        self.messages: List[Message] = [self.bot.started_message]

    def generate_response(self) -> BotMessage:
        """
        Gera uma resposta do bot com base nas mensagens do chat.
        
        Demonstra delegação, pois o Chat delega a geração da resposta para o Bot.
        """
        # Delegação: o Chat solicita ao Bot que gere uma resposta
        response = self.bot.invoke(self.messages)
        return response

    def add_message(self, message: Message):
        """
        Adiciona uma mensagem ao histórico do chat.
        
        Polimorfismo: aceita qualquer objeto que seja uma subclasse de Message.
        """
        self.messages.append(message)

    def get_messages(self):
        """
        Retorna todas as mensagens do chat.
        
        Encapsulamento: fornece acesso controlado aos dados internos.
        """
        return self.messages

    def messages_to_openai(self):
        """
        Converte todas as mensagens para o formato da OpenAI.
        
        Demonstra como o polimorfismo simplifica operações em coleções de objetos.
        """
        # Polimorfismo: chama o mesmo método em diferentes objetos
        return [message.to_openai() for message in self.messages]


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


client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

bot = Bot(
    name="Assistente POO",
    instructions="Você é um assistente que ajuda a explicar conceitos de Programação Orientada a Objetos.",
    llm=client
)

chat = Chat(bot=bot)

if __name__ == "__main__":
    exemplo_uso()
