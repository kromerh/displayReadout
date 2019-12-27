import cv2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class PressureReadoutObjectStorage():
    """
    This class contains the functions relevant to the pressure readout of the pump display with storage images.
    """

    def read_test_image(self,path):
        """
        Reads a pre-saved test image at location path (csv file) and returns it.
        """
        img = pd.read_csv(path, index_col=0).values

        return img

    def convert_rgb2gray(self, rgb):

        r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
        gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

        return gray

    def scale_image(self, img, scale_perc):
        """
        Takes an image img (numpy array) and returns a scaled (in percent) down version of the image (as np array.)
        """
#         scale_perc = 40 # percent of original size
        width = int(img.shape[1] * scale_perc / 100)
        height = int(img.shape[0] * scale_perc / 100)
        dim = (width, height)

        scaled_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

        return scaled_img

        def draw_rectangle(img, size, p0, p1, border=5):
            """
            Draws a rectangle with bordersize in the image img at position p0 (vertical), p1 (horizontal). The framesize of the sub-image is size.
            returns the image with the rectangle
            """
            img_t = img.copy()
            img_t[p0:p0+size+border,p1:p1+border] = 255.0 # left side
            img_t[p0:p0+size+border,p1+size:p1+size+border] = 255.0 # right side
            img_t[p0:p0+border,p1:p1+size] = 255.0 # top side
            img_t[p0+size:p0+size+border,p1:p1+size] = 255.0 # bottom side

            return img_t