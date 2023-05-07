data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
        count =+ 1
        if len(data) % 1000 == 0:
        	print(len(data))
print('total:', len(data), 'comments')
sum = 0
for p in data:
    sum += len(p)
print('total:', sum, 'words')
print('Per comment average words is:', sum/len(data))



