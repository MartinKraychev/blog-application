import os


def delete_file(path):
    """ Deletes file from filesystem. """
    if os.path.isfile(path):
        os.remove(path)
