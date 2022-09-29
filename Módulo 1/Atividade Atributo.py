class Notebook:

    def __init__(self, marca, processador, memoria_ram):
        self.marca = marca
        self.processador = processador
        self.memoria_ram = memoria_ram

    def get_marca(self):
        return self.marca

    def get_processador(self):
        return self.processador

    def get_memoria_ram(self):
        return self.memoria_ram

    def set_memoria_ram(self, true):
        if self.memoria_ram == 8:
            print(true)


Newnotebook = Notebook('lenovo', 'intel_i5', 8)
Newnotebook.get_marca()
Newnotebook.get_processador()
Newnotebook.get_memoria_ram()

print('Marca do Notebook:', Newnotebook.get_marca(), '\nModelo Processador:', Newnotebook.get_processador(), '\nMemória RAM:', Newnotebook.get_memoria_ram())

memoria_ram = Newnotebook.get_memoria_ram()
u = input('Deseja fazer o upgrade da memória? [Y/N]')
if u == 's':
    upgrade = memoria_ram*2
else:
    upgrade = memoria_ram
Newnotebook.set_memoria_ram(upgrade)
print('O novo notebook possui', Newnotebook.get_memoria_ram(), 'de RAM.')
