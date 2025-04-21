import random
# 0.1 ~ 2
class DummySensor:
    env_values ={}
    def set_env(self):
        self.env_values["mars_base_internal_temperature"] = random.randrange(18, 31)
        self.env_values["mars_base_external_temperature"] = random.randrange(0, 22)
        self.env_values["mars_base_internal_humidity"] = random.randrange(50, 61)
        self.env_values["mars_base_external_illuminance"] = random.randrange(500, 716)
        self.env_values["mars_base_internal_co2"] = format((random.uniform(0, 1) * 0.2), ".2f")
        self.env_values["mars_base_internal_oxygen"] = random.randrange(4, 8)

    def get_env(self):
        return self.env_values

ds = DummySensor()

ds.set_env()
print(ds.get_env())

