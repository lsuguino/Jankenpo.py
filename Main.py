import random


print('Vamos jogar Jankenpô?')

tesoura = '''
Tesoura:
   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.

'''

pedra = '''
Pedra:
       _____
    /\| | | |
   / /|_|_|_|
   \        |
    \_______/
    /______/

'''
papel = '''
Papel:
  .--""--.___.._
 (  <__>  )     `-.
 |`--..--'|      <|
 |       :|       /
 |       :|--""-./
 `.__  __;' o!O
     ""     

'''
jankenpo = [pedra, papel, tesoura]

user_choice = int(input('Qual você escolhe? \nDigite: "0" para Pedra\n"1" para Papel\n"2" Tesoura\n'))
if user_choice >= 0 and user_choice <= 2:
    print('Você escolheu')
    print(jankenpo[user_choice])

pc_choice = random.randint(a=0, b=2)
print("o NPC escolheu")
print(jankenpo[pc_choice])
if user_choice >= 3 or user_choice < 0:
    print('Você escreveu um número inválido')
elif pc_choice > user_choice:
    print("Você GANHOU!")
elif user_choice == 2 and pc_choice == 0:
    print("Você PERDEU!")
elif user_choice == 1 and pc_choice == 0:
    print("Você GANHOU!")
elif user_choice > pc_choice:
    print("Você GANHOU!")
elif user_choice == pc_choice:
    print("EMPATE!")

