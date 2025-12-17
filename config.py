"""
Módulo de gerenciamento de configurações para o robô.

Este módulo fornece funcionalidades para carregar e gerenciar
configurações de robôs a partir de diferentes fontes.
"""

import json
import os
from typing import Dict, Any


class Config:
    """
    Classe para gerenciar configurações do robô.
    
    Permite carregar configurações de arquivos JSON, dicionários
    ou variáveis de ambiente.
    """
    
    def __init__(self, config_dict: Dict[str, Any] = None):
        """
        Inicializa a configuração.
        
        Args:
            config_dict: Dicionário opcional com configurações iniciais
        """
        self._config = config_dict or {}
    
    @classmethod
    def from_file(cls, file_path: str) -> 'Config':
        """
        Carrega configurações de um arquivo JSON.
        
        Args:
            file_path: Caminho para o arquivo de configuração
            
        Returns:
            Instância de Config com as configurações carregadas
            
        Raises:
            FileNotFoundError: Se o arquivo não for encontrado
            json.JSONDecodeError: Se o arquivo não for JSON válido
        """
        with open(file_path, 'r', encoding='utf-8') as f:
            config_dict = json.load(f)
        return cls(config_dict)
    
    @classmethod
    def from_env(cls, prefix: str = 'ROBO_') -> 'Config':
        """
        Carrega configurações de variáveis de ambiente.
        
        Args:
            prefix: Prefixo das variáveis de ambiente a considerar
            
        Returns:
            Instância de Config com as configurações das variáveis de ambiente
        """
        config_dict = {}
        for key, value in os.environ.items():
            if key.startswith(prefix):
                config_key = key[len(prefix):].lower()
                config_dict[config_key] = value
        return cls(config_dict)
    
    def get(self, key: str, default: Any = None) -> Any:
        """
        Obtém um valor de configuração.
        
        Args:
            key: Chave da configuração
            default: Valor padrão se a chave não existir
            
        Returns:
            Valor da configuração ou valor padrão
        """
        return self._config.get(key, default)
    
    def set(self, key: str, value: Any):
        """
        Define um valor de configuração.
        
        Args:
            key: Chave da configuração
            value: Valor a ser definido
        """
        self._config[key] = value
    
    def update(self, config_dict: Dict[str, Any]):
        """
        Atualiza múltiplas configurações.
        
        Args:
            config_dict: Dicionário com configurações a atualizar
        """
        self._config.update(config_dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Retorna as configurações como dicionário.
        
        Returns:
            Dicionário com todas as configurações
        """
        return self._config.copy()
    
    def save(self, file_path: str):
        """
        Salva as configurações em um arquivo JSON.
        
        Args:
            file_path: Caminho onde salvar o arquivo de configuração
        """
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(self._config, f, indent=2, ensure_ascii=False)
    
    def __repr__(self) -> str:
        """Representação em string da configuração."""
        return f"Config({self._config})"


# Configurações padrão recomendadas
DEFAULT_CONFIG = {
    'log_level': 'INFO',
    'task_delay': 0,
    'retry_attempts': 3,
    'timeout': 30,
    'verbose': True
}


def create_default_config() -> Config:
    """
    Cria uma configuração com valores padrão.
    
    Returns:
        Instância de Config com configurações padrão
    """
    return Config(DEFAULT_CONFIG.copy())


if __name__ == "__main__":
    # Exemplo de uso
    print("Criando configuração padrão...")
    config = create_default_config()
    print(config)
    
    print("\nAdicionando configurações personalizadas...")
    config.set('name', 'MeuRobo')
    config.set('max_executions', 10)
    print(config)
    
    print("\nSalvando configuração...")
    config.save('exemplo_config.json')
    print("Configuração salva em 'exemplo_config.json'")
