name = input('Your name: ')
question = input('Your question: ')
answer = ''

import random
random_number = random.randint(0, 9)

if random_number == 0:
  answer = 'Yes - definitely.'
elif random_number == 1:
  answer = 'Signs point to yes.'
elif random_number == 2:
  answer = 'It is decidedly so.'
elif random_number == 3:
  answer = 'Without a doubt.'
elif random_number == 4:
  answer = 'Reply hazy, try again.'
elif random_number == 5:
  answer = 'Ask again later.'
elif random_number == 6:
  answer = 'Better not tell you now.'
elif random_number == 7:
  answer = 'My sources say no.'
elif random_number == 8:
  answer = 'Outlook not so good.'
elif random_number == 9:
  answer = 'Very doubtful.'
else:
  print('Error')

import sys
if question == '':
  print("\nThe Magic 8-Ball cannot provide a fortune unless you ask it something!")
  sys.exit()

if name == '':
  print("\nQuestion: " + question)
  print("Magic 8-Ball's answer: " + answer)
else:
  print('\n' + name + ' asks: ' + question)
  print("Magic 8-Ball's answer: " + answer)