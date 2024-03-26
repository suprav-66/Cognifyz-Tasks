# Temperature Conversion 
# Defining a function for conversion

def temp_conversion(temp,current_unit,to_be_convered):
# Using "F" for Fahrenheit, "C" for Celsius and "K" for Kelvin
# Converting from Celsius to Fahrenheit ###
    if to_be_convered == "F" and current_unit == "C":
        new_temp = round(9 / 5 * temp + 32, 3)
        print("The converted temperature in Fahrenheit scale is " + str(new_temp) + " degrees")
        
# Converting from Fahrenheit into Celsius ###    
    elif to_be_convered == "C" and current_unit == "F":
        new_temp = round(5 / 9 * (temp - 32), 3)
        print("The converted temperature in Celsius scale is " + str(new_temp) + " degrees")    
        
# Converting from Celsius to Kelvin ###    
    elif to_be_convered == "K" and current_unit == "C":
        new_temp = round(temp + 273.15, 3)
        print("The converted temperature in Kelvin scale is " + str(new_temp) + " degrees")
        
# Converting from Kelvin to Celsius ###    
    elif to_be_convered == "C" and current_unit == "K":
         new_temp = round(temp - 273.15, 3)
         print("The converted temperature in Celsius scale is " + str(new_temp) + " degrees")
         
# Converting from Kelvin to Fahrenheit ###    
    elif to_be_convered == "F" and current_unit == "K":
        new_temp = round(9 / 5 * (temp - 273.15) + 32, 3)
        print("The converted temperature in Fahrenheit scale is " + str(new_temp) + " degrees")
        
# Converting from Fahrenheit to Kelvin ###    
    else:
        new_temp = round(5 / 9 * (temp - 32) + 273.15, 3)
        print("The converted temperature in Kelvin scale is " + str(new_temp) + " degrees")     

t=float(input("Enter values in integer or float"))
cu=input("Enter either C / K / F ")
tc=input("Enter either C / K / F ")

ob1=temp_conversion(t,cu,tc)
      