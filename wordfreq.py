import sys


testfile = "lab1/examples/article1.txt"
stopwords = "lab1/eng_stopwords.py"
def tokenize(testfile):
    words = []
    temp_words = []
    with open(testfile, 'r', encoding='utf-8') as text_file:
        for line in text_file.readlines():
            words += line.split()

        for word in words:
            temp_word = ""
            if not word[-1].isalpha() and not word[-1].isdigit():
                loops = 0
                for i in range(1, len(word) + 1):
                    if word[-i].isalpha() or temp_word.isdigit():
                        break
                    temp_words += word[-i]
                    loops += 1
                    temp_word = word[:-loops]
                words[words.index(word)] = word[:-loops]
                word = word[:-loops]
            if word and not word[0].isalpha() and not word[0].isdigit(): 
                loops = 0
                for i in range(len(word)):
                    if word[i].isalpha() or temp_word.isdigit():
                        break
                    temp_words += word[i]
                    loops += 1
                    temp_word = word[loops:]
                words[words.index(word)] = word[loops:]

    words += temp_words
    return words
    # print(words)

f = open("lab1/eng_stopwords.txt")
stopwords =[]
for line in f.readlines():
            stopwords += line.split()
def word_count(list):
    dict = {}
    for word in list:
        if word in dict.keys():
            dict[word] +=1
        elif word not in stopwords:
            dict[word] = 1
            
    # print(dict)
    return dict


def topmost2(dict,n):
    sorted_dict = sorted(dict.items(),key=lambda item:item[1],reverse=True) 
    for i in range(n):
        #len1 = len(str(sorted_dict[i][0]))
        #len2 = len(str(sorted_dict[i][1]))
        #amount_of_spaces = 30-len1-len2
        #print(f'{sorted_dict[i][0]}{" "*amount_of_spaces}{sorted_dict[i][1]}')
        print(f"{sorted_dict[i][0]:<20}{sorted_dict[i][1]:>20}")

topmost2(word_count(tokenize(testfile)), 20)