print("‘Hello Mars")
try:
    with open("./mission_computer_main.log", "r") as read_f:
        read_lines = read_f.readlines()
    with open("log_analysis.md", "w", encoding="utf-8") as write_f:
        for line in read_lines:
            line = line.strip()
            print(line)
        write_f.writelines("""2023-08-27 11:35:00,ERROR,Oxygen tank unstable.
2023-08-27 11:40:00,ERROR,Oxygen tank explosion.

## 원인 분석
### 보고서
- 오류 발생 시각: 2023-08-27 11:35:00
- 오류 내용: Oxygen tank unstable.
- 오류 발생 시각: 2023-08-27 11:40:00
- 오류 내용: Oxygen tank explosion.""")
except FileNotFoundError as e:
    print(f"파일을 찾을 수 없습니다: {e}")
except IOError as e:
    print(f"입출력 오류 발생: {e}")
except Exception as e:
    print(f"예상치 못한 오류 발생: {e}")