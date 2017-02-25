#Rewrite your pay computation with time and a half
#for overtime and create a function called computepay
#which takes two parameters (hour and rate)


#hours 45
#rate 10
# pay 475

def computepay(h,r):
	if h<=40:
		p = r* h
	else:
		p = r * 40 + (r * 1.5 * (h - 40) )
	return p

try:
	inp = raw_input("Enter Hours: ")
	hours = float(inp)
	inp = raw_input("Enter Rate: ")
	rate = float(inp)
	
except:
	print "Error, please enter numeric input"
	quit()

pay = computepay(hours, rate)
print pay