'''
Description:
<This program incorporates 3 functions to allow a user to look up 
info regarding an animal and their respective body and brain mass>
'''
import csv

def find_insert_position(terrestrial_animal, string_list):
    for i in range(len(string_list)):
        if terrestrial_animal <= string_list[i]:
            return i
    return len(string_list)

    #Loop over the string_list to find the animal's name in it
   





def populate_lists(animal_name, animal_weight, brain_weight):
    #Open the file to read it and store ONLY the name of the animal into the animal_name list
    animal_name_list = open("BrainBodyWeightKilos.csv", "r")

    #read each line in the file and separate the values so it is easier to append ONLY the names
    for line in animal_name_list:
        name_info = line.split(",")
        animal_name.append(name_info[0].title())
        animal_weight.append(float(name_info[1]))
        brain_weight.append(float(name_info[2]))
    animal_name_list.close()





def write_converted_csv(output_animal_file, list_of_strings, weight_floats, brain_floats):
    #This program goes through the file of interest and 
    #Converts values as necessary and then formats it as 
    #A CSV file

    output_animal_file = open(output_animal_file, 'w')
    for i in range(len(list_of_strings)):
        animals = list_of_strings[i]
        body_weight = round((weight_floats[i] * 2.205), 2)
        brain_weight = round((brain_floats[i] * 0.0022), 2)

        string_format = animals + "," + str(body_weight) + "," + str(brain_weight) + '\n'

        output_animal_file.write(string_format)
    
    output_animal_file.close()
    




def main():
    #The functions defined prior will be used in main, but NOT directly at first
    #First, create a smaller program that handles user input
    mammal_name = []
    mammal_body_weight = []
    mammal_brain_weight = []
    populate_lists(mammal_name, mammal_body_weight, mammal_brain_weight)

    animal_choice = ""

    while animal_choice != "Q":
        print()
        animal_choice = input('Enter animal name (or "q" to quit): ').title()
        if animal_choice == 'Q':
            break
        if animal_choice not in mammal_name:
            print("File does not contain \"" + animal_choice +  "\".")
            add_choice = input("Add \"" + animal_choice + "\" to file? (y|n) ").lower()
            if add_choice == 'y':
                i = find_insert_position(animal_choice, mammal_name)
                animal_choice_weight = input('Enter body weight for "' + animal_choice + "\" in kilograms: ")
                animal_choice_brainmass = input('Enter brain weight for "' + animal_choice +  "\" in grams: ")
                mammal_name.insert(i, animal_choice)
                mammal_body_weight.insert(i, float(animal_choice_weight))
                mammal_brain_weight.insert(i, float(animal_choice_brainmass))

        else:
            i = mammal_name.index(animal_choice)
            print(animal_choice +": body = " + str(mammal_body_weight[i]) + ", brain = " + str(mammal_brain_weight[i]))
            delete_option = input("Delete \"" + animal_choice +"\"? (y|n) ").lower()
            if delete_option == 'y':
                mammal_name.pop(i)
                mammal_body_weight.pop(i)#body mass associated with animal_choice)
                mammal_brain_weight.pop(i)#brain mass associated with animal_choice)
    write_converted_csv("BrainBodyWeightPounds.csv", mammal_name, mammal_body_weight, mammal_brain_weight )

