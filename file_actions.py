def create_file(file_name, content=None):
    """Create file with or without content"""
    mode = "w" if content else "x"
    file = open(file_name, mode)
    if content:
       file.write(content)
    file.close()



def modify__file(file_name, content, overwrite=False):
    """Modify file_name file.
    if overwrite is true, overwrite the file, if not, just update the file."""
    mode = "w" if overwrite else "a"
    file = open(file_name, mode)
    file.write(" " + content)
    file.close()



def read_file(file_name, mode='r'):
    """Read file´s content and returns content"""
    file = open(file_name, mode)
    output_file = file.read()
    file.close()
    return output_file