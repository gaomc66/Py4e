fname = input("Enter file name: ")
fh = open(fname)
count = 0
sum = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        index = line.find(":")
        line = line.rstrip()
        value = line[index+1:]
        fval = float(value)
        sum = sum + fval
        count = count + 1

print("Average spam confidence:"sum/count)
