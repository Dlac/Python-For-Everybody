#take the following python code that stores a string
#str = 'x-dspam-confidence: 0.8475
#use find and string slicing to extract the portion of the string after the colon
# character and tehn use the float function to conver tthe extracted string int a floating point number

x = 'X-DSPAM-Confidence: 0.8475'
print x
pos = x.find(':')
#print pos
num = float(x[pos+1:])
print num, type(num)

