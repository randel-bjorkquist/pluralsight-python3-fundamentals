#--------------------------------------------------------------------------------------------------
#temperature = 95
#temperature = 75
temperature = 50

forecast = "rainy"
#forecast = "summy"

raining = True

#--------------------------------------------------------------------------------------------------
# NOTE: verion 1 - separate if-elif-else blocks
#if temperature > 80:
#  print("It's too hot!")
#  print("Stay inside!")
#elif temperature < 60:
#  print("It's too cold!")
#  print("Stay inside!")
#else:
#  print("Enjoy the outdoors!")


#--------------------------------------------------------------------------------------------------
# NOTE: combining conditions with 'or' 
if temperature > 80 or temperature < 60:
  print("Stay inside!")
else:
  print("Enjoy the outdoors!")


#--------------------------------------------------------------------------------------------------
# NOTE: combining conditions with 'and' 
if temperature < 80 and forecast != "rainy":
  print("Go outside!")
else:
  print("Stay inside!")


#--------------------------------------------------------------------------------------------------
# NOTE: using the 'not' keyword
if not forecast == "rainy":
  print("Go outside!")
else:
  print("Stay inside!")


#--------------------------------------------------------------------------------------------------
if raining:
  print("Stay inside!")

if not raining:
  print("Go outside!")
else:
  print("Stay inside!")

