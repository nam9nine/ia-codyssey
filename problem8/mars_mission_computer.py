import os
import platform
import psutil

from problem7.mars_mission_computer import MissionComputer


def load_settings():
    settings_file = os.path.join(os.path.dirname(__file__), 'setting.txt')
    try:
        with open(settings_file, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.strip().startswith('#')]
    except FileNotFoundError:
        return None

def get_mission_computer_info(self):
    '''미션 컴퓨터 시스템 정보를 설정 파일에 따라 출력합니다.'''
    try:
        cpu_cores = os.cpu_count()
        total_memory = psutil.virtual_memory().total
    except Exception as e:
        self.env_values = {'error': str(e)}
        self.print_json()
        return
    info = {
        'operating_system': platform.system(),
        'os_version': platform.version(),
        'cpu_type': platform.processor() or platform.machine(),
        'cpu_cores': cpu_cores,
        'total_memory': total_memory
    }
    settings = load_settings()
    if settings:
        self.env_values = {k: v for k, v in info.items() if k in settings}
    else:
        self.env_values = info
    self.print_json()

def get_mission_computer_load(self):
    '''미션 컴퓨터 부하 정보를 설정 파일에 따라 출력합니다.'''
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
    except Exception as e:
        self.env_values = {'error': str(e)}
        self.print_json()
        return
    load = {
        'cpu_usage_percent': cpu_usage,
        'memory_usage_percent': memory_usage
    }
    settings = load_settings()
    if settings:
        self.env_values = {k: v for k, v in load.items() if k in settings}
    else:
        self.env_values = load
    self.print_json()

if __name__ == "__main__":
    MissionComputer.get_mission_computer_info = get_mission_computer_info
    MissionComputer.get_mission_computer_load = get_mission_computer_load

    runComputer = MissionComputer()

    runComputer.get_mission_computer_info()
    runComputer.get_mission_computer_load()
