import requests, time
import tkinter as tk

username = ""
password = ""


def Logintk():
    global username
    global password
    username = usernametk.get()
    password = passtk.get()
    



window = tk.Tk()
window.title("duinocoin python wallet")
window.geometry("1600x900")
window.configure(bg="black")

tk.Label(text="welcome!\n\nUse the form below to log in!",bg="black", foreground="purple", height=5).pack()
tk.Label(text="Username:", bg="black", fg="purple")
usernametk = tk.Entry()
usernametk.pack()
tk.Label(text="password:", bg="black", fg="purple").pack()
passtk = tk.Entry()
passtk.pack()
tk.Button(text="Login", bg="grey", command=Logintk).pack()



while True:
    time.sleep(0.0)
    window.update()
    print(username, password)
    


