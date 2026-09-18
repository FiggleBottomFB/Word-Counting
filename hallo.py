dict = {"hej":45,
        "jag":3,
        "tjena":12}

def topmost(dict,n):
    sorted_dict = sorted(dict.items(),key=lambda item:item[1],reverse=True)
    list = []
    for key,value in sorted_dict.items():
        len1 = len(key)
        len2 = len(str(value))
        amount_of_spaces = 30-len1-len2
        list.append(f'{key}{" "*amount_of_spaces}{value}')
    for i in range(n):
        print(list[i])

#topmost(dict,2)

def topmost2(dict,n):
    sorted_dict = sorted(dict.items(),key=lambda item:item[1],reverse=True) 
    for i in range(n):
        #len1 = len(str(sorted_dict[i][0]))
        #len2 = len(str(sorted_dict[i][1]))
        #amount_of_spaces = 30-len1-len2
        #print(f'{sorted_dict[i][0]}{" "*amount_of_spaces}{sorted_dict[i][1]}')
        print(f"{sorted_dict[i][0]:<20}{sorted_dict[i][1]:>20}")
    
#topmost2(dict,2)  

list = ["a","a","b","b","a"]

def word_count(list):
    dict = {}
    for word in list:
        if word in dict.keys():
            dict[word] +=1
        else:
            dict[word] = 1
            
    print(dict)

word_count(list)