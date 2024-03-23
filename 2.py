import random

question = []
dare = []

print('ENTER QUESTION. IF YOU FINISHED, ENTER "DONE": ')

while 1:
   data = input()
   if data != 'DONE':
       question.append(data)
       print('QUESTION IS ENTERED')
   else:
       break


print('ENTER DARE. IF YOU FINISHED, ENTER "DONE": ')
while 1:
   data = input()
   if data != 'DONE':
       dare.append(data)
       print('DARE IS ENTERED')
   else:
       break

print('YOU ARE IN THE GAME!')
while 1:
   if input('TRUTH OR DARE?: ') != 'DARE':
       print(random.choice(question))
   else:
       print(random.choice(dare))