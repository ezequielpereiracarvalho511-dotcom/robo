# 🤖 Framework de Automação de Robôs

Framework Python completo para criar robôs de automação personalizados. Este projeto fornece uma estrutura modular e extensível para redesenhar e criar novos robôs de automação a partir de aplicativos existentes.

## 📋 Características

- **Arquitetura Modular**: Classes base extensíveis (Robot, WebRobot, DataRobot)
- **Sistema de Configuração**: Gerenciamento flexível de configurações via JSON ou variáveis de ambiente
- **Utilitários Poderosos**: Decoradores para retry, timing, logging e mais
- **Fácil de Usar**: API simples e intuitiva
- **Extensível**: Crie seus próprios robôs especializados
- **Logging Integrado**: Sistema de logs completo para monitoramento

## 🚀 Início Rápido

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/ezequielpereiracarvalho511-dotcom/robo.git
cd robo
```

2. Instale dependências (se necessário):
```bash
pip install -r requirements.txt
```

### Uso Básico

```python
from robo import Robot

# Criar um robô simples
robo = Robot("MeuRobo")

# Adicionar tarefas
def minha_tarefa():
    print("Executando minha tarefa!")

robo.add_task(minha_tarefa)

# Executar
robo.run()
```

## 📚 Exemplos

O projeto inclui três exemplos completos:

### 1. Exemplo Básico (`exemplo_basico.py`)
Demonstra uso básico do framework com múltiplas tarefas sequenciais.

```bash
python exemplo_basico.py
```

### 2. Exemplo de Processamento de Dados (`exemplo_dados.py`)
Mostra como usar `DataRobot` para coletar, processar e gerar relatórios de dados.

```bash
python exemplo_dados.py
```

### 3. Exemplo Avançado (`exemplo_avancado.py`)
Demonstra funcionalidades avançadas: retry, timing, hashing e tratamento de erros.

```bash
python exemplo_avancado.py
```

## 🏗️ Estrutura do Projeto

```
robo/
├── robo.py               # Classes principais (Robot, WebRobot, DataRobot)
├── config.py             # Gerenciamento de configurações
├── utils.py              # Utilitários e decoradores
├── __init__.py           # Inicialização do pacote
├── exemplo_basico.py     # Exemplo básico de uso
├── exemplo_dados.py      # Exemplo com processamento de dados
├── exemplo_avancado.py   # Exemplo com recursos avançados
├── config_exemplo.json   # Arquivo de configuração de exemplo
├── requirements.txt      # Dependências do projeto
└── README.md            # Esta documentação
```

## 📖 Documentação das Classes

### Robot
Classe base para criar robôs de automação.

**Características:**
- Gerenciamento de tarefas
- Sistema de logging
- Execução sequencial ou contínua
- Monitoramento de status

**Exemplo:**
```python
from robo import Robot

robo = Robot("MeuRobo", config={'log_level': 'INFO'})
robo.add_task(minha_funcao)
robo.run()
```

### WebRobot
Robô especializado para automação web (estende Robot).

**Uso futuro:**
- Integração com Selenium/Playwright
- Navegação automatizada
- Scraping de dados

### DataRobot
Robô especializado para processamento de dados (estende Robot).

**Características:**
- Armazenamento de dados
- Processamento de informações
- Geração de relatórios

**Exemplo:**
```python
from robo import DataRobot

robo = DataRobot("ProcessadorDados")
robo.store_data('chave', 'valor')
dados = robo.get_data('chave')
```

### Config
Gerenciador de configurações flexível.

**Características:**
- Carregamento de JSON
- Variáveis de ambiente
- Valores padrão

**Exemplo:**
```python
from config import Config

# De arquivo JSON
config = Config.from_file('config.json')

# De variáveis de ambiente
config = Config.from_env(prefix='ROBO_')

# Programático
config = Config({'log_level': 'INFO'})
```

## 🛠️ Utilitários

### Decoradores

#### @retry
Repete execução em caso de falha.
```python
@retry(attempts=3, delay=1.0)
def funcao_que_pode_falhar():
    # código
```

#### @timing
Mede tempo de execução.
```python
@timing
def funcao_demorada():
    # código
```

#### @log_execution
Registra início e fim de execução.
```python
@log_execution
def funcao_importante():
    # código
```

### Funções Auxiliares

- `generate_hash()`: Gera hashes de strings
- `save_json()` / `load_json()`: I/O de JSON
- `format_timestamp()`: Formatação de datas
- `wait_until()`: Espera condicional
- `sanitize_filename()`: Limpa nomes de arquivo
- `chunk_list()`: Divide listas em chunks

## ⚙️ Configuração

### Arquivo de Configuração (JSON)

```json
{
  "name": "MeuRobo",
  "log_level": "INFO",
  "task_delay": 0.5,
  "retry_attempts": 3,
  "timeout": 30,
  "verbose": true
}
```

### Variáveis de Ambiente

Configure com prefixo `ROBO_`:
```bash
export ROBO_LOG_LEVEL=DEBUG
export ROBO_TASK_DELAY=1
export ROBO_RETRY_ATTEMPTS=5
```

## 🎯 Casos de Uso

1. **Automação Web**: Scraping, testes, preenchimento de formulários
2. **Processamento de Dados**: ETL, análise, relatórios
3. **Monitoramento**: Verificação de sistemas, coleta de métricas
4. **Integração**: Sincronização entre sistemas
5. **Tarefas Agendadas**: Execução periódica de operações

## 🔧 Extensão

Crie seus próprios robôs especializados:

```python
from robo import Robot

class MeuRoboCustomizado(Robot):
    def __init__(self, name, config=None):
        super().__init__(name, config)
        # Inicialização customizada
    
    def metodo_especial(self):
        # Funcionalidade específica
        pass
```

## 📝 Boas Práticas

1. **Use configurações**: Externalize parâmetros em arquivos de configuração
2. **Logging adequado**: Configure níveis de log apropriados
3. **Tratamento de erros**: Use decorador @retry para operações não determinísticas
4. **Tarefas modulares**: Divida operações complexas em tarefas menores
5. **Testes**: Teste cada tarefa individualmente antes de integrar

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Enviar pull requests
- Melhorar documentação

## 📄 Licença

Este projeto está disponível para uso livre. Sinta-se à vontade para adaptar e modificar conforme necessário.

## 💡 Suporte

Para questões ou suporte, abra uma issue no repositório do GitHub.

---

**Desenvolvido com ❤️ para facilitar a automação de tarefas**