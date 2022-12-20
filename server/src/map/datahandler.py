import numpy as np
import torch

class District():
    def __init__(self, img_path, latitude, longitude, object, scale):
        # img_path
        # string of image path from main.py folder
        # latitude
        # numpy array of size 4, demension 1 composed of float
        # from upper left corner, counterclockwise
        # longitude
        # numpy array of size 4, demension 1 composed of float
        # from upper left corner, counterclockwise
        # object
        # numpy array of size 4 x 2, demension n
        # n is number of objects
        # 4 is vertex
        # 2 is pixel of x, y in (0,0) - bottom left ~ (1,1) - upper right scale region
        # TODO: counterclockwise?
        # scale
        # numpy array of size 2, demension 1
        # 2 is x, y meter scale which one image covers.
        self.img_path = img_path
        self.latitude = latitude
        self.longitude = longitude
        self.object = object
        self.scale = scale

    # returns image path
    def path(self):
        return self.img_path

    def get_img(self):
        return torch.load(self.img_path)[0]

    # returns center point of the image in latitude scale.
    def lat_center(self):
        lat = 0.5 * (self.latitude[0] + self.latitude[2])
        return lat

    # returns center point of the image in longitude scale.
    def lon_center(self):
        lon = 0.5 * (self.longitude[0] + self.longitude[2])
        return lon

    # returns center point of object in meter scale.
    def obj_center(self):
        return 0.5 * (self.object[:][0] + self.object[:][2]) * self.scale

    # returns latitude range which the image covers.
    def lat_range(self):
        return max(self.latitude) - min(self.latitude)

    # returns longitude range which the image covers.
    def lon_range(self):
        return max(self.longitude) - min(self.longitude)

    # returns horizontal - vertical range which the object covers in meter scale.
    # horizontal is shorter, vertical is longer direction
    # assumed this object is a car
    def obj_range(self):
        pixel_firstside = object[:][1] - object[:][0]
        pixel_secondside = object[:][3] - object[:][0]
        horizontal_size = min(np.linalg.norm(pixel_firstside[:]), np.linalg.norm(pixel_secondside[:]))
        vertical_size = max(np.linalg.norm(pixel_firstside[:]), np.linalg.norm(pixel_secondside[:]))
        return horizontal_size, vertical_size