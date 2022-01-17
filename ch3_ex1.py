hours = input('enter hours here ')
rate = input('enter rate here ')
fh = float(hours)
fr = float(rate)
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
        pay = fh * fr
    elif hours > 40:
        basepay = 40 * fr
        rate = fr * 1.5
        pay = (fh - 40) * fr + basepay


print('Pay: $' + str(pay))
