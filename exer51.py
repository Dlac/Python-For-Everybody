#Exercise 5.1
#Write a program which reads list of numbers until done is entered. once done is entered, print out
#the the total, count, and average of the numbers


count = 0
total = 0
while True:
	inp = raw_input('Enter a number: ')
	
	# Handle the edge cases
	if inp == 'done' : break
	if len(inp) < 1 : break 
	
	# Do the work
	try:
		num = float(inp)
	except:
		print "Invalid Input"
		continue
	count = count + 1
	total = total + num
	print num, total, count
print 'Average' , total/count