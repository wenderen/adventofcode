inp = 1113222113

# run length encoding variant
def rle(n):
	res = []
	for c in str(n):
		if not res or c != res[-1][1]:
			res.append((1,c))
		else:
			res[-1] = (res[-1][0] + 1, c)
	return int(''.join(str(p[0]) + p[1] for p in res))

out = inp
for i in xrange(40):
	out = rle(out)

print len(str(out)) # 252594