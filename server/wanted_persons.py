import cv2
import json
import numpy as np
import argparse
import os
from os import path
from PIL import Image
import face_processing.face_detection as fd
import face_processing.face_recognition as fr

WANTED_PATH = path.join("resources", "wanted")

# Initialize and retrive need information and functionality
detector = fd.FaceDetector()
recognizer = fr.FaceRecognizer()

def main(args=None):
    persons = load_persons(args.verbose) # Value is not use. Dict is only to quickly look up names.
    if args.operation is not None:
        perform_operation(persons, args.operation, args.operation_args, args.verbose)
    else:
        try:
            print("The following commands are available:\n  add [NAME] [IMAGE_PATH]\n  remove [NAME]\n  list\n  exit")
            while True:
                input_raw = input(">")
                input_parsed = parse_input(input_raw)
                perform_operation(persons, input_parsed["operation"], input_parsed["args"], args.verbose)
                
        except KeyboardInterrupt:
            print("Program terminated")
            exit()

def parse_input(str_input: str) -> dict:
    result = {}
    str_split = str_input.split(" ")
    result["operation"] = str_split[0]
    str_split.remove(str_split[0])
    result["args"] = str_split
    return result


def perform_operation(persons: dict, operation: str, args: list, verbose: bool):
    if operation.lower() == "add":
        if len(args) == 2:
            add_person(persons, verbose, args[0], args[1])
        else:
            print("Wrong number of arguments for add operation. Should look like: wantedPersons.py add [NAME] [IMAGE_PATH]")
    elif operation.lower() == "remove":
        if len(args) == 1:
            remove_person(persons, verbose, args[0])
        else:
            print("Wrong number of arguments for remove operation. Should look like: wantedPersons.py remove [NAME]")
    elif operation.lower() == "list":
        if len(args) == 0:
            list_persons(persons)
        else:
            print("Wrong number of arguments for list operation. Should look like: wantedPersons.py list")
    elif operation.lower() == "exit":
        exit()
    else:
        print("Unknown operation. Use either add, remove, list or exit.")

def load_persons(verbose: bool) -> dict:
    persons = {}
    if verbose:
        print("INFO: Loading existing persons...", end="")
    if path.exists(WANTED_PATH):
        for filename in os.listdir(WANTED_PATH):
            persons[filename.replace(".npy", "")] = None
    if verbose:
        print("done")
    return persons

def add_person(persons: dict, verbose: bool, name: str, image_path: str, wanted_folder_path: str = WANTED_PATH):
    if verbose:
        print("Adding \"" + name + "\" to database...", end="")
    
    # Validate input
    if name in persons:
        print("ERROR: Name already exists in wanted database.")
        return

    if not path.exists(image_path):
        print("ERROR: Path does not exist.")
        return

    # Load image and detect face
    image = cv2.imread(image_path)
    faces = detector.get_faces(image)

    if len(faces) == 1:
        # Produce features from image and save
        face = Image.fromarray(cv2.cvtColor(faces[0].face, cv2.COLOR_BGR2RGB))
        face_features = recognizer.get_features(recognizer.preprocess_image(face))
        np.save(path.join(wanted_folder_path, name), face_features)
        persons[name] = None 
    else:
        print("ERROR: Image multiple or no faces.")
    if verbose:
        print("done")
    
def remove_person(persons: dict, verbose: bool, name: str, wanted_folder_path: str = WANTED_PATH):
    if verbose:
        print("INFO: Removing \"" + name + "\" from database...", end="")
    if name not in persons:
        print("ERROR: Name does not exist in wanted database.")
        return
    del persons[name]
    os.remove(path.join(wanted_folder_path, name + ".npy"))
    if verbose:
        print("done")

def list_persons(persons: dict, wanted_folder_path: str = WANTED_PATH):
    print("Wanted persons:")
    for filename in os.listdir(wanted_folder_path):
        print("  " + filename.replace(".npy", ""))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("operation", type=str, metavar="OP", default=None, nargs="?", help="The operation to be performed.")
    parser.add_argument("operation_args", type=str, metavar="ARG", default=None, nargs="*", help="Arguments for the operation.")
    parser.add_argument("-v", "--verbose", action="store_true", default=False, required=False, help="Displays more text.")
    args = parser.parse_args()
    main(args)