import os
import subprocess
from pyface.api import FileDialog, OK


def get_save_as_filename():
    wildcard =  'PNG file (.png)|*.png|TIFF file (.tiff)|*.tiff|EPS file (.eps)|*.eps|SVG file (.svg)|*.svg|'
    dialog = FileDialog(action='save as', title='Save as', wildcard=wildcard)
    if dialog.open() == OK:
        filename = dialog.path
        if filename:
            return filename
    return None

def get_file_list_from_dialog():
    wildcard = 'XYE XY (*.xye *.xy)|*.xye; *.xy|' \
               'XYE (*.xye)|*.xye|' \
               'XY (*.xy)|*.xy|' \
               'All files (*.*)|*.*'
    dlg = FileDialog(title='Choose files', action='open files', wildcard=wildcard)
    if dlg.open() == OK:
        return dlg.paths
    return []

def open_file_with_default_handler(filename):
    startfile(filename)

def open_file_dir_with_default_handler(filename):
    startfile(os.path.split(filename)[0])

def startfile(filename):
    try:
        os.startfile(filename)
    except:
        subprocess.Popen(['xdg-open', filename])

