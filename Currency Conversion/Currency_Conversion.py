# -*- coding: utf-8 -*-
"""

@author: Vinay Kumar Gunuputi
"""

import xml.etree.ElementTree as ET
import pandas as pd
import requests
from io import StringIO



def fetch_data_from_url(url: str) -> pd.DataFrame:
    """
    Parameters:
    url (str) : It is used in requests to get the xml data
    
    Returns:
    pd.DataFrame : It should give thedataframe based on given Url
  
    """
    try:
        data_df = pd.DataFrame([], columns=['TIME_PERIOD', 'OBS_VALUE'])
        response = requests.get(url=url)
        
        if response.status_code == 200:
            xml_string = response.content
            root = ET.fromstring(xml_string)
            nsmap = dict([node for _, node in ET.iterparse(StringIO(str(xml_string, 'utf-8')),
                                                           events=['start-ns'])])
            elements = root.findall('message:DataSet/generic:Series/generic:Obs', namespaces=nsmap)
            for obs in elements:
                dimension_value = obs.find('generic:ObsDimension', namespaces=nsmap).get('value')
                obs_value = obs.find('generic:ObsValue', namespaces=nsmap).get('value')
                data_df.loc[len(data_df)] = [dimension_value, float(obs_value)]
        else:
            print("Error occurred: {} ".format(response.content))
        
    except Exception as e:
        error_message = "Exception occurred while fetching data: " + str(e)
        print(error_message)
    
    return data_df

def get_exchange_rate(source: str, target: str = "EUR") -> pd.DataFrame:
    """
    Parameters:
    source (str) : It is used in Exchange rate URL
    target (str) Optional : It is used in Exchange rate URL. ( default is "EUR")
  
    Returns:
    pd.DataFrame : It should give the exchange rate dataframe based on given
                   source and target values.
  
    """
    
    try:
        
        exchange_rate_url = "https://sdw-wsrest.ecb.europa.eu/service/data/EXR/M.{}.{}.SP00.A?detail=dataonly".format(source, target)
        exchange_rate_df = fetch_data_from_url(exchange_rate_url)
        
    except Exception as e:
        error_message = "Exception occured in get_exchange_rate function : "+str(e)
        print(error_message)
    
    return exchange_rate_df


def get_raw_data(identifier: str) -> pd.DataFrame:
    """
    Parameters:
    identifier (str) : It is used in raw_data URL

    Returns:
    pd.DataFrame : It should give the raw data dataframe based on given identifier value.
  
    """
    
    try:
        
        raw_data_url = "https://sdw-wsrest.ecb.europa.eu/service/data/BP6/{}?detail=dataonly".format(identifier)
        raw_data_df = fetch_data_from_url(raw_data_url)
        
    except Exception as e:
        error_message = "Exception occured in get_raw_data function : "+str(e)
        print(error_message)
    
    return raw_data_df




def get_data(identifier: str, target_currency: str = None) -> pd.DataFrame:
    try:
        """
        Parameters:
        identifier (str) : It is used in raw_data URL when get_raw_data function is called.
        target_currency (str) Optional : It is used in Exchange rate URL. ( default is None)

        Returns:
        pd.DataFrame : It should give the dataframe based on given identifier and target_currency value.
      
        """
        
        if target_currency is None:
            get_data_df = get_raw_data(identifier)
        else:
            source = identifier.split('.')[12]
            get_data_df = get_exchange_rate(source,target=target_currency)
    except Exception as e:
        error_message = "Exception occured in get_data function : "+str(e)
        print(error_message)
    
    return get_data_df
    









