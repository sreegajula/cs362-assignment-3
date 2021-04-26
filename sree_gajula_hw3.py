def main():
    check_leap()

def check_leap ():
    year = input("Enter a year to see if that year is a leap year: ")
    leap = " is a leap year"
    not_leap = " is not a leap year"

    if (int(year) % 4) == 0:
        if (int(year) % 100) == 0:
            if (int(year) % 400) == 0:
                print(year + leap)
            else:
                print(year + not_leap)
        else:
            print(year + leap)
    else:
        print(year + not_leap)

    input("Press the Enter key to exit this program.")

if __name__ == "__main__":
    main()