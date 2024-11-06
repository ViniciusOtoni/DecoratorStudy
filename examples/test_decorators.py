from decorators.couting import count_calls  
from decorators.logging import log_decorator
from decorators.params import loop


def test():

    @loop(2)         # Repete 2 vezes
    @log_decorator   # Loga a chamada
    @count_calls     # Contagem de chamadas
    def soma(*args):
        return sum(args)

    # Testa a função soma
    print("Testando a função soma:")
    soma(10, 5)

    # ----------------------------------------- #

    @loop(3)         
    @log_decorator   
    @count_calls     
    def saudacao(nome, **kwargs):
        mensagem = f"Olá, {nome}!"
        for chave, valor in kwargs.items():
            mensagem += f"\nSua {chave} é: {valor}"
        return mensagem

    # Testando a função saudação com kwargs
    print("\nTestando a função saudação:")
    saudacao("Vinicius", linguagem="Python", nivel="avançado")  # Passando o argumento diretamente como kwargs
