import yaml
import dotmap


def load_config(filepath_config):
    with open(filepath_config, "r") as f:
        config = yaml.safe_load(f)
    config = dotmap.DotMap(config)
    return config
