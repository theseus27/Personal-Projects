PLACES = 5
AM_PLACES = 0
DEC_PLACES = 2
IMP_PLACES = 4

def american_to_decimal(am):
    if am < 100 and am > -100:
        return -1
    if am <= -100:
        return round(1 - (100/am), PLACES)
    else:
        return round((am/100) + 1, PLACES)
    
def american_to_implied(am):
    if am < 100 and am > -100:
        return -1
    if am <= -100:
        return round((-1*am) / (-1*am + 100), PLACES)
    else:
        return round(100 / (am + 100), PLACES)
    
def decimal_to_american(dec):
    if dec < 1.01:
        return -1
    if dec < 2: # Returning negative American odds
        return round((-100 / (dec-1)), PLACES)
    else: # Returning positive American odds
        return round(((dec-1) * 100), PLACES)
    
def implied_to_american(imp):
    if imp < 0 or imp > 1:
        return -1
    if imp <= .5: # Returning positive American odds
        return round((100/imp - 100), PLACES)
    else:
        return round((100 / (1 - 1/imp)), PLACES)

def decimal_to_implied(dec):
    if dec < 1.01:
        return -1
    return round(1 / dec, PLACES)

def implied_to_decimal(imp):
    if imp < 0 or imp > 1:
        return -1
    return round(1 / imp, PLACES)

def print_odds(odds, form):
    am = odds
    imp = odds
    dec = odds

    if form == "American":
        imp = round(american_to_implied(am), IMP_PLACES)
        dec = round(american_to_decimal(am), DEC_PLACES)
        am = int(am)
    elif form == "Decimal":
        am = int(decimal_to_american(dec))
        imp = round(decimal_to_implied(dec), IMP_PLACES)
        dec = round(dec, DEC_PLACES)
    elif form == "Implied":
        am = int(implied_to_american(imp))
        dec = round(implied_to_decimal(imp), DEC_PLACES)
        imp = round(imp, IMP_PLACES)
    else:
        print("Invalid form")
        return

    am_str =  ("American: " + str(am)).ljust(20)
    dec_str = ("Decimal: " + str(dec)).ljust(20)
    imp_str = ("Implied: " + str(imp*100) + "%").ljust(20)

    hundred_return = ("$100 Wins: $" + str(round(dec*100 - 100, 2)))

    print(am_str + dec_str + imp_str + hundred_return)

# print(american_to_decimal(240))
# print(american_to_decimal(-198))
# print(american_to_implied(-110))
# print(american_to_implied(160))
# print(decimal_to_american(3.4))
# print(decimal_to_american(1.51))
# print(implied_to_american(.5238))
# print(implied_to_american(.3846))
# print(decimal_to_implied(5.5))
# print(implied_to_decimal(.181))

# print_odds(-198, "American")
# print_odds(1.51, "Decimal")
# print_odds(.6644, "Implied")
# print(both_sides_avg(-240, 198, 55))