from pathlib import Path
import subprocess

cwd = Path(".\\").absolute()
subprocess.call(f"madoko-local.cmd -rl --homedir {cwd}")