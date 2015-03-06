tmax=10000
tmin=-10000
m=tmax-tmin

with open('2sum.txt') as f:
    lines=f.readlines()

S=[int(line.strip()) for line in lines]

h={}
for i in S:
    if i/m in h:
        h[i/m].append(i)
    else:
        h[i/m]=[i]

sumsHash={}
for a in S:
    if ((tmin-a)/m) in h:
        for item in h[(tmin-a)/m]:
            if item + a >= -10000 and item + a <= 10000:
                sumsHash[item+a]=1
    elif ((tmin-a)/m + 1) in h:
        for item in h[((tmin-a)/m + 1)]:
            if item + a >= -10000 and item + a <= 10000:
                sumsHash[item+a]=1

print len(sumsHash)                