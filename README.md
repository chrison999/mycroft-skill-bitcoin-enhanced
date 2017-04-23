# mycroft-skill-bitcoin-enhanced
A skill for MycroftAI that querys various bitcoin statistics.

## DESCRIPTION:

This Mycroft skill is an enhancement of the bitcoin-skill by Red5d.
(https://github.com/Red5d/mycroft_skills/tree/master/bitcoin)

The bitcoin statistics are obtained from bitcoinaverage.com.
(https://api.bitcoinaverage.com/all)

The original skill assumes the currency is  US dollars (USD) and
only provided the 24-hour average price.  I have expanded the
statistics to include all of the following:

- Asking Price
- Bid Price
- Last Price
- 24-hour Average Price
- Volume (in BTC)

As well, I have created a regex that distinguishes between the 
currencies available at bitcoinaverage.  The current list of 
available currencies is as follows:

| Currency | Say this to Mycroft |
| -------- | ------------------- |
| Brazilian Reals (BRL) | "Reals" |
| British Pounds (GBP) | "Pounds" |
| Canadian Dollars (CAD) | "Canadian Dollars" |
| Euros (EUR) | "Euros" |
| Chinese Yuans (CNY) | "Yuans" |
| Czech Koruna (CZK) | "Koruna" |
| Indonesian Rupiahs (IDR) | "Rupiahs" |
| Israeli Shekels (ILS) | "Shekels" |
| Indian Rupees (INR) | "Rupees" |
| Japanese Yens (JPY) | "Yens" |
| South Korean Won (KRW) | "Won" |
| Mexican Pesos (MXN) | "Pesos" |
| Malaysian Ringgit (MYR) | "Ringgit" |
| Nigerian Nairas (NGN) | "Mairas" |
| Polish Zlotys:  (PLN)| "Zlotys" |
| Russian Roubles (RUB) | "Roubles" |
| Swedish Kronas (SEK) | "Kronas" |
| Singapore Dollars (SGD) | "Singapore Dollars" |
| Turkish Lira (TRY) | "Lira" |
| US Dollars (USD) | "USA Dollars"
 "American Dollars" |
| South African Rands (ZAR) | "Rands" |

###### NOTE:

For most currencies use the currency's short name (e.g. "Euros" or
"Shekels").  However, this does not work when the currency's name is
"dollars" because there are multiple currencies with that name.  In
those cases you *must* use the full name (e.g. "Canadian Dollars" or
"Singapore Dollars").  In the case of US dollars you can use either
"American Dollars" or "USA Dollars."  If no currency is specified
"USD" is used.

## USAGE:

###### Asking Price

Say any phrase that contains one of the following keywords:

| Keyword(s) | Example |
| ---------- | ------- |
| high bitcoin price | "Mycroft, what is the high bitcoin price in Pesos?" |
| highest bitcoin price | "Mycroft, tell me the hightst bitcoin price."
| asking bitcoin price | "Mycroft, give me the asking bitcoin price in Canadian Dollars." |
| bitcoin ask price | "Mycroft, what is the bitcoin ask price?" |
| bitcoin asking price | "Mycroft, I want to know the bitcoin asking price." |

###### Bid Price

Say any phrase that contains one of the following keywords:

| Keyword(s) | Example |
| ---------- | ------- |
| low bitcoin price | "Mycroft, tell me the low bitcoin price." |
| lowest bitcoin price | Mycroft, what is the lowest bitcoin price in Pounds?" |
| bitcoin bid price | "Mycroft, give me the current bitcoin bid price."

###### Last Price

Say any phrase that contains one of the following keywords:

| Keyword(s) | Example |
| ---------- | ------- |
| bitcoin price | "Mycroft, what is the bitcoin price in Lira?" |
| last bitcoin price | "Mycroft, tell me the last bitcoin price." |
| bitcoin last price | "Mycroft, what is the bitcoin last price?" |
| current bitcoin price | "Mycroft, give me the bitcoin price." |

###### 24-hour Average Price

Say any phrase that contains one of the following keywords:

| Keyword(s) | Example |
| ---------- | ------- |
| average bitcoin price | "Mycroft, what is the average bitcoin price in Zlotys?" |
| bitcoin average price | "Mycroft, tell me the bitcoin average price." |

*(Example:  "Tell me the average bitcoin price in Yuan.)*

###### 24-hour Volume

Say any phrase that contains one of the following keywords:

| Keyword(s) | Example |
| ---------- | ------- |
| bitcoin volume | "Mycroft, what is the bitcoin volume in Won?" |
| volume of bitcoin | "Mycroft, tell me the volume of bitcoin." |

## TODO:

1.  This is the initial version of this skill and I have only done
preliminary debugging of the code.  I would welcome people testing the skill
and letting me know of any problems/bugs at chrison999 (at) yahoo.ca. 
Please put "Mycroft Bitcoin Skill" in the subject of your message.

2.  Bitcoinaverage.com has a lot more statistics available such has
statistics for exchanges selling bitcoin in each currency.  Possible future
enhancements could include:
    - Reporting which exchanges sell bitcoin in each currency *(e.g. "What are
the bitcoin exchanges for Euros?")*
    - Reporting statistic for an exchange *(e.g. "What is the last price for
bitcoin in Euros for Bitonic?")*
