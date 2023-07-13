import os
import json



def create_file(file_name, content=None):
    """Create file with or without content"""
    mode = "w" if content else "x"
    try:
        file = open(file_name, mode)
    except FileExistsError as error:
        raise OSError(f'File "{file_name}" already exists') from error
    except PermissionError as error:
        raise OSError(f'You do not have permission to create "{file_name}"') from error

    if content:
       file.write(content)
    file.close()



def modify__file(file_name, content, overwrite=False):
    """Modify file_name file.
    if overwrite is true, overwrite the file, if not, just update the file."""
    if not isinstance(content, str) or content == "":
        raise ValueError("Content agument must be specified")  #Stops the execution of the function

    mode = "w" if overwrite else "a"
    file = open(file_name, mode)
    file.write(" " + content)
    file.close()



def read_file(file_name):
    """Read file´s content and returns it"""
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"File {file_name} was not found")

    file = open(file_name)
    output = file.read()
    if output == "":
        raise ValueError(f"Not data found in file '{file_name}'")
    file.close()
    return output