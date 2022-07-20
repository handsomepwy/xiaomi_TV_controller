import requests
import tkinter
from tkinter import PhotoImage
tv_ip = "192.168.1.9"
# 在这里设置你的小米电视ip


def up():
    requests.get('https://{}:6095/controller?action=keyevent&keycode=up'.format(tv_ip))


def down():
    requests.get('https://{}:6095/controller?action=keyevent&keycode=down'.format(tv_ip))


def left():
    requests.get('https://{}:6095/controller?action=keyevent&keycode=left'.format(tv_ip))


def right():
    requests.get('https://{}:6095/controller?action=keyevent&keycode=right'.format(tv_ip))


def enter():
    requests.get('https://{}:6095/controller?action=keyevent&keycode=enter'.format(tv_ip))


def home():
    requests.get('https://{}:6095/controller?action=keyevent&keycode=home'.format(tv_ip))


def menu():
    requests.get('https://{}:6095/controller?action=keyevent&keycode=menu'.format(tv_ip))


def volup():
    requests.get('https://{}:6095/controller?action=keyevent&keycode=volumeup'.format(tv_ip))


def voldown():
    requests.get('https://{}:6095/controller?action=keyevent&keycode=volumedown'.format(tv_ip))


def back():
    requests.get('https://{}:6095/controller?action=keyevent&keycode=back'.format(tv_ip))


def power():
    requests.get('https://{}:6095/controller?action=keyevent&keycode=power'.format(tv_ip))
# 每个按钮的网址访问


root = tkinter.Tk()
root.title("小米电视遥控器")
root.iconbitmap("tv_icon.ico")
up_pic = PhotoImage(file="up.png")
down_pic = PhotoImage(file="down.png")
left_pic = PhotoImage(file="left.png")
right_pic = PhotoImage(file="right.png")
enter_pic = PhotoImage(file="enter.png")
home_pic = PhotoImage(file="home.png")
menu_pic = PhotoImage(file="menu.png")
volup_pic = PhotoImage(file="volup.png")
voldown_pic = PhotoImage(file="voldown.png")
power_pic = PhotoImage(file="power.png")
back_pic = PhotoImage(file="back.png")
# 导入不同按钮图片
up_btn = tkinter.Button(root, text="向上", command=up, image=up_pic)
up_btn.grid(row=1, column=1)
down_btn = tkinter.Button(root, text="向下", command=down, image=down_pic)
down_btn.grid(row=3, column=1)
left_btn = tkinter.Button(root, text="向左", command=left, image=left_pic)
left_btn.grid(row=2, column=0)
right_btn = tkinter.Button(root, text="向右", command=right, image=right_pic)
right_btn.grid(row=2, column=2)
enter_btn = tkinter.Button(root, text="确认", command=enter, image=enter_pic)
enter_btn.grid(row=2, column=1)
home_btn = tkinter.Button(root, text="主页", command=home, image=home_pic)
home_btn.grid(row=3, column=2)
menu_btn = tkinter.Button(root, text="菜单", command=menu, image=menu_pic)
menu_btn.grid(row=4, column=2)
volup_btn = tkinter.Button(root, text="音量加", command=volup, image=volup_pic)
volup_btn.grid(row=3, column=0)
voldown_btn = tkinter.Button(root, text="音量减", command=voldown, image=voldown_pic)
voldown_btn.grid(row=4, column=0)
back_btn = tkinter.Button(root, text="返回", command=back, image=back_pic)
back_btn.grid(row=5, column=1)
power_btn = tkinter.Button(root, text="电源键", command=power, image=power_pic)
power_btn.grid(row=6, column=1)
# tkinter按钮, 布局可换
root.mainloop()
