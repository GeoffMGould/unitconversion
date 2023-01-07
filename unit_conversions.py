import re; import sys;
import numpy as np

## This program will convert one or more rectangular surfaces from sqaure inches
# input by user into total square feet of all surfaces

INFT_CONVERSION = 144 # 144 square inches in one square foot
CMFT_CONVERSION = 929.0304 # 929.0304 sq cm in one square foot, using 2.54cm/in
INMTR_CONVERSION = 1550 # 1550 square inches in a square meter
CMMTR_CONVERSION = 10000 # 100000 square inches in a square meter
measure_units = ""
measurements_list = []
surfaces_counter = 1


def render_input(dim_num,measure_units = measure_units):
    if (str(surfaces_counter).endswith("1")) & (not((len(str(surfaces_counter)) > 1) & ((str(surfaces_counter)[len(str(surfaces_counter))-2] == "1")))):
        inp1 = input("Enter {} dimension of {}st surface in {}\n".format(dim_num,surfaces_counter,measure_units))
    elif (str(surfaces_counter).endswith("2")) & (not((len(str(surfaces_counter)) > 1) & ((str(surfaces_counter)[len(str(surfaces_counter))-2] == "1")))):
        inp1 = input("Enter {} dimension of {}nd surface in {}\n".format(dim_num,surfaces_counter, measure_units))
    elif (str(surfaces_counter).endswith("3")) & (not((len(str(surfaces_counter)) > 1) & ((str(surfaces_counter)[len(str(surfaces_counter))-2] == "1")))):
        inp1 = input("Enter {} dimension of {}rd surface in {}\n".format(dim_num,surfaces_counter, measure_units))
    else:
        inp1 = input("Enter {} dimension of {}th surface in {}\n".format(dim_num,surfaces_counter, measure_units))
    return inp1

print("Enter 'Q' at any prompt to exit the program")


while True:
    inp_units = input("""Which unit will you be using to input your measurements?\n
1.Inches\n2.Centimeters\n""")
    if re.search("^(\s)*1(\s)*$",inp_units):
        print("You have chosen inches\n")
        measure_units = "inches"
        break
    elif re.search("^(\s)*2(\s)*$",inp_units):
        measure_units = "centimeters"
        print("You have chosen centimeters\n")
        break
    elif re.search("^\s*[Qq](uit)?\s*$",inp_units):
        print("Exiting program")
        sys.exit(0)
    else:
        print("Please input either '1' or '2'\n")
        continue

while True:
    out_units = input("""Which unit will you be converting to?\n
1.Square Feet\n2.Square Meters\n""")
    if re.search("^(\s)*1(\s)*$",out_units):
        print("You have chosen square feet\n")
        converted_units = "sq ft"
        break
    elif re.search("^(\s)*2(\s)*$",out_units):
        converted_units = "sq m"
        print("You have chosen square meters\n")
        break
    elif re.search("^\s*[Qq](uit)?\s*$",out_units):
        print("Exiting program")
        sys.exit(0)
    else:
        print("Please input either '1' or '2'\n")
        continue


while True:
    while True: # first dim for surface
        inp1 = render_input("first", measure_units=measure_units)
        if re.search("^(\d)+(\.)?(\d)*$",inp1):
            measurement1 = float(inp1)
            break
        elif re.search("^\s*[Qq](uit)?\s*$",inp1):
            print("Exiting program")
            sys.exit(0)
        else:
             print("input must be numeric with optional decimal point, please try again\n")
             continue

    while True: # second dim for surface
        inp2 = render_input("second", measure_units=measure_units)
        if re.search("^(\d)+(\.)?(\d)*$",inp2):
             measurements_list.append(float(inp2)*float(inp1))
             break
        elif re.search("^\s*[Qq](uit)?\s*$",str(inp2)):
            print("Exiting program")
            sys.exit(0)
        else:
             print("input must be numeric with optional decimal point, please try again\n")
             continue

    while True:
        input_additional = input("Are there additional surfaces to convert? (Y/N)\n")
        if re.search("^(\s)*[Yy](es)?(\s)*$",input_additional):
            surfaces_counter +=1
            break # goes to final 'continue' statement to start new surface*
        elif re.search("^(\s)*[Nn]([Oo])?(\s)*$",input_additional):
            measure_to_out = np.array(measurements_list)
            if measure_units == "inches":
                if converted_units == "sq ft":
                    total_sqft = round(np.sum(np.divide(measure_to_out,INFT_CONVERSION)),2)
                    print("Total Surface Area in Square Feet is:",total_sqft)
                elif converted_units == "sq m":
                    total_sqm = round(np.sum(np.divide(measure_to_out,INMTR_CONVERSION)),2)
                    print("Total Surface Area in Square Meters is:",total_sqm)
            elif measure_units == "centimeters":
                if converted_units == "sq ft":
                    total_sqft = round(np.sum(np.divide(measure_to_out,CMFT_CONVERSION)),2)
                    print("Total Surface Area in Square Feet is:",total_sqft)
                elif converted_units == "sq m":
                    total_sqm = round(np.sum(np.divide(measure_to_out,CMMTR_CONVERSION)),2)
                    print("Total Surface Area in Square Meters is:",total_sqm)
            print("Program exiting now - goodbye")
            sys.exit(0)
        elif re.search("^\s*[Qq](uit)?\s*$",str(input_additional)):
            print("Exiting program")
            sys.exit(0)
        else:
            print("Please enter 'Y' or 'N'\n")
            continue
    continue # *additional surface
