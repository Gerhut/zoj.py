for i in xrange(input()):
	history = ['http://www.acm.org/']
	point = 0
	raw_input()
	if i > 0:
		print
	while True:
		command = raw_input().split()
		if command[0] == 'BACK':
			if point == 0:
				print 'Ignored'
			else:
				point -= 1
				print history[point]
		elif command[0] == 'FORWARD':
			if point == len(history) - 1:
				print 'Ignored'
			else:
				point += 1
				print history[point]
		elif command[0] == 'VISIT':
			url = command[1].strip()
			point += 1
			history[point:] = [url]
			print url
		elif command[0] == 'QUIT':
			break
