import yaml
from src import mid
from src.mid import inter_user
import os
# #Python version = 3.7
# import numpy as np
# from src.datahandler import District
#
#
# if(__name__ == "__main__") :
#     path = "./data/training/test_image.png"
#     latitude = np.array( [37.222829, 37.347723, 37.347723, 37.222829] )
#     longitude = np.array( [127.222829, 127.222829, 127.347723, 127.347723] )
#     object = np.array( 1024, 4, 2 )
#     for i in range(1024) :
#         for j in range(4) :
#             object[i][j][0] = 100
#             object[i][j][1] = 50
#
#     scale = np.array( [400, 800] )
#     district = District(path, latitude, longitude, object, scale)


def main():
    inter_user.turn_on(cfg)
    targets = os.listdir(f'{mid.PATH_data}')
    inter_user.get_traffic(targets[0])
    print()


if __name__ == '__main__':
    with open('_config.yml', 'r') as f:
        cfg = yaml.safe_load(f)
    main()