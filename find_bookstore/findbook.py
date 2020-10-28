import operator
tag1 = ['공포','시사','철학']
tag2 = ['공포','영화','영어']
tag3 = ['짐','암','속']
tag4 = ['키','파','차']
tag5 = ['공포','시사','철학']
tag6 = ['고행','시사','철학']

tags = [tag2,tag3,tag4,tag5,tag6]

matching = {}
for i in tags:
    count = 0
    for j,k in zip(tag1,i):
        print(j,k)
        if(j==k):
            count+=1
    matching[count]=i
print(matching)
matching = sorted(matching.items(), key=operator.itemgetter(0),reverse=True)
print(matching)

