print('Здравствуйте.')
print('Привет.')
start_phrase =' '
summ = 0

x = input('Выберите операцию:  ')
numbers = int(input('Сколько будет чисел?: '))

for number in range(1, numbers + 1):
  print (' Введите',number,'- е число: ',end =' ')
  number_1=input()
  
  if number == 1:
    start_phrase = number_1 
    summ = int(number_1)

  elif number >= 2 and x == '+':  
    start_phrase += x
    start_phrase += number_1
    summ += int(number_1)

  elif number >= 2 and x == '-':
    start_phrase += x  
    start_phrase += number_1
    summ -= int(number_1)

  elif number >= 2 and x == '*':
    start_phrase += x  
    start_phrase += number_1
    summ *= int(number_1)

  elif number >= 2 and x == '//':
    start_phrase += x  
    start_phrase += number_1
    summ //= int(number_1)

print( start_phrase,'=',summ)





 

