# dict = {"hej":45,
#         "jag":3,
#         "tjena":12}
# len1 = len(str(sorted_dict[i][0]))
# len2 = len(str(sorted_dict[i][1]))
# amount_of_spaces = 30-len1-len2
#print(f'{sorted_dict[i][0]}{" "*amount_of_spaces}{sorted_dict[i][1]}')

def topmost2(dict,n):
    sorted_dict = sorted(dict.items(),key=lambda item:item[1],reverse=True) #converts the dict to a list of tuples and sorts it
    for i in range(n): #makes it so only the top 20 words for example is printed
        print(f"{sorted_dict[i][0]:<20}{sorted_dict[i][1]:>20}") #prints the word with the correct amount of spaces so it looks clean
topmost2(dict,2)  

list = ["a","a","b","b","a","the"]

f = open("lab1/eng_stopwords.txt")

#splits the stopword file into a list
stopwords =[]
for line in f.readlines():
            stopwords += line.split()
def word_count(list):
    dict = {}
    for word in list:
        if word in dict.keys(): #checks if the word exists in the dictionary
            dict[word] +=1 #adds 1 to the amount
        elif word not in stopwords: #if it is new adds it with amount = 1
            dict[word] = 1 
            
    print(dict)

word_count(list)

