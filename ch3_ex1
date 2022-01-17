hours = input('enter hours ')
rate = input('enter rate ')
pay = 'dog'

try:
    rate_check = int(rate)
except:
    rate_check = -1
#overtime pay
if rate_check > 0 :
    if hours > 40:
        rate = rate * 1.5

else:
    print('error, please input numeric value')

try:
    hours_check = int(hours)
except:
    hours_check = -1

if hours_check == -1:
    print('error, please enter number value')
if hours_check > 0:
    pay = (hours - 40) * rate + 400

print('Pay: $' + str(pay))
