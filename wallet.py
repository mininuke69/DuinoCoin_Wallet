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
    time.sleep(0.2)
    userdata = requests.get("https://server.duinocoin.com/users/" + username).json()

def LogOn():
    GetUserData()

    usernameLabel.pack_forget()
    usernameEntry.pack_forget()
    passwordLabel.pack_forget()
    passwordEntry.pack_forget()
    loginbutton.pack_forget()
    welcomeLabel.pack_forget()

    balTk = tk.Label(text="Balance: " + str(userdata["result"]["balance"]["balance"]) + "ᕲ", bg=bgcol, fg=txtcol);balTk.pack(anchor="nw", padx=10)
    txLabel = tk.Label(text="Last transactions:", bg=bgcol, fg=txtcol);txLabel.pack(anchor="nw",padx=10, pady=5)
    
    txList = ""
    for i in range(5):
        thistx = userdata["result"]["transactions"][i]
        if thistx["recipient"] == username:
            txList = txList + "received " + str(thistx["amount"]) + " ᕲ from " + thistx["sender"] + " on " + thistx["datetime"] + " with memo: '" + thistx["memo"] + "' id: " + str(thistx["id"]) + " hash: " + thistx["hash"] + "\n\n"
        else:
            txList = txList + "sent " + str(thistx["amount"]) + " ᕲ to " + thistx["sender"] + " on " + thistx["datetime"] + " with memo: '" + thistx["memo"] + "' id: " + str(thistx["id"]) + " hash: " + thistx["hash"] + "\n\n"
    txListLabel = tk.Label(text=txList, justify=tk.LEFT, bg=bgcol, fg=txtcol);txListLabel.pack(anchor="nw", padx=10)




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

welcomeLabel = tk.Label(text="welcome!\n\nUse the form below to log in!",bg=bgcol, foreground=txtcol);welcomeLabel.pack()
usernameLabel = tk.Label(text="Username:", bg=bgcol, fg=txtcol);usernameLabel.pack()
usernameEntry = tk.Entry();usernameEntry.pack()
passwordLabel = tk.Label(text="password:", bg=bgcol, fg=txtcol);passwordLabel.pack()
passwordEntry = tk.Entry();passwordEntry.pack()
loginmessagetk = tk.Label(text="", bg=bgcol, fg="red");loginmessagetk.pack()
loginbutton = tk.Button(text="Login", bg="blue", command=Logintk);loginbutton.pack()



while True:
    window.update()
    time.sleep(0.0)