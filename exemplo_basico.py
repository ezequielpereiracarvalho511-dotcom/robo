"""
Exemplo de uso básico do robô de automação.

Este script demonstra como criar e executar um robô simples.
"""

from robo import Robot
from config import create_default_config
from utils import timing
import time


def tarefa_1():
    """Primeira tarefa de exemplo."""
    print("  → Executando tarefa 1: Coleta de dados")
    time.sleep(0.5)
    print("  ✓ Dados coletados com sucesso")


def tarefa_2():
    """Segunda tarefa de exemplo."""
    print("  → Executando tarefa 2: Processamento")
    time.sleep(0.5)
    print("  ✓ Processamento concluído")


def tarefa_3():
    """Terceira tarefa de exemplo."""
    print("  → Executando tarefa 3: Relatório")
    time.sleep(0.5)
    print("  ✓ Relatório gerado")


@timing
def main():
    """Função principal do exemplo."""
    print("=" * 60)
    print("EXEMPLO 1: Robô Simples")
    print("=" * 60)
    
    # Criar configuração
    config = create_default_config()
    config.set('task_delay', 0.5)
    
    # Criar robô
    robo = Robot("RoboExemplo", config.to_dict())
    
    # Adicionar tarefas
    robo.add_task(tarefa_1)
    robo.add_task(tarefa_2)
    robo.add_task(tarefa_3)
    
    # Executar
    print("\nIniciando execução do robô...\n")
    robo.run()
    
    # Mostrar status
    print("\n" + "=" * 60)
    print("STATUS DO ROBÔ")
    print("=" * 60)
    status = robo.status()
    for key, value in status.items():
        print(f"{key}: {value}")
    
    print("\n✓ Exemplo concluído com sucesso!")


if __name__ == "__main__":
    main()
