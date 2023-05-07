data = []
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())
        if len(data) % 1000 == 0:
        	print(len(data))

print('total:', len(data), 'comments')
sum = 0
for p in data:
    sum += len(p)
print('total:', sum, 'words')
print('Per comment average words is:', sum/len(data), '字')

#bad = []
#for d in data:
#   if 'bad' in d:
#		bad.append(d)
#print('the comments with "bad" this word are total', len(bad), '筆')

bad = [d for d in data if 'bad' in d]
print('the comments with "bad" this word are total', len(bad), '筆')

good = ['good' in d for d in data]
#print(good)
t= [d for d in good if d == True]
#print(t)
print('the comments with "bad" this word are total', len(t), '筆')




