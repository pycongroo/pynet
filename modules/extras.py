def extract_from_file(path_orig):
    """Funcion para extraer enlaces desde un archivo de texto."""
    arch = open(path_orig, 'r')
    data = arch.readlines()
    links = map(lambda linea: linea[:-1], data)
    return links
