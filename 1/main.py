print("‘Hello Mars")
try:
    with open("/Users/namnine9/major_dev/1/mission_computer_main.log", "r") as read_f:
        read_lines = read_f.readlines()
    with open("/Users/namnine9/major_dev/1/log_analysis.md", "w", encoding="utf-8") as write_f:
        for line in read_lines:
            line = line.strip()
            print(line)
            write_f.writelines(line + "\n")
except FileNotFoundError as e:
    print(f"파일을 찾을 수 없습니다: {e}")
except IOError as e:
    print(f"입출력 오류 발생: {e}")
except Exception as e:
    print(f"예상치 못한 오류 발생: {e}")