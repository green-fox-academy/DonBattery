a = 24
out = 0
# if w is even increment out by one

if bool(a):
    out += 1

print(out)




b = 13
out2 = ""
# if b is between 10 and 20 set out2 to "Sweet!"
# if less than 10 set out2 to "More!",
# if more than 20 set out2 to "Less!"

if 10 <= b <= 20:
    out2 = "Sweet!"
elif b < 10:
    out2 = "Moar!"
else:
    out2 = "Less!"

print(out2)



c = 123
credits = 100
is_bonus = False
# if credits are at least 50,
# and is_bonus is false decrement c by 2
# if credits are smaller than 50,
# and is_bonus is false decrement c by 1
# if is_bonus is true c should remain the same

if (credits >= 50) and not(is_bonus):
    c -= 2
elif (c < 50) and not(is_bonus):
    c -= 1

print(c)




d = 8
time = 120
out3 = ""
# if d is dividable by 4
# and time is not more than 200
# set out3 to "check"
# if time is more than 200
# set out3 to "Time out"
# otherwise set out3 to "Run Forest Run!"

if d % 4 == 0:
    if time <= 200:
        out3 = "check"
    elif time > 200:
        out = "Time out"
    else:
        out = "Run Forest Run!"

print(out3)
