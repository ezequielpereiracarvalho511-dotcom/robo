"""
Exemplo de robô de processamento de dados.

Este script demonstra como usar a classe DataRobot para
processar e armazenar dados.
"""

from robo import DataRobot
from config import Config
from utils import timing, log_execution
import random


class ProcessadorDados:
    """Classe auxiliar para processamento de dados."""
    
    def __init__(self, robo: DataRobot):
        """
        Inicializa o processador.
        
        Args:
            robo: Instância do DataRobot
        """
        self.robo = robo
    
    @log_execution
    def coletar_dados(self):
        """Simula coleta de dados."""
        print("  Coletando dados...")
        dados = [random.randint(1, 100) for _ in range(10)]
        self.robo.store_data('dados_brutos', dados)
        print(f"  ✓ {len(dados)} registros coletados")
    
    @log_execution
    def processar_dados(self):
        """Processa os dados coletados."""
        print("  Processando dados...")
        dados = self.robo.get_data('dados_brutos')
        
        if not dados:
            print("  ✗ Nenhum dado para processar")
            return
        
        # Estatísticas
        resultado = {
            'total': len(dados),
            'soma': sum(dados),
            'media': sum(dados) / len(dados),
            'maximo': max(dados),
            'minimo': min(dados)
        }
        
        self.robo.store_data('resultado', resultado)
        print("  ✓ Processamento concluído")
    
    @log_execution
    def gerar_relatorio(self):
        """Gera relatório dos resultados."""
        print("  Gerando relatório...")
        resultado = self.robo.get_data('resultado')
        
        if not resultado:
            print("  ✗ Nenhum resultado disponível")
            return
        
        print("\n" + "=" * 50)
        print("RELATÓRIO DE PROCESSAMENTO")
        print("=" * 50)
        print(f"Total de registros: {resultado['total']}")
        print(f"Soma: {resultado['soma']}")
        print(f"Média: {resultado['media']:.2f}")
        print(f"Máximo: {resultado['maximo']}")
        print(f"Mínimo: {resultado['minimo']}")
        print("=" * 50)


@timing
def main():
    """Função principal do exemplo."""
    print("=" * 60)
    print("EXEMPLO 2: Robô de Processamento de Dados")
    print("=" * 60)
    print()
    
    # Criar configuração
    config = Config({
        'log_level': 'INFO',
        'task_delay': 0.3
    })
    
    # Criar robô de dados
    robo = DataRobot("RoboDados", config.to_dict())
    
    # Criar processador
    processador = ProcessadorDados(robo)
    
    # Adicionar tarefas
    robo.add_task(processador.coletar_dados)
    robo.add_task(processador.processar_dados)
    robo.add_task(processador.gerar_relatorio)
    
    # Executar
    print("Iniciando processamento...\n")
    robo.run()
    
    print("\n✓ Exemplo de processamento de dados concluído!")


if __name__ == "__main__":
    main()
