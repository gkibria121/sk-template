from pathlib import Path
import concurrent.futures
import subprocess

path = Path.cwd()

num_workers = 0
commands = []
for dr in Path.iterdir(path):

    if dr.is_dir() and '__' not in str(dr):
        num_workers+=1
        pip_install_command = f"pip install -e {dr}"
        commands.append(pip_install_command)

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
        return f"Command '{command}' executed successfully."
    except subprocess.CalledProcessError as e:
        return f"Command '{command}' failed with error: {e}"

for command in commands:
    run_command(command)
