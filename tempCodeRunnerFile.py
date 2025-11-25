user_input = int(input('enter ur number here'))
sum = 0
for i in range(user_input):
    if i % 2 == 1:
        sum = sum + i
print(sum)