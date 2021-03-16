from collections import Counter
import operator

#s = 'qwertyuiopasdfghjklzxcvbnm'
s ='aabbbccde'
d = dict(Counter(s))
l = list(d.values())
l.sort(reverse=True)

#sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
sorted_d = dict( sorted(d.items(), key=lambda x:(-x[1],x[0])))
counter = 1
for k,v in sorted_d.items():
    if counter<=3:
        print(k,v)
        counter +=1
        