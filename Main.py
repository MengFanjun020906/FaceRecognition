from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
import time
import cv2
import numpy as np
from retinaface import Retinaface
import extract_name
import compare
from SelectPic import pick_video
from SelectPic import pick_pic
from SelectPic import encode_pic
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
import predict_pic
import predict_video


if __name__ == '__main__':
    predict_pic.detect_pic(pick_pic())
    predict_video.detect_video(pick_video())


