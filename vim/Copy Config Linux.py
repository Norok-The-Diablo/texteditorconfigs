import subprocess
username = subprocess.check_output(['whoami']).strip()
user = username.decode()
subprocess.run(["rm", "-rf", f"/home/{user}/.config/nvim"])
subprocess.run(["cp", "-r", "nvim", f"/home/{user}/.config/"])
subprocess.run(["rm", "-rf", f"/home/{user}/.vim"])
subprocess.run(["cp", "-r", ".vim", f"/home/{user}"])
subprocess.run(["cp", "-r", ".vimrc", f"/home/{user}"])
subprocess.run(["sudo", "cp", "-r", "nvimfont.ttf", "/usr/share/fonts/"])
