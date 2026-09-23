import sys
import wordfreq

def printTopMost(dict,n):
    if len(dict) < n:
        n = len(dict)
    sorted_dict = sorted(dict.items(),key=lambda item:item[1],reverse=True) #converts the dict to a list of tuples and sorts it
    for i in range(n): #makes it so only the top 20 words for example is printed
        print(f"{sorted_dict[i][0]:<20}{sorted_dict[i][1]:>5}") #prints the word with the correct amount of spaces so it looks clean


input_file = open(sys.argv[1], encoding="utf-8")
lines = []
for line in input_file.readlines():
    lines += line

stop_words_file = open(sys.argv[2], encoding="utf-8")
stop_words = []
for line in stop_words_file.readlines():
    stop_words = line.split()

def main():
    printTopMost(wordfreq.countWords(wordfreq.tokenize(lines), stop_words), int(sys.argv[3]))

main()

input_file.close()
stop_words_file.close()