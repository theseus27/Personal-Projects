import sys
sys.path.insert(0, "odds_math")
from odds_conversion import american_to_implied
from calculate_profits import profit

BONUS_VAL = 20
PROFIT_BOOST = 1.5
TEST_AMOUNTS = [.5*i for i in range(2*BONUS_VAL*2+1)] # 50c intervals
#TEST_AMOUNTS = [i for i in range(BONUS_VAL*2+1)] # $1 intervals

BEST_OF_BOTH_THRESHOLD = .6

##### HELPER FUNCTIONS #####
def print_stats(avg_profit, profits, amounts, probs):
    print_str = "$"  + str(avg_profit) + " -- Bets: " + str(amounts) + "\n"

    print_str += "     "
    for i in range(len(probs)):
        print_str += str(round(probs[i]*100, 2)) + "%  $" + str(round(profits[i], 2)) + "  ||   "
    return print_str[:-5]

def normalize_probs(probs):
    new_probs = []
    total = sum(probs)
    for i in range(len(probs)):
        new_probs.append(probs[i] / total)
    return new_probs

def calc_profs(am_odds, amounts, bonus_idx):
    spent = sum(amounts) - BONUS_VAL
    profits = []
    for i in range(len(am_odds)):
        if i == bonus_idx:
            profits.append(profit(am_odds[i], amounts[i]) - spent)
        else:
            profits.append(profit(am_odds[i], amounts[i])*PROFIT_BOOST + amounts[i] - spent)
    return profits

##### OPTIMIZE PROFIT #####
def optimize_avg_profit_4_way(am_odds, probs):
    optimal_bets = []
    optimal_bonus_idx = 0
    max_profit = 0

    for i in range(len(am_odds)):
        amounts = [0 for _ in range(len(am_odds))]
        amounts[i] = BONUS_VAL

        changable_idxs = [j for j in range(len(am_odds))]
        changable_idxs.remove(i)

        for j in range(len(TEST_AMOUNTS)):
            for k in range(len(TEST_AMOUNTS)):
                for m in range(len(TEST_AMOUNTS)):
                    amounts[changable_idxs[0]] = round(TEST_AMOUNTS[j], 2)
                    amounts[changable_idxs[1]] = round(TEST_AMOUNTS[k], 2)
                    amounts[changable_idxs[2]] = round(TEST_AMOUNTS[m], 2)
                    
                    profs = calc_profs(am_odds, amounts, i)
                    avg_profit = 0
                    for x in range(len(probs)):
                        avg_profit += (probs[x]*profs[x])
    
                    avg_profit = round(avg_profit, 2)

                    if min(profs) > 0 and avg_profit > max_profit:
                        max_profit = avg_profit
                        optimal_bets = [amounts[x] for x in range(len(amounts))]
                        optimal_bonus_idx = i
    
    return optimal_bets, optimal_bonus_idx, max_profit

def optimize_avg_profit_3_way(am_odds, probs):
    optimal_bets = []
    optimal_bonus_idx = 0
    max_profit = 0

    for i in range(len(am_odds)):
        amounts = [0 for _ in range(len(am_odds))]
        amounts[i] = BONUS_VAL

        changable_idxs = [j for j in range(len(am_odds))]
        changable_idxs.remove(i)

        for j in range(len(TEST_AMOUNTS)):
            for k in range(len(TEST_AMOUNTS)):
                amounts[changable_idxs[0]] = round(TEST_AMOUNTS[j], 2)
                amounts[changable_idxs[1]] = round(TEST_AMOUNTS[k], 2)
                
                profs = calc_profs(am_odds, amounts, i)
                avg_profit = 0
                for x in range(len(probs)):
                    avg_profit += (probs[x]*profs[x])

                avg_profit = round(avg_profit, 2)

                if min(profs) > 0 and avg_profit > max_profit:
                    max_profit = avg_profit
                    optimal_bets = [amounts[x] for x in range(len(amounts))]
                    optimal_bonus_idx = i
    
    return optimal_bets, optimal_bonus_idx, max_profit

