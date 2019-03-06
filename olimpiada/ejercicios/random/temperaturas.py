def intro_part_of_the_day(part):
    """Asks for the temperature of the corresponding part of the day"""
    correct = False
    while correct == False:
        try:
            part_of_the_day = input(part + ": ")
        except TypeError:
            pass
        else:
            if part_of_the_day <= 50 and part_of_the_day >= -30:
                correct = True
    return part_of_the_day

def intro_day(day):
    """Gets the temperature oin the morning, afternoon and night"""
    print "Day", day
    morning = intro_part_of_the_day("morning")
    afternoon = intro_part_of_the_day("afternoon")
    night = intro_part_of_the_day("night")
    return morning, afternoon, night

def get_min_and_max(morning, afternoon, night):
    """Gives the minimum and maximum temperatures from the ones given"""
    return min(morning, afternoon, night), max(morning, afternoon, night) # I use the Python built-in methods to get the minimum and maximum temperatures

def get_type_of_day(min, max):
    """Gives the type of day given the minimum and maximum temperatures"""
    type = "non-stable"
    print ((max+30)-(min+30) <= 5)
    if (max+30)-(min+30) <= 5:
        type = "stable"
        if min < 7:
            type += "-cold"
        else:
            if max > 28:
                type += "-hot"
    return type

def define_day(day):
    """Collects the information of the temperatures and gives the type of day"""
    morning, afetnoon, night = intro_day(day) # I get the temperatures
    min, max = get_min_and_max(morning, afetnoon, night) # Here i get the mimimum and maximum temperatures from the ons i got in the previous step
    type = get_type_of_day(min, max) # Here i get the type of the day by entering the min and max temperatures
    return type

def get_week():
    """Collects the information and classifies the 7 days of the week. It also counts how many of each type are there"""
    cold = 0
    stable = 0
    hot = 0
    for i in range(7):
        day = define_day(i+1)
        if day == "stable":
            stable += 1
        else:
            if day == "stable-cold":
                cold += 1
                stable += 1
            else:
                if day == "stable-hot":
                    hot += 1
                    stable += 1
    return cold, stable, hot

repeat = "y"
while repeat == "y":
    cold, stable, hot = get_week()
    print "There are", stable, "stable days", cold, "cold days and", hot, "hot days"
    repeat = raw_input("Do you want to repeat?(y/n): ")
