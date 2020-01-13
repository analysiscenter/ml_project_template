import sys
import subprocess

mode = '{{ cookiecutter.libmode }}'
print("Mode is:{}.".format(mode))

library = '{{ cookiecutter.include_library }}'

libpaths = {
'SeismicPro': 'https://github.com/gazprom-neft/SeismicPro.git',
'SeismiQB': 'https://github.com/gazprom-neft/seismiqb.git',
'PetroFlow': 'https://github.com/gazprom-neft/petroflow.git',
}

if mode is "git.submodule":

    path = libpaths[library]
    subprocess.run(['git', 'submodule', 'add', path])
    subprocess.run(['git', 'submodule', 'update', '--init'])

    pass
else:
    print("Error! only 'git.submodule' mode is currenly valid. {} given".format(mode))
    sys.exit(1)

pass
