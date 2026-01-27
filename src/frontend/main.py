from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.withdraw()

def get_file(file_type: str= ".png") -> str:
    """
    Opens a file dialog from home directory if found, otherwise from cwd.
    :param file_path: A string that specifies the specific file type desired. 
                        Currently takes only one value specifically in the 
                        .ext format.
    :return: Returns the absolute path of the file
    """

    target_path = "~/"
    # if not os.path.exists(target_path):
    #     target_path = os.getcwd()
    # file_type = "*" + file_type

    file_path = filedialog.askopenfilename(
                    parent= root,
                    title= f"Select a {file_type[1:]}",
                    filetypes= [(file_type[1:], file_type)],
                    initialdir= target_path
                )

get_file()