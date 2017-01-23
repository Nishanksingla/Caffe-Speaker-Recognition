import os, sys
files = os.listdir("spoken_numbers")
names_list=[]
num = 0
mapping={}
count = {}
f = open('synset_numbers.txt', 'w')
for file in files:
#    print file
    list = file.split(".")
    filename = list[0]
#    print filename
    if "_" in filename:
        name = filename.split("_")[1]
#        print name
        if name not in mapping:
            mapping[name] = num
            f.write(name+" "+str(num)+"\n")
            num = num + 1
#        f.write("spoken_numbers/"+file+" "+str(mapping[name])+"\n")
print sorted(mapping.items())
#            count[name] = 0
#        else:
#            count[name] = count[name] + 1
#print count
#print mapping
#for n in count:
#    print n
#    if count[n] > 1:

