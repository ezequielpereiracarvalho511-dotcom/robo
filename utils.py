"""
Módulo de utilitários para o robô.

Fornece funções auxiliares comuns para automação e processamento de dados.
"""

import time
import hashlib
import json
from datetime import datetime
from typing import Any, Callable
import functools


def retry(attempts: int = 3, delay: float = 1.0, exceptions: tuple = (Exception,)):
    """
    Decorador para repetir execução de função em caso de erro.
    
    Args:
        attempts: Número de tentativas
        delay: Tempo de espera entre tentativas (segundos)
        exceptions: Tupla de exceções que devem acionar retry
        
    Returns:
        Decorador
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < attempts - 1:
                        print(f"Tentativa {attempt + 1}/{attempts} falhou: {str(e)}")
                        time.sleep(delay)
                    else:
                        print(f"Todas as {attempts} tentativas falharam")
            raise last_exception
        return wrapper
    return decorator


def timing(func: Callable) -> Callable:
    """
    Decorador para medir tempo de execução de função.
    
    Args:
        func: Função a ser medida
        
    Returns:
        Função decorada
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"{func.__name__} executado em {elapsed_time:.2f}s")
        return result
    return wrapper


def log_execution(func: Callable) -> Callable:
    """
    Decorador para registrar execução de função.
    
    Args:
        func: Função a ser registrada
        
    Returns:
        Função decorada
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] Iniciando {func.__name__}")
        try:
            result = func(*args, **kwargs)
            print(f"[{datetime.now()}] {func.__name__} concluído com sucesso")
            return result
        except Exception as e:
            print(f"[{datetime.now()}] {func.__name__} falhou: {str(e)}")
            raise
    return wrapper


def generate_hash(data: str, algorithm: str = 'sha256') -> str:
    """
    Gera hash de uma string.
    
    Args:
        data: Dados a serem hasheados
        algorithm: Algoritmo de hash (md5, sha1, sha256, sha512)
        
    Returns:
        Hash em formato hexadecimal
        
    Raises:
        ValueError: Se o algoritmo não for suportado
    """
    # Whitelist de algoritmos seguros
    allowed_algorithms = ['md5', 'sha1', 'sha256', 'sha512']
    if algorithm not in allowed_algorithms:
        raise ValueError(f"Algoritmo não suportado. Use um dos seguintes: {allowed_algorithms}")
    
    hash_obj = hashlib.new(algorithm)
    hash_obj.update(data.encode('utf-8'))
    return hash_obj.hexdigest()


def save_json(data: Any, file_path: str, indent: int = 2):
    """
    Salva dados em arquivo JSON.
    
    Args:
        data: Dados a serem salvos
        file_path: Caminho do arquivo
        indent: Indentação do JSON
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)


def load_json(file_path: str) -> Any:
    """
    Carrega dados de arquivo JSON.
    
    Args:
        file_path: Caminho do arquivo
        
    Returns:
        Dados carregados
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def format_timestamp(dt: datetime = None, format_str: str = '%Y-%m-%d %H:%M:%S') -> str:
    """
    Formata timestamp.
    
    Args:
        dt: Objeto datetime (usa datetime.now() se None)
        format_str: String de formato
        
    Returns:
        Timestamp formatado
    """
    if dt is None:
        dt = datetime.now()
    return dt.strftime(format_str)


def wait_until(condition: Callable[[], bool], timeout: float = 10.0, interval: float = 0.5) -> bool:
    """
    Aguarda até que uma condição seja verdadeira.
    
    Args:
        condition: Função que retorna booleano
        timeout: Tempo máximo de espera (segundos)
        interval: Intervalo entre verificações (segundos)
        
    Returns:
        True se condição foi satisfeita, False se timeout
    """
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            if condition():
                return True
        except Exception:
            # Ignora exceções na condição e continua tentando
            pass
        time.sleep(interval)
    return False


def sanitize_filename(filename: str) -> str:
    """
    Remove caracteres inválidos de nome de arquivo.
    
    Args:
        filename: Nome de arquivo original
        
    Returns:
        Nome de arquivo sanitizado
    """
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename


def chunk_list(lst: list, chunk_size: int) -> list:
    """
    Divide uma lista em chunks de tamanho específico.
    
    Args:
        lst: Lista a ser dividida
        chunk_size: Tamanho de cada chunk
        
    Returns:
        Lista de chunks
    """
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]


if __name__ == "__main__":
    # Exemplos de uso
    
    @timing
    @retry(attempts=2)
    def exemplo_funcao():
        print("Executando função de exemplo...")
        time.sleep(1)
        return "Sucesso"
    
    print("Testando decoradores:")
    resultado = exemplo_funcao()
    print(f"Resultado: {resultado}\n")
    
    print("Testando hash:")
    texto = "Olá, mundo!"
    print(f"Texto: {texto}")
    print(f"Hash: {generate_hash(texto)}\n")
    
    print("Testando timestamp:")
    print(f"Timestamp atual: {format_timestamp()}\n")
    
    print("Testando sanitização de nome de arquivo:")
    nome_invalido = "arquivo:teste<>.txt"
    print(f"Nome original: {nome_invalido}")
    print(f"Nome sanitizado: {sanitize_filename(nome_invalido)}")
