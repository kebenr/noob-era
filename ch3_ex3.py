score = input('put score here ')
grade = 'dog'

try:
    score_check = int(score)
except:
    score_check = -1

if score > 1:
    grade = 'invalid input'
elif score >= .9:
    grade = 'a'
elif score >= .8:
    grade = 'b'
elif score >= .7:
    grade = 'c'
elif score >= .6:
    grade = 'd'
elif score < .6:
    grade = 'f'

if score_check == -1:
    grade = 'invalid input'

print(grade)
