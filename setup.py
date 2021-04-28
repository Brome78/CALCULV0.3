
from cx_Freeze import setup, Executable
base = None
executables = [Executable("CALCULV0.3.py", base=base, icon="icone.ico")]

packages = ["tkinter", "tkinter.messagebox", "math"]
options = {
    'build_exe': {    
        'packages':packages,
    },
}
setup(
    name = "Calcul V0.3",
    author = "Brome78",
    options = options,
    version = "0.3",
    description = 'Programme de calcul',
    executables = executables,
    icon = "icone de l'app"
)