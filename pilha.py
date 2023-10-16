class Pilha:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.topo = -1
        self.dados = [None] * capacidade

    def push(self, dado):
        if self.pilha_esta_cheia():
            raise Exception("PilhaCheiaErro")
        if not isinstance(dado, (int, str)) and not (isinstance(dado, tuple) and len(dado) == 4):
            raise Exception("TipoErro")
        self.topo += 1
        self.dados[self.topo] = dado

    def pop(self):
        if self.pilha_esta_vazia():
            raise Exception("PilhaVaziaErro")
        dado = self.dados[self.topo]
        self.topo -= 1
        return dado

    def pilha_esta_vazia(self):
        return self.topo == -1

    def pilha_esta_cheia(self):
        return self.topo == self.capacidade - 1

    def swap(self):
        if self.topo > 0:
            self.dados[self.topo], self.dados[self.topo - 1] = self.dados[self.topo - 1], self.dados[self.topo]

    def length(self):
        return self.topo + 1
