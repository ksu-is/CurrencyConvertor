# imports functions from customtkinter library and requests library to get currency exchange rates
from customtkinter import *
import requests
import webbrowser

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

# opens a new tab that displays the hyperlinks to news artciles as the titles and opens them when clicked
def show_news_articles():
    news_articles = CTkToplevel(app)
    news_articles.geometry("600x400")
    news_articles.title("Currency News")

    news_data = {
        "USD": ("Dollar resumes fall as investors wait on trade talks", "https://www.reuters.com/markets/currencies/dollar-sellers-take-breather-sterling-stands-tall-2025-04-16/"),
        "EUR": ("Attentive ECB can lean against Euro rise", "https://www.reuters.com/markets/currencies/attentive-ecb-can-lean-against-euro-rise-mike-dolan-2025-04-14/"),
        "GBP": ("GBP/USD stages six-day rally for first time in 2025", "https://www.forex.com/en-us/news-and-analysis/gbpusd-stages-six-day-rally-for-first-time-in-2025/"),
        "JPY": ("Yen hits strongest point since September as tariff talks begin", "https://asia.nikkei.com/Business/Markets/Currencies/Yen-hits-strongest-point-since-September-as-tariff-talks-begin"),
        "KWD": ("Kuwait plots payment system and digital Dinar", "https://www.fintechfutures.com/paytech/kuwait-plots-payment-system-and-digital-dinar")
    }

    CTkLabel(news_articles, text="Currency News Articles:", font=("Arial", 14, "bold")).pack(pady=(10, 5))

    for currency, (headline, link) in news_data.items():
        label = CTkLabel(
            news_articles,
            text=f"{currency}: {headline}",
            text_color="blue",
            cursor="hand2",
            font=("Arial", 12)
        )
        label.pack(anchor="w", padx=20, pady=3)

        label.bind("<Button-1>", lambda e, url=link: webbrowser.open(url))

      
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
