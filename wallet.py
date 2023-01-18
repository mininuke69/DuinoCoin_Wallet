import requests, time
import tkinter as tk

username = ""
password = ""
userdata = ""

bgcol = "black"
txtcol = "green"
errorcol = "red"

def GetUserData():
    global userdata
    userdata = requests.get("https://server.duinocoin.com/users/" + username).json()

def LogOn():
    usernameLabel.pack_forget()
    usernameEntry.pack_forget()
    passwordLabel.pack_forget()
    passwordEntry.pack_forget()
    loginbutton.pack_forget()

    balTk = tk.Label(text=userdata["balance"]["balance"], )




def Logintk():
    global username
    global password

    response = requests.get("https://server.duinocoin.com/auth/" + usernameEntry.get() + "?password=" + str(passwordEntry.get())).json()
    loginmessagetk.config(fg=txtcol, text="logging in...")
    time.sleep(0.5)
    loginmessagetk.config(text="")
    success = response["success"]
    
    if success == True:
        username = usernameEntry.get()
        password = passwordEntry.get()
        loginmessagetk.config(text=f"Logged in, server: {response['server']}!", fg=txtcol)
        LogOn()
        
    else:
        error = "login error: " + response["message"]
        loginmessagetk.config(text=error, fg=errorcol)




window = tk.Tk()
window.title("duinocoin python wallet")
window.geometry("1600x900")
window.configure(bg=bgcol)

tk.Label(text="welcome!\n\nUse the form below to log in!",bg=bgcol, foreground=txtcol, height=5).pack()
usernameLabel = tk.Label(text="Username:", bg=bgcol, fg=txtcol);usernameLabel.pack()
usernameEntry = tk.Entry();usernameEntry.pack()
passwordLabel = tk.Label(text="password:", bg=bgcol, fg=txtcol);passwordLabel.pack()
passwordEntry = tk.Entry();passwordEntry.pack()
loginmessagetk = tk.Label(text="", bg=bgcol, fg="red");loginmessagetk.pack()
loginbutton = tk.Button(text="Login", bg="blue", command=Logintk);loginbutton.pack()



while True:
    time.sleep(0.0)
    window.update()