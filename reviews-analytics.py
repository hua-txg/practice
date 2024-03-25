data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print(len(data))
print(data[0])
print('檔案讀取完了，總共有', len(data), '筆資料')

#計算平均留言的長度，將每一筆留言的長度sum計算出來，除以留言筆數，就是留言的平均長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言的平均長度為', sum_len/len(data))