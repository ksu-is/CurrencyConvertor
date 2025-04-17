from customtkinter import *

app = CTk()
app.geometry("800x500")
app.title("GlobeChange")

btn = CTkButton(master=app, text="News")
btn.place(relx=0.2, rely=0.05, anchor="ne")

textbox = customtkinter = CTkTextbox(app)
textbox.insert(0.0, "Enter Currency Amount")

btn = CTkButton(master=app, text="Convert")
btn.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()