"""
Framework de Automação de Robôs

Este pacote fornece classes e utilitários para criar robôs de automação.
"""

from .robo import Robot, WebRobot, DataRobot
from .config import Config, create_default_config
from .utils import retry, timing, log_execution

__version__ = '1.0.0'
__author__ = 'Robo Automation Framework'

__all__ = [
    'Robot',
    'WebRobot',
    'DataRobot',
    'Config',
    'create_default_config',
    'retry',
    'timing',
    'log_execution',
]
