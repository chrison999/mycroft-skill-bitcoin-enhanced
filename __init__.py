from os.path import dirname, join

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
import requests

__author__ = 'Red5d', 'chrison999'

class BitcoinSkill(MycroftSkill):
    def __init__(self):
        super(BitcoinSkill, self).__init__(name="BitcoinSkill")

    def initialize(self):
        intent = IntentBuilder("BitcoinIntent").require("BitcoinKeyword") \
            .optionally("Currency").build()
        self.register_intent(intent, self.handle_intent)

    def handle_intent(self, message):

        currency = message.data.get("Currency")  # optional parameter

        if currency:
            choices = {
                       'reals': 'BRL',
                       'canadian dollars': 'CAD',
                       'euros': 'EUR',
                       'yuans': 'CNY',
                       'koruna': 'CZK',
                       'rupiahs': 'IDR',
                       'shekels': 'ILS',
                       'rupees': 'INR',
                       'yens': 'JPY',
                       'won': 'KRW',
                       'pesos': 'MXN',
                       'ringgit': 'MYR',
                       'nairas': 'NGN',
                       'zlotys':  'PLN',
                       'roubles': 'RUB',
                       'kronas': 'SEK',
                       'singapore dollars': 'SGD',
                       'lira': 'TRY',
                       'u s a dollars': 'USD',
                       'american dollars': 'USD',
                       'rands': 'ZAR',
                       'pounds': "GBP"}
            result = choices.get(str(currency), 'USD')
            price = requests.get("https://api.bitcoinaverage.com/all").json()[str(result)]['averages']['24h_avg']
            self.speak("The current average "+str(currency)+" bitcoin price is "+str(price)+".")
        else:
            price = requests.get("https://api.bitcoinaverage.com/all").json()['USD']['averages']['24h_avg']
            self.speak("The current average U S dollar bitcoin price is "+str(price)+".")

    def stop(self):
        pass


def create_skill():
    return BitcoinSkill()
