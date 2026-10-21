import random as random
import time
from config import *


class Entities():

    def __init__(self, name, profession, level):
        self.name = name
        self.profession = profession
        self.level = level
        self.current_move = None

    def attack_hits(self):
        return random.random() < self.accuracy


    def execute_move(self, entity_move, opposing_entity):
        print('---')
        print(f'{self.name} uses {entity_move}!')
        time.sleep(1)
        self.move_set[entity_move](opposing_entity)

class Player(Entities):

    def print_stats(self):
        print('---')
        print(f"These are your character's stats:")
        time.sleep(1)
        print('=' * equals_divider)
        print(f'Name: {self.name}'
              f'\nClass: {self.profession}'
              f'\nLevel: {self.level}'
              f'\nHP: {self.max_hp}'
              f'\nStrength: {self.strength}'
              f'\nDexterity: {self.dexterity}'
              f'\nArmour: {self.armour}'
              f'\nXP before level-up: {self.xp_before_level_up}'
              f'\nMoveset: {list(self.move_set.keys())}')
        print('=' * equals_divider)

    def choose_move(self):
        print(f'What will {self.name} do: ')
        time.sleep(1)
        move_set_list = list(self.move_set.keys())
        choosing_move = True
        while choosing_move:
            for i in range(len(move_set_list)):
                print(f'{i + 1}. {move_set_list[i]}')
            time.sleep(1)
            try:
                move_index = int(input(f'Please enter a number: ')) - 1
                choosing_move = False
                self.current_move = move_set_list[move_index]
            except (ValueError, IndexError):
                print('Invalid input!')

    def gain_xp(self, enemy):
        xp_calculator = round((((enemy.level * 100) + random.randint(-50, 50)) / 100) * 250)
        self.xp_before_level_up -= xp_calculator
        print(f"You gained {xp_calculator} XP for defeating Lv {enemy.level} {enemy.name}!")

    def stat_reset(self):
        self.max_hp = self.level * 60 + self.level
        self.current_hp = self.max_hp
        self.strength = self.base_strength
        self.armour = self.base_armour
        self.dexterity = self.base_dexterity
        self.accuracy = 0.8
        print(f'Your health and stats have returned to normal!')


    def level_up(self):
        while self.xp_before_level_up <= 0:
            print(f'{self.name} levelled up!')
            self.level += 1
            picking_stats = True
            while picking_stats:
                stats_choice = input(f'Assign your 3 stat points (s/a/d): ').lower()
                if stats_choice == 's':
                    self.base_strength += 3
                    picking_stats = False
                elif stats_choice == 'a':
                    self.base_armour += 3
                    picking_stats = False
                elif stats_choice == 'd':
                    self.base_dexterity += 3
                    picking_stats = False
                else:
                    print('Invalid choice!')
            self.xp_before_level_up = self.level ** 2 * 30 + self.xp_before_level_up








class Knight(Player):
    def __init__(self, name, profession, level):
        super().__init__(name, profession, level)
        self.strength = random.randint(9, 10)
        self.armour = random.randint(11, 12)
        self.dexterity = player_stat_points - self.strength - self.armour
        self.max_hp = 300
        self.current_hp = self.max_hp
        self.xp_before_level_up = self.level ** 2 * 30
        self.accuracy = 0.8
        self.move_set = {'Sword Thrust': self.sword_thrust, 'Sharpen Blade': self.sharpen_blade, 'Fortify': self.fortify}
        self.blocking = False
        self.base_strength = self.strength
        self.base_armour = self.armour
        self.base_dexterity = self.dexterity

    def sword_thrust(self, enemy):
        if not self.attack_hits():
            print('But the attack missed')
        else:
            damage = round(attack_constant * self.strength / enemy.armour)
            enemy.current_hp -= damage
            print(f'It does {damage} damage!')


    def sharpen_blade(self, enemy):
        self.strength *= stat_boost_multiplier
        print(f'{self.name} increases their strength')

    def fortify(self, enemy):
        print(f"{self.name} increased their armour and healed slightly")
        fortify_heal = 50
        if self.current_hp <= self.max_hp - fortify_heal:
            self.current_hp += fortify_heal
        else:
            self.current_hp = self.max_hp
        self.armour *= stat_boost_multiplier * 0.90


class Warrior(Player):
    def __init__(self, name, profession, level):
        super().__init__(name, profession, level)
        self.strength = random.randint(11, 12)
        self.armour = random.randint(9, 10)
        self.dexterity = player_stat_points - self.strength - self.armour
        self.max_hp = 300
        self.current_hp = self.max_hp
        self.xp_before_level_up = self.level ** 2 * 30
        self.accuracy = 0.8
        self.move_set = {'Slash': self.slash, 'Intimidate': self.intimidate, 'Double Strike': self.double_strike}
        self.base_strength = self.strength
        self.base_armour = self.armour
        self.base_dexterity = self.dexterity

    def slash(self, enemy):
        if not self.attack_hits():
            print('But the attack missed')
        else:
            damage = round(attack_constant * self.strength / enemy.armour) + random.randint(-3, 3)
            enemy.current_hp -= damage
            print(f'It does {damage} damage!')

    def intimidate(self, enemy):
        if not self.attack_hits():
            print("But the enemy wasn't intimidated")
        else:
            enemy.strength /= stat_boost_multiplier
            print("The enemy's strength decreased!")

    def double_strike(self, enemy):
        print(f"{self.name} uses his first strike")
        if not self.attack_hits():
            damage_1 = 0
            print('But the attack missed')
        else:
            damage_1 = round(((attack_constant * self.strength / enemy.armour) + random.randint(-3, 3)) / 2)
            print(f'It does {damage_1} damage!')
        print(f"{self.name} uses his second strike")
        if not self.attack_hits():
            damage_2 = 0
            print('But the attack missed')
        else:
            damage_2 = round(((attack_constant * self.strength / enemy.armour) + random.randint(-3, 3)) / 2)
            print(f'It does {damage_2} damage!')
        enemy.current_hp -= (damage_1 + damage_2)



