#tela de inicio
wait = input("Pressione para continuar")
print()
print("Iniciando jogo..")
#inserção de usuário
nome = input("Digite o seu úsuario: ")
print()
print("Bem vindo", nome)
#História
print("Você está em mundo cyberpunk, "
"é o assassino mais procurado da cidade "
"e precisa de suprimentos e armas né, "
"então voce pega o seu celular e vai no app da XCORP, "
"a agencia de mercenários que voce trabalha, pedindo um contrato, "
"voce tem 3 alternativas, "
"pegar 1 canivete, uma bazuca ou uma katana, escolha com sabedoria.")
print()
#Interação
canivete = "canivete"
bazuca = "bazuca"
katana = "katana"
nome = input("Qual arma voce deseja?: ")
print(f"Voce escolheu a {nome}, aproveite")
print()
print("Voce avista um inimigo, o que deseja fazer?")
print()
print("Atirar ou fugir")
acao = input("Atirar ou fugir: ")
if acao == "Atirar":
    wait = input("Atirar")
    print("Voce acertou em cheio e ele morreu na horas mas tem reforço vindo mlk")
else:
    wait = input("Fugir")
    print("A policia não te achou sortudo pode fazer o que quiser pela cidade")
#Automação
import random
 
num = random.randint(0, 1) 
if num > 0.5:
    print('UMA GRANADA CAIU NA SUA FRENTE')
else:
    print('SUA MELHOR AMIGA ESTÁ TE LIGANDO')
#Ação  2
if num > 0.5: 
   acao == input("Corra")
else:
   acao == input("Atenda")
#Ação 2.1
if input("Correr?: ") == "Sim":
  print("Voce escapou mas a granada explodiu seu timpano")
else:
  print("Morreu otário")
#Ação 2.2
if input("Atender?: ") == "Sim":
   print("Ela perguntou onde voce tava e voce disse que tava comprando pão")
else:
   print("Ela te odeia agora e te dedurou para as autoridades locais")

