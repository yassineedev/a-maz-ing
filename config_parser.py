class ConfigError(Exception):
    pass


class MazeConfig():
    def __init__(self):
        self.width = None
        self.height = None
        self.entry = None
        self.exit = None
        self.output_file = None
        self.perfect = None

def load_config(config_file):
    config_data = MazeConfig()
    names = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"]

    with open(config_file, "r") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if '=' not in line:
                    raise ConfigError(f"Invalid line in config: {line}")
            key, value = line.split('=', 1)
            if key not in names:
                 raise ConfigError(f"Invalid line in config: {line}")
            key = key.strip().lower()
            value = value.strip()
            if key == "width":
                value = int(value)
                if value > 100:
                     raise ConfigError("max of widthe is '100'")
            if key == "height":
                 value = int(value)
                 if value > 100:
                     raise ConfigError("max of height is '100'")
            if key == "entry" or key == "exit":
                 vx, vy = value.split(",")
                 value = (int(vx), int(vy))
            if key == "perfect":
                 if value != "True" and value != "False":
                      raise ConfigError("perfect acsipt jast True or False")
            setattr(config_data, key, value)
    return config_data