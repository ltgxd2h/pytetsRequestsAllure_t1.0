import configparser
import os

path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),'sitting.ini')

def read_sitting():
    config = configparser.ConfigParser()
    config.read(path,encoding='utf8')
    return config

get_sitting = read_sitting()

if __name__ == '__main__':

    print(get_sitting['host']['api_ssourl_test1'])
    print(path)