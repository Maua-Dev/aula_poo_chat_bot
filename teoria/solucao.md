# Construindo um Chat Bot com Programação Orientada a Objetos - Solução

## Implementação Completa (Gabarito)

Abaixo está a implementação completa de todas as classes do sistema de chat bot, com comentários detalhados explicando os conceitos de POO aplicados:

```python
from typing import List, Union
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


if __name__ == "__main__":
    # Este código seria executado apenas se este arquivo fosse executado diretamente
    exemplo_uso()
```

## Análise dos Conceitos de POO Aplicados

### 1. Encapsulamento
- Atributos e métodos são encapsulados dentro das classes apropriadas
- O método privado `_get_prompt()` na classe `Bot` esconde detalhes de implementação
- Os métodos públicos expõem apenas o que é necessário para interagir com as classes

### 2. Herança
- `UserMessage`, `BotMessage` e `SystemMessage` herdam da classe base `Message`
- Cada subclasse especializa o comportamento ao definir um papel específico
- A reutilização de código é evidente no método `to_openai()` herdado

### 3. Polimorfismo
- O método `to_openai()` é chamado de forma polimórfica em objetos de diferentes tipos de mensagem
- O método `add_message()` da classe `Chat` aceita qualquer subclasse de `Message`
- Este polimorfismo permite tratar mensagens de diferentes tipos de maneira uniforme

### 4. Composição
- A classe `Chat` é composta por um `Bot` e uma coleção de `Message`
- A relação de composição é mais adequada que herança, pois um chat "contém" um bot, não "é um" bot
- A composição permite maior flexibilidade, como trocar o bot durante a execução

### 5. Abstração
- `Bot` abstrai a complexidade da interação com o modelo de linguagem
- `Chat` abstrai o gerenciamento da conversa
- As classes representam entidades do mundo real (mensagens, bot, chat)

## Extensões Possíveis do Sistema

### 1. Adicionando Mensagens com Imagens

```python
class ImageBotMessage(BotMessage):
    def __init__(self, text: str, image_url: str):
        super().__init__(text)
        self.image_url = image_url
    
    def to_openai(self):
        base_dict = super().to_openai()
        # Adiciona a URL da imagem no formato adequado
        base_dict["content"] = [
            {"type": "text", "text": self.text},
            {"type": "image_url", "image_url": {"url": self.image_url}}
        ]
        return base_dict
```

### 2. Persistência do Histórico

```python
# Método adicional para a classe Chat
def save_history(self, filename: str):
    """Salva o histórico da conversa em um arquivo."""
    with open(filename, "w") as f:
        for msg in self.messages:
            f.write(f"{msg.role}: {msg.text}\n")
    
    return f"Histórico salvo em {filename}"

def load_history(self, filename: str):
    """Carrega o histórico da conversa de um arquivo."""
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split(": ", 1)
            if len(parts) == 2:
                role, text = parts
                if role == "user":
                    self.add_message(UserMessage(text))
                elif role == "assistant":
                    self.add_message(BotMessage(text))
                elif role == "system":
                    self.add_message(SystemMessage(text))
```

### 3. Fábrica de Bots

```python
class BotFactory:
    """
    Fábrica para criar bots com personalidades pré-configuradas.
    Demonstra o padrão de projeto Factory Method.
    """
    @staticmethod
    def create_support_bot(llm):
        return Bot(
            name="Suporte Técnico",
            instructions="Você é um assistente de suporte técnico. Seja detalhista e paciente.",
            llm=llm
        )
    
    @staticmethod
    def create_teacher_bot(llm):
        return Bot(
            name="Professor",
            instructions="Você é um professor de programação. Explique conceitos detalhadamente e dê exemplos práticos.",
            llm=llm
        )
    
    @staticmethod
    def create_concierge_bot(llm):
        return Bot(
            name="Concierge",
            instructions="Você é um concierge virtual. Ofereça recomendações personalizadas e seja sempre prestativo.",
            llm=llm
        )
```

## Resposta às Perguntas de Reflexão

1. **Como a hierarquia de mensagens facilita a extensão do sistema?**
   - A hierarquia permite adicionar novos tipos de mensagens (como `ImageBotMessage`) sem modificar o código existente
   - As novas classes herdam o comportamento básico e só precisam implementar o que é específico
   - O sistema continua tratando todas as mensagens de forma uniforme através do polimorfismo

2. **Qual o benefício de encapsular a lógica de geração de respostas na classe Bot?**
   - Separa claramente as responsabilidades: o Bot gera respostas, o Chat gerencia a conversa
   - Facilita a manutenção, pois alterações na lógica de geração de respostas ficam isoladas
   - Permite trocar a implementação do Bot sem afetar outras partes do sistema

3. **Por que a classe Chat mantém uma referência ao Bot em vez de herdar dele?**
   - Composição é mais adequada que herança neste caso, pois um Chat "contém" um Bot, não "é um" Bot
   - A composição permite maior flexibilidade, como trocar o Bot durante a execução
   - Seguindo o princípio "prefira composição à herança", evitamos herdar implementações que não fazem sentido

4. **Como o polimorfismo está sendo aplicado no tratamento das mensagens?**
   - O método `add_message()` aceita qualquer subclasse de `Message`
   - A lista `messages` pode conter diferentes tipos de mensagens
   - O método `to_openai()` é chamado polimorficamente em cada mensagem, sem precisar verificar seu tipo

5. **Como adicionar suporte a mensagens com imagens?**
   - Criando uma nova classe `ImageBotMessage` que herda de `BotMessage`
   - Sobrescrevendo o método `to_openai()` para incluir a URL da imagem no formato adequado
   - O restante do sistema continua funcionando sem modificações graças ao polimorfismo

## Conclusão

Este projeto demonstra como a Programação Orientada a Objetos pode ser aplicada para criar um sistema modular, extensível e fácil de manter. Através dos conceitos de encapsulamento, herança, polimorfismo, composição e abstração, conseguimos implementar um chat bot que pode ser facilmente adaptado para diferentes contextos e estendido com novas funcionalidades.

A estrutura de classes que desenvolvemos permite:
- Adicionar novos tipos de mensagens
- Trocar o modelo de linguagem sem afetar o resto do sistema
- Salvar e carregar históricos de conversa
- Criar bots com diferentes personalidades

Esta flexibilidade demonstra o poder da POO para modelar problemas complexos de forma organizada e extensível.