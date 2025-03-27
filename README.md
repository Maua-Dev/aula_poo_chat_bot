# Chat Bot POO - Projeto de Aula

Este repositório contém o material para a aula de Programação Orientada a Objetos (POO) focada na implementação de um Chat Bot utilizando Python. O projeto demonstra conceitos fundamentais de POO como encapsulamento, herança, polimorfismo e composição através da construção de um assistente virtual que utiliza modelos de linguagem para gerar respostas.

## Estrutura do Repositório

```
chat-bot-poo/
├── app/                          # Aplicação FastAPI do Chat Bot
│   ├── __init__.py
│   ├── static/                   # Arquivos estáticos (CSS)
│   └── templates/                # Templates HTML
├── teoria/                       # Material teórico
│   ├── introducao.md             # Introdução e caso de estudo
│   └── solucao.md                # Solução comentada e análise
├── pratica/                      # Exercícios práticos
│   ├── aula_poo.py               # Implementação aula poo
│   ├── aula_poo_resolvido.py     # Aula poo resolvido
├── main.py                       # Ponto de entrada da aplicação FastAPI
├── requirements.txt              # Dependências do projeto
└── README.md                     # Este arquivo
```

## Configuração do Ambiente

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Chave de API da OpenAI (para utilizar o modelo de linguagem)

### Criando um Ambiente Virtual

Recomenda-se o uso de um ambiente virtual para isolar as dependências do projeto:

```bash
# No Windows
python -m venv venv
venv\Scripts\activate

# No macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Instalando as Dependências

Uma vez ativado o ambiente virtual, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

### Configurando a API da OpenAI

Crie um arquivo `.env` na raiz do projeto com sua chave de API:

```
OPENAI_API_KEY=sua_chave_api_aqui
```

## Executando o Projeto

### Interface Web (FastAPI)

Para iniciar o servidor web com a interface do Chat Bot:

```bash
# Na raiz do projeto
uvicorn main:app --reload
```

Após iniciar o servidor, acesse a interface em: http://localhost:8000

### Implementação para Estudo

Para estudar a implementação básica:

```bash
# Na pasta pratica
python aula_poo.py
```

## Material de Estudo

### Parte Teórica

Na pasta `teoria/` você encontrará:

- **introducao.md**: Apresentação do caso de estudo, requisitos e estrutura básica do projeto
- **solucao.md**: Implementação completa comentada e análise dos conceitos de POO aplicados

### Parte Prática

Na pasta `pratica/` você encontrará os arquivos para a prática em sala:

- **aula_poo.py**: Versão inicial para implementação durante a aula
- **aula_poo_resolvido.py**: Versão completa com a solução implementada

## Aplicação Web

A pasta `app/` contém a implementação de uma interface web para o Chat Bot utilizando FastAPI:

- **static/**: Arquivos CSS para estilização da interface do usuário
- **templates/**: Templates HTML para renderizar a interface

O arquivo `main.py` na raiz é o ponto de entrada da aplicação FastAPI, que você pode executar conforme instruído na seção "Executando o Projeto".

## Conceitos de POO Explorados

Este projeto demonstra vários conceitos fundamentais de Programação Orientada a Objetos:

1. **Encapsulamento**: Isolamento dos detalhes de implementação dentro das classes
2. **Herança**: Criação de hierarquias de classes que compartilham comportamentos
3. **Polimorfismo**: Tratamento de diferentes tipos de objetos de maneira uniforme
4. **Composição**: Construção de objetos complexos através da combinação de objetos mais simples
5. **Abstração**: Representação de conceitos do mundo real como classes e objetos

## Recursos Adicionais

- [Documentação da OpenAI](https://platform.openai.com/docs/api-reference)
- [Documentação do FastAPI](https://fastapi.tiangolo.com/)
- [Tutorial de POO em Python](https://docs.python.org/3/tutorial/classes.html)

## Licença

Este projeto é disponibilizado para fins educacionais sob a licença MIT.