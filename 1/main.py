print("‘Hello Mars")
try:
    with open("./mission_computer_main.log", "r") as read_f:
        read_lines = read_f.readlines()
        for line in read_lines:
            line = line.strip()
            print(line)

except FileNotFoundError as e:
    print(f"파일을 찾을 수 없습니다: {e}")
except IOError as e:
    print(f"입출력 오류 발생: {e}")
except Exception as e:
    print(f"예상치 못한 오류 발생: {e}")