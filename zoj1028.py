for i in xrange(input()):
  disk = map(int, raw_input().split())
	if disk.pop(0) % 2 == 1:
		print 'YES'
	else:
		even = sum(disk[::2])
		odd = sum(disk[1::2])
		print (even == odd or even == odd + 1) and 'YES' or 'NO'
