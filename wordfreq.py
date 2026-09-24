def tokenize(lines):
    words = []
    temp_words = []

    # split all the lines where there is a whitespace
    for line in lines:
        words += line.split()

    # a temporary variable used if numbers, chars and/or special chars is in the same word
    temp_word = ""
    temp_number = ""

    for word in words:
        for i in range(len(word)):
            # if the current char is a letter, add that char to temp_word
            # also check if there is a current temp_number, if there is then add temp_number to temp_words
            if word[i].isalpha():
                if len(temp_number) > 0:
                    temp_words.append(temp_number.lower())
                    temp_number = ""
                temp_word = "".join((temp_word, word[i]))
            # this if statement does the same thing as the previous one but checks for digits instead of letters
            if word[i].isdigit():
                if len(temp_word) > 0:
                    temp_words.append(temp_word.lower())
                    temp_word = ""
                temp_number = "".join((temp_number, word[i]))

            # checks if the current char is a special char, if it is then add temp_word or temp_number to
            # temp_words if one of them exists, and then add the special char to the temp_words list
            if not word[i].isalpha() and not word[i].isdigit():
                if len(temp_word) > 0:
                    temp_words.append(temp_word.lower())
                    temp_word = ""
                elif len(temp_number) > 0:
                    temp_words.append(temp_number.lower())
                    temp_number = ""
             
                temp_words.append(word[i])

            # if this is the last char in the word, add the word to temp_words
            if i+1 == len(word):
                if len(temp_word) > 0:
                    temp_words.append(temp_word.lower())
                    temp_word = ""
                if len(temp_number) > 0:
                    temp_words.append(temp_number.lower())
                    temp_number = ""

    # replaces the words list with the temp_words list
    words = temp_words
    return words

def countWords(list, stopwords):
    dict = {}
    for word in list:
        if word in dict.keys(): #checks if the word exists in the dictionary
            dict[word] +=1 #adds 1 to the amount
        elif word not in stopwords: #if it is new adds it with amount = 1
            dict[word] = 1
            
    return dict