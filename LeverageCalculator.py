print("Investering med hävstång!")

InitialCapital = 4400000
HouseValue = 3800000
HouseLoan = 3000000
HouseAmortization = 0#0.02
Inflation = 1.02

Capital = InitialCapital - (HouseValue-HouseLoan)
YearlySavings = 250000

AvanzaLoan = 0
AvanzaLoanFactor = 0.0
AvanzaRate = 0.0389 #0.0294

IskReturn = 1.10 #1.07
IskTax = 0.011

print('År ', 0, 'Kapital = ',Capital, '\t\t Avanzalån = ',AvanzaLoan)

for x in range(1, 5):
    HouseValue = HouseValue*Inflation
    HouseLoan = HouseLoan*(1-HouseAmortization)
   
    AvanzaLoan = Capital*AvanzaLoanFactor
    print('År ', x, 'AvanzaLoan = ',AvanzaLoan)
    AvanzaGain = AvanzaLoan*(IskReturn-1)
    print('År ', x, 'AvanzaGain = ',AvanzaGain)
    #AvanzaLoanInterest = AvanzaLoan*AvanzaRate
    #print('År ', x, 'AvanzaLoanInterest = ',AvanzaLoanInterest)
    AvanzaGainNet = AvanzaLoan*(IskReturn-1) - AvanzaLoan*AvanzaRate
    print('År ', x, 'AvanzaGainNet = ',AvanzaGainNet)
   
    Capital = (Capital+YearlySavings)*IskReturn + AvanzaGainNet
    Capital = Capital*(1-IskTax)
    print('År ', x, 'Kapital = ',Capital)

print('\n')
print('Husvärde = \t', HouseValue)
print('Huslån = \t', HouseLoan)
print('Kapital = \t', Capital)
print('Totalt = \t', Capital+HouseValue-HouseLoan)
print('Avanzalån = \t', AvanzaLoan)

print('\n')
Roe = Capital / 1700000#3600000
RoeTot = (Capital+HouseValue-HouseLoan) / 4400000
print('Return on Equity = \t\t\t', Roe, '\tPer year = ', pow(Roe,1/x))
#print('Return on Equity (incl. house) = \t', RoeTot, '\tPer year = ', pow(RoeTot,1/x))