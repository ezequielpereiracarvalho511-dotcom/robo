"""
Módulo principal do robô de automação.

Este módulo fornece a classe base Robot para criar robôs de automação
que podem executar tarefas programadas automaticamente.
"""

import time
import logging
from typing import Callable, Dict, Any, List
from datetime import datetime


class Robot:
    """
    Classe base para criar robôs de automação.
    
    Esta classe fornece funcionalidades básicas para criar robôs que podem:
    - Executar tarefas automatizadas
    - Registrar logs de operações
    - Gerenciar estado de execução
    - Executar ações sequenciais
    """
    
    def __init__(self, name: str, config: Dict[str, Any] = None):
        """
        Inicializa o robô.
        
        Args:
            name: Nome do robô
            config: Dicionário de configurações opcionais
        """
        self.name = name
        self.config = config or {}
        self.tasks: List[Callable] = []
        self.is_running = False
        self.execution_count = 0
        
        # Configurar logging
        self._setup_logging()
        self.logger.info(f"Robô '{self.name}' inicializado")
    
    def _setup_logging(self):
        """Configura o sistema de logging do robô."""
        log_level = self.config.get('log_level', 'INFO')
        log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        
        logging.basicConfig(
            level=getattr(logging, log_level),
            format=log_format
        )
        self.logger = logging.getLogger(self.name)
    
    def add_task(self, task: Callable, name: str = None):
        """
        Adiciona uma tarefa ao robô.
        
        Args:
            task: Função a ser executada
            name: Nome opcional para a tarefa
        """
        task_name = name or task.__name__
        self.tasks.append(task)
        self.logger.info(f"Tarefa '{task_name}' adicionada")
    
    def run(self):
        """Executa todas as tarefas do robô em sequência."""
        if not self.tasks:
            self.logger.warning("Nenhuma tarefa para executar")
            return
        
        self.is_running = True
        self.execution_count += 1
        start_time = time.time()
        
        self.logger.info(f"Iniciando execução #{self.execution_count}")
        
        try:
            for i, task in enumerate(self.tasks, 1):
                self.logger.info(f"Executando tarefa {i}/{len(self.tasks)}: {task.__name__}")
                task()
                
                # Delay entre tarefas se configurado
                delay = self.config.get('task_delay', 0)
                if delay > 0:
                    time.sleep(delay)
            
            elapsed_time = time.time() - start_time
            self.logger.info(f"Execução #{self.execution_count} concluída em {elapsed_time:.2f}s")
            
        except Exception as e:
            self.logger.error(f"Erro durante execução: {str(e)}")
            raise
        finally:
            self.is_running = False
    
    def run_continuous(self, interval: int = 60):
        """
        Executa o robô continuamente em intervalos.
        
        Args:
            interval: Intervalo em segundos entre execuções
        """
        self.logger.info(f"Iniciando modo contínuo (intervalo: {interval}s)")
        
        try:
            while True:
                self.run()
                self.logger.info(f"Aguardando {interval}s até próxima execução...")
                time.sleep(interval)
        except KeyboardInterrupt:
            self.logger.info("Execução contínua interrompida pelo usuário")
    
    def status(self) -> Dict[str, Any]:
        """
        Retorna o status atual do robô.
        
        Returns:
            Dicionário com informações de status
        """
        return {
            'name': self.name,
            'is_running': self.is_running,
            'execution_count': self.execution_count,
            'tasks_count': len(self.tasks),
            'config': self.config
        }
    
    def clear_tasks(self):
        """Remove todas as tarefas do robô."""
        self.tasks.clear()
        self.logger.info("Todas as tarefas foram removidas")


class WebRobot(Robot):
    """
    Robô especializado para automação web.
    
    Estende a classe Robot com funcionalidades específicas para web.
    """
    
    def __init__(self, name: str, config: Dict[str, Any] = None):
        """
        Inicializa o robô web.
        
        Args:
            name: Nome do robô
            config: Dicionário de configurações opcionais
        """
        super().__init__(name, config)
        self.browser = None
        self.logger.info("WebRobot inicializado")
    
    def open_browser(self, url: str = None):
        """
        Abre o navegador.
        
        Args:
            url: URL inicial para navegar (opcional)
        """
        self.logger.info(f"Abrindo navegador{' em ' + url if url else ''}")
        # Implementação de abertura de navegador seria adicionada aqui
        # Por exemplo, usando selenium, playwright, etc.
    
    def close_browser(self):
        """Fecha o navegador."""
        self.logger.info("Fechando navegador")
        # Implementação de fechamento seria adicionada aqui


class DataRobot(Robot):
    """
    Robô especializado para processamento de dados.
    
    Estende a classe Robot com funcionalidades para manipulação de dados.
    """
    
    def __init__(self, name: str, config: Dict[str, Any] = None):
        """
        Inicializa o robô de dados.
        
        Args:
            name: Nome do robô
            config: Dicionário de configurações opcionais
        """
        super().__init__(name, config)
        self.data_store: Dict[str, Any] = {}
        self.logger.info("DataRobot inicializado")
    
    def store_data(self, key: str, value: Any):
        """
        Armazena dados no robô.
        
        Args:
            key: Chave para identificar os dados
            value: Valor a ser armazenado
        """
        self.data_store[key] = value
        self.logger.info(f"Dados armazenados: {key}")
    
    def get_data(self, key: str) -> Any:
        """
        Recupera dados armazenados.
        
        Args:
            key: Chave dos dados a recuperar
            
        Returns:
            Valor armazenado ou None se não encontrado
        """
        return self.data_store.get(key)
    
    def clear_data(self):
        """Limpa todos os dados armazenados."""
        self.data_store.clear()
        self.logger.info("Dados limpos")


if __name__ == "__main__":
    # Exemplo de uso
    def tarefa_exemplo():
        print("Executando tarefa de exemplo...")
        time.sleep(1)
    
    # Criar e executar um robô simples
    robo = Robot("MeuRobo")
    robo.add_task(tarefa_exemplo, "Tarefa 1")
    robo.add_task(tarefa_exemplo, "Tarefa 2")
    robo.run()
    
    print("\nStatus do robô:")
    print(robo.status())
