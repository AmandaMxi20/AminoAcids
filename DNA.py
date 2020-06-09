# -*- coding: utf-8 -*-
"""Created on Wed Jun  4 12:35:29 2020

@author: sirmqo
"""


#function to read from file
def mutate():
    #reads from the main file and from the normal one
    File1 = open("DNA.txt","r")
    file2 = open("normalDNA.txt","w")
    #adds the main file to a string
    end = File1.read().replace("\n", "")
    for x in range(len(end)):
        #checks through the whole string and a is replaced with A
        if end[x] == "a":
            File2.writelines("A")
        else: 
            File2.writelines(end[x])
            
    #reads from the main file and from the normal one
    File_mutate = open("mutatedDNA","r")
    File_mutate_fixed = open("mutatedDNA.txt","w")
    #adds the main file to a string
    end = File_mutate.read().replace("\n", "")
    for x in range(len(end)):
        #checks through the whole string and a is replaced with A
        if end[x] == "a":
            File_mutate_fixed.writelines("T")
        else: 
            File_mutate_fixed.writelines(end[x])
            
    #closes all the files
    File1.close()
    File2.close()
    File_mutate.close()
    File_mutate_fixed.close()

#reads everything from file and returns it
def readFromFile(file):
    File_object = open(file,"r")
    return File_object.read().replace("\n", "")

tfile = "DNA_sequence.txt"
#taking the DNA sequence from the .txt file and adding it to a string
DNAfirst = readFromFile(tfile)

#function to create a protein from the DNA sequence
def translate(DNA):
    #dictionary containing only the first 5 amino acids 
    protein = { 
        'ATA':'I', 'ATC':'I', 'ATT':'I',
        'ATG':'M',                  
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'TTC':'F', 'TTT':'F', 
        'TTA':'L', 'TTG':'L', 
    } 
    
    protein = "" 
    #runs through the DNA sequence taking strings of 3 in length
    for x in range(0, len(DNA), 3): 
        #finds the 3 length codon
        codon = DNA[x: x + 3] 
        #tests if the codon is in the table
        if codon in aminoacids:
            #adds the amino
            proteinsequence +=proteinacids[codon]
        else:
            #adds an X because it doesn't contain an amino
            proteinacids += "X"
    return proteinequence

def txtTranslate():
    #recall the mutate
    mutate()
    #adds the contents of the text files to the variables "mut" and "nor"
    mut = readFromFile("mutatedDNA.txt")
    nor = readFromFile("normalDNA.txt")
    #turns them into protein strings
    mutend = translate(mut)
    norend = translate(nor)
    #prints out the finished products
    print("-----------------------------------------------") 
    print("MutatedDNA output : " + "\n"+ mutend + "\n\n" + "NormalDNA output : "+ "\n" + norend)
    print(" ")
    
#runs the translation
txtTranslate()

#the example given

print("\n" +   translate(("ATTCTCATA")))
print( "  ")
