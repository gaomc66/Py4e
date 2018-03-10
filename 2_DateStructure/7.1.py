fname = input("Enter file name:")
try:
    fh = open(fname)
except:
    print("X_X")
    quit()
content = fh.read()
print(content)
