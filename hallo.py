# dict = {"hej":45,
#         "jag":3,
#         "tjena":12}
# len1 = len(str(sorted_dict[i][0]))
# len2 = len(str(sorted_dict[i][1]))
# amount_of_spaces = 30-len1-len2
#print(f'{sorted_dict[i][0]}{" "*amount_of_spaces}{sorted_dict[i][1]}')

def topmost2(dict,n):
    sorted_dict = sorted(dict.items(),key=lambda item:item[1],reverse=True) #gör om dicten till en lista med tuples och sortar den
    for i in range(n): #väljer så top 20 ord är med t.ex
        print(f"{sorted_dict[i][0]:<20}{sorted_dict[i][1]:>20}") #printar det med 20 spaces emmelan så det ser cleant ut
topmost2(dict,2)  

list = ["a","a","b","b","a","the"]

f = open("lab1/eng_stopwords.txt")

#delar upp stopwords i en lista
stopwords =[]
for line in f.readlines():
            stopwords += line.split()
def word_count(list):
    dict = {}
    for word in list:
        if word in dict.keys(): #kollar om ordet redan finns med
            dict[word] +=1 #plussar på antal
        elif word not in stopwords: # om det inte finns
            dict[word] = 1 #lägg till
            
    print(dict)

word_count(list)

