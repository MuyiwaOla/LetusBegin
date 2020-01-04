print ('This is the temperature converter')
"""
[formula c/5 = f-32/9][where c = temperature in celsius and f = temperature in fahrenheit]
c = str(input('Please insert degrees celcius:'))
f= str(input('Please insert degrees fahrenheit:'))
"""
f = float(input('Please state the degree fahrenheit you would like to convert:'))
fcalc =((f -32)/9)*5
c = float(input('Please state the degree celcius you would like to convert:'))
ccalc = ((c *9)/5)+32
print('This is your degree fahrenheit',ccalc)
print('This is your degree celcius',fcalc)
 
