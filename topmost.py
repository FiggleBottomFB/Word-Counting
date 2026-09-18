test_dict = {"apple":3, "banana":7, "pear":2}
def topmost(dict, n):
    sorted_dict = sorted(dict.items(),key=lambda item:item[1],reverse=True)
    for i in range(n):
        pass
    print(sorted_dict) 
topmost(test_dict)
