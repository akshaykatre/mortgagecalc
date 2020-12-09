from mortgagecalc import linearmortgage

df = linearmortgage(mortgageamount, 
                    rate=interestrate, 
                    time=repaymentyears)

def plotter():
    