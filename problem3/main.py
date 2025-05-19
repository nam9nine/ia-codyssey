try:
    with open("./Mars_Base_Inventory_List.csv", "r") as f:

       list_l = f.readlines()
       list_l = sorted(list_l, key = lambda x : x.split(",")[4], reverse=True)
        
       list_e = []
       list_e.append(list_l[0])
       for li in list_l[1:]:
           if float(li.split(",")[4]) >= 0.7:
               print(li)
               list_e.append(li)
    print(list_e)
   
    with open("./Mars_Base_Inventory_danger.csv", "w") as w:
        for i in list_e:
            w.write(i)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
