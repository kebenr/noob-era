import random
name = input('put name here: ')
question = input('whats your question dog? ')
answer = ['yes dog', 'decidely brother', 'no doubt esketit', 'faded. try again', 'im lazy rn ask later',
'better off not knowing rn', 'lmao nah', 'not so good', 'very sus']

answer = answer[random.randint(0,8)]

if question == (''):
  print ('yo dawg you fucced up lemme get a question')
elif name == (''):
  print ('Question: ' + question)
  print ("Magic 8-Ball's answer: " + answer)
else:
  print (name + ' asks: ' + question)
  print ("Magic 8-Ball's answer: " + answer)

#changelog replaced individual strings under each elif with a list, added user input
#condense if elif statements
