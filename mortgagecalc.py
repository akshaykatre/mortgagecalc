import pandas 

def fpp(principal, time):
    ''' fixed principal payment (fpp)
    Is the amount that is paid back toward the principal every month

    Remain unchanged for linear mortgage

    Principal is the amount borrowed
    Time should be provided in months
    ''' 
    return principal/time


def mip(principal, rate):
    ''' 
    Monthly interest payment (mip)
    The interest paid every month 

    rate is defined in percentage and annually, therefore needs adjustment
            for monthly calculations
    ''' 
    return principal*(rate/100)/12


def linearmortgage(principal=0, rate=1.9, time=30):
    timeinmonths = time*12
    rprincipal = principal
    fixedpayment = fpp(rprincipal, timeinmonths)
    data = {}
    for months in range(timeinmonths):
        monthlyinterest =  mip(rprincipal, rate)
        monthlypayment = fixedpayment + monthlyinterest
       # print(round(principal, 2), round(rprincipal,2), round(fixedpayment, 2), 
       #         round(monthlyinterest,2), round(monthlypayment, 2))
        data.update({months:[round(principal, 2), round(rprincipal,2), round(fixedpayment, 2), 
                round(monthlyinterest,2), round(monthlypayment, 2)]})
        rprincipal -= fixedpayment
    return data 

def annuity(principal, rate, time):
    oner = (1+(rate/12))**(-time*12)
    onem = 1 - oner
    oned = onem/(rate/12)
    #print(oner, onem, oned, principal, rate, time)
    return round(principal/oned, 2)

#def annuitymortgage():
