import sys

test = "test.txt"
testfile = "lab1/examples/article1.txt"
stopwords = "lab1/eng_stopwords.py"

# here the textfile is opened 
lines = []
with open(testfile, 'r', encoding='utf-8') as text_file:
    for line in text_file.readlines():
        # split the current line and add all elements to the words list
        lines += line

# print(lines)
def tokenize(lines):
    words = []
    temp_words = []

    for line in lines:
        words += line.split()

    # here the textfile is opened 
    # with open(testfile, 'r', encoding='utf-8') as text_file:
    #     for line in text_file.readlines():
    #         # split the current line and add all elements to the words list
    #         words += line.split()

    for word in words:
        # a temporary variable used for splitting chars from digits
        temp_word = ""

        # checks if the last char in the string is not a letter and not a digit
        if not word[-1].isalpha() and not word[-1].isdigit():
            loops = 0
            # loops through the last indexes in the word and checks for sepcial chars
            for i in range(1, len(word) + 1):
                # if last character is alpha or the whole word is a sequence of numbers, break the loop
                if word[-i].isalpha() or temp_word.isdigit():
                    break
                # otherwhise add the last char to a temporary list and increment counted number of loops
                temp_words += word[-i]
                loops += 1
                # slice the word to remove the last char(s) in the string
                temp_word = word[:-loops]
            # replace the original word with the edited word and store it for the next step
            words[words.index(word)] = temp_word
            word = temp_word

        # does the same things as the previous if statement but checks for leading special chars in the newly edited word
        if word and not word[0].isalpha() and not word[0].isdigit(): 
            loops = 0
            for i in range(len(word)):
                if word[i].isalpha() or temp_word.isdigit():
                    break
                temp_words += word[i]
                loops += 1
                temp_word = word[loops:]
            words[words.index(word)] = word[loops:]

    # adds the special chars to word list and returns the complete list
    words += temp_words
    # print(words)
    for i in range(len(words)):
        words[i] = words[i].lower()

    return words


# f = open("lab1/eng_stopwords.txt")
# stopwords =[]
# for line in f.readlines():
#             stopwords += line.split()
def countWords(list, stopwords):
    dict = {}
    for word in list:
        if word in dict.keys():
            dict[word] +=1
        elif word not in stopwords:
            dict[word] = 1
            
    # print(dict)
    return dict


# def topmost2(dict,n):
#     sorted_dict = sorted(dict.items(),key=lambda item:item[1],reverse=True) 
#     for i in range(n):
#         #len1 = len(str(sorted_dict[i][0]))
#         #len2 = len(str(sorted_dict[i][1]))
#         #amount_of_spaces = 30-len1-len2
#         #print(f'{sorted_dict[i][0]}{" "*amount_of_spaces}{sorted_dict[i][1]}')
#         print(f"{sorted_dict[i][0]:<20}{sorted_dict[i][1]:>20}")

def printTopMost(dict,n):
    if len(dict) < n:
        n = len(dict)
    sorted_dict = sorted(dict.items(),key=lambda item:item[1],reverse=True) 
    for i in range(n):
        #len1 = len(str(sorted_dict[i][0]))
        #len2 = len(str(sorted_dict[i][1]))
        #amount_of_spaces = 30-len1-len2
        #print(f'{sorted_dict[i][0]}{" "*amount_of_spaces}{sorted_dict[i][1]}')
        print(f"{sorted_dict[i][0]:<20}{sorted_dict[i][1]:>5}")

# topmost2(word_count(tokenize(testfile)), 20)