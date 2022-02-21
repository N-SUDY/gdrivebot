# From https://github.com/Dank-del/EsseX/blob/master/thebot/modules/__init__.py
from glob import glob
from os.path import dirname, basename, isfile

'''Methods Directory.'''

def __list_all_modules():
    # This generates a list of modules in this folder for the * in __main__ to work.
    mod_paths = glob(f'{dirname(__file__)}/*.py')
    return [
        basename(f)[:-3] for f in mod_paths if isfile(f)
        and f.endswith(".py")
        and not f.endswith('__init__.py')
        ]


ALL_MODULES = sorted(__list_all_modules())
__all__ = ALL_MODULES + ["ALL_MODULES"]