#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
import os
import shutil
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("../Mail Merge Project Start/Input/Names/invited_names.txt", mode="r+") as file:
    names = file.readlines()


for name in range(0,len(names)):
    current_name = names[name]
    New_name = current_name.strip()
    f = open(f"Letter_for_{New_name}.txt", mode = "w")
    f.write(f"Dear {New_name},\n\nYou are invited to my birthday this Saturday\n\nHope you can make it!\n\nGasser.")
    f.close()
    source = f'C:/Users/Gasser Gaballah/PycharmProjects/Mail+Merge+Project+Start/Mail Merge Project Start/Letter_for_{New_name}.txt'
    destination = f"C:/Users/Gasser Gaballah/PycharmProjects/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/Letter_for_{New_name}.txt"
    shutil.move(source, destination)
