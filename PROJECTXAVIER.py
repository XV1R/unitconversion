# Filename: project_1.py

### ADD YOUR NAME, STUDENT ID AND SECTION NUMBER BELOW ###
# NAME:Xavier A. Rosado 
# STUDENT ID: 802195719
# SECTION:016
############      DEFINE CONSTANTS BELOW      ############
KILOMETERS_PER_MILE = 1.60934
KILOGRAMS_PER_POUND = 2.20462
FARENHEIT_PER_CELCIUS_FRACTION = (9/5) 
FARENHEIT_PER_CELCIUS_CONSTANT = 32

############       ADD YOUR CODE BELOW        ############

def convert_miles_to_kilometers():
    miles = input("Enter the miles to be converted: ")
    if is_float(miles) and float(miles) > 0:
        # Convert string to numeric miles
        miles = float(miles)
        # Conversion should be rounded to 2 decimal places.
        km =  round(miles * KILOMETERS_PER_MILE, 2)
        print(miles, "miles are equivalent to", km, "kilometers")
    else:
        print("Illegal unit of conversion. Input miles are not a valid number.")
#   tab test 

def process_conversion(numericOption):
    if numericOption == 1:
        convert_miles_to_kilometers()
    # Add code to handle other menu selections.
    elif numericOption == 2:
            convert_kilometers_to_miles()
    elif numericOption == 3:
           convert_pounds_to_kilograms()
    elif numericOption == 4:
            convert_kilograms_to_pounds()
    elif numericOption == 5:
            convert_celsius_to_farenheit()
    elif numericOption == 6:
            convert_farenheit_to_celsius()
    elif numericOption == 7:
            convert_mph_to_kph()
    elif numericOption == 8:
            convert_kph_to_mph()

#FUNCTIONS 

def convert_kilometers_to_miles():
        kilometers = input('Enter the kilometers to be converted: ')
        if is_float(kilometers) and float(kilometers) > 0:
                kilometers = float(kilometers)
                miles = round(kilometers / KILOMETERS_PER_MILE, 2)
                print(kilometers, 'kilometers are equivalent to', miles, 'miles')
        else:
            print('Illegal unit of conversion. Input kilometers are not a valid number.')


def convert_kilograms_to_pounds():
        kilograms = input('Enter the kilograms to be converted: ')
        if is_float(kilograms) and float(kilograms) > 0:
                kilograms = float(kilograms)
                pounds = round(kilograms * KILOGRAMS_PER_POUND, 2)
                print(kilograms, 'kilograms are equivalent to', pounds, 'pounds')
        else:
                print('Illegal unit of conversion. Input kilograms are not a valid number.')


def convert_pounds_to_kilograms():
        pounds = input('Enter the pounds to be converted: ')
        if is_float(pounds) and float(pounds) > 0:
                pounds = float(pounds)
                kilograms = round(pounds / KILOGRAMS_PER_POUND, 2)
                print(pounds, 'pounds are equivalent to', kilograms, 'kilograms')
        else:
                print('Illegal unit of conversion. Input pounds are not a valid number.')




#FIX THIS, ASK PROFESSOR/SHIVA PLEASE DONT FORGET 29/SEP/19 22:18 -XAVIER
def convert_celsius_to_farenheit():
        celsius = input('Enter the degrees in Celsius to be converted: ' )
        if is_float(celsius):
                celsius = float(celsius)
                farenheit = round((celsius * 9/5) + 32, 2)
                print(celsius, 'celsius are equivalent to', farenheit,'farenheit')
        else:
                print('Illegal unit of conversion. Input celsius are not a number.')


def convert_farenheit_to_celsius():
        farenheit = input('Enter the degrees in Farenheit to be converted: ')
        if is_float(farenheit):
                farenheit = float(farenheit)
                celsius = round((farenheit-32)*(5/9), 2)
                print(farenheit, 'farenheit are equivalent to', celsius, 'celsius')
        else:
                print('Illegal unit of conversion. Input farenheit are not a number')
def convert_mph_to_kph():
        miles_per_hour = input('Enter the miles per hour to be converted: ')
        if is_float(miles_per_hour):
                miles_per_hour = float(miles_per_hour)
                kilometers_per_hour = round(miles_per_hour * KILOMETERS_PER_MILE, 2)
                print(miles_per_hour, 'miles per hour are equivalent to', kilometers_per_hour, 'kilometers per hour')
        else:
                print('Illegal unit of converssion. Input miles per hour are not a number.')


def convert_kph_to_mph():
        kilometers_per_hour = input('Enter the kilometers per hour to be converted: ')
        if is_float(kilometers_per_hour):
                kilometers_per_hour = float(kilometers_per_hour)
                miles_per_hour = round(miles_per_hour / KILOMETERS_PER_MILE, 2)
                print(kilometers_per_hour, 'kilometers per hour are equivalent to', miles_per_hour, 'miles per hour')

        else:
                print('Illegal unit of conversion. Input kilometers per hour are not a number.')
#def miles to kilometers per hour function

############ DO NOT MODIFY THE SECTION BELOW  ############

def is_float(s):
    try:
        float(s)
        # Return True if no exception is thrown
        return True
    except ValueError:
        return False


def print_program_menu():
    print("\n--------")
    print( "Welcome to the unit conversion program. Please, choose an option:")
    print("1. Miles to kilometers")
    print("2. Kilometers to miles")
    print("3. Pounds to kilograms ")
    print("4. Kilograms to pounds")
    print("5. Celsius to Fahrenheit")
    print("6. Fahrenheit to Celsius")
    print("7. Miles/hour to kilometers/hour")
    print("8. Kilometers/hour to miles/hour")
    print("9. Exit")


def identify_option(option):
    # Verify that a number was input
    if option.isdigit():
        numericOption = int(option)
        # Check if the selection is within permitted range
        if numericOption >= 1 and numericOption <= 9:
            return numericOption
        else:
            return -1 # Invalid option
    else:
        return -1 # Invalid option


def main():
    done = False
    while not done:
        print_program_menu()
        userOption = input("Enter option: ")
        optionInfo = identify_option(userOption)
        if optionInfo != -1:
            # Option was valid
            if optionInfo == 9:
                done = True
                print ("Thanks for using the unit conversion program!")
            else:
                process_conversion(optionInfo)
        else:
            # Option was invalid
            print ("Invalid option\n")


# This line makes python start the program from the main function
if __name__ == "__main__":
    main()
