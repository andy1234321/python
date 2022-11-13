# import random
#
# cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
# is_game = "y"
# while is_game == "y":
#     computer = [random.choice(cards)]
#     player = [random.choice(cards)]
#     score = 0
#     get_card = "y"
#     while get_card == "y":
#         player.append(random.choice(cards))
#         if sum(player) > 21 and 11 in player:
#             for i in range(0, len(player)):
#                 if player[i] == 11:
#                     player[i] = 1
#                     break
#         score = sum(player)
#         print(f"твоя рука:{player}.Очков:{score}")
#         print("первая карта ии:", computer[0])
#         if score > 21:
#             get_card = "n"
#         else:
#             get_card = input("y - взять карту,n-остановиться:")
#
#     while sum(computer) < 17:
#         computer.append(random.choice(cards))
#         if sum(computer) > 21 and 11 in computer:
#             for i in range(0, len(computer)):
#                 if computer[i] == 11:
#                     computer[i] = 1
#                     break
#     score_computer = sum(computer)
#     print("=" * 10)
#     print(f"твоя итоговая рука:{player}.Очков:{score}")
#     print(f"твоя итоговая ии:{computer}.Очков:{score_computer}")
#     if score > 21 and score_computer > 21:
#         print("ничья")
#     elif score > 21:
#         print("ты проиграл")
#     elif score_computer > 21:
#         print("ты умнее чем компьютер")
#     elif score == score_computer:
#         print("ничья")
#     elif score > score_computer:
#         print("ты умнее чем компьютер")
#     else:
#         print("проиграл")
#     is_game = input("играем дальше y-да n-нет")
