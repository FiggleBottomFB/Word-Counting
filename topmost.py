import sys
import wordfreq

def printTopMost(dict,n):
    if len(dict) < n:
        n = len(dict)
    sorted_dict = sorted(dict.items(),key=lambda item:item[1],reverse=True) #converts the dict to a list of tuples and sorts it
    for i in range(n): #makes it so only the top 20 words for example is printed
        print(f"{sorted_dict[i][0]:<20}{sorted_dict[i][1]:>5}") #prints the word with the correct amount of spaces so it looks clean


input_file = open(sys.argv[1], encoding="utf-8") #Takes the first argument in terminal for input_file
lines = []
for line in input_file.readlines(): #Reads input_file and creates lines of words in lines list
    lines.append(line)

stop_words_file = open(sys.argv[2], encoding="utf-8") #Takes the second argument in terminal for stop_words_file
stop_words = []
for line in stop_words_file.readlines(): #Read the stop_words_file a creates a list of stopwords
    stop_words += line.split()

def main(): #Function for running the whole program
    printTopMost(wordfreq.countWords(wordfreq.tokenize(lines), stop_words), int(sys.argv[3])) 

main() #Runs Main

input_file.close()
stop_words_file.close()