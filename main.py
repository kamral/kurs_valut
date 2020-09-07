import requests
from bs4 import BeautifulSoup
import time
import smtplib

class Currency:

    dollar_rub='https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=ljkkfh+r+&aqs=chrome.1.69i57j0l7.3270j0j7&sourceid=chrome&ie=UTF-8'
    headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'}

    current_converted_price=0

    difference=0.1

    def __init__(self):
        self.current_converted_price=\
            float(self.get_currency_price().replace(',','.'))

    def get_currency_price(self):
        full_page = requests.get(self.dollar_rub, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {'class': 'DFlfde SwHCTb',
                                        "data-precision": "2"})
        return convert[0].text

    def check_currency(self):
        currency=float(self.get_currency_price().replace(',','.'))
        if currency>=self.current_converted_price+self.difference:
            print('Курс сильно вырос, может пора что то делать?')
            self.send_mail()
        elif currency<=self.current_converted_price-self.difference:
            print('Курс сильно упал, может пора что то делать?')
            self.send_mail()
        print('Сейчас курс:1 доллар='+ str(currency))
        time.sleep(3)
        self.check_currency()

def send_mail(self):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo
    server.starttls()
    server.ehlo()
    server.login('kamra010101@gmail.com','q l v m f h c b')
    subject='Курс рубля'
    body='Курс доллара изменился!'
    message=f'Subject:{subject}\n\n{body}'
    server.sendmail(
        'kamilmagaramov1991@gmail.com',
        'kamral010101@gmail.com',
        message
    )
    server.quit()


currency=Currency()
currency.check_currency()


