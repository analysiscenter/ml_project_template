import sys
import subprocess
import json


mode = '{{ cookiecutter.libmode }}'
print("Mode is:{}.".format(mode))

library = '{{ cookiecutter.include_library }}'

libpaths = {
'SeismicPro': 'https://github.com/gazprom-neft/SeismicPro.git',
'SeismiQB': 'https://github.com/gazprom-neft/seismiqb.git',
'PetroFlow': 'https://github.com/gazprom-neft/petroflow.git',
# 'testlib': 'https://github.com/analysiscenter/segy.git',
}

if mode is "git.submodule":

    subprocess.run(['git', 'init'])

    path = libpaths[library]
    subprocess.run(['git', 'submodule', 'add', path])
    subprocess.run(['git', 'submodule', 'update', '--init', '--recursive'])

    with open('extra/.cookiecutter.json') as inpf:
        context = json.load(inpf)

    context['libmode'] = 'no_submodules'

    with open('extra/.cookiecutter.json', 'w') as outf:
        json.dump(context, outf, indent=4)

    subprocess.run(['git', 'add', '*'])
    subprocess.run(['git', 'commit', '-m', '"initial commit"'])
