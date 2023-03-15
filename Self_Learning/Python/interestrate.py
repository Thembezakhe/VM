#Calculates annual compounded interest enumerate

def future_value(PV, i, n):
    return PV*((1 + i/100))**n

PV = 1000
i = 20
n =2
print('When you borrow R',PV,'at an intrest rate of',i,'% compunded annually', end='')
print(', you will pay back R',round(future_value(PV, i, n)),'after',n,'year(s)')

