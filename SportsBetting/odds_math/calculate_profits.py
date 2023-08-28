from odds_conversion import american_to_decimal as a_to_d
from odds_conversion import american_to_implied as a_to_i
from odds_conversion import decimal_to_american as d_to_a
from odds_conversion import decimal_to_implied as d_to_i
from odds_conversion import implied_to_american as a_to_i
from odds_conversion import implied_to_decimal as i_to_d

def profit(am, bet):
    if am < 100 and am > -100:
        return -1
    if am <= 100:
        return abs(round(bet*100 / am, 2))
    else:
        return round(am*bet / 100, 2)

def both_sides_avg(odds1, odds2, bet1):
    bet2 = 100 - bet1
    prof1 = profit(odds1, bet1) + bet1 - 100
    prof2 = profit(odds2, bet2) + bet2 - 100

    imp1 = a_to_i(odds1)
    imp2 = a_to_i(odds2)

    value = prof1*imp1 + prof2*imp2
    return round(value, 2)

def both_sides_avg_w_predict(odds1, odds2, bet1, pred1):
    bet2 = 100 - bet1
    prof1 = profit(odds1, bet1) + bet1 - 100
    prof2 = profit(odds2, bet2) + bet2 - 100
    pred2 = 1 - pred1

    value = prof1*pred1 + prof2*pred2
    return round(value, 2)

def optimize_odds(odds1, odds2):
    winnings = []
    for i in range(101):
        print(both_sides_avg(odds1, odds2, i))
        winnings.append([i, both_sides_avg(odds1, odds2, i)])

    winnings = sorted(winnings, key=lambda x: x[1], reverse=True)

    print("Best 5 Bets / $100 | Odds1 = " + str(odds1) + " | Odds2 = " + str(odds2))
    for i in range(5):
        print("Bet: " + str(winnings[i][0]) + "  Net: " + str(winnings[i][1]))

def optimize_odds_w_predict(odds1, odds2, pred1):
    winnings = []
    for i in range(101):
        print(both_sides_avg(odds1, odds2, i))
        winnings.append([i, both_sides_avg_w_predict(odds1, odds2, i, pred1)])

    winnings = sorted(winnings, key=lambda x: x[1], reverse=True)

    print("Best 5 Bets / $100 | Odds1 = " + str(odds1) + " | Odds2 = " + str(odds2) + " | Prediction Team1 = " + str(pred1))
    for i in range(5):
        print("Bet: " + str(winnings[i][0]) + "  Net: " + str(winnings[i][1]))

# optimize_odds(-240, 198)
# optimize_odds_w_predict(-240, 198, .55)