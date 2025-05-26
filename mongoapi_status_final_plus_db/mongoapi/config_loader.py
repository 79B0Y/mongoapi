import yaml

def load_config(path='configuration.yaml'):
    with open(path, 'r') as file:
        return yaml.safe_load(file)