class ConfigError(Exception):
    pass


class MazeConfig:
    def __init__(self):
        self.width = None
        self.height = None
        self.entry = None
        self.exit = None
        self.output_file = None
        self.perfect = None
        self.algo = "dfs"
        self.is_path_42 = True


Mandatory_keys= {"width", "height", "entry", "exit", "output_file", "perfect"}


def load_config(config_file):
    config_data = MazeConfig()
    allowed_keys = {"width", "height", "entry", "exit", "output_file", "perfect", "algo"}

    try:
        with open(config_file, "r") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                if "=" not in line:
                    raise ConfigError(
                        f"Line {line_number}: Invalid format. Expected KEY=VALUE, got: '{line}'"
                    )

                key, value = line.split("=", 1)
                key = key.strip().lower()
                value = value.strip()

                if key not in allowed_keys:
                    raise ConfigError(
                        f"Line {line_number}: Unknown key '{key}'. "
                        f"Allowed keys: {', '.join(allowed_keys)}"
                    )

                try:
                    if key in ("width", "height"):
                        value = int(value)

                    elif key in ("entry", "exit"):
                        parts = value.split(",")
                        if len(parts) != 2:
                            raise ValueError
                        x, y = parts
                        value = (int(x), int(y))

                    elif key == "perfect":
                        v = value.lower()
                        if v == "true":
                            value = True
                        elif v == "false":
                            value = False
                        else:
                            raise ConfigError(
                                f"Line {line_number}: PERFECT must be True or False. Got: '{value}'"
                            )

                    elif key == "ALGO":
                        v = value.lower()
                        if v not in ("dfs", "prim"):
                            raise ConfigError(
                                f"Line {line_number}: Invalid algorithm '{value}'. "
                                "Supported algorithms: dfs, prim"
                            )
                        value = v

                    else:
                        value = value

                except ValueError:
                    if key in ("entry", "exit"):
                        raise ConfigError(
                            f"Line {line_number}: {key.upper()} must be in format x,y "
                            f"(example: 0,0). Got: '{value}'"
                        )
                    else:
                        raise ConfigError(
                            f"Line {line_number}: {key.upper()} must be an integer. Got: '{value}'"
                        )

                setattr(config_data, key, value)

    except FileNotFoundError:
        raise ConfigError(f"Config file not found: '{config_file}'")

    last_check(config_data)
    return config_data


def last_check(config):
    for key in Mandatory_keys:
        if getattr(config, key) is None:
            raise ConfigError(f"Missing required config key: {key.upper()}")

    width = config.width
    height = config.height
    entry_x, entry_y = config.entry
    exit_x, exit_y = config.exit

    if height < 7 or width < 9:
        config.is_path_42 = False
        print("i not can draw path 42 because this maze is small")

    if height > 100 or width > 100:
        raise ConfigError("the maze is very big maz the height is 100 and maze the width is 100")
    
    if not (0 <= entry_x < width) or not (0 <= entry_y < height):
        raise ConfigError(
            f"ENTRY position ({entry_x},{entry_y}) is outside maze bounds")

    if not (0 <= exit_x < width) or not (0 <= exit_y < height):
        raise ConfigError(
            f"EXIT position ({exit_x},{exit_y}) is outside maze bounds")

    if config.entry == config.exit:
        raise ConfigError(
            "ENTRY and EXIT cannot be the same position"
        )
