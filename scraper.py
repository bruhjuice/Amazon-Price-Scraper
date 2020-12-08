# In 2020, Amazon updated their site and the Requests combined with BeautifulSoup libraries no longer work for scraping site data
# However, the Requests-HTML library was one of the methods that I found to work as of December 2020. 

from requests_html import HTMLSession
import smtplib
from datetime import datetime
import time
# URL of watched product. Example URL is Cyberpunk 2077 video game
URL = "https://www.amazon.com/Cyberpunk-2077-PlayStation-4/dp/B07DJWBYKP/ref=zg_bsnr_videogames_home_1?_encoding=UTF8&psc=1&refRID=T2BS1538E3QG5NWFKWXR"

# Function that prints the current time to the minute using datetime library
def print_time():
    now = datetime.now()
    print (str(now.hour) + ":" + str(now.minute))

# Function that scrapes the title of product and current price using requests-HTML library
def check_price(URL):
    session = HTMLSession()
    r = session.get(URL)
    r.html.render(sleep = 1)
    title = r.html.xpath('//*[@id="productTitle"]', first = True).text
    price = r.html.xpath('//*[@id="priceblock_ourprice"]', first = True).text
    price = float(price[1:7])
    print ("Watching: " + title.strip() + ". Current price: " + str(price))
    return price

# Function that sends an email usinng smtplib library. Email contains a link to the watched item
def send_mail(URL):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
# Provide login info for email that is sending. (Email + password)
    server.login("ExampleSender@gmail.com", "ExamplePasscode123")
    subject = "Price Decrease!"
    body = "Your watched item has been discounted! Link to item: " + URL 
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        "ExampleRecipient1@gmail.com",
        "Recipient2@gmail.com",
        msg
    )
    server.quit()
    print ("Email has been sent! Check inbox.")

# Initialize current_price and original_price
current_price = check_price(URL)
original_price = current_price
# While current_price is greater than or equal to original_price, continue to check every 10 minutes if the product has been discounted
# At the beginning of each check, print out the time (Confirmation for user that code is still running and checking)
while (current_price >= original_price):
    print("Still running... current time is ", end="")  
    print_time()
    time.sleep(600)
    current_price = check_price(URL)
# If the current_price ever goes below the original price, alert the user by calling send_mail()
send_mail(URL)
