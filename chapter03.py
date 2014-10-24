#Exercise 3.1
# hrs = raw_input("Enter Hours:")
# h = float(hrs)
# rate= raw_input("Enter rate:")
# r=float(rate)
# if h<=40:
#     pay=h*r
# else :
#     pay=40*r+(h-40)*r*1.5
# print pay  

#Exercise 3.2-1
# hrs = raw_input("Enter Hours:")
# h = float(hrs)
# rate= raw_input("Enter rate:")
# r=float(rate)
# try:

#     if h<=40:
#         pay=h*r
#     else :
#         pay=40*r+(h-40)*r*1.5
#     print pay 
# except:
#     print 'Error, please enter numeric input'   

#Exercise 3.2-2
try:
	hrs = raw_input("Enter Hours:")
	h = float(hrs)
	rate= raw_input("Enter rate:")
	r=float(rate)
except:
	print "Error,please enter numeric input"
	quit()

print h, r
if h<=40:
    pay=h*r
else :
    pay=40*r+(h-40)*r*1.5
print pay 




