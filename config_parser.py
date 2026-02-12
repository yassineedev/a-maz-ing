class ConfigError(Exception):
    pass


class MazeConfig:
    def __init__(self):
        self.width = None
        self.height = None
        self.entry = None
        self.exit = None
        self.output_file = None
        self.perfect = True
        self.algo = "dfs"


Mandatory_keys = {"width", "height", "entry", "exit", "output_file", "perfect"}


def load_config(config_file):
    config_data = MazeConfig()
    allowed_keys = {
        "width",
        "height",
        "entry",
        "exit",
        "output_file",
        "perfect",
        "algo",
    }

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
                        f"Allowed keys: {', '.join(sorted(allowed_keys))}"
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
                                f"Line {line_number}: PERFECT must be True or Fa gilse. Got: '{value}'"
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

    if not (9 <= width <= 100):
        raise ConfigError(f"WIDTH must be between 9 and 100. Got: {width}")

    if not (7 <= height <= 100):
        raise ConfigError(f"HEIGHT must be between 7 and 100. Got: {height}")

    if not (0 <= entry_x < width) or not (0 <= entry_y < height):
        raise ConfigError(
            f"ENTRY position ({entry_x},{entry_y}) is outside maze bounds "
            f"(0..{width-1}, 0..{height-1})"
        )

    if not (0 <= exit_x < width) or not (0 <= exit_y < height):
        raise ConfigError(
            f"EXIT position ({exit_x},{exit_y}) is outside maze bounds "
            f"(0..{width-1}, 0..{height-1})"
        )

    if config.entry == config.exit:
        raise ConfigError("ENTRY and EXIT cannot be the same position")
