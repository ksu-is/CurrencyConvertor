# imports functions from customtkinter library and requests library to get currency exchange rates
from customtkinter import *
import requests

# uses Frankfurter api to fetch current exchange rates in order to convert base currency (from_curr) to a different currency (to_curr)
def convert_currency(amount, from_curr, to_curr):
    try:
        
        url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_curr}&to={to_curr}"
        response = requests.get(url)

# raises an error status if the api fails 
        response.raise_for_status()
        result = response.json()
        return round(result['rates'][to_curr], 2)
    except Exception as e:
        print("API failed", e)
    
# converts currency and shows result visually
def on_convert():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()
        result = convert_currency(amount, from_curr, to_curr)
        result_label.configure(text=f"{amount} {from_curr} = {result} {to_curr}")
    except ValueError:
        result_label.configure(text="Please enter a valid number.")
      
# GUI Setup using customtkinter
app = CTk()
app.geometry("800x500")
app.title("GlobeChange")
set_appearance_mode("Dark")
set_default_color_theme("green")

# Amount input text box
amount_entry = CTkEntry(app, placeholder_text="Enter amount")
amount_entry.pack(pady=5)

# Different currencies drop down selection
from_currency = CTkComboBox(app, values=["USD", "EUR", "GBP", "JPY", "KWD"])
to_currency = CTkComboBox(app, values=["USD", "EUR", "GBP", "JPY", "KWD"])
from_currency.pack(pady=5)
to_currency.pack(pady=5)
from_currency.set("USD")
to_currency.set("EUR")

# Label on GUI
label = CTkLabel(app, text="Currency Converter", font=("Arial", 24))
label.pack(pady=10)

# News Button
btn = CTkButton(master=app, text="News")
btn.place(relx=0.2, rely=0.05, anchor="ne")

# Convert Currency Button 
convert_btn = CTkButton(master=app, text="Convert", command=on_convert)
convert_btn.pack(pady=10)

result_label = CTkLabel(app, text="", font=("Arial", 18))
result_label.pack(pady=10)

app.mainloop()
