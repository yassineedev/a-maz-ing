class ConfigError(Exception):
    pass


class MazeConfig():
    def __init__(self):
        self.width = None
        self.entry = None
        self.exit = None
        self.output_file = None
        self.perfect = None


def load_config(config_file):
    config_data = MazeConfig()

    with open(config_file, "r") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, value = line.split('=', 1)
            key = key.lower()
            config_data.key = value
            print(config_data.key)
    
     
    return config_data
