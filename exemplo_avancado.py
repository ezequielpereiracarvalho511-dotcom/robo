"""
Exemplo avançado com múltiplas funcionalidades.

Demonstra uso de decoradores, retry, timing e configurações avançadas.
"""

from robo import Robot
from config import Config
from utils import retry, timing, log_execution, generate_hash
import random


class RoboAvancado(Robot):
    """Robô com funcionalidades avançadas."""
    
    def __init__(self, name: str, config: dict = None):
        """Inicializa o robô avançado."""
        super().__init__(name, config)
        self.resultados = []
    
    @retry(attempts=3, delay=0.5)
    @log_execution
    def tarefa_com_retry(self):
        """Tarefa que pode falhar e será repetida."""
        print("  Tentando executar tarefa sensível...")
        
        # Simula 30% de chance de falha
        if random.random() < 0.3:
            raise Exception("Erro simulado na tarefa")
        
        print("  ✓ Tarefa executada com sucesso")
        self.resultados.append("Tarefa com retry: OK")
    
    @timing
    @log_execution
    def tarefa_com_timing(self):
        """Tarefa com medição de tempo."""
        print("  Executando tarefa com medição de tempo...")
        import time
        time.sleep(0.8)  # Simula trabalho
        print("  ✓ Tarefa concluída")
        self.resultados.append("Tarefa com timing: OK")
    
    @log_execution
    def tarefa_com_hash(self):
        """Tarefa que gera hashes."""
        print("  Gerando hashes de segurança...")
        dados = f"Execução #{self.execution_count}"
        hash_result = generate_hash(dados)
        print(f"  Hash gerado: {hash_result[:16]}...")
        self.resultados.append(f"Hash: {hash_result[:8]}")
    
    def exibir_resultados(self):
        """Exibe todos os resultados."""
        print("\n" + "=" * 60)
        print("RESULTADOS DA EXECUÇÃO")
        print("=" * 60)
        for i, resultado in enumerate(self.resultados, 1):
            print(f"{i}. {resultado}")
        print("=" * 60)


def main():
    """Função principal."""
    print("=" * 60)
    print("EXEMPLO 3: Robô Avançado")
    print("=" * 60)
    print("Demonstra: retry, timing, logging e hashing")
    print()
    
    # Configuração avançada
    config = Config({
        'log_level': 'INFO',
        'task_delay': 0.5,
        'retry_attempts': 3,
        'timeout': 30
    })
    
    # Criar robô avançado
    robo = RoboAvancado("RoboAvancado", config.to_dict())
    
    # Adicionar tarefas com diferentes funcionalidades
    robo.add_task(robo.tarefa_com_retry, "Tarefa com Retry")
    robo.add_task(robo.tarefa_com_timing, "Tarefa com Timing")
    robo.add_task(robo.tarefa_com_hash, "Tarefa com Hash")
    robo.add_task(robo.exibir_resultados, "Exibir Resultados")
    
    # Executar
    print("Iniciando execução do robô avançado...\n")
    try:
        robo.run()
    except Exception as e:
        print(f"\n✗ Erro durante execução: {str(e)}")
        return
    
    # Status final
    print("\n" + "=" * 60)
    print("STATUS FINAL")
    print("=" * 60)
    status = robo.status()
    print(f"Nome: {status['name']}")
    print(f"Execuções: {status['execution_count']}")
    print(f"Tarefas configuradas: {status['tasks_count']}")
    print(f"Em execução: {status['is_running']}")
    
    print("\n✓ Exemplo avançado concluído!")


if __name__ == "__main__":
    main()
