import random

with open("dataset.txt", "rb") as f:
    data = f.read().split('\n')

random.shuffle(data)

print "length of data"
print len(data)

train_data = data[:3500]
test_data = data[3500:]

f_train = open("train.txt","w")

for data in train_data:
    f_train.write(data + '\n')



f_test = open("test.txt","w")

for testdata in test_data:
    f_test.write(testdata + '\n')