def optimize_avg_profit_2_way(am_odds, probs):
    optimal_bets = []
    optimal_bonus_idx = 0
    max_profit = 0

    for i in range(len(am_odds)):
        amounts = [0 for _ in range(len(am_odds))]
        amounts[i] = BONUS_VAL

        changable_idxs = [j for j in range(len(am_odds))]
        changable_idxs.remove(i)

        for j in range(len(TEST_AMOUNTS)):
            amounts[changable_idxs[0]] = round(TEST_AMOUNTS[j], 2)
            
            profs = calc_profs(am_odds, amounts, i)
            
            avg_profit = 0
            for x in range(len(probs)):
                avg_profit += (probs[x]*profs[x])
            avg_profit = round(avg_profit, 2)
            
            #print("Amounts: " + str(amounts) + "  Profs: " + str(profs) + "  AvgProf: " + str(avg_profit))

            if min(profs) > 0 and avg_profit > max_profit:
                max_profit = avg_profit
                optimal_bets = [amounts[x] for x in range(len(amounts))]
                optimal_bonus_idx = i
    
    return optimal_bets, optimal_bonus_idx, max_profit

##### EVEN DISTRIBUTION #####
def even_distro_profits_4_way(am_odds, probs):
    optimal_bets = []
    optimal_bonus_idx = 0
    smallest_diff = BONUS_VAL * 100000

    for i in range(len(am_odds)):
        amounts = [0 for _ in range(len(am_odds))]
        amounts[i] = BONUS_VAL

        changable_idxs = [j for j in range(len(am_odds))]
        changable_idxs.remove(i)

        for j in range(len(TEST_AMOUNTS)):
            for k in range(len(TEST_AMOUNTS)):
                for m in range(len(TEST_AMOUNTS)):
                    amounts[changable_idxs[0]] = round(TEST_AMOUNTS[j], 2)
                    amounts[changable_idxs[1]] = round(TEST_AMOUNTS[k], 2)
                    amounts[changable_idxs[2]] = round(TEST_AMOUNTS[m], 2)
                    
                    profs = calc_profs(am_odds, amounts, i)

                    diff = abs(profs[0]-profs[1]) + abs(profs[0]-profs[2]) + abs(profs[0]-profs[3]) + abs(profs[1]-profs[2]) + abs(profs[1]-profs[3]) + abs(profs[2]-profs[3])

                    diff = round(diff, 2)

                    if min(profs) > 0 and diff < smallest_diff:
                        smallest_diff = diff
                        optimal_bets = [amounts[x] for x in range(len(amounts))]
                        optimal_bonus_idx = i

    return optimal_bets, optimal_bonus_idx, smallest_diff

def even_distro_profits_3_way(am_odds, probs):
    optimal_bets = []
    optimal_bonus_idx = 0
    smallest_diff = BONUS_VAL * 100000

    for i in range(len(am_odds)):
        amounts = [0 for _ in range(len(am_odds))]
        amounts[i] = BONUS_VAL

        changable_idxs = [j for j in range(len(am_odds))]
        changable_idxs.remove(i)

        for j in range(len(TEST_AMOUNTS)):
            for k in range(len(TEST_AMOUNTS)):
                amounts[changable_idxs[0]] = round(TEST_AMOUNTS[j], 2)
                amounts[changable_idxs[1]] = round(TEST_AMOUNTS[k], 2)
                
                profs = calc_profs(am_odds, amounts, i)

                diff = abs(profs[0]-profs[1]) + abs(profs[0]-profs[2]) + abs(profs[1]-profs[2])

                diff = round(diff, 2)

                if min(profs) > 0 and diff < smallest_diff:
                    smallest_diff = diff
                    optimal_bets = [amounts[x] for x in range(len(amounts))]
                    optimal_bonus_idx = i

    return optimal_bets, optimal_bonus_idx, smallest_diff

def even_distro_profits_2_way(am_odds, probs):
    optimal_bets = []
    optimal_bonus_idx = 0
    smallest_diff = BONUS_VAL * 100000

    for i in range(len(am_odds)):
        amounts = [0 for _ in range(len(am_odds))]
        amounts[i] = BONUS_VAL

        changable_idxs = [j for j in range(len(am_odds))]
        changable_idxs.remove(i)

        for j in range(len(TEST_AMOUNTS)):
            amounts[changable_idxs[0]] = round(TEST_AMOUNTS[j], 2)
            
            profs = calc_profs(am_odds, amounts, i)

            #print("Amounts: " + str(amounts) + "  Profs: " + str(profs))

            diff = abs(profs[0]-profs[1])

            diff = round(diff, 2)

            if min(profs) > 0 and diff < smallest_diff:
                smallest_diff = diff
                optimal_bets = [amounts[x] for x in range(len(amounts))]
                optimal_bonus_idx = i

    return optimal_bets, optimal_bonus_idx, smallest_diff

