#Write your code below this row 👇
total = 0
for num in range(1,101):
    if num % 2 == 0:
        total += num
print(total)
##------------------ MY CODE
total = 0 
for number in range(2, 101, 2):
    total += number
print(total)

##------------------------------------
def totalEven(rangeNum):
    total = 0
    for num in range(1, rangeNum +1):
        if num % 2 == 0:
            total += num
    print(total)

totalEven(100)