def arithmetic(num1, num2, math):
    if math == '+':
        return num1 + num2
    elif math == '-':
         return num1 - num2
    elif math == '*':
        return num1 * num2
    elif math == '/':
        return num1 / num2
    else:
        return 'неизвестная операция'
print (arithmetic(3,5,'_'))