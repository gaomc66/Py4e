fn = "mbox-short.txt"
try:
    fh = open(fn)
except:
    print("...x")
    quit()
for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    emailadd = line.split()
    print(emailadd[1])
    emailname = emailadd[1].split('@')
    print(emailname)
    print("name:" + emailname[0])
