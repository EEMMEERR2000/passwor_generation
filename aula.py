import random
from random import choice, randint

escolha_pc =['pedra','papel','tesoura']
escolha_pc_choice = choice(escolha_pc)

loop = True

while loop:
   
    escolha_pc = ['Pedra','Papel','Tesoura']
   
    escolha_pc_choice = choice(escolha_pc)
print('eu escolhi minha jogada, escolha a sua!')
    
print("""
      MENU DE OPÇÕES:
      [1]- Pedra
      [1]- Papel
      [1]- Tesoura
      [1]- Sair do jogo""")

escolha_player = str(input('escolha asua jogada: '))

if escolha_player == '1':
    if escolha_pc_choice == 'Pedra':
        print('-=' * 20)
        print('RESULTADO: EMPATE')
        print('-=' * 20)
    if escolha_pc_choice == 'Papel':
        print('-=' * 20)
        print('RESULTADO: COMPUTADOR VENCEU')
        print('-=' * 20)
    if escolha_pc_choice == 'Tesoura':
        print('-=' * 20)
        print('RESULTADO: EMER VENCEU')
        print('-=' * 20)

elif escolha_player == '2':
    if escolha_pc_choice == 'Pedra':
        print('-=' * 20)
        print('RESULTADO: EMER VENCEU')
        print('-=' * 20)
    if escolha_pc_choice == 'Papel':
        print('-=' * 20)
        print('RESULTADO: EMPATE') 
        print('-=' * 20)
    if escolha_pc_choice == 'Tesoura':
        print('-=' * 20)
        print('RESULTADO: COMPUTADOR VENCEU')
        print('-=' * 20)

elif escolha_pc_choice == '3':
    if escolha_pc_choice == 'Pedra':
        print('-=' * 20)
        print('RESULTADO: COMPUTADOR VENCEU')
        print('-=' * 20)
    if escolha_pc_choice == 'Papel':
        print('-=' * 20)
        print('RESULTADO: EMER VENCEU')
        print('-=' * 20)
    if escolha_pc_choice == 'Tesoura':
        print('-=' * 20)
        print('RESULTADO: EMPATE')
        print('-=' * 20)
        
elif escolha_player == '4':
    loop = False
else:
    print('Opçao Invalida')
    