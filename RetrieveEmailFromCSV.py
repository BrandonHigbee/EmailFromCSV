import re


iteration = 0
            
def ScrubAndWrite(email):
    newmail = re.sub(r'<|>|/|\?|,|!|\*|\^|\$|\(|\)|\[|\]|\{\}|;|:|\'|\|-|\"|([0-9]{3})-([0-9]{3})-([0-9]{4})', '', email)

    with open('excel___' + str(iteration) + '.csv','a') as writefile:
        print(newmail, file=writefile)


    


while iteration != 1:
    iteration = iteration + 1
    with open('excel_' + str(iteration) + '.csv','r') as readfile:
        f = readfile.read()
        f2 = f.split()
    
        for word in f2:
            if "@" in word and "." in word: 
                ScrubAndWrite(word)
        
        print("Finished reading and writing.")

print('Mission complete.')
