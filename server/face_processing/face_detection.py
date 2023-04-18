import os
import cv2

CASCADE_PATH = os.path.join("resources", "haarcascade_frontalface_default.xml")
DEFAULT_OFFSET = 10

class FaceDetector:
    """
    This class holds methods for analyzing/finding faces on images
    """
    def __init__(self, face_cascade_path = CASCADE_PATH):
        # Create the face haar cascade:
        self.casc_path = face_cascade_path
        self.face_cascade = cv2.CascadeClassifier(self.casc_path)

    def find_faces_on_frame(self, image):
        """
        This class function finds and returns cropped faces on an image
        """
        # Grayscale the frame:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame:
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)

        # Draw rectangles around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        return image

    def get_faces(self, image, face_offset = DEFAULT_OFFSET):
        """
        This class function finds and returns cropped faces on an image
        """
        # Grayscale the frame:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the frame:
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)

        # Crop faces from the original image:
        cropped_faces = []
        for (x, y, w, h) in faces:
            #Finds all faces and puts them in a list:
            cropped_faces.append(Face(image, x, y, w, h, face_offset))
        return cropped_faces


class Face:
    """
    Contains information regarding one face found on a frame
    """
    def __init__(self, image, x, y, w, h, offset):
        height, width, channels = image.shape
        
        # Ensure left coordinate is not out of bounds
        if x - offset < 0:
            left_coord = 0 
        else:
            left_coord = x - offset
        
        # Ensure right coordinate is not out of bounds
        if x + w + offset > width:
            right_coord = width
        else:
            right_coord = x + w + offset

        # Ensure top coordinate is not out of bounds
        if y - offset < 0:
            top_coord = 0 
        else:
            top_coord = y - offset
        
        # Ensure bottom coordinate is not out of bounds
        if y + h + offset > height:
            bottom_coord = height
        else:
            bottom_coord = y + h + offset
        
        self.face = image[top_coord:bottom_coord, left_coord:right_coord]
        self.upper_left_x = left_coord
        self.upper_left_y = top_coord
        self.width = right_coord - left_coord
        self.height = bottom_coord - top_coord