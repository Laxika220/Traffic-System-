#take input from the user 
hour = input("Enter then hour(0-23): ")
day = input("Enter the day type(weekday/weekend): ")

def get_traffic_light_duration(hour, day):
    hour = int(hour)
    day = day.strip().lower()

    if day == "weekday":
        if (7 <= hour < 10) or (17 <= hour < 20):
            return "Peak hours: Green light duration = 60 seconds"
        else:
            #return can only be used within a function 
            return "Normal hours: Green light duration = 30 seconds"

    elif day == "weekend":
        if(10 <= hour < 12) or (18 <= hour < 21):
            return "Moderate traffic: Green light duration 40 seconds"
        else:
            return "Low traffic: Green light duration = 20 seconds"
    
    else: 
        return "Invalid input.Try again.Please enter week day or weekend as mentioned in the parameters."
    
    #calling the function and printing the result.
try: 
        hour = int(hour)
        if 0 <= hour < 23:
            print(get_traffic_light_duration(hour, day))
        else: 
            print("Hours must be between 0 and 23.")
except ValueError:
        print("invalid number")

        
