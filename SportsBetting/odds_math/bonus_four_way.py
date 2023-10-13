from odds_conversion import american_to_implied
from optimize_bonus_bet import normalize_probs

BONUS_PERCENT_1 = 1.5
BONUS_PERCENT_2 = 1.25
BONUS_PERCENT_3 = 1.20
BONUS_MAX_1 = 25
BONUS_MAX_2 = 10
BONUS_MAX_3 = 25

#AMT_OPTIONS = [i for i in range(26)]
AMT_OPTIONS = [1, 2, 3, 5, 10, 15, 20, 25]

def calc_profit(odds, amounts, idx1, idx2, idx3):
    cost = sum(amounts)
    profits = []
    for i in range(4):
        prof = odds[i]/100*amounts[i]
        if i == idx1:
            prof *= BONUS_PERCENT_1
        elif i == idx2:
            prof *= BONUS_PERCENT_2
        elif i == idx3:
            prof *= BONUS_PERCENT_3
        prof += amounts[i]
        profits.append(round(prof - cost, 2))
    return profits



def try_amounts(odds, idx1, idx2, idx3):
    probabilites = normalize_probs([american_to_implied(odds[i]) for i in range(len(odds))])

    best_profit = 0
    closest_margin = 100000

    for i in range(len(AMT_OPTIONS)):
        for j in range(len(AMT_OPTIONS)):
            for k in range(len(AMT_OPTIONS)):
                for l in range(len(AMT_OPTIONS)):
                    amts = [AMT_OPTIONS[i], AMT_OPTIONS[j], AMT_OPTIONS[k], AMT_OPTIONS[k]]

                    if amts[idx1] > BONUS_MAX_1 or amts[idx2] > BONUS_MAX_2 or amts[idx3] > BONUS_MAX_3:
                        continue

                    profits = calc_profit(odds, amts, idx1, idx2, idx3)

                    avg_profit = 0
                    for i in range(len(profits)):
                        avg_profit += round(profits[i]*probabilites[i], 2)
                    avg_profit = round(avg_profit, 2)

                    if avg_profit > best_profit and min(profits) >= -4:
                        #print("BEST PROFIT Amounts: " + str(amts) + "  Idxs: [" + str(idx1) + ", " + str(idx2) + ", " + str(idx3) + "]  Profits: " +  str(profits) + " Avg Profit: " + str(avg_profit))
                        best_profit = avg_profit

                    margin = abs(profits[0]-profits[1]) + abs(profits[0]-profits[2]) + abs(profits[0]-profits[3]) + abs(profits[1]-profits[2]) + abs(profits[1]-profits[3]) + abs(profits[2]-profits[3])
                    margin = round(margin, 2)

                    if margin < closest_margin and min(profits) >= -5:
                        #print("BEST MARGIN Amounts: " + str(amts) + "  Idxs: [" + str(idx1) + ", " + str(idx2) + ", " + str(idx3) + "]  Profits: " +  str(profits) + " Avg Profit: " + str(avg_profit))
                        closest_margin = margin

    print(str(idx1) + " " + str(idx2) + " " + str(idx3))
    print(best_profit)

                    




def bonus_four_way():
    odds = [600, 255, 390, 120]

    bonus1_idx = 0
    bonus2_idx = 1
    bonus3_idx = 2
    
    for i in range(4):
        bonus1_idx = i
        for j in range(4):
            if i == 3 and j == 3:
                break
            elif j == i:
                j += 1
                bonus2_idx = j
            else:
                bonus2_idx = j
            for k in range(4):
                if i == 4 and k == 4 or j == 4 and k == 4:
                    break
                elif k == j or k == i:
                    continue
                else:
                    bonus3_idx = 3

                    try_amounts(odds, i, j, k)

#bonus_four_way()

def calc_best_bonuses(odds, idx1, idx2, idx3):
    probabilities = normalize_probs([american_to_implied(odds[i]) for i in range(len(odds))])
    best_profit = 0
    closest_margin = 100000

    for i in range(26):
        for j in range(26):
            for k in range(26):
                for l in range(26):
                    amts = [i, j, k, l]

                    if amts[idx1] > BONUS_MAX_1 or amts[idx2] > BONUS_MAX_2 or amts[idx3] > BONUS_MAX_3:
                        continue

                    profits = calc_profit(odds, amts, idx1, idx2, idx3)

                    avg_profit = 0
                    for i in range(len(profits)):
                        avg_profit += round(profits[i]*probabilities[i], 2)
                    avg_profit = round(avg_profit, 2)

                    if avg_profit > best_profit and min(profits) >= -4:
                        print("BEST PROFIT Amounts: " + str(amts) + "  Idxs: [" + str(idx1) + ", " + str(idx2) + ", " + str(idx3) + "]  Profits: " +  str(profits) + " Avg Profit: " + str(avg_profit))
                        best_profit = avg_profit

                    margin = abs(profits[0]-profits[1]) + abs(profits[0]-profits[2]) + abs(profits[0]-profits[3]) + abs(profits[1]-profits[2]) + abs(profits[1]-profits[3]) + abs(profits[2]-profits[3])
                    margin = round(margin, 2)

                    if margin < closest_margin and min(profits) >= -5:
                        print("BEST MARGIN Amounts: " + str(amts) + "  Idxs: [" + str(idx1) + ", " + str(idx2) + ", " + str(idx3) + "]  Profits: " +  str(profits) + " Avg Profit: " + str(avg_profit))
                        closest_margin = margin

    print(best_profit)

calc_best_bonuses([600, 255, 390, 120], 3, 1, 0)

def calc_one():
    odds = [600, 255, 390, 120]
    probabilities = normalize_probs([american_to_implied(odds[i]) for i in range(len(odds))])
    profits = calc_profit(odds, [5, 10, 15, 20], 3, 1, 0)
    avg_profit = 0
    for i in range(len(profits)):
        avg_profit += round(profits[i]*probabilities[i], 2)
    avg_profit = round(avg_profit, 2)

    rounded_probs = [round(probabilities[i], 4) for i in range(len(probabilities))]
    print("Probs: " + str(rounded_probs) + " Profits: " +  str(profits) + " Avg Profit: " + str(avg_profit))