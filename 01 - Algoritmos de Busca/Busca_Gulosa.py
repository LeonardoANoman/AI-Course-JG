from Vetor_Ordenado import VetorOrdenado
from Grafo import Grafo

class Gulosa:
  def __init__(self, objetivo):
    self.objetivo = objetivo
    self.encontrado = False

  def buscar(self, atual):
    print('-------')
    print('Atual: {}'.format(atual.rotulo))
    atual.visitado = True

    if atual == self.objetivo:
      self.encontrado = True
    else:
      vetor_ordenado = VetorOrdenado(len(atual.adjacentes))
      for adjacente in atual.adjacentes:
        if adjacente.vertice.visitado == False:
          adjacente.vertice.visitado == True
          vetor_ordenado.insere(adjacente.vertice)
      vetor_ordenado.imprime()

      if vetor_ordenado.valores[0] != None:
        self.buscar(vetor_ordenado.valores[0])  

# grafo = Grafo()
# vetor = VetorOrdenado(5)
# vetor.insere(grafo.arad)
# vetor.insere(grafo.craiova)
# vetor.insere(grafo.bucharest)
# vetor.insere(grafo.dobreta)

# busca_gulosa = Gulosa(grafo.bucharest)
# busca_gulosa.buscar(grafo.arad)

