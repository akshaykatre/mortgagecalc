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
    
def linearrate(principal, mip, years):
    return round( (1200 * (mip*(years*12) - principal))/(principal*(years*12)) , 2)

def annuityrate(principal, mip, years):
    startinterest = 1.0
    ## Lets assume the interest rate can go as high as 25! 
    while startinterest < 25:
        if abs(annuity(principal, startinterest, years)[0][-1] - mip) < 1.0:
            return startinterest
        startinterest += 0.01
    return None 

def interestbounds(principal, years, mip, limits=0):
    #if mtype==None:
    #    return None
    data = {}
    values = (mip-limits, mip, mip+limits)
    lrates = [] 
    arates = [] 
    for v in values:
        lrates.append(linearrate(principal, v, years))
        arates.append(annuityrate(principal, v, years)) 
    data.update({'linear': lrates, 'annuity': arates})
    return data


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

def annuity(principal=0, rate=1.9, time=30):
    timeinmonths = time*12
    
    oner = (1+(rate/(12*100)))**(-timeinmonths)
    onem = 1 - oner
    oned = onem/(rate/(12*100))
    #print(oner, onem, oned, principal, rate, time)
    data = {}
    rprincipal = principal
    fixedpayment = round(principal/oned, 2)
    for months in range(timeinmonths):
        monthlyinterest = mip(rprincipal, rate)
        monthlypayment = fixedpayment # + monthlyinterest
        data.update({months:[round(principal, 2), round(rprincipal,2), round(fixedpayment, 2), 
                round(monthlyinterest,2), round(monthlypayment, 2)]})
        rprincipal -= (fixedpayment - monthlyinterest)

    return data #round(principal/oned, 2)

#def annuitymortgage():
