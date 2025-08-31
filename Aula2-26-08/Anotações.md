

# Aula 2 - TEP 

## Trabalhando com ambientes Virtuais no Python

Ambientes virtuais são como "ilhas" isoladas dentro do seu sistema, onde você pode instalar e gerenciar pacotes Python de forma independente para cada projeto.  
Isso significa que cada projeto terá sua própria versão do Python e suas próprias bibliotecas, evitando conflitos entre diferentes versões e dependências.

### Por que usar ambientes virtuais?

- **Isolamento de projetos**: Cada projeto terá seu próprio conjunto de pacotes, evitando conflitos de versão.  
- **Gerenciamento de dependências**: Facilita o controle das versões exatas de cada pacote utilizado em um projeto.  
- **Reprodutibilidade**: Permite que outros desenvolvedores reproduzam o ambiente do seu projeto com facilidade.  
- **Organização**: Mantém seu ambiente Python organizado e livre de confusões.  

---

### a) Criando um ambiente virtual local com Python no terminal


# Criar ambiente
python -m venv meu_ambiente

# Ativar ambiente - Linux/WSL
source meu_ambiente/bin/activate

# Ativar ambiente - Windows
meu_ambiente\Scripts\activate


Instalando pacotes

pip install <nome_do_modulo>

## Criando conta no GPT

### Passo a passo

1. Crie e exporte uma chave de API.
    
2. Acesse o site da OpenAI:  
    👉 [https://platform.openai.com/](https://platform.openai.com/?utm_source=chatgpt.com)
    
3. Crie uma chave de API no painel.
    
4. Armazene a chave em um local seguro (por exemplo, no `.zshrc` ou outro arquivo de configuração).
    
5. Exporte como variável de ambiente no terminal.

Exportando variáveiois de ambiente
#### Linux/macOS
export OPENAI_API_KEY="sua_api_key_aqui"

Windows (PowerShell)

setx OPENAI_API_KEY "sua_api_key_aqui"

set OPENAI_API_KEY=sua_api_key_aqui

Arquivo de exemplo:

`from openai import OpenAI`

`client = OpenAI()`

`completion = client.chat.completions.create(`
    `model="gpt-4o-mini",`
    `messages=[`
        `{"role": "system", "content": "You are a helpful assistant."},`
        `{"role": "user", "content": "Write a haiku about recursion in programming."}`
    `]`
`)`

`print(completion.choices[0].message)`

Executar:

python example.py


Com o modelo Groq seria o mesmo processo.