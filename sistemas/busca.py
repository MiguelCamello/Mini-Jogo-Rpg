def buscar_objeto(nome, objetos):
    for obj in objetos:
        if obj.nome.lower() == nome.lower():
            return obj
    return None