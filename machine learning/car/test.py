import subprocess
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext
import sys

window = Tk()

# Write terminal output to file
savefile = 'text.txt'
hold_stdout = sys.stdout
sys.stdout = open(savefile, 'w')
sys.stdout = hold_stdout

# modify window
window.title("Server Commander")
window.geometry("600x350")

tab_control = ttk.Notebook(window)

# Creating tabs
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

# Modifying tabs
tab_control.add(tab1, text='Server')
tab_control.add(tab2, text='Computer')


# Creating button & actions
# Tab Server
def issue():
    subprocess.run('ssh sweetth@192.168.1.99 sudo systemctl start pyload', shell=True)
    messagebox.showinfo('Start PyLoad', 'PyLoad Started successfully!')


btn = Button(tab1, text="Start Pyload", command=issue, height=1, width=12)
btn.grid(column=1, row=5, sticky='news')


def issue():
    subprocess.run("ssh sweetth@192.168.1.99 sudo systemctl stop pyload", shell=True)
    messagebox.showinfo('Stop PyLoad', 'Pyload Stopped successfully!')


btn = Button(tab1, text="Stop PyLoad", command=issue, height=1, width=12)
btn.grid(column=2, row=5, sticky='news')


def issue():
    subprocess.run("ssh sweetth@192.168.1.99 python -m mnamer -bvr /mnt/hd/Download/", shell=True)
    messagebox.showinfo('Mnamer', 'Mnamer successfully!')


btn = Button(tab1, text="Mnamer", command=issue, height=1, width=12)
btn.grid(column=1, row=6, sticky='news')


def issue():
    subprocess.run("ssh sweetth@192.168.1.99 /usr/local/sbin/extractall.sh", shell=True)
    messagebox.showinfo('Extract Files', 'Extract Files successfully!')


btn = Button(tab1, text="Extract Files", command=issue, height=1, width=12)
btn.grid(column=1, row=7, sticky='news')


def issue():
    subprocess.run("ssh sweetth@192.168.1.99 rm /mnt/hd/Download/*.rar", shell=True)
    messagebox.showinfo('Remove Rar', 'Remove Rar successfully!')


btn = Button(tab1, text="Remove Rar", command=issue, height=1, width=12)
btn.grid(column=2, row=7, sticky='news')


def issue():
    subprocess.run("deepin-terminal -e ssh sweetth@192.168.1.99", shell=True)
    messagebox.showinfo('SSH GoFlex', 'SSH GoFlex successfully!')


btn = Button(tab1, text="SSH GoFlex", command=issue, height=1, width=12)
btn.grid(column=1, row=8, sticky='news')


def issue():
    subprocess.run("deepin-terminal -e ssh sweetth@192.168.1.24", shell=True)
    messagebox.showinfo('SSH Paco', 'SSH Paco successfully!')


btn = Button(tab1, text="SSH Paco", command=issue, height=1, width=12)
btn.grid(column=2, row=8, sticky='news')


def issue():
    subprocess.run("sudo -u sweetth mount /mnt/share && dde-file-manager /mnt/share/", shell=True)
    messagebox.showinfo('Mount GoFlex', 'Mount GoFlex successfully!')


btn = Button(tab1, text="Mount GoFlex", command=issue, height=1, width=12)
btn.grid(column=1, row=9, sticky='news')


def issue():
    subprocess.run("sudo umount /mnt/share", shell=True)
    messagebox.showinfo('Umount GoFlex', 'Umount GoFlex successfully!')


btn = Button(tab1, text="Umount GoFlex", command=issue, height=1, width=12)
btn.grid(column=2, row=9, sticky='news')


def issue():
    subprocess.run("ssh sweetth@192.168.1.99 sudo systemctl reboot", shell=True)
    messagebox.showinfo('Reboot NAS', 'Reboot NAS successfully!')


btn = Button(tab1, text="Reboot NAS", command=issue, height=1, width=12)
btn.grid(column=1, row=10, sticky='news')


def issue():
    subprocess.run("ssh sweetth@192.168.1.99 sudo systemctl poweroff", shell=True)
    messagebox.showinfo('Power Off NAS', 'Power Off NAS successfully!')


btn = Button(tab1, text="Power Off NAS", command=issue, height=1, width=12)
btn.grid(column=2, row=10, sticky='news')

text_area = scrolledtext.ScrolledText(tab1, width=50, height=15, wrap="word")
text_area.grid(column=3, row=1, rowspan=12)


# Tab Computer
def issue():
    subprocess.run('sudo systemctl start pyload', shell=True)
    messagebox.showinfo('Start PyLoad', 'PyLoad Started successfully!')


btn = Button(tab2, text="Start PyLoad", command=issue, height=1, width=12)
btn.grid(column=1, row=1, sticky='news')


def issue():
    subprocess.run("sudo systemctl stop pyload", shell=True, )
    messagebox.showinfo('Stop PyLoad', 'Pyload Stopped successfully!')


btn = Button(tab2, text="Stop PyLoad", command=issue, height=1, width=12)
btn.grid(column=2, row=1, sticky='news')

text_area = scrolledtext.ScrolledText(tab2, width=50, height=15, wrap="word")
text_area.grid(column=3, row=1, rowspan=12)

tab_control.pack(expand=1, fill='both')

# event loop
window.mainloop()