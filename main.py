# random alias generator in python
import random as rd

male_name_file = "aliases/male.txt"
female_name_file = "aliases/female.txt"
sur_name_file = "aliases/surname.txt"


maleNames = open(male_name_file, "r")
femaleNames = open(female_name_file, "r")
surNames = open(sur_name_file, "r")

def first(): 
    while True:
        gender = input("Enter gender: [M\F] ")
        gender = gender.lower()
        if (gender == "m"):
            lines = maleNames.readlines()
            numberOfLines = len(lines)
            name_no = rd.randint(0, numberOfLines - 1)
            firstName = lines[name_no].strip()
            break
        elif (gender == "f"):
            lines = femaleNames.readlines()
            numberOfLines = len(lines)
            name_no = rd.randint(0, numberOfLines - 1)
            firstName = lines[name_no].strip()
            break
        else:
            print("Wrong Choice! [Male(M)\Female(F)]")


    firstName = firstName.lower() 
    return firstName

def sur(): 
    lines = surNames.readlines()
    numberOfLines =   len(lines)
    name_no = rd.randint(0, numberOfLines - 1)

    surName = lines[name_no].strip()
    return surName


# Coming feature in future 
# a = int(input("How many names to print? "))

firstName = first()
surName = sur()
final_name = firstName + " " +  surName
final_name = final_name.title()
print("Random Name:", final_name)



