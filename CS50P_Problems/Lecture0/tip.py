def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# convert an amount in dollars in float
# Use float class constructor
# float(<str>)

def dollars_to_float(d)-> float: 
    return float(d[1:])

# convert a percentage to float
# str[:-1] - all the elements of str until the last
def percent_to_float(p):
    return float(p[:-1])/100


main()