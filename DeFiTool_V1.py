def APRD():
    global APRDcalc, APRcalc
    APRDcalc = interest
    APRcalc = APRDcalc * 365
    APY_calculator()
    returns()
    multiplier()
    
def APR():
    global APRDcalc, APRcalc
    APRcalc = interest
    APRDcalc = APRcalc / 365
    APY_calculator()
    returns()
    multiplier()

def APY():
    global APYcalc
    PossCompPerYear = 10
    APY_calculator()
    if APYcalc:
        pass

def returns():
    global compoundedReturn, basicReturn, APRcalcList
    #return with compounding
    compoundedReturn = investment
    for a in range(round((compoundsPerYear / 365) * days)):
        compoundedReturn = compoundedReturn + (compoundedReturn  * ((APRDcalc / (compoundsPerYear / 365)) / 100))

    #return with no compounding
    basicReturn = investment + (investment * ((APRDcalc / 100)* days))
    APRcalcList = []
    for b in range(1,366):
        APRcalcList.append(APRDcalc * b)

def multiplier():
    global compMult, basicMult
    #compounded multiplier
    compMult = compoundedReturn / investment
    
    #basic multiplier
    basicMult = basicReturn / investment

def APY_calculator():
    global APYcalc, APYcalcList
    APYcalc = 100
    APYcalcList = []
    for c in range(compoundsPerYear):
        APYcalc = APYcalc + (APYcalc  * ((APRDcalc / (compoundsPerYear / 365)) / 100))
        APYcalcList.append(APYcalc)
    
def result():
    global APYcalc
    if APYcalc < 1000:
        APYcalc = f"{APYcalc:.2f}"
    elif APYcalc >= 1000 and APYcalc < 1000000:
        APYcalc = APYcalc / 1000
        APYcalc = f"{APYcalc:.2f}Tho"
    elif APYcalc >= 1000000 and APYcalc < 1000000000:
        APYcalc = APYcalc / 1000000
        APYcalc = f"{APYcalc:.2f}Mil"
    else:
        APYcalc = APYcalc / 1000000000
        APYcalc = f"{APYcalc:.2f}Bil"
    print("\n" + f"Normal: {basicReturn:.2f}$ ({basicMult:.2f}x)")
    print(f"Compounded: {compoundedReturn:.2f}$ ({compMult:.2f}x)")
    print(f"APY: {APYcalc}%")
    print(f"APRD: {APRDcalc:.2f}%")
    print(f"APR: {APRcalc:.2f}%")

investment = float(input("Investment($): "))
days = int(input("Days: "))
choose = input("[1]APRD [2]APR [3]APY: ")
interest = float(choose[2:])
if choose[0] == "1":
    compoundsPerYear = int(input("Compounds per year: "))
    APRD()
    dailyInterest = float(choose[2:])
elif choose[0] == "2":
    compoundsPerYear = int(input("Compounds per year: "))
    APR()
else:
    APRDcalc = int(input("APRD: "))
    APY()
    
result()