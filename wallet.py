import requests, time
import tkinter as tk

window = tk.Tk()
window.title("duinocoin python wallet")
window.geometry("1600x900")
window.configure(bg="black")

tk.Label(text="welcome!\n\nUse the form below to log in!",bg="black", foreground="purple", height=5).pack()
tk.Label(text="Username:", bg="black", fg="purple")
usernametk = tk.Entry(bg="grey")
usernametk.pack()



while True:
    time.sleep(0.0)
    print(usernametk.get())
    window.update()
    


