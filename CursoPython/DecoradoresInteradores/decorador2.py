def duplicar(func):#passando funcao como argumento
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    
    return envelope


@duplicar
def aprender(tecnologia):
    print(f'Estou aprendendo {tecnologia}')
    return tecnologia.upper()

tecnologia = aprender("python")
print(tecnologia)