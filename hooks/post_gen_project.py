import sys
import subprocess
import json


library = '{{ cookiecutter.include_library }}'

print("Library is", library)

libpaths = {
'SeismicPro': 'https://github.com/gazprom-neft/SeismicPro.git',
'SeismiQB': 'https://github.com/gazprom-neft/seismiqb.git',
'PetroFlow': 'https://github.com/gazprom-neft/petroflow.git',
'batchflow': 'https://github.com/analysiscenter/batchflow.git'
# 'testlib': 'https://github.com/analysiscenter/segy.git',
}

print("initializing git repo ...")
subprocess.run(['git', 'init'])

if library is not "no":

    print("adding submodule", library, "...")

    path = libpaths[library]
    subprocess.run(['git', 'submodule', 'add', path])
    subprocess.run(['git', 'submodule', 'update', '--init', '--recursive'])

subprocess.run(['git', 'add', '*'])
subprocess.run(['git', 'commit', '-m', '"initial commit"'])
