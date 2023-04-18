
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1' 
# 0 = all messages are logged (default behavior)
# 1 = INFO messages are not printed
# 2 = INFO and WARNING messages are not printed
# 3 = INFO, WARNING, and ERROR messages are not printed

import numpy as np
from os import path
from PIL import Image
import tensorflow as tf
from numpy import dot
from numpy.linalg import norm

ENCODER_PATH = path.join(path.dirname(path.abspath(__file__)), "models", "encoder.h5")

class FaceRecognizer:
    def __init__(self, encoder_path = ENCODER_PATH):
        # load model
        self.encoder = tf.keras.models.load_model(encoder_path, compile=False)
        self.encoder.build((None, 64, 64, 3))

    def get_features(self, image):
        """
        Extract facial features from image.
        """
        if len(image.shape) == 3:
            x = image[None]
            return self.encoder.predict(x)[0]
        elif len(image.shape) == 4:
            x = image
            return self.encoder.predict(x)
        else:
            raise Exception('img size does not match')

    def compare_images(self, image1_path, image2_path):
        """
        Compares two images with a face on each
        """
        img1_features = self.get_features(self.preprocess_image_from_file(image1_path))
        img2_features = self.get_features(self.preprocess_image_from_file(image2_path))
        return self.compare_features(img1_features, img2_features)

    @classmethod
    def compare_features(cls, features1, features2):
        """
        Compares two facial features
        """
        return cls.cosine_similarity(features1[None], features2[None])

    @classmethod
    def cosine_similarity(cls, f1, f2):
        return dot(f1[0], f2[0]) / (norm(f1[0]) * norm(f2[0]))

    @classmethod
    def preprocess_image_from_file(cls, path):
        """
        Prepares image for feature extraction.
        """
        im = Image.open(path)
        width, height = im.size
        new_width = 140
        new_height = 140
        
        left = (width - new_width) / 2
        top = (height - new_height) / 2
        right = (width + new_width) / 2
        bottom = (height + new_height) / 2
        im = im.crop((left, top, right, bottom))
        im = im.resize((64, 64), Image.ANTIALIAS)
        im = (np.array(im) / 255.).astype(np.float32)
        im = 2*im -1
        return im

    @classmethod
    def preprocess_image(cls, im):
        """
        Prepares image for feature extraction.
        """
        width, height = im.size
        new_width = 140
        new_height = 140
        
        left = (width - new_width) / 2
        top = (height - new_height) / 2
        right = (width + new_width) / 2
        bottom = (height + new_height) / 2
        im = im.crop((left, top, right, bottom))
        im = im.resize((64, 64), Image.ANTIALIAS)
        im = (np.array(im) / 255.).astype(np.float32)
        im = 2*im -1
        return im