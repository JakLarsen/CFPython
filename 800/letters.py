n = set(input())
print([len(n)-2, len(n)-4]["," in n])

#grandmaster: print(len(set(input()+', '))-4) - adds ', ' 
#if its not there to make -4 standard subtract