##### BEST OF BOTH WORLDS #####
def best_of_both_4_way(am_odds, probs, max_prof, even_prof):
    for i in range(len(am_odds)):
        amounts = [0 for _ in range(len(am_odds))]
        amounts[i] = BONUS_VAL

        changable_idxs = [j for j in range(len(am_odds))]
        changable_idxs.remove(i)

        for j in range(len(TEST_AMOUNTS)):
            for k in range(len(TEST_AMOUNTS)):
                for m in range(len(TEST_AMOUNTS)):
                    amounts[changable_idxs[0]] = round(TEST_AMOUNTS[j], 2)
                    amounts[changable_idxs[1]] = round(TEST_AMOUNTS[k], 2)
                    amounts[changable_idxs[2]] = round(TEST_AMOUNTS[m], 2)
                    
                    profs = calc_profs(am_odds, amounts, i)

                    diff = abs(profs[0]-profs[1]) + abs(profs[0]-profs[2]) + abs(profs[0]-profs[3]) + abs(profs[1]-profs[2]) + abs(profs[1]-profs[3]) + abs(profs[2]-profs[3])
                    diff = round(diff, 2)

                    avg_profit = 0
                    for x in range(len(probs)):
                        avg_profit += (probs[x]*profs[x])
                    avg_profit = round(avg_profit, 2)

                    if min(profs) >= BEST_OF_BOTH_THRESHOLD*max_prof or min(profs) >= even_prof:
                        print(print_stats(avg_profit, profs, amounts, probs))

def best_of_both_3_way(am_odds, probs, max_prof, even_prof):
    for i in range(len(am_odds)):
        amounts = [0 for _ in range(len(am_odds))]
        amounts[i] = BONUS_VAL

        changable_idxs = [j for j in range(len(am_odds))]
        changable_idxs.remove(i)

        for j in range(len(TEST_AMOUNTS)):
            for k in range(len(TEST_AMOUNTS)):
                amounts[changable_idxs[0]] = round(TEST_AMOUNTS[j], 2)
                amounts[changable_idxs[1]] = round(TEST_AMOUNTS[k], 2)
                
                profs = calc_profs(am_odds, amounts, i)

                diff = abs(profs[0]-profs[1]) + abs(profs[0]-profs[2]) + abs(profs[1]-profs[2])
                diff = round(diff, 2)

                avg_profit = 0
                for x in range(len(probs)):
                    avg_profit += (probs[x]*profs[x])
                avg_profit = round(avg_profit, 2)

                if min(profs) >= BEST_OF_BOTH_THRESHOLD*max_prof or min(profs) >= even_prof:
                    print(print_stats(avg_profit, profs, amounts, probs))

def best_of_both_2_way(am_odds, probs, max_prof, even_prof):
    for i in range(len(am_odds)):
        amounts = [0 for _ in range(len(am_odds))]
        amounts[i] = BONUS_VAL

        changable_idxs = [j for j in range(len(am_odds))]
        changable_idxs.remove(i)

        for j in range(len(TEST_AMOUNTS)):
            amounts[changable_idxs[0]] = round(TEST_AMOUNTS[j], 2)
            
            profs = calc_profs(am_odds, amounts, i)

            diff = abs(profs[0]-profs[1])
            diff = round(diff, 2)

            avg_profit = 0
            for x in range(len(probs)):
                avg_profit += (probs[x]*profs[x])
            avg_profit = round(avg_profit, 2)

            if min(profs) >= BEST_OF_BOTH_THRESHOLD*max_prof or min(profs) >= even_prof:
                print(print_stats(avg_profit, profs, amounts, probs))


def optimize_avg_profit(am_odds, probs):
    optimal_bets = []
    optimal_bonus_idx = 0
    max_profit = 0

    if len(am_odds) == 4:
        optimal_bets, optimal_bonus_idx, max_profit = optimize_avg_profit_4_way(am_odds, probs)
    elif len(am_odds) == 3:
        optimal_bets, optimal_bonus_idx, max_profit = optimize_avg_profit_3_way(am_odds, probs)
    elif len(am_odds) == 2:
        optimal_bets, optimal_bonus_idx, max_profit = optimize_avg_profit_2_way(am_odds, probs)
    else:
        print("Illegal odds length of " + str(len(am_odds)))

    profs = calc_profs(am_odds, optimal_bets, optimal_bonus_idx)

    return max_profit, optimal_bets, profs

