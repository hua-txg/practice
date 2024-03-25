data = []
with open('foot.txt', 'r') as f:
	for line in f:
		data.append(line)
print(len(data))
print(data)
print(data[0])
print('-------------------------')
with open('foot.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
print(data)