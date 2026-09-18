def topmost(dict, n):
    sorted_list = sorted(dict.items(),key=lambda item:item[1],reverse=True)
    for i in range(n):
        print(f"{sorted_list[i][0]:<20} {sorted_list[i][1]:>20}")
