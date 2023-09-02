num1= int(input('enter the first number: '))
num2= int(input('enter the second number: '))
op = input('enter operator: ')

if op=='+':
    print('the addition is', num1+num2)

elif op=='-':
    print ('the substraction is', num1-num2)

elif op=='*':
    print('the multiplication is', num1*num2)

elif op=='/':
    print('the division is ', abs(num1/num2))


else:
    print('invalid operator')  