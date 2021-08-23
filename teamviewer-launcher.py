#!/bin/python3

import tkinter as tk
from tkinter import messagebox

class Dialog:
	dialogTk = None
	passwordLabel = None
	password = None
	passwordEntry = None
	loginButton = None
	result = None
	exitType = None
	def __init__(self):
		self.dialogTk = tk.Tk()
		self.dialogTk.geometry('200x80')
		self.dialogTk.title('Passowrd')
		self.dialogTk.protocol("WM_DELETE_WINDOW", self.on_closing)
		self.dialogTk.bind('<Escape>', self.on_closing)
		self.dialogTk.bind('<Return>', self.confirm)

		self.passwordLabel = tk.Label(self.dialogTk,text="需要输入Root用户密码启动:", justify=tk.LEFT)
		self.passwordLabel.grid(row=0, padx=5, sticky=tk.W)
		self.password = tk.StringVar()
		self.passwordEntry = tk.Entry(self.dialogTk, textvariable=self.password, show='*')
		self.passwordEntry.grid(row=1, padx=5, sticky=tk.W+tk.E)
		self.passwordEntry.focus_set()
		self.loginButton = tk.Button(self.dialogTk, text="确认", command=self.confirm, default=tk.ACTIVE)
		self.loginButton.grid(row=3, column=0)
		self.dialogTk.mainloop()

	def on_closing(self, event = None):
		if tk.messagebox.askokcancel("Quit", "真的要退出吗?"):
			self.result = None
			self.exitType = "quit"
			self.dialogTk.destroy()
	def confirm(self, event = None):
		#print(self.password.get())
		self.result = self.password.get()
		self.exitType = "entry"
		self.dialogTk.destroy()


isValidPassword = False
while (not isValidPassword):
	d = Dialog()
	if (d.exitType == "quit"):
		exit(0)
	sudoPassword = d.result
	#print(sudoPassword)
	isValidPassword = (type(sudoPassword) is str) and (len(sudoPassword)>0)

import os
p = os.system('echo %s|sudo -S systemctl start teamviewerd.service' % (sudoPassword))
#print(p)

import time
time.sleep(2)

p = os.system('/opt/teamviewer/tv_bin/script/teamviewer')
#print(p)
