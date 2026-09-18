import sys


testfile = "test.txt"
stopwords = "lab1/eng_stopwords.py"
def tokenize(testfile):
    words = []
    temp_words = []
    with open(testfile, 'r', encoding='utf-8') as text_file:
        for line in text_file.readlines():
            words += line.split()

        for word in words:
            if not word[-1].isalpha() and not word[-1].isdigit():
                loops = 0
                for i in range(1, len(word) + 1):
                    if word[-i].isalpha():
                        break
                    temp_words += word[-i]
                    loops += 1
                words[words.index(word)] = word[:-loops]
                word = word[:-loops]
            if not word[0].isalpha() and not word[0].isdigit():
                loops = 0
                for i in range(len(word)):
                    if word[i].isalpha():
                        break
                    temp_words += word[i]
                    loops += 1
                words[words.index(word)] = word[loops:]

    words += temp_words
    print(words)



tokenize(testfile)