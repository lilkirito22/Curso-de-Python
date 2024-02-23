def meu_decorador(func):
    def wrapper():
        print("antes de ser chamada")
        func()
        print("depois de ser chamada")
    
    return wrapper

@meu_decorador
def minha_funcao():
    print("minha funçao foi chamada")


minha_funcao()
