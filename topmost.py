# test_dict = {"apple":3, "banana":7, "pear":2}
# def topmost(dict, n):
#     sorted_dict = sorted(dict.items(),key=lambda item:item[1],reverse=True)
#     for i in range(n):
#         pass
#     print(sorted_dict) 
# topmost(test_dict)

def printTopMost(dict,n):
    sorted_dict = sorted(dict.items(),key=lambda item:item[1],reverse=True) 
    for i in range(n):
        #len1 = len(str(sorted_dict[i][0]))
        #len2 = len(str(sorted_dict[i][1]))
        #amount_of_spaces = 30-len1-len2
        #print(f'{sorted_dict[i][0]}{" "*amount_of_spaces}{sorted_dict[i][1]}')
        print(f"{sorted_dict[i][0]:<20}{sorted_dict[i][1]:>20}")

def topmost(dict, n):
    sorted_list = sorted(dict.items(),key=lambda item:item[1],reverse=True)
    for i in range(n):
        print(f"{sorted_list[i][0]:<20} {sorted_list[i][1]:>20}")
