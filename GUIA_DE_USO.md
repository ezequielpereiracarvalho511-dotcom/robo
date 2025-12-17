# Guia de Uso - Framework de Automação de Robôs

## Índice
1. [Instalação](#instalação)
2. [Conceitos Básicos](#conceitos-básicos)
3. [Exemplos Práticos](#exemplos-práticos)
4. [API Reference](#api-reference)
5. [Perguntas Frequentes](#perguntas-frequentes)

---

## Instalação

### Requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Passos

1. Clone o repositório:
```bash
git clone https://github.com/ezequielpereiracarvalho511-dotcom/robo.git
cd robo
```

2. (Opcional) Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. Instale dependências (se necessário):
```bash
pip install -r requirements.txt
```

---

## Conceitos Básicos

### O que é um Robô?

Um robô no contexto deste framework é uma classe Python que automatiza tarefas sequenciais. Cada robô pode:
- Executar múltiplas tarefas em ordem
- Registrar logs de suas operações
- Gerenciar seu próprio estado
- Repetir execuções com intervalos definidos

### Anatomia de um Robô

```python
from robo import Robot

# 1. Criar o robô
robo = Robot("NomeDoRobo")

# 2. Definir tarefas
def minha_tarefa():
    print("Fazendo algo útil...")

# 3. Adicionar tarefas ao robô
robo.add_task(minha_tarefa)

# 4. Executar
robo.run()
```

---

## Exemplos Práticos

### Exemplo 1: Automação Simples

Criar um robô que executa três tarefas sequenciais:

```python
from robo import Robot
import time

def tarefa_1():
    print("Iniciando processamento...")
    time.sleep(1)

def tarefa_2():
    print("Processando dados...")
    time.sleep(1)

def tarefa_3():
    print("Finalizando...")
    time.sleep(1)

# Criar e configurar o robô
robo = Robot("ProcessadorSimples")
robo.add_task(tarefa_1)
robo.add_task(tarefa_2)
robo.add_task(tarefa_3)

# Executar
robo.run()
```

### Exemplo 2: Robô com Configurações

```python
from robo import Robot
from config import Config

# Criar configuração
config = Config({
    'log_level': 'DEBUG',
    'task_delay': 0.5,  # 0.5 segundos entre tarefas
    'retry_attempts': 3
})

# Criar robô com configuração
robo = Robot("RoboConfigurado", config.to_dict())

def processar():
    print("Processando com configurações personalizadas")

robo.add_task(processar)
robo.run()
```

### Exemplo 3: Processamento de Dados

```python
from robo import DataRobot

# Criar robô de dados
robo = DataRobot("AnalisadorDados")

def coletar():
    dados = [1, 2, 3, 4, 5]
    robo.store_data('numeros', dados)
    print(f"Coletados: {dados}")

def analisar():
    dados = robo.get_data('numeros')
    soma = sum(dados)
    robo.store_data('soma', soma)
    print(f"Soma: {soma}")

def relatorio():
    soma = robo.get_data('soma')
    print(f"Resultado final: {soma}")

robo.add_task(coletar)
robo.add_task(analisar)
robo.add_task(relatorio)
robo.run()
```

### Exemplo 4: Usando Decoradores

```python
from robo import Robot
from utils import retry, timing, log_execution

robo = Robot("RoboComDecorators")

@retry(attempts=3, delay=1)
@timing
@log_execution
def tarefa_critica():
    # Esta tarefa será:
    # 1. Logada (início e fim)
    # 2. Cronometrada
    # 3. Repetida até 3x em caso de erro
    print("Executando tarefa crítica...")
    # seu código aqui

robo.add_task(tarefa_critica)
robo.run()
```

### Exemplo 5: Execução Contínua

```python
from robo import Robot

robo = Robot("MonitorContínuo")

def verificar_sistema():
    print("Verificando sistema...")
    # verificações aqui

robo.add_task(verificar_sistema)

# Executar a cada 60 segundos
# Use Ctrl+C para interromper
robo.run_continuous(interval=60)
```

---

## API Reference

### Classe Robot

#### Construtor
```python
Robot(name: str, config: Dict[str, Any] = None)
```
- `name`: Nome do robô
- `config`: Dicionário opcional de configurações

#### Métodos

**add_task(task: Callable, name: str = None)**
- Adiciona uma tarefa ao robô
- `task`: Função a ser executada
- `name`: Nome opcional da tarefa

**run()**
- Executa todas as tarefas em sequência

**run_continuous(interval: int = 60)**
- Executa o robô continuamente
- `interval`: Tempo em segundos entre execuções

**status() -> Dict**
- Retorna informações sobre o estado do robô

**clear_tasks()**
- Remove todas as tarefas do robô

### Classe DataRobot

Herda de `Robot` e adiciona:

**store_data(key: str, value: Any)**
- Armazena dados no robô

**get_data(key: str) -> Any**
- Recupera dados armazenados

**clear_data()**
- Limpa todos os dados

### Classe Config

#### Métodos de Criação

**Config(config_dict: Dict = None)**
- Cria config a partir de dicionário

**Config.from_file(file_path: str)**
- Carrega config de arquivo JSON

**Config.from_env(prefix: str = 'ROBO_')**
- Carrega config de variáveis de ambiente

#### Métodos

**get(key: str, default: Any = None) -> Any**
- Obtém valor de configuração

**set(key: str, value: Any)**
- Define valor de configuração

**save(file_path: str)**
- Salva configurações em JSON

### Decoradores (utils)

**@retry(attempts=3, delay=1.0, exceptions=(Exception,))**
- Repete função em caso de erro

**@timing**
- Mede tempo de execução

**@log_execution**
- Registra início e fim da função

### Funções Utilitárias (utils)

**generate_hash(data: str, algorithm='sha256') -> str**
- Gera hash de string

**save_json(data, file_path, indent=2)**
- Salva dados em JSON

**load_json(file_path) -> Any**
- Carrega dados de JSON

**format_timestamp(dt=None, format_str='%Y-%m-%d %H:%M:%S') -> str**
- Formata timestamp

**wait_until(condition: Callable, timeout=10, interval=0.5) -> bool**
- Espera até condição ser satisfeita

**sanitize_filename(filename: str) -> str**
- Remove caracteres inválidos de nome de arquivo

**chunk_list(lst: list, chunk_size: int) -> list**
- Divide lista em chunks

---

## Perguntas Frequentes

### Como criar meu próprio tipo de robô?

```python
from robo import Robot

class MeuRoboCustomizado(Robot):
    def __init__(self, name, config=None):
        super().__init__(name, config)
        # Suas inicializações aqui
    
    def metodo_especial(self):
        # Sua funcionalidade especial
        pass
```

### Como carregar configurações de arquivo?

```python
from config import Config

config = Config.from_file('meu_config.json')
robo = Robot("MeuRobo", config.to_dict())
```

### Como fazer o robô executar indefinidamente?

```python
robo = Robot("RoboContínuo")
robo.add_task(minha_tarefa)
robo.run_continuous(interval=300)  # A cada 5 minutos
```

### Como lidar com erros?

Use o decorador `@retry`:

```python
from utils import retry

@retry(attempts=3, delay=2)
def tarefa_que_pode_falhar():
    # código que pode falhar
    pass
```

### Como ver os logs detalhados?

Configure o nível de log:

```python
config = Config({'log_level': 'DEBUG'})
robo = Robot("MeuRobo", config.to_dict())
```

### Como compartilhar dados entre tarefas?

Use `DataRobot`:

```python
robo = DataRobot("RoboDados")

def tarefa_1():
    robo.store_data('resultado', 42)

def tarefa_2():
    valor = robo.get_data('resultado')
    print(f"Valor: {valor}")

robo.add_task(tarefa_1)
robo.add_task(tarefa_2)
robo.run()
```

### Como medir performance?

Use o decorador `@timing`:

```python
from utils import timing

@timing
def tarefa_demorada():
    # código
    pass
```

### Como configurar delay entre tarefas?

```python
config = Config({'task_delay': 2})  # 2 segundos
robo = Robot("MeuRobo", config.to_dict())
```

---

## Dicas e Boas Práticas

1. **Modularize suas tarefas**: Crie funções pequenas e específicas
2. **Use configurações**: Externalize parâmetros em arquivos
3. **Log apropriadamente**: Use níveis de log adequados (DEBUG, INFO, WARNING, ERROR)
4. **Tratamento de erros**: Use @retry para operações não determinísticas
5. **Teste individualmente**: Teste cada tarefa antes de integrar
6. **Documentação**: Documente suas tarefas customizadas

---

## Suporte

Para mais informações, consulte:
- README.md principal
- Exemplos incluídos no projeto
- Código fonte dos módulos

---

**Última atualização**: 2025-12-17
