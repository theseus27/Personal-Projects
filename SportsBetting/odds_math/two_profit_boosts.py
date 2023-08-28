import sys
sys.path.insert(0, "odds_math")
from odds_conversion import american_to_implied
from calculate_profits import profit

PROFIT_BOOST_1 = 1.5
PROFIT_BOOST_2 = 1.25
MAX_BET_1 = 25
MAX_BET_2 = 25

TEST_AMOUNTS_1 = [i for i in range(MAX_BET_1+1)] # $1 intervals
TEST_AMOUNTS_2 = [i for i in range(MAX_BET_2+1)]

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

# Expects to take odds and amounts as 'profit boost 1' first
def calc_profs(am_odds, amounts):
    spent = sum(amounts)
    profits = []
    profits.append(profit(am_odds[0], amounts[0])*PROFIT_BOOST_1 - spent)
    profits.append(profit(am_odds[1], amounts[1])*PROFIT_BOOST_2 - spent)
    return profits

##### OPTIMIZE PROFIT #####
def optimize_avg_profit(am_odds, probs):
    optimal_bets = [-1, -1]
    best_profits = [-1, -1]
    max_profit = 0

    amounts = [0, 0]
    for i in range(len(TEST_AMOUNTS_1)):
        amounts[0] = TEST_AMOUNTS_1[i]
        for j in range(len(TEST_AMOUNTS_2)):
            amounts[1] = TEST_AMOUNTS_2[j]
            
            profs = calc_profs(am_odds, amounts)
            
            avg_profit = 0
            for x in range(len(probs)):
                avg_profit += (probs[x]*profs[x])
            avg_profit = round(avg_profit, 2)

            if min(profs) > 0 and avg_profit > max_profit:
                max_profit = avg_profit
                optimal_bets = [amounts[x] for x in range(len(amounts))]
                best_profits = [profs[x] for x in range(len(profs))]
    
    return max_profit, optimal_bets, best_profits

##### EVEN DISTRIBUTION #####
def even_profits(am_odds, probs):
    optimal_bets = [-1, -1]
    smallest_diff = MAX_BET_1 * 100000
    optimal_profits = [-1, -1]

    amounts = [0, 0]
    for i in range(len(TEST_AMOUNTS_1)):
        amounts[0] = TEST_AMOUNTS_1[i]
        for j in range(len(TEST_AMOUNTS_2)):
            amounts[1] = TEST_AMOUNTS_2[j]
            
            profs = calc_profs(am_odds, amounts)

            diff = abs(profs[0]-profs[1])

            diff = round(diff, 2)

            if min(profs) > 0 and diff < smallest_diff:
                smallest_diff = diff
                optimal_bets = [amounts[x] for x in range(len(amounts))]
                optimal_profits = [profs[x] for x in range(len(profs))]

    avg_prof = 0
    for i in range(len(probs)):
        avg_prof += (probs[i]*optimal_profits[i])
    avg_prof = round(avg_prof, 2)
    return avg_prof, optimal_bets, optimal_profits

##### BEST OF BOTH WORLDS #####
def best_of_both(am_odds, probs, max_prof, even_prof):
    print_strings = []

    amounts = [0, 0]
    for i in range(len(TEST_AMOUNTS_1)):
        amounts[0] = TEST_AMOUNTS_1[i]
        for j in range(len(TEST_AMOUNTS_2)):
            amounts[1] = TEST_AMOUNTS_2[j]
            
            profs = calc_profs(am_odds, amounts)

            diff = abs(profs[0]-profs[1])
            diff = round(diff, 2)

            avg_profit = 0
            for x in range(len(probs)):
                avg_profit += (probs[x]*profs[x])
            avg_profit = round(avg_profit, 2)

            if min(profs) >= BEST_OF_BOTH_THRESHOLD*max_prof or min(profs) >= even_prof:
                print_strings.append([avg_profit, print_stats(avg_profit, profs, amounts, probs)])

    print_strings = sorted(print_strings, key=lambda x: x[0], reverse=True)
    for i in range(min(5, len(print_strings))):
        print(print_strings[i][1])


# Always write odds best to worst
def main():
    odds_list = [[-245, 200], [-102, -118], [145, 120], [190, 170]]

    for odds in odds_list:
        probs = normalize_probs([american_to_implied(odds[i]) for i in range(len(odds))])

        max_profit, max_bets, max_profs = optimize_avg_profit(odds, probs)
        even_prof, even_bets, even_profs = even_profits(odds, probs)

        print(odds)
        print("MAX: " + print_stats(max_profit, max_profs, max_bets, probs))
        print("EVEN: " + print_stats(even_prof, even_profs, even_bets, probs))

        print("Best of Both")
        best_of_both(odds, probs, max_profit, even_prof)
        print("\n")

main()