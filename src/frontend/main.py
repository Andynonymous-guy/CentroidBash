from tkinter import *
from tkinter import filedialog
from src.backend.vision.with_opencv import test_corners
import os
from cv2 import circle 
from cv2 import imshow

root = Tk()
root.withdraw()

def get_file(file_type: str= ".png") -> str:
    """
    Basic file grabber using Tkinter GUI and OS path management.
    
    :param file_type: Specifier for file type in "*.ext" format. Currently takes only one . 
    :type file_type: str
    :return: string literal of the file path selected by the user.
    :rtype: str
    """

    target_path = "~/"
    if not os.path.exists(os.path.expanduser("~/")):
        print("Defaulting to current directory.")
        target_path = os.getcwd()
    file_type = "*" + file_type

    file_path = filedialog.askopenfilename(
                    parent= root,
                    title= f"Select a {file_type[1:]}",
                    filetypes= [(file_type[1:], file_type)],
                    initialdir= target_path
                )
    
    # Graceful exit on window closure.
    if not file_path:
        raise SystemExit("No input received, program terminated.")
    
    return file_path


def test_run_pipeline():
    file_path = os.getcwd() + "/tests/test_images/Polygon1.png"
    print(file_path)
    corners = test_corners(file_path)
    return

if __name__ == "__main__":
    test_run_pipeline()