from PyQt5.QtGui import QColor, QImage, qRgb
import numpy as np

class HistogramUtil(object):
    def __init__(self):
        raise AssertionError("HistogramUtil cannot be instantiated.")

    @staticmethod
    def __makeCumulativeHistogram(histogram):
        cumulative_hist = np.zeros((3, 256), dtype=np.int32)

        for k in range(0, 3):
            cumulative_hist[k][0] = histogram[k][0]

        for k in range(0, 3):
            for i in range(1, 256):
                cumulative_hist[k][i] = cumulative_hist[k][i - 1] + histogram[k][i]

        return cumulative_hist

    @staticmethod
    def calcHistogram(img):
        len_w = img.size().width()
        len_h = img.size().height()
        hist = np.zeros((3, 256), dtype=np.int32)

        for i in range(0, len_w):
            for j in range(0, len_h):
                c = QColor(img.pixel(i, j)).getRgb()
                for k in range(0, 3):
                    hist[k][c[k]] += 1
        
        return hist

    @staticmethod
    def getHistogramMatchingLUT(input_hist, target_hist):
        input_hist_cumulative = HistogramUtil.__makeCumulativeHistogram(input_hist)
        target_hist_cumulative = HistogramUtil.__makeCumulativeHistogram(target_hist)

        lut = np.zeros((3, 256), dtype=np.int32)

        for k in range(0, 3):
            for i in range(0, 256):
                j = 0

                while target_hist_cumulative[k][j] < input_hist_cumulative[k][i] and j < 255:
                    j += 1

                lut[k][i] = j

        return lut

    @staticmethod
    def matchHistogram(lut, input_img):
        len_w = input_img.size().width()
        len_h = input_img.size().height()

        result_img = QImage(input_img)

        for w in range(0, len_w):
            for h in range(0, len_h):
                c = QColor(input_img.pixel(w, h)).getRgb()

                result_img.setPixel(w, h, qRgb(lut[0][c[0]], lut[1][c[1]], lut[2][c[2]]))

        return result_img
