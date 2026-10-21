import random
import time
from utils import *
from classes import *
from config import *
def main():

    # start_game()
    running = True
    while running:
        player_name = create_name()
        player = choose_class(player_name)
        player.print_stats()
        continue_confirm()

        floor = 1

        while True:

            enemy = create_enemy(floor)
            generate_floor(floor, enemy.level, enemy.name)
            fighting = True
            while fighting:
                print_all_stats(player, enemy)
                player.choose_move()
                enemy.choose_move()
                entity_list = calculate_order(player, enemy)
                for i, entity in enumerate(entity_list):
                    if i == 0:
                        target = entity_list[1]
                    else:
                        target = entity_list[0]
                    entity.execute_move(entity.current_move, target)
                    if player.current_hp <= 0 or enemy.current_hp <= 0:
                        fighting = False
                        break
            if player.current_hp <= 0:
                break
            print(f"The enemy has been defeated"
                  f"\n YOU WIN!")
            player.gain_xp(enemy)
            time.sleep(1)
            player.level_up()
            time.sleep(1)
            player.stat_reset()
            time.sleep(1)
            player.print_stats()
            continue_confirm()
            floor += 1

        print(f'You have been defeated on floor {floor}')
        print(f'{player.name} has perished')
        restarting = True
        while restarting:
            play_again = input("Would you like to play again? (y/n): ").upper()
            if play_again == 'N':
                running = False
            elif play_again != 'Y':
                print("Invalid input!")
            else:
                restarting = False












if __name__ == '__main__':
    main()