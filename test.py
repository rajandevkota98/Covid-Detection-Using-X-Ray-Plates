from xray.utils.common import write_yaml_file
import os, sys
def test():
    try: 
        dict_ = {
        'label': 2
        }
        write_yaml_file('config/config.yaml',dict_)
    except Exception as e:
            print(e)

if __name__ == '__main__':
    test()