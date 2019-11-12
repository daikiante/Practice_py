import utils
# random module import
import random

print('''Let's start Rock-paper-scissors''')
player_name = input('Enter your name：')
print('What is your choice？（0: Rock, 1: Scissors, 2: Paper）')
player_hand = int(input('Enter the number：'))

if utils.validate(player_hand):
    # randintを用いて0から2までの数値を取得し、変数computer_handに代入してください
    computer_hand = random.randint(0,2)
    
    if player_name == '':
        utils.print_hand(player_hand)
    else:
        utils.print_hand(player_hand, player_name)

    utils.print_hand(computer_hand, 'Computer')
    
    result = utils.judge(player_hand, computer_hand)
    print('Result is ' + result)
else:
    print('Choise ONLY number')
