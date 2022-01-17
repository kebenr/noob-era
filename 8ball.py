import random
name = ('dog water')
question = ('super dog water or nah?')
answer = ['yes dog', 'decidely brother', 'doubt none', 'faded. try again', 'im lazy rn ask later',
'better off not knowing rn', 'lmao nah', 'not so good', 'very sus']

random_number = random.randint(1,9)
if random_number == 1:
  answer = answer[0]
elif random_number == 2:
  answer = answer[1]
elif random_number == 3:
  answer = answer[2]
elif random_number == 4:
  answer = answer[3]
elif random_number == 5:
  answer = answer[4]
elif random_number == 6:
  answer = answer[5]
elif random_number == 7:
  answer = answer[6]
elif random_number == 8:
  answer = answer[7]
elif random_number == 9:
  answer = answer[8]
else:
  answer = ('Error')

if question == (''):
  print ('yo dawg you fucced up lemme get a question')
elif name == (''):
  print ('Question: ' + question)
  print ("Magic 8-Ball's answer:" + answer)
else:
  print (name + ' asks: ' + question)
  print ("Magic 8-Ball's answer:" + answer)

#changelog replaced individual strings under each elif with a list
