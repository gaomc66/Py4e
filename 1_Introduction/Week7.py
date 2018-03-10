enter = None
total = 0
count = 0
average = 0

while True :
    enter = input("Enter a number:")
    if enter == "done" :
        break
    try:
        value = float(enter)
    except:
        enter = print("Invalid Input", enter)
        continue

    total = total + value
    print(total)
    count = count + 1
    print(count)
    average = total / count
    print(average)

print(total, count, average)
