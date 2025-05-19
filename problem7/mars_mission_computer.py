from problem6.mars_mission_computer import DummySensor
import time

class MissionComputer:
    def __init__(self):
        self.env_values = {}
        self.ds = DummySensor()
        self.count = 0
        self.values_storage = {
            "mars_base_internal_temperature": 0,
            "mars_base_external_temperature": 0,
            "mars_base_internal_humidity": 0,
            "mars_base_external_illuminance": 0,
            "mars_base_internal_co2": 0.0,
            "mars_base_internal_oxygen": 0
        }
        self.interval = 300.0
        
    def get_sensor_data(self):
        last_time = time.monotonic()
        while True:
            try:
                now = time.monotonic()

                self.ds.set_env()
                data = self.ds.get_env()

                self.env_values['mars_base_internal_temperature'] = data['mars_base_internal_temperature']
                self.env_values['mars_base_external_temperature'] = data['mars_base_external_temperature']
                self.env_values['mars_base_internal_humidity'] = data['mars_base_internal_humidity']
                self.env_values['mars_base_external_illuminance'] = data['mars_base_external_illuminance']
                self.env_values['mars_base_internal_co2'] = data['mars_base_internal_co2']
                self.env_values['mars_base_internal_oxygen'] = data['mars_base_internal_oxygen']

                # json형식으로 출력
                self.print_json()
                
                # 환경 값 수집
                for v in self.env_values:
                    self.values_storage[v] += self.env_values[v]

                self.count += 1

                if now - last_time >= self.interval:
                    self.print_average()
                    last_time = time.monotonic()
                    self.values_storage = {
                        k: 0.0 if isinstance(prev, float) else 0
                        for k, prev in self.values_storage.items()
                    }

                time.sleep(5)


            except KeyboardInterrupt:
                print("\nSystem stopped…")
                break;
            
    def print_json(self):
        lines = []
        for k, v in self.env_values.items():
            lines.append(f'\t"{k}": "{v}"')
        print("{")
        print(",\n".join(lines))
        print("}")

    def print_average(self):
        for v in self.values_storage:
            print(f'{v} : {self.values_storage[v] / self.count}')
        self.count = 0
        
def main():
    RunComputer = MissionComputer()
    RunComputer.get_sensor_data()

if __name__ == "__main__":
    main()
