import random
from abc import ABC, abstractmethod

class Jogo(ABC):
  @abstractmethod
  def iniciar(self):
    pass
  @abstractmethod
  def jogar(self):
      pass

# Class para armazenar o nome do jogador
class Jogador:
    def __init__(self, nome):
        self.__nome = nome
        self.__pontuacao = 0

    def get_nome(self):
        return self.__nome

    def get_pontuacao(self):
        return self.__pontuacao
# Função para adicionar os pontos e armazenar no self._pontuação para depois exibir no ranking quando solicitado
    def adicionar_pontos(self, pontos):
        self.__pontuacao += pontos
        print(f"Pontos adicionados! Pontuação atual de {self.__nome}: {self.__pontuacao}")

# Propriedade Ranking onde vai puxar algumas funções de Jogador para exibir
class Ranking:
    def __init__(self):
        self.__jogadores = []

    def adicionar_jogador(self, jogador: Jogador):
        self.__jogadores.append(jogador)

    def exibir_ranking(self):
        print("\n=== RANKING TOP 5 ===")

        ranking_ordenado = sorted(self.__jogadores, key=lambda j: j.get_pontuacao(), reverse=True)

# Repetição para exibir em ordem os jogadores
        for i, jogador in enumerate(ranking_ordenado[:5], 1):
            print(f"{i}º - {jogador.get_nome()}: {jogador.get_pontuacao()} pontos")

class JogoAdivinhacao(Jogo):

    def __init__(self, jogador: Jogador):
      self.__numero_secreto = random.randint(1, 100)
      self.__tentativas = 0
      self.__limite = 10
      self.__jogador = jogador

# Sistema de repetição para verificar a dificuldade escolhida e setar o limite de tentativas para o jogador
    def escolher_dificuldade(self):
        print("\nEscolha o nível de dificuldade:")
        print("1 - Fácil (15 tentativas)")
        print("2 - Médio (10 tentativas)")
        print("3 - Difícil (5 tentativas)")

        opcao = input("Opção: ")

        if opcao == '1':
            self.__limite = 15
            print("Nível Fácil selecionado!")
        elif opcao == '3':
            self.__limite = 5
            print("Nível Difícil selecionado!")
        else:
            self.__limite = 10
            print("Nível Médio selecionado (padrão)!")

    def iniciar(self):
      self.escolher_dificuldade()
      print(f"\nJOGO DE ADIVINHAÇÃO - Jogador: {self.__jogador.get_nome()}")
      print("Tente adivinhar o número entre 1 e 100")
      print(f"Você tem {self.__limite} tentativas")

    def jogar(self):

        while self.__tentativas < self.__limite:

            try:
                palpite = int(input("Digite seu palpite: "))
            except:
                print("Digite apenas números!")
                continue

            self.__tentativas += 1

            if palpite == self.__numero_secreto:
              print(f"Parabéns, {self.__jogador.get_nome()}! Você acertou!")
              print("Tentativas usadas: ", self.__tentativas)
              pontos_ganhos = (self.__limite - self.__tentativas + 1) * 10
              self.__jogador.adicionar_pontos(pontos_ganhos)
              return

            elif palpite < self.__numero_secreto:
              print("O número secreto é MAIOR")

            else:
              print("O número secreto é MENOR")

        print("Suas tentativas acabaram!")
        print("O número secreto era:", self.__numero_secreto)

def executar_jogo(jogo: Jogo):
    jogo.iniciar()
    jogo.jogar()

ranking_geral = Ranking()

while True:
    nome = input("\nDigite o nome do jogador (ou 'ranking' para ver o ranking): ")
    if nome.lower() == 'ranking':
        break

    novo_jogador = Jogador(nome)
    jogo = JogoAdivinhacao(novo_jogador)
    executar_jogo(jogo)

    ranking_geral.adicionar_jogador(novo_jogador)

ranking_geral.exibir_ranking()
