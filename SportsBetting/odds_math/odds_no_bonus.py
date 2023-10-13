CAP = 5000
from odds_conversion import american_to_implied
from calculate_profits import profit
HIGH_AMOUNTS = [i for i in range(1, 1000)]
LOW_AMOUNTS = [i for i in range(1, 51)]

def calc_profs(odds, amts):
    spent = sum(amts)
    profits = []
    for i in range(len(odds)):
            profits.append(profit(odds[i], amts[i]) - spent + amts[i])
    #print(odds)
    return profits


def try_amounts(odds):
    best_prof = -10000
    best_profs = []
    best_amts = []

    min_loss = 100
    min_loss_profs = []
    min_loss_amts = []

    best_prof_no_loss = -10000
    bpnl_profs = []
    bpnl_amts = []

    amts = []
    for i in range(len(HIGH_AMOUNTS)):
        for j in range(len(LOW_AMOUNTS)):
                amts = [HIGH_AMOUNTS[i], LOW_AMOUNTS[j]]
                profits = calc_profs(odds, amts)
                loss = round((min(profits) / sum(amts) * -100), 3)

                if sum(profits) >= best_prof and min(profits) >= -.02*sum(amts):
                      best_prof = sum(profits)
                      best_profs = [profits[x] for x in range(len(profits))]
                      best_amts = [amts[x] for x in range(len(amts))]

                if loss <= min_loss:
                    min_loss = loss
                    min_loss_amts = [amts[x] for x in range(len(amts))]
                    min_loss_profs = [profits[x] for x in range(len(profits))]

                if sum(profits) >= best_prof_no_loss and min(profits) >= 0:
                    best_prof_no_loss = sum(profits)
                    bpnl_amts = [amts[x] for x in range(len(amts))]
                    bpnl_profs = [profits[x] for x in range(len(profits))]

    if best_prof != -10000:
        print("Best profit: " + str(best_prof) + "  Amts " + str(best_amts) + "  yields " + str(best_profs))

    if best_prof_no_loss != -10000:
        print("Best Profit No Loss: " + str(best_prof_no_loss) + " Amts " + str(bpnl_amts) + " yields " + str(bpnl_profs))

    
    print("Min loss:    " + str(min_loss) + "  Amts " + str(min_loss_amts) + " yields " + str(min_loss_profs))

def optimize():
      # Odds need to go [super negative, super positive]
      #odds = [[-5000, 1800], [-2800, 850], [-4000, 1100], [-2500, 800], [-80000, 2750], [-3500, 1550], [-8000, 2600], [-1800, 900], [-1600, 900], [-10000, 1300], [-7500, 2200]]
      odds = [[-2100, 1200]]

        # -7500 vs 2200 - Draftkings DET vs KC, Jason Cabinda TD

      for pair in odds:
            print("Odds: " + str(pair))
            try_amounts(pair)
            print("\n")

optimize()