class Rogue(Player):
    def __init__(self, name, profession, level):
        super().__init__(name, profession, level)
        self.strength = random.randint(9, 10)
        self.armour = random.randint(9, 10)
        self.dexterity = player_stat_points - self.strength - self.armour
        self.max_hp = 300
        self.current_hp = self.max_hp
        self.xp_before_level_up = self.level ** 2 * 30
        self.accuracy = 0.8
        self.move_set = {'Quick Stab': self.quick_stab, 'Throwing Knife': self.throwing_knife, 'Smokescreen': self.smokescreen}
        self.base_strength = self.strength
        self.base_armour = self.armour
        self.base_dexterity = self.dexterity

    def quick_stab(self, enemy):
            damage = round((attack_constant * self.strength / enemy.armour) - + random.randint(-3, 3) - 6)
            enemy.current_hp -= damage
            print(f'It does {damage} damage!')

    def throwing_knife(self, enemy):
        self.accuracy *= 0.8
        if not self.attack_hits():
            print('But the knife whistled past the enemy')
        else:
            damage = round((attack_constant * (self.strength + 5) / enemy.armour)) + random.randint(-3, 3)
            enemy.current_hp -= damage
            print(f'It does {damage} damage!')
        self.accuracy /= 0.8

    def smokescreen(self, enemy):
        if not self.attack_hits():
            print('But the attack missed')
        else:
            enemy.accuracy /= stat_boost_multiplier
            print("The enemy's accuracy decreased!")


class Enemy(Entities):

    def print_stats(self):
        print(f'Name: {self.name}'
              f'\nClass: {self.profession}'
              f'\nLevel: {self.level}'
              f'\nHP: {self.max_hp}'
              f'\nStrength: {self.strength}'
              f'\nDexterity: {self.dexterity}'
              f'\nArmour: {self.armour}')

    def choose_move(self):
        self.current_move = (random.choice(list(self.move_set.keys())))


class Bandit(Enemy):
    def __init__(self, name, profession, level):
        super().__init__(name, profession, level)
        self.strength = random.randint(5, 6) + level
        self.armour = random.randint(5, 6) + level
        self.dexterity = enemy_stat_points - self.strength - self.armour + level
        self.max_hp = 30 + level * 50
        self.current_hp = self.max_hp
        self.accuracy = 0.8
        self.move_set = {'Thrust': self.thrust, 'Quick Step': self.quick_step}
        self.blocking = False

    def thrust(self, player):
        if not self.attack_hits():
            print('But the attack missed!')
        else:
            damage = round(attack_constant * self.strength / player.armour) + random.randint(-3, 3)
            player.current_hp -= damage
            print(f'It does {damage} damage!')

    def quick_step(self, player):
        print(f'{self.name} starts dashing from side to side')
        time.sleep(1)
        if player.accuracy >= 0.3:
            print(f"{player.name}'s accuracy fell")
            player.accuracy *= 0.8
        else:
            print(f"{player.name}'s accuracy is already at minimum")



class Zombie(Enemy):
    def __init__(self, name, profession, level):
        super().__init__(name, profession, level)
        self.strength = random.randint(7, 8) + level
        self.armour = random.randint(5, 6) + level
        self.dexterity = enemy_stat_points - self.strength - self.armour + level
        self.max_hp = 40 + level * 50
        self.current_hp = self.max_hp
        self.accuracy = 0.8
        self.move_set = {'Bite': self.bite, 'Feast': self.feast}

    def bite(self, player):
        if not self.attack_hits():
            print('But the attack missed!')
        else:
            damage = round(attack_constant * self.strength / player.armour) + random.randint(-3, 3)
            player.current_hp -= damage
            print(f'{self.name} does {damage} damage!')

    def feast(self, player):
        feast_heal = round(self.max_hp / 4)
        if self.current_hp >= self.max_hp - feast_heal:
            self.current_hp = self.max_hp
        else:
            self.current_hp += feast_heal
        print(f'{self.name} is now at {self.current_hp} HP')



class Skeleton(Enemy):
    def __init__(self, name, profession, level):
        super().__init__(name, profession, level)
        self.strength = random.randint(5, 6) + level
        self.armour = random.randint(7, 8) + level
        self.dexterity = enemy_stat_points - self.strength - self.armour + level
        self.max_hp = 40 + level * 50
        self.current_hp = self.max_hp
        self.accuracy = 0.8
        self.move_set = {'Longbow Shot': self.longbow_shot, 'Harden': self.harden}

    def longbow_shot(self, player):
        if not self.attack_hits():
            print('But the attack missed!')
        else:
            damage = round(attack_constant * self.strength / player.armour) + random.randint(-6, 6)
            player.current_hp -= damage
            print(f'{self.name} does {damage} damage!')

    def harden(self, player):
        print(f"{self.name} increased it's armour")
        self.armour += 1.5
