import time
from classes import *
from config import *


def continue_confirm():
    time.sleep(1)
    return input((f'Press ENTER to continue'))


def start_game():
    print(f'Welcome to Endless Tower RPG!')
    time.sleep(1)
    print(f'You will fight against enemies on each floor of the tower.')
    time.sleep(2)
    print(f'Each floor will get progressively harder')
    continue_confirm()


def create_name():
    player_name = input("Please enter your character's name: ").upper()
    return player_name


def choose_class(player_name):
    picking_class = True
    print("Please pick your character's class: ")
    while picking_class:
        for i in range(len(player_classes)):
            print(f'{i + 1}. {player_classes[i]}')
        player_class_index = int(input('Please enter a number: ')) - 1
        try:
            if player_classes[player_class_index] == 'Knight':
                player = Knight(player_name, player_classes[player_class_index], 5)
            elif player_classes[player_class_index] == 'Warrior':
                player = Warrior(player_name, player_classes[player_class_index], 5)
            elif player_classes[player_class_index] == 'Rogue':
                player = Rogue(player_name, player_classes[player_class_index], 5)
            picking_class = False
        except (ValueError, IndexError):
            print('Invalid choice!')
            time.sleep(1)
    return player

def entering_tower():
    print('You approach the doors to the endless tower')
    print('The never-ending battle starts here')
    print(f''
          f'\n'
          f'\n')


def create_enemy(floor):
    enemy_type = random.choice(enemy_classes)
    if enemy_type == 'Bandit':
        return Bandit(enemy_type, enemy_type, random.randint(1, 3) + floor)
    if enemy_type == 'Zombie':
        return Zombie(enemy_type, enemy_type, random.randint(1, 3) + floor)
    if enemy_type == 'Skeleton':
        return Skeleton(enemy_type, enemy_type, random.randint(1, 3) + floor)


def generate_floor(current_floor, enemy_level, floor_enemy):
    print(f'You have entered floor {current_floor}')
    time.sleep(1)
    print(f'You are attacked by a level {enemy_level} {floor_enemy}!')
    time.sleep(1)


def print_all_stats(player, enemy):
    print('=' * equals_divider)
    print(f'{player.name}   Lv {player.level}'
          f'\n{round(player.current_hp)} / {player.max_hp} HP')
    print('=' * equals_divider)
    print(f'{enemy.name}   Lv {enemy.level}'
          f'\n{round(enemy.current_hp)} / {enemy.max_hp} HP')
    print('=' * equals_divider)


def player_move(move, player, enemy_name):
    if move == 'Sword Thrust':
        enemy_damage = player.sword_thrust()
    return enemy_damage

def calculate_order(player, enemy):
    if player.dexterity != enemy.dexterity:
        entities_dict = {player.dexterity: player, enemy.dexterity: enemy}
        entity_dexterities = list(entities_dict.keys())
        entity_dexterities.sort(reverse=True)
        ordered_dict = {dexterities: entities_dict[dexterities] for dexterities in entity_dexterities}
        return list(ordered_dict.values())
    else:
        entity_list = [player, enemy]
        random.shuffle(entity_list)
        return entity_list