def even_profit_distribution(am_odds, probs):
    optimal_bets = []
    optimal_bonus_idx = 0
    smallest_diff = BONUS_VAL*100000

    if len(am_odds) == 4:
        optimal_bets, optimal_bonus_idx, smallest_diff = even_distro_profits_4_way(am_odds, probs)
    elif len(am_odds) == 3:
        optimal_bets, optimal_bonus_idx, smallest_diff = even_distro_profits_3_way(am_odds, probs)
    elif len(am_odds) == 2:
        optimal_bets, optimal_bonus_idx, smallest_diff = even_distro_profits_2_way(am_odds, probs)
    else:
        print("Illegal odds length of " + str(len(am_odds)))

    profs = calc_profs(am_odds, optimal_bets, optimal_bonus_idx)
    avg_prof = 0
    for i in range(len(probs)):
        avg_prof += (probs[i]*profs[i])
    avg_prof = round(avg_prof, 2)

    return avg_prof, optimal_bets, profs

def best_of_both(am_odds, probs, max_prof, even_prof):
    if len(am_odds) == 4:
        best_of_both_4_way(am_odds, probs, max_prof, even_prof)
    elif len(am_odds) == 3:
        best_of_both_3_way(am_odds, probs, max_prof, even_prof)
    elif len(am_odds) == 2:
        best_of_both_2_way(am_odds, probs, max_prof, even_prof)
    else:
        print("Illegal odds length of " + str(len(am_odds)))

# Always write odds best to worst
def main():
    odds_list = [[-245, 200], [-102, -118]]

    # -300, 250 => 19           Braves/Pirates Moneyline
    # -250, 205 => 17.50        Rockies/Brewers Moneyline        
    # 330, 420, 230, 175 => 14  Giants/LAA Run Lines/Total Runs
    # -128, 370, [245] => 48     Rangers/A's Race to 5
    # 148, 225, [184] => 40     Giants/A's Race to 5
    # -170, 270, [490] => 30    Rangers A's Race to 4
    # -215, 360, [520] => 33    Braves/Pirates Race to 4
    # -154, 440, [265] => 47    Braves/Pirates Race to 5

    # Look for the best Race to x runs where the last odds is > 400

    for odds in odds_list:
        probs = normalize_probs([american_to_implied(odds[i]) for i in range(len(odds))])

        max_profit, max_bets, max_profs = optimize_avg_profit(odds, probs)
        even_prof, even_bets, even_profs = even_profit_distribution(odds, probs)

        print(odds)
        print("MAX: " + print_stats(max_profit, max_profs, max_bets, probs))
        print("EVEN: " + print_stats(even_prof, even_profs, even_bets, probs))

        print("Best of Both")
        best_of_both(odds, probs, max_profit, even_prof)
        print("\n")

def tester():
    odds = [-245, 200]
    probs = normalize_probs([american_to_implied(odds[i]) for i in range(len(odds))])

    print("BONUS BET on first, odds are [" + str(odds[0]) + ", " + str(odds[1]) + "]")
    for j in range(len(TEST_AMOUNTS)):
        amounts = [BONUS_VAL, TEST_AMOUNTS[j]]
        profs = calc_profs(odds, amounts, 0)
        avg_profit = 0
        for x in range(len(probs)):
            avg_profit += (probs[x]*profs[x])
        avg_profit = round(avg_profit, 2)

        print(print_stats(avg_profit, profs, amounts, probs))

    print("\n\nBONUS BET on second, odds are [" + str(odds[0]) + ", " + str(odds[1]) + "]")
    for j in range(len(TEST_AMOUNTS)):
        amounts = [TEST_AMOUNTS[j], BONUS_VAL]
        profs = calc_profs(odds, amounts, 1)
        avg_profit = 0
        for x in range(len(probs)):
            avg_profit += (probs[x]*profs[x])
        avg_profit = round(avg_profit, 2)

        print(print_stats(avg_profit, profs, amounts, probs))

#main()
tester()