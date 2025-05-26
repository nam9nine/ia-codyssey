import time
import threading
import multiprocessing
from problem8.mars_mission_computer import MissionComputer


def threading_mode():
    run_computer = MissionComputer()
    threads = [
        threading.Thread(target=run_computer.get_mission_computer_info, name='computer_info', daemon=True),
        threading.Thread(target=run_computer.get_mission_computer_load, name='computer_load', daemon=True),
        threading.Thread(target=run_computer.get_sensor_data, name='sensor_data', daemon=True),
    ]
    for t in threads:
        t.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print('멀티 쓰레드 모니터링 종료.')

def multiprocessing_mode():
    runComputer1 = MissionComputer()
    runComputer2 = MissionComputer()
    runComputer3 = MissionComputer()
    processes = [
        multiprocessing.Process(target=runComputer1.get_mission_computer_info, name='computer_info'),
        multiprocessing.Process(target=runComputer2.get_mission_computer_load, name='computer_load'),
        multiprocessing.Process(target=runComputer3.get_sensor_data, name='sensor_data'),
    ]
    for p in processes:
        p.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        for p in processes:
            p.terminate()
        print('멀티 프로세스 모니터링 종료.')

def main():
    threading_mode()
    multiprocessing_mode()


if __name__ == '__main__':
    main()