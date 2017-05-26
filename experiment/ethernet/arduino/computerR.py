with open("r.txt") as f:
	content = f.readlines()

counter = []
for x in content:
    counter.append(int(x.split(":")[3]))

l = len(counter)
print l
print counter

R = (l-2)*1000000.0/2
print R
tmp = 0.0
#for x in range(0,l-2):
x=0
while x < l-2:

	tmp += counter[x+2] - counter [x]
	print tmp
	x=x+2

R=R/tmp
print R


