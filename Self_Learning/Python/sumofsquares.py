def sum_of_squares():
    #Ask user to input the total numbers
    total = int (input('Enter the total of the numbers to work with: '))
    number = 1
    while (number <= total):
        input ('Enter number ', number, ':')
        number = number + 1
    return print (number*number)
    
sum_of_squares()
    