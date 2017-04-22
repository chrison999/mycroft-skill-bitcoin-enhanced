# mycroft-skill-bitcoin-enhanced
A skill for MycroftAI that querys various bitcoin statistics.

## DESCRIPTION:

This Mycroft skill is an enhancement of the bitcoin-skill by Red5d.
(https://github.com/Red5d/mycroft_skills/tree/master/bitcoin)

The bitcoin statistics are obtained from bitcoinaverage.com.
(https://api.bitcoinaverage.com/all)

[The original skill assumes the currency is  US dollars (USD) and
only provided the 24-hour average price.  I have expanded the
statistic to include all of the following:

- Asking Price
- Bid Price
- Last Price
- 24-hour Average Price
- Volume (in BTC)

As well, I have created a regex to distinguish between the 
currencies available at bitcoinaverage.  The current list of 
available currencies is as follows:

- Brazilian Reals (BRL)
- British Pounds (GBP)
- Canadian Dollars (CAD)
- Euros (EUR)
- Chinese Yuans (CNY)
- Czech Koruna (CZK)
- Indonesian Rupiahs (IDR)
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

###### NOTE:

For most currencies use the currency's short name (e.g. "euros" or
"shekels").  However, this does not work when the currency's name is
"dollars" because there are multiple currencies with that name.  In
those cases you must use the full name (e.g. "canadian dollars" or
"singapore dollars").  In the case of US dollars you can use either
"american dollars" or "usa dollars."  If no currency is specified
"USD" is used.

## USAGE:

Say any of the following:

- What is the bitcoin price in euros
- What is bitcoin in canadian dollars
- tell me the price of bitcoin in pounds

## TODO

Once I have the average price intent hammered out I want to create intents
for the following:

- [ ] 24-hour average price
- [ ] lowest bid price
- [ ] highest ask price
- [ ] last price
- [ ] 24-hour volume
