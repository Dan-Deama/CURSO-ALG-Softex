class Notebook:

    def __init__(self, marca, processador, memoria):
        self.marca = marca
        self.processador = processador
        self.memoria = memoria

    def get_marca(self):
        return self.marca

    def get_processador(self):
        return self.processador

    def get_memoria(self):
        return self.memoria

Notebook = Notebook ('lenovo','inteli5','8gb')
Notebook.get_marca()
Notebook.get_processador()
Notebook.get_memoria()