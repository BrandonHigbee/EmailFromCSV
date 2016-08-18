# 		Author: Brandon Higbee
# 		Last Modified: 8/17/2016

##		Description:
## Open files named "excel_#" and read every word in them, looking for instances of words with @'s and .'s (emails)
## When an email is found, it will remove any excess characters in it (uses reg expression at line 13) and exports it to a new .csv file named "excel___#"
## The program in its current state will read multiple files in the directory it is located in, based on user input (line 16).
## 
##		How to use:
## Change every excel file you want to work with to a .csv file (warning: will delete formatting)
## Rename every file to "excel_#", where # is replaced with 1 to the maximum numeber of files
## Put this .py file in the directrory with the files and run the code. The program will create new files called "excel___#"


import re

#Removes excess characters and writes to file
def ScrubAndWrite(email):
    
    newmail = re.sub(r'<|>|/|\?|,|!|\*|\^|\$|\(|\)|\[|\]|\{\}|;|:|\'|%|\|-|\"|([0-9]{3})-([0-9]{3})-([0-9]{4})', '', email)
    #currenly removes: phone numebers (###-###-####), symbols:  < > / ? , ! * ^ $ ( ) [ ] { } ; : ' - " %
    
    print(newmail, file=writefile)


iteration = 0
iterationMax = int(input("How many files to find emails in?: ")) #How many files to read?


		
while iteration != iterationMax:
    iteration = iteration + 1
    with open('excel___' + str(iteration) + '.csv','a') as writefile:
        with open('excel_' + str(iteration) + '.csv','r') as readfile:  #open read file
            f = readfile.read()                                         #import entire file contents into a string
            f2 = f.split()                                              #split the string into a workable list/array
    
            for word in f2:                                             #for every member in that list
                if "@" in word and "." in word:                         #if its an email (has @ and .)
                    ScrubAndWrite(word)                                 #remove excess characters and export the word to file
        
        print("Finished reading and writing file #" + str(iteration))

print('Mission complete.')
