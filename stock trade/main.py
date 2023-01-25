import requests
import smtplib

EMAIL = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "DZG8H8CIXYNAYDKO"
NEWS_API_KEY = "38227f924cec44ba8865a58317769697"

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_date = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_date["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = "🔺" if difference > 0 else "🔻"
difference_abs = abs(difference)
diff_percent = (difference_abs / float(yesterday_closing_price)) * 100

if diff_percent > 5:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]
    first_three_articles = articles[:3]
    formatted_articles = [
        f" {STOCK_NAME}: {up_down}{round(diff_percent, 4)}% \n Headline: {article['title']}. \n Brief: {article['description']}"
        for article in
        first_three_articles]

    for article in formatted_articles:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject: STOCK ALERT!!\n\n {article}"
        )
