def main():
    dollars = dollars_to_float(input("What was your meal in dollars? "))
    percent = percent_to_float(input("What percentage would like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    return float(d[1:])

def percent_to_float(p):
    return float(p[:-1]) / 100

main()
