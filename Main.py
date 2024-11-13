from UI import App
from tkinter import messagebox
try:
	root=App.App()
	root.mainloop()
except Exception as e:
	messagebox.showerror(title='ERROR', message=e)