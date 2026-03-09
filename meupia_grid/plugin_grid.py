# -*- coding: utf-8 -*-

try:
    import js
    RUNNING_IN_BROWSER = True
except ImportError:
    RUNNING_IN_BROWSER = False

def grid_iniciar(largura: int, altura: int):
    """Inicializa o grid visual com as dimensões especificadas."""
    if RUNNING_IN_BROWSER and hasattr(js, 'window') and hasattr(js.window, 'meuPiaGridAPI'):
        js.window.meuPiaGridAPI.iniciar(largura, altura)
    else:
        print(f"[Mock Grid] Grid inicializado com tamanho {largura}x{altura}")

def grid_parede(x: int, y: int):
    """Define uma célula do grid como parede/obstáculo."""
    if RUNNING_IN_BROWSER and hasattr(js, 'window') and hasattr(js.window, 'meuPiaGridAPI'):
        js.window.meuPiaGridAPI.parede(x, y)
    else:
        print(f"[Mock Grid] Parede adicionada em ({x}, {y})")

def grid_visitar(x: int, y: int, passo: int):
    """Marca uma célula como visitada (útil para rastrear o algoritmo)."""
    if RUNNING_IN_BROWSER and hasattr(js, 'window') and hasattr(js.window, 'meuPiaGridAPI'):
        js.window.meuPiaGridAPI.visitar(x, y, passo)
    else:
        print(f"[Mock Grid] Célula ({x}, {y}) visitada no passo {passo}")