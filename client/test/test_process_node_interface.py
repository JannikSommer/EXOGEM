import unittest
from os import path
from process_node_interface import ProcessNodeInterface

class TestEncodeImage(unittest.TestCase):
    def test_encode_data(self):
        #Test if data is encoded correctly to base64
        data = "Encode this!"
        
        data_encoded = ProcessNodeInterface.encode_image(bytes(data, "utf-8"))
        self.assertEqual(data_encoded, "RW5jb2RlIHRoaXMh")

    def test_decode_data(self):
        #Test if data is decoded correctly from base64
        data = "RW5jb2RlIHRoaXMh"
        
        data_decoded = ProcessNodeInterface.decode_image(data)
        self.assertEqual(data_decoded, bytes("Encode this!", "utf-8"))

    def test_encode_and_decode_image(self):
        #Tests if face.png encoded and decoded without dataloss.
        with open(path.join(path.dirname(path.abspath(__file__)), "images", "face.png"), 'rb') as file:
            raw_image = file.read()
            encoded_image = ProcessNodeInterface.encode_image(raw_image)
            decoded_image = ProcessNodeInterface.decode_image(encoded_image)
            
            self.assertEqual(decoded_image, raw_image)


if __name__ == "__main__":
    unittest.main()