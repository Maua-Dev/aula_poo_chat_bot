# Construindo um Chat Bot com Programação Orientada a Objetos

## Contexto do Projeto

Uma startup de tecnologia está desenvolvendo uma plataforma de atendimento ao cliente e precisa de um chat bot para automatizar as interações iniciais com os usuários. Como desenvolvedor, você foi designado para implementar um sistema de chat utilizando Programação Orientada a Objetos.

## Requisitos do Sistema

O chat bot deve:
- Processar mensagens de texto enviadas pelos usuários
- Manter um histórico das conversas
- Utilizar um modelo de linguagem para gerar respostas relevantes
- Ter uma personalidade configurável por meio de instruções
- Ser facilmente extensível para novos tipos de mensagens

## Conceitos de POO a serem aplicados

Durante a implementação, vamos aplicar os seguintes conceitos:

1. **Encapsulamento** - Ocultar detalhes da implementação e expor apenas interfaces necessárias
2. **Herança** - Criar hierarquias de classes que compartilham comportamentos
3. **Polimorfismo** - Tratar objetos de diferentes classes de maneira uniforme
4. **Composição** - Construir objetos complexos usando outros objetos como partes
5. **Abstração** - Representar conceitos do mundo real como classes e objetos

## Entidades principais do sistema

### Mensagens

As mensagens são o núcleo do sistema de chat e precisam representar diferentes papéis:

```
Message (classe base)
├── UserMessage (mensagens do usuário)
├── BotMessage (respostas do bot)
└── SystemMessage (instruções e configurações)
```

### Bot

O bot é responsável por gerar respostas com base nas mensagens anteriores:

- Possui um nome e instruções de comportamento
- Utiliza um modelo de linguagem (LLM)
- Formata as mensagens para a API do modelo
- Gera respostas baseadas no contexto da conversa

### Chat

O chat gerencia a interação entre usuários e bot:

- Mantém a lista de mensagens (histórico)
- Coordena o envio e recebimento de mensagens
- Solicita respostas ao bot
- Fornece métodos para adicionar e recuperar mensagens

## Atividade prática

1. Identifique os atributos e métodos necessários para cada classe
2. Desenhe um diagrama de classes mostrando as relações entre elas
3. Implemente as classes seguindo os princípios de POO
4. Crie um programa simples que demonstre o funcionamento do sistema

### Estrutura básica para começar

```python
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
```

## Como o sistema deve funcionar

Após implementar as classes, o sistema deve permitir interações como esta:

```python
# Criando o bot
bot = Bot(
    name="Assistente de Suporte", 
    instructions="Você é um assistente de suporte técnico. Seja detalhista e paciente.", 
    llm=OpenAI()
)

# Criando o chat
chat = Chat(bot=bot)

# Início da conversa
print(chat.messages[0].text)  # Exibe a mensagem de boas-vindas

# Simulando interação
user_input = "Meu computador está muito lento. O que posso fazer?"
chat.add_message(UserMessage(user_input))

# Gerando resposta
response = chat.generate_response()
chat.add_message(response)

print(f"{bot.name}: {response.text}")
```

## Perguntas para reflexão

Durante a implementação, considere:

1. Como a hierarquia de mensagens facilita a extensão do sistema?
2. Qual o benefício de encapsular a lógica de geração de respostas na classe Bot?
3. Por que a classe Chat mantém uma referência ao Bot em vez de herdar dele?
4. Como o polimorfismo está sendo aplicado no tratamento das mensagens?
5. Se quiséssemos adicionar suporte a mensagens com imagens, como modificaríamos o sistema?

## Desafios adicionais

Se terminar a implementação básica, tente estas extensões:

1. Adicione uma nova classe `ImageBotMessage` que permite ao bot enviar URLs de imagens
2. Implemente um método para salvar o histórico de conversa em um arquivo
3. Crie uma interface simples de linha de comando para interagir com o chat bot
4. Implemente uma classe `BotFactory` que possa criar diferentes tipos de bots pré-configurados