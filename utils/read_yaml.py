import yaml
import os

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "test_data", "data.yaml")

def read_yaml():
    f  = open(data_path, encoding="utf8")
    data = yaml.safe_load(f)
    return data

get_yaml = read_yaml()

if __name__ == '__main__':
    print(get_yaml['clientStatus'])