# mycroft-skill-bitcoin-enhanced
A skill for MycroftAI that querys various bitcoin statistics.

DESCRIPTION:

This Mycroft skill is an enhancement of the bitcoin-skill by Red5d.
(https://github.com/Red5d/mycroft_skills/tree/master/bitcoin)

The bitcoin statistics are obtained from bitcoinaverage.com.
(https://api.bitcoinaverage.com/all)

The original skill assumes the currency is  US dollars (USD).
What I have done is create a regex to distinguish between the 
currencies available at bitcoinaverage.  The current list of 
available currencies is as follows:

- Brazilian Reals (BRL)
- British Pounds (GBP)
- Canadian Dollars (CAD)
- Euros (EUR)
- Yuans (CNY)
- Czech Koruna (CZK)
- IndonesianRupiahs (IDR)
- Israeli shekels (ILS)
- Indian Rupees (INR)
- Japanese Yens (JPY)
- South Korean Won (KRW)
- Mexican Pesos (MXN)
- Malaysian Ringgit (MYR)
- Nigerian Nairas (NGN)
- Polish Zlotys:  (PLN)
- Russian Roubles (RUB)
- Swedish Kronas (SEK)
- Singapore Dollars (SGD)
- Turkish Lira (TRY)
- US Dollars (USD)
- South African Rands (ZAR)

NOTE:

For most currencies you can use the currency's name (e.g. "euros" or
"shekels").  This does not work when the currency's name is "dollars"
because there are multiple currencies with that name.  In those cases
you must use the full name (e.g. "canadian dollars" or "singapore
dollars").  In the case of US dollars you can use either "american
dollars" or "usa dollars."

USAGE:

Say any of the following:

- What is the bitcoin price in euros
- What is bitcoin in canadian dollars
- tell me the price of bitcoin in pounds

TODO

Once I have the average price intent hammered out I want to create intents
for the following:

- lowest bid price
- highest ask price
- last price
- 24 hour volume
