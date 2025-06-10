nums = [1, 2, 3, 4, 5]


#if you know how many time the loop will run than use for loop
#if the condition in false it will stop 
#continue will skip the current iteration
for num in nums:
    if num == 3:
        print("Found !")
        continue
    print("This is in single for loop", num)

print()

# for two loops

for num in nums:
    for letter in 'abc':
        print ("This is in double for loop", num, letter)


# range in loop
for i in range(1, 11):
    print(i)

print()
#if you don't know how many time the loop will run then use while loop
#it will run until the condition is false

x = 0

while x < 10:
    if x == 5:
     break
    print(x)
    x += 1


while True:
    if x == 5:
     break
    print(x)
    x += 1