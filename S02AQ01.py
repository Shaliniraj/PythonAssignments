#This program calculates the mileage of the car

maxfuelcapacity = input("Enter the max fuel capacity of your car")
maxfuelcapacity = int(maxfuelcapacity)

startingreading = input("Enter the starting reading of your car's odometer")
startingreading = int(startingreading)

endingreading = input("Enter the endingreading reading of your car's odometer")
endingreading = int(endingreading)

distance = endingreading-startingreading
print("distance",distance)

carmileage = distance/maxfuelcapacity
print("Mileage of your car is",carmileage)
