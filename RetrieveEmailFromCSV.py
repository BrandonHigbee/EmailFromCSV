# 		Author: Brandon Higbee
# 		Last Modified: 2/14/2018
##		Description:
## Open .csv files in the executable directory and reads every word in them, looking for instances of words with @'s and .'s (emails)
## When an email is found, it will remove any excess characters in it (uses reg expression in ScrubWordToEmail function) and exports
## it to a new .csv file with the same name in the 'cleaned' directory
## 
##		How to use:
## Slap your .csv files in the same directory as this script file and run it,
## the cleaned files will be put in the directory /cleaned

import os
import re
import glob
import shutil

def ScrubWordToEmail(word):
    # Removes excess characters and returns something resembling an email.
    # Currenly removes: phone numebers (###-###-####), symbols:  < > / ? , ! * ^ $ ( ) [ ] { } ; : ' - " %
    email = re.sub(r'<|>|/|\?|,|!|\*|\^|\$|\(|\)|\[|\]|\{\}|;|:|\'|%|\|-|\"|([0-9]{3})-([0-9]{3})-([0-9]{4})', '', word)
    
    return email    

def GetCSVFilesInDir(path):
    return glob.glob(path)


listOfCSVFiles = GetCSVFilesInDir("*.csv")

# Delete existing cleaned directory and creates a new one.
shutil.rmtree('cleaned', ignore_errors=True) 
os.makedirs('cleaned', exist_ok=True)

# For debugging.
print(listOfCSVFiles)

# Opens each file in the list, reads every word and pulls ones that look like emails.
# When it finds a word, it will remove excess characters and write it to a file with the
# same name in the 'cleaned' directory.
for filePath in listOfCSVFiles:
    with open('cleaned\\' + filePath, 'a') as writeFile:
        with open(filePath, 'r') as readFile:
            fileContents = readFile.read()
            fileContentsAsCollection = fileContents.split()

            for word in fileContentsAsCollection:
                if "@" in word and "." in word:
                    email = ScrubWordToEmail(word)
                    print(email, file = writeFile)

print('Scrubbed files can be found in the "cleaned" folder.')




