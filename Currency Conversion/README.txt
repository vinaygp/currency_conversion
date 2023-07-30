
# Currency Conversion Python Script

## Description
This Python script provides three functions for Currency conversion: "get_exchange_rate", "get_raw_data", and "get_data".

 It allows you to perform Currency Conversion easily.


Installion:
1. Make sure you have Python 3.7+ installed.
2. Make sure you have Installed Pandas, requests, xml, pytest packages.


## Usage
Import the "Currency_Conversion.py", "test_currency_conversion.py" module into your Python script or interactive session to use the functions.


### 1. get_exchange_rate

from Currency_Conversion import get_exchange_rate

# Scenario 1:  call get_exchange_rate function with Source cuurency only
exchange_rate_df = get_exchange_rate("GBP")
print(exchange_rate_df.head())  # Output: It will give the first five rows from that dataframe.

# Scenario 2:  call get_exchange_rate function with Source and target currencies. 
exchange_rate_df = get_exchange_rate("GBP",target="PLN")
print(exchange_rate_df.head())  # Output: It will give the first five rows from that dataframe.



### 2. get_raw_data

from Currency_Conversion import get_raw_data
raw_data_df = get_raw_data("M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N")
print(raw_data_df.head())  # Output: It will give the first five rows from that dataframe.


### 3. get_data

from Currency_Conversion import get_data
# Scenario 1:  call get_data function with Identifier only
data_df = get_data("M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.GBP._T.T.N")
print(data_df.head())  # Output: It will give the first five rows from that dataframe.

# Scenario 2: call get_data function with  Identifier and target_currency
data_df = get_data("M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.GBP._T.T.N",target_currency="EUR")
print(data_df.head())  # Output: It will give the first five rows from that dataframe.


You can run the test cases by executing pytest in the terminal from the directory where the test file is located.

It has test cases for above functions.


Function details:
Function 1:
get_exchange_rate --> This function takes source currency and target currency from the user.
If the target currency is not given then it will take default one.
It will get the xml data from the requests module by giving source and target currencies in the exchange rate url.
Then It will convert that data into required Dataframe.

Function 2:
get_raw_data --> This function takes identifier from the user and returns the raw_data dataframe.
It will get the xml data from the requests module by giving identifier in the raw_data url.
Then It will convert that data into required Dataframe.

Function 3:
get_data --> This function takes identifier and target currency from the user and dataframe.
if the target is None, then it will call the get_raw_data function2 by passing identifier 
and get the raw_data dataframe.
if the target is not None, then it will get the source currency from identifier and call the get_exchange_rate
function1 and get the exchange rate data frame.









