#amino acid SLC code table 
slcCode = {
    "ATT" : " Isoleucine", "ATC" : " Isoleucine", "ATA" : " Isoleucine",
    "CTT" : " Leucine", "CTC" : " Leucine", "CTA" : " Leucine", "TTA" : " Leucine", "TTG" : " Leucine",
    "GTT" : " Valine", "GTC" : " Valine", "GTA" : " Valine", "CTG" : " Valine",
    "TTT" : " Phenylalanine", "TTC" : " Phenylalanine", 
    "ATG" : " Methionine",
    }
#the code above takes in the SLC code then it prints out the amino acid to the user
protein = ""
seq = input("Enter a DNA Sequence: ")
if len(seq)%3 == 0: 
    for i in range(0, len(seq), 3): 
        codon = seq[i:i + 3] 
        protein+= slcCode[codon]
        print(seq +" is representing: "+ protein)


#The following program translates DNA from a text file and outputs the slc sequence of that text file to the user

#The function below takes a codon list and translates to the the relvant SLC symbol using if, elif and else.
def translate(codon_list):
    slc_sequence = ""
    for i in range(len(codon_list)):
        if len(codon_list[i]) < 3:
            slc_sequence += "(+ " + codon_list[i] + ")"
        elif codon_list[i] == "ATT" or codon_list[i] == "ATC" or codon_list[i] == "ATA":
            slc_sequence += " Isoleucine "
        elif codon_list[i] == "CTT" or codon_list[i] == "CTC" or codon_list[i] == "CTA" or codon_list[i] == "CTG" or codon_list[i] == "TTA" or codon_list[i] == "TTG":
            slc_sequence += " Leucine "
        elif codon_list[i] == "GTT" or codon_list[i] == "GTC" or codon_list[i] == "GTA" or codon_list[i] == "GTG":
            slc_sequence += " Valine "
        elif codon_list[i] == "TTT" or codon_list[i] == "TTC":
            slc_sequence += " Phenylalanine "
        elif codon_list[i] == "ATG":
            slc_sequence += " Methionine "
        else:
            slc_sequence += "X"
    print(slc_sequence)

#The mutate function reads a DNA sequence from a text file, changes the lowercase a to A and T and writes the new DNA sequence to 2 seperate .txt files
def mutate(textfile):
    sequence_file = open(textfile, "r", encoding = "utf-8-sig")
    sequence = ""
    for line in sequence_file:
        sequence += line
    sequence_file.close()

    mutate_file = open("mutatedDNA.txt", "w") #Creates the Mutated DNA string and saves it to mutatedDNA.txt
    mutate_file.write(sequence.replace("a", "T"))
    mutate_file.close()    

    normal_file = open("normalDNA.txt", "w") #Creates the corrected normal DNA string and saves it to normalDNA.txt
    normal_file.write(sequence.replace("a", "A"))
    normal_file.close()

#The function below opens a .txt file and cleans and formats a DNA string into a list of codons. It then calls the translate function defined earlier and outputs the SLC symbols list    
def txtTranslate(textfile):
    sequence_file = open(textfile, "r", encoding = "utf-8-sig")
    sequence = ""
    for line in sequence_file:
        sequence += line.replace("\n", "")
    sequence_file.close()
    codon_list = [sequence[i:i+3] for i in range(0, len(sequence), 3)] #This was a cool find. Shorthand for splitting the DNA sequence string into a list of codons (3 at a time) without throwing an out of range error
    translate(codon_list)

mutate(str(input("Please input the text file you would like to mutate (ie, DNA.txt): "))) #Calls the mutate function on the inputed .txt file
#Below piece of code allows you to call the txtTranslate function on as many .txt files as you want using a while loop.
runTranslate = "y"
while runTranslate == "y":
    runTranslate = input("Would you like to translate a text file? [Y/N]: ").lower()
    if runTranslate == "y":
        txtTranslate(str(input("Please enter the txt file you would like to translate (normalDNA.txt or mutatedDNA.txt): ")))
    else:
        break



    
