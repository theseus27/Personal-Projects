# def calc_profs(am_odds, amounts, bonus_idx):
#     spent = sum(amounts) - BONUS_VAL
#     profits = []
#     for i in range(len(am_odds)):
#         if i == bonus_idx:
#             profits.append(profit(am_odds[i], amounts[i]) - spent)
#         else:
#             profits.append(profit(am_odds[i], amounts[i]) + amounts[i] - spent)
#     return profits