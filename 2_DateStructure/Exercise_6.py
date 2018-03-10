nums = []
while (True):
    num = input("Enter a number:")
    try:
        fnums = float(num)
    except:
        if num == 'done': break
        else :
            print("Please check your input")
            continue
    nums.append(fnums)
# sumnums = str(sum(nums))
# print(type(sumnums))
print('sum:' + str(sum(nums)))
print(len(nums))
print(max(nums))
print(min(nums))

print(sum(nums)/len(nums))
