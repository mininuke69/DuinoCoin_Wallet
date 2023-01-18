import requests, time
import tkinter as tk

username = ""
password = ""
userdata = ""

def GetUserData():
    global userdata
    userdata = requests.get("https://server.duinocoin.com/users/" + username).json()

def HideLoginForm():
    usernameLabel.pack_forget()
    usernameEntry.pack_forget()
    passwordLabel.pack_forget()
    passwordEntry.pack_forget()
    loginbutton.pack_forget()

def Logintk():
    global username
    global password

    response = requests.get("https://server.duinocoin.com/auth/" + usernameEntry.get() + "?password=" + str(passwordEntry.get())).json()
    loginmessagetk.config(fg="white", text="logging in...")
    time.sleep(0.5)
    loginmessagetk.config(text="")
    success = response["success"]
    
    if success == True:
        username = usernameEntry.get()
        password = passwordEntry.get()
        loginmessagetk.config(text=f"Logged in, server: {response['server']}!", fg="white")
        HideLoginForm()
        
    else:
        error = "login error: " + response["message"]
        loginmessagetk.config(text=error, fg="red")




window = tk.Tk()
window.title("duinocoin python wallet")
window.geometry("1600x900")
window.configure(bg="black")

tk.Label(text="welcome!\n\nUse the form below to log in!",bg="black", foreground="purple", height=5).pack()
usernameLabel = tk.Label(text="Username:", bg="black", fg="purple");usernameLabel.pack()
usernameEntry = tk.Entry();usernameEntry.pack()
passwordLabel = tk.Label(text="password:", bg="black", fg="purple");passwordLabel.pack()
passwordEntry = tk.Entry();passwordEntry.pack()
loginmessagetk = tk.Label(text="", bg="black", fg="red");loginmessagetk.pack()
loginbutton = tk.Button(text="Login", bg="blue", command=Logintk);loginbutton.pack()



while True:
    time.sleep(0.0)
    window.update()    