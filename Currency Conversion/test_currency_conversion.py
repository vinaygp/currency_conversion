# -*- coding: utf-8 -*-
"""

@author: Vinay Kumar Gunuputi
"""

import pytest
import pandas as pd
from Currency_Conversion import get_exchange_rate, get_raw_data, get_data


@pytest.mark.parametrize("source, target, expected_cols", [
    ("GBP", "", ["TIME_PERIOD", "OBS_VALUE"]),                ## Passing source. Pass
    ("PLN", "EUR", ["TIME_PERIOD", "OBS_VALUE"]),             ## Passing source and target. Pass
    ("UIOI", "FTYI", ["TIME_PERIOD", "OBS_VALUE"]),           ## Passing wrong data to test negative scenario. Failed
])

def test_get_exchange_rate(source, target, expected_cols):
    exchange_rate_df = get_exchange_rate(source, target)
    assert isinstance(exchange_rate_df, pd.DataFrame)
    assert len(exchange_rate_df) >0
    assert set(exchange_rate_df.columns) == set(expected_cols)

@pytest.mark.parametrize("identifier, expected_cols", [
    ("M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N", ["TIME_PERIOD", "OBS_VALUE"]),    ## Passing identifier. Pass
    ("YUTUU", ["TIME_PERIOD", "OBS_VALUE"]),                    ## Passing wrong data to test negative scenario. Failed
])

def test_get_raw_data(identifier, expected_cols):
    raw_data_df = get_raw_data(identifier)
    assert isinstance(raw_data_df, pd.DataFrame)
    assert len(raw_data_df) > 0
    assert set(raw_data_df.columns) == set(expected_cols)
    
    
@pytest.mark.parametrize("identifier, target_currency,expected_cols", [
    ("M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N",None, ["TIME_PERIOD", "OBS_VALUE"]),  ## Passing identifier and target_currency. Pass
    ("M.N.I8.W1.S1.S1.T.N.FA.F.F7.T.EUR._T.T.N","YTRE", ["TIME_PERIOD", "OBS_VALUE"]),  ## Passing wrong data to test negative scenario. Failed
])

def test_get_data(identifier,target_currency, expected_cols):
    data_df = get_data(identifier,target_currency)
    assert isinstance(data_df, pd.DataFrame)
    assert len(data_df) > 0
    assert set(data_df.columns) == set(expected_cols)


