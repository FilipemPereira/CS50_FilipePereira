
'''
 If up for a challenge, optionally add support for 12-hour times, allowing the user to input times in these formats too:

    #:## a.m. and ##:## a.m.
    #:## p.m. and ##:## p.m.   
'''
def convert(time):
    # split - split the str passed as input in two variables of type int
    # map - map the elements of the list returned by the split method to type int
    hours, minutes = map(int, time.split(":"))
    if not(0 <= hours < 24) or not (0 <= minutes < 60):
        return "Error!! Enter valid hours in 24-hour time format"
    convertedMinutes = minutes/60
    return hours + convertedMinutes

def main():
    time = input("What time is it? (e. 2:00)")
    convertedTime = convert(time)
    if 7 <= convertedTime < 8:
        print("Breakfast Time")
    elif 12 <= convertedTime < 13:
        print("Launch Time")
    elif 18 <= convertedTime < 19:
        print("Dinner Time")
    else: 
        print("")


if __name__ == "__main__":
    main()