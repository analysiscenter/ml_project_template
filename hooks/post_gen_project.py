import sys
import subprocess

subprocess.run(['git', 'init'])

mode = '{{ cookiecutter.libmode }}'
print("Mode is:{}.".format(mode))

library = '{{ cookiecutter.include_library }}'

libpaths = {
'SeismicPro': 'https://github.com/gazprom-neft/SeismicPro.git',
'SeismiQB': 'https://github.com/gazprom-neft/seismiqb.git',
'PetroFlow': 'https://github.com/gazprom-neft/petroflow.git',
'testlib': 'https://github.com/analysiscenter/segy.git',
}

if mode is "git.submodule":

    path = libpaths[library]
    subprocess.run(['git', 'submodule', 'add', path])
    subprocess.run(['git', 'submodule', 'update', '--init', '--recursive'])

    pass
else:
    print("Error! only 'git.submodule' mode is currenly valid. {} given".format(mode))
    sys.exit(1)

pass

subprocess.run(['git', 'add', '*'])
subprocess.run(['git', 'commit', '-m', '"initial commit"'])
