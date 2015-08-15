#this will be analyze.py

#data
#http://athyra.idyll.org/~t/transfer/aa.txt
#http://athyra.idyll.org/~t/transfer/bb.txt
#http://athyra.idyll.org/~t/transfer/cc.txt
#http://athyra.idyll.org/~t/transfer/dd.txt


print "hello world!"

aalist = []
for line in open ("aa.txt"):
    line = line.strip()
    aalist.append(line)

start = aalist[0]
print start

#kmers of 4
k=5
for j in range(0,len(start) - k + 1):
    print j, start[j:j+k]
