#take the input in meters from the user
meters = float(input("Enter the value in meters: "))

#conversion factor
conv_fac = 3.28084

#calculate feet from input
feet = meters * conv_fac

print('%0.2f meters is equal to %0.2f feet.' %(meters, feet))