# For more info about file modificators see: https://docs.python.org/3/library/functions.html#open

# Open file as text
#f = open("input.txt", "r")
# Open file in binary mode
#f = open("input.txt", "rb")
# Open file for write
#f = open("output.txt", "w") # If file does not exist will be created
# Open file for update in binary mode
# If file is opened with w, all previous file content will be removed
#f = open("output.txt", "w+")

import json




f = open("input.txt", "r")
f.close()


def read_file():
    try:
        with open("some_file.txt", "r") as f:
            pass
    except FileNotFoundError as e:
        print("File does not exist!")

    with open("input.txt", "r") as f:
        numbers = []

        # glavne operacije sa listom su 
        # append - dodavanje eleemnta u listu
        # pop - skidanje poslednjeg elementa u listi
        # if concrete_elem in numbers - provera da li je element u listi-u
        # if concrete_elem not in numbers - provera da li element nije u listi-u

        for line in f.readlines():
            numbers.append(int(line))
        print("List")
        print(numbers)
        print("Sorted")
        print(sorted(numbers))

        # add - dodavanje elementa u set
        # remove - brisanje elemnta iz set-a
        # clear - brisanje celog set-a
        # if concrete_elem in list_set - provera da li je element u set-u
        # if concrete_elem not in list_set - provera da li element nije u set-u

        list_set = set(numbers)
        print("Set")
        print(list_set)


        # Dictionary
        person = {
                "name": "John",
                "surname": "Doe",
                "Address": "Somewhere in Serbia",
                "Age": 35
            }

        with open("inputdict.txt", "r") as f:
            person_from_file = json.loads(f.read())
            print(json.dumps(person_from_file))

            # Osnovne operacije za rad sa json-om
            # json.loads - pretvara string u dictionary
            # json.dumps - pretvara python dictionary u string

            # Setovanje vrednosti za kljuc
            person_from_file["name"] = "Charlie"
            print("Renamed")
            print(json.dumps(person_from_file))
            # Uzimanje vrednosti objekta 
            print(f"{person_from_file['name']} {person_from_file['surname']}")



        

