from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.withdraw()

def get_file(file_type: str= ".png") -> str:
    """
    Prompts user to select image, starting in home directory if found, 
    defaulting to current directory if not.
    :param file_path: Image format specifier, must be in "*.ext" form.
    :return: Returns the absolute path of the file
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