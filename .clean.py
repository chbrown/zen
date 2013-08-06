import os
import shutil


def remove(filepath):
    if os.path.exists(filepath):
        if os.path.isdir(filepath):
            shutil.rmtree(filepath)
        else:
            os.remove(filepath)


def rename(filepath, destination):
    if os.path.exists(filepath):
        os.rename(filepath, destination)


remove('style/__init__.py')
remove('style/__init__.pyc')
rename('sanity/', '.sanity/')

remove('.sanity/sanity.egg-info')
remove('.sanity/build')
remove('.sanity/dist')
