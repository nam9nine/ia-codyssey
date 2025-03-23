
try:
    with open("./mission_computer_main.log") as f:
        readlines = f.readlines()
        log_list = []
        
        for line in  readlines[1:]:
            log_list.append([item.strip() for item in line.split(",")])
            
        log_list.sort(reverse=True)                                         
    
        for i in log_list:
            print(i)
        
        log_dict = {}

        for i in range(len(log_list)):
            log_dict[log_list[i][0]] = log_list[i][1] + " " + log_list[i][2]

    with open("./mission_computer_main.json", "w") as w:
        w.write("{")
        for time, message in log_dict.items():
            if time == list(log_dict.keys())[-1]:
                w.write(f"\n\t\"{time}\" : \"{message}\"")
            else:
                w.write(f"\n\t\"{time}\" : \"{message}\",")
        w.write("\n}")

    # 보너스 문제
    text = input("입력하세요 : ")
    for _, message in log_dict.items():
        if text in message:
            print(message)
        
except FileNotFoundError:
    print("로그 파일을 찾을 수 없습니다.")
except Exception as e:
    print(f"예외 발생: {e}")


