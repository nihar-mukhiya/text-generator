
import pprint



f = open("test.txt")
message = f.read()
list = message.split()
#print(list)
counts = {}
print(list)
start_at = -1
i = 1
my_set = set(list)
for w in my_set:
    print(w)
    w = {}
print(w)
for word in list:
    if(word not in counts.keys()):
        p = list.index(word, start_at + 1)
        start_at = p
        p+=1




    else:
        if(list.index(word) != (len(list) - 1)):
            p =list.index(word, start_at + 1)

            p+=1
        else:
            p = list.index(word)



    m = (list[p])

    w[i] = m
    i+=1











    #counts[word] = []
    #counts[word] = p
    #print(counts[word])
"""
    if word in counts:

        counts[word] += 1
        p = list.index(word, start_at + 1)
        start_at = p

        print(p)
    else:

        counts[word] = 1
        #print(counts)
        #p = list.index(word)
        #print(p)
        print(counts)

        p+=1
        print(p)
        next = list[p]
        print(next)
    #pprint.pprint(counts)

"""