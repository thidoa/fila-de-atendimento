class Fila:
    def __init__(self):
        self.filan = []

    def inserir(self, item):
        self.filan.append(item)
    def excluir(self):
        if not self.vazia():
            del self.filan[-1]
    def tamanho(self):
        return len(self.filan)
    def vazia(self):
        return self.tamanho() == 0

class Fila_prioritario:
    def __init__(self):
        self.fila_prioritario = []

    def inserir_prioritario(self, item):
        self.fila_prioritario.append(item)

    def excluir_prioritario(self):
        if not self.vazia_prioritario():
            del self.fila_prioritario[-1]

    def tamanho_prioritario(self):
        return len(self.fila_prioritario)

    def vazia_prioritario(self):
        return self.tamanho_prioritario() == 0



fila = Fila()
fila_prioritario = Fila_prioritario()

print("=-"*20)
print('1.....Add preferencial')
print('2...........Add normal')
print('3...............Listas')
print('4..............Remover')
print('5..............Tamanho')
print('0.................Sair')

opcao = int(input("Qual opçao? "))

x = 0
y = 0
teste = 0


while opcao != 0:
    if opcao == 1:
        x = x + 1
        fila_prioritario.inserir_prioritario(x)
        print('Inseriu um na fila do prioritaria!')
    elif opcao == 2:
        y = y + 1
        fila.inserir(y)
        print('Inseriu um na fila do normal!')
    elif opcao == 3:
        print('Fila normal =>', fila.filan)
        print('Fila prioritaria =>', fila_prioritario.fila_prioritario)
    elif opcao == 4:
        if fila_prioritario.vazia_prioritario() and fila.vazia():
            print('***************************')
            print('As duas filas estao vazias!')
            print('***************************')
        elif not fila_prioritario.vazia_prioritario() and fila.vazia():
            fila_prioritario.excluir_prioritario()
            teste = 0
        elif fila_prioritario.vazia_prioritario() and not fila.vazia():
            fila.excluir()
            teste = 1
        elif not fila_prioritario.vazia_prioritario() and not fila.vazia():
            if teste == 0:
                fila_prioritario.excluir_prioritario()
                teste = 1
            else:
                fila.excluir()
                teste = 0
    elif opcao == 5:
        print('Tamanho da fila prioritaria => ', fila_prioritario.tamanho_prioritario())
        print('Tamanho da fila normal => ', fila.tamanho())

    print("=-"*20)
    print('1.....Add preferencial')
    print('2...........Add normal')
    print('3...............Listas')
    print('4..............Remover')
    print('5..............Tamanho')
    print('0.................Sair')

    opcao = int(input("Qual opçao? "))
