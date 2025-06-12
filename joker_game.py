from random import randrange, choice
import time

class Joker_game:
    def __init__(self, player_name, players):
        self.game_finish = False
        self.winners = []
        self.player_list = [[] for _ in range(players)]
        self.player_name = player_name
        self.cards = []
        # start to distribute 54 poker cards randomly (including 2 jokers)
        suits = ['spades', 'clubs', 'diamonds', 'hearts']
        for suit in suits:
            for i in range(2, 11):
                self.cards.append((suit, str(i)))    
            self.cards.append((suit, 'J'))
            self.cards.append((suit, 'Q'))
            self.cards.append((suit, 'K'))
            self.cards.append((suit, 'A'))
        n = len(self.cards) // players
        for p in self.player_list:
            for _ in range(n):
                p.append(self.cards.pop(randrange(0, len(self.cards))))
        if players == 3:
            self.player_list[randrange(0, players)].append(self.cards.pop())    
        self.player_list[randrange(0, players)].append(('red', 'joker'))
        self.player_list[randrange(0, players)].append(('black', 'joker'))
    
    # sort cards with my quicksort implementation 3625
    def sort_cards(self):
        for p in self.player_list:
            my_quick_sort(p, card_value)
            
    def throw_pairs(self):
        self.sort_cards()
        for i in range(len(self.player_list)):
            current_player = f'Com {i}'
            if i == 0:
                current_player = self.player_name
            index = 0
            while (index + 1) < len(self.player_list[i]):
                if self.player_list[i][index][1] == 'joker':
                    index += 1
                    continue
                if card_value(self.player_list[i][index]) == card_value(self.player_list[i][index + 1]):
                    print(f'{current_player} threw out a pair: {self.player_list[i].pop(index)} & {self.player_list[i].pop(index)}')
                    time.sleep(0.3) 
                    continue
                index += 1

    def player_draw(self):
        while True:
            try:
                p = int(input(f'Choose a Com player to draw a card from! valid input: 1 ~ {len(self.player_list) - 1} (a number): '))
            except:
                print('Invalid input!', 'Try again!')
                continue
            if not 1 <= p <= (len(self.player_list) - 1):
                print('Invalid input!', 'Try again!') 
                continue
            if self.check_win(p):
                print(f'Com {p} has already won, choose others!')
                continue
            if 1 <= p <= (len(self.player_list) - 1):
                break
            print('Invalid input!', 'Try again!')

        self.player_list[0].append(self.player_list[p].pop(randrange(0, len(self.player_list[p]))))
        print(f'You drew a card {self.player_list[0][-1]} from Com {p}')
        print('Your current cards: ')
        print(self.player_list[0])
        time.sleep(0.5)
        print('Throw out pairs if neccessary: ')
        self.throw_pairs()
    
    def player_turn(self):
        self.show_status()
        if self.check_win(0):
            if len(self.winners) == len(self.player_list) - 1:
                self.game_finish = True
                return
            return
        self.player_draw()

    def com_turn(self):
        if self.game_finish:
            return
        print('\n')
        time.sleep(0.3)
        print("Com players' turn")
        time.sleep(0.5)
        for i in range(1, len(self.player_list)):
            if self.check_win(i):
                if len(self.winners) == len(self.player_list) - 1:
                    self.game_finish = True
                    return
                continue
            player_drawn_index = choice(max_index(self.player_list, i))
            self.player_list[i].append(self.player_list[player_drawn_index].pop(randrange(0, len(self.player_list[player_drawn_index]))))
            if player_drawn_index == 0:
                print(f'Com {i} drew a card from {self.player_name}')
            else:    
                print(f'Com {i} drew a card from Com {player_drawn_index}')
            print('Throw out pairs if neccessary: ')
            self.throw_pairs()

    def check_win(self, i):
        if i in self.winners:
            return True
        elif len(self.player_list[i]) == 0:
            self.winners.append(i)
            if i == 0:
                print('You win')
            else:
                print(f'Com {i} wins')
            return True
        return False

    def show_status(self):
        print()
        for i in range(len(self.player_list)):
            if i == 0:
                print(f'{self.player_name} has {len(self.player_list[i])} cards')
                continue
            print(f'Com {i} has {len(self.player_list[i])} cards')
        print()

    def show_final_result(self):
        print()
        loser = (sum({i for i in range(len(self.player_list))})) - sum(self.winners)
        print('Final results: ')
        for i, j in enumerate(self.winners):
            if j == 0:
                print(f'{i + 1}: {self.player_name}')
            else:    
                print(f'{i + 1}: Com {j}')
        if loser == 0:
            print(f'You lose!')
        else:
            print(f'Com {loser} loses')
        print()
        time.sleep(10)

def max_index(l, index):
    max_elem = l[0]
    max_list = [0]
    for i in range(1, len(l)):
        if i == index:
            continue
        if len(l[i]) > len(max_elem):
            max_list.clear()
            max_list.append(i)
            max_elem = l[i]
        elif len(l[i]) == len(max_elem):
            max_list.append(i)
    return tuple(max_list)

def card_value(card_tuple):
    try:
        return int(card_tuple[1])
    except:
        return sum([ord(c) for c in card_tuple[1]])

def partition(arr, fct, start, end):
    p = arr[randrange(start, end - 1)]
    i = start 
    j = end - 1
    while True:
        while fct(arr[i]) < fct(p):
            i += 1
        while fct(arr[j]) > fct(p):
            j -= 1
        if j <= i:
            return j + 1
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

def q_sort(arr, fct, start, end):
    if (end - start) <= 1:
        return
    p = partition(arr, fct, start, end)
    q_sort(arr, fct, start, p)
    q_sort(arr, fct, p, end)

def my_quick_sort(arr, fct):
    q_sort(arr, fct, 0, len(arr))

def game():
    try:
        name = input('Enter your name: ')
        players = int(input('How many Com players (1 ~ 3)? '))
        if not 1 <= players <= 3:
            print('Invalid input :((')
            print('Game is not successfully launched')
            quit()    
    except:
        print('Invalid input :((')
        print('Game is not successfully launched')
        quit()

    g = Joker_game(name, players + 1)
    g.throw_pairs()
    while not g.game_finish:
        g.player_turn()
        g.com_turn()
    g.show_final_result()

game()