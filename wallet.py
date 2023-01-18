import requests, time
import tkinter as tk

username = ""
password = ""


def Logintk():
    global username
    global password


    response = requests.get("https://server.duinocoin.com/auth/" + usernametk.get() + "?password=" + str(passtk.get())).json()
    loginmessagetk.config(fg="white", text="logging in...")
    time.sleep(0.5)
    loginmessagetk.config(text="")
    print(response)
    success = response["success"]
    
    if success == True:
        username = usernametk.get()
        password = passtk.get()
        loginmessagetk.config(text=f"Logged in, server: {response['server']}!", fg="white")
    else:
        error = "login error: " + response["message"]
        loginmessagetk.config(text=error, fg="red")

    
    


window = tk.Tk()
window.title("duinocoin python wallet")
window.geometry("1600x900")
window.configure(bg="black")

tk.Label(text="welcome!\n\nUse the form below to log in!",bg="black", foreground="purple", height=5).pack()
tk.Label(text="Username:", bg="black", fg="purple")
usernametk = tk.Entry();usernametk.pack()
tk.Label(text="password:", bg="black", fg="purple").pack()
passtk = tk.Entry();passtk.pack()
loginmessagetk = tk.Label(text="", bg="black", fg="red");loginmessagetk.pack()
tk.Button(text="Login", bg="blue", command=Logintk).pack()



while True:
    time.sleep(0.2)
    window.update()
    print(username, password)
    


