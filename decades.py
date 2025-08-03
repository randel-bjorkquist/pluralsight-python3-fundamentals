# NOTE: Make sure to convert the input into an int, or the calculation 
#       for 'decades' will throw an exception
age = int(input("How old are you? "))

# NOTE: when dividing and using a single forward-slash, the result is a decimal
#decades = age / 12

# NOTE: when dividing and using a double forward-slashs, the result is intiger 
#       division or the remainder is chopped off
decades = age // 10
years   = age  % 10

print("You are " + str(decades) + " decade(s) and " + str(years) + " year(s) old.")


#dob = input("When were you born? ")
