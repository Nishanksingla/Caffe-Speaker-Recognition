import os, sys
files = os.listdir("speaker_recognition/spoken_numbers")
names_list=[]
num = 0
mapping={}
count = {}
f = open('dataset.txt', 'w')
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
            num = num + 1
        f.write("spoken_numbers/"+file+" "+str(mapping[name])+"\n")


