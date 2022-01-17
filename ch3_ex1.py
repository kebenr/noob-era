hours = 45
rate = 10
pay = 'dog'

try:
    rate_check = int(rate)
except:
    rate_check = -1
if rate_check == -1:
    print('error, please input numeric value')

try:
    hours_check = int(hours)
except:
    hours_check = -1
if hours_check == -1:
    print('error, please enter number value')

if hours_check and rate_check > 0:
    if hours <= 40:
        pay = hours * rate
    elif hours > 40:
        basepay = 40 * rate
        rate = rate * 1.5
        pay = (hours - 40) * rate + basepay


print('Pay: $' + str(pay))
