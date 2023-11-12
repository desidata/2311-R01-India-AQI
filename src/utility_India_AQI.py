import pandas as pd
import numpy as np
from typing import List
import datetime


def get_state_aggregate(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function takes a pd DataFrame containing air quality data for various cities in India and aggregates the data by state, year, month, day, and hour.
    
    Args:
    - df: pd DataFrame containing air quality data
    
    Returns:
    - pd DataFrame containing aggregated air quality data by state, year, month, day, and hour
    """

    df['State'] = df['State'].ffill()
    df['City']  = df['City'].ffill()
    df = df.rename(columns={'Current AQI value': 'AQI'})
    
    # create a new dataframe to hold the aggregated data
    agg_df = pd.DataFrame(columns=['State', 'Date','Year', 'Month', 'Day', 'Hour', 'AQI_median', 'AQI_mean', 'AQI_max', 'AQI_min'])
    
    # drop records with non-numeric or missing data in the 'AQI' column
    df = df[pd.to_numeric(df['AQI'], errors='coerce').notnull()]

    # group the data by state, year, month, day, and hour and calculate the median, mean, max, and min AQI values
    grouped = df.groupby(['State', 'Year', 'Month', 'Day', 'Hour'])['AQI'].agg(['median', 'mean', 'max', 'min'])
    
    # populate the new dataframe with the aggregated data
    agg_df['State']      = [i[0] for i in grouped.index]
    agg_df['Year']       = [i[1] for i in grouped.index]
    agg_df['Month']      = [i[2] for i in grouped.index]
    agg_df['Day']        = [i[3] for i in grouped.index]
    agg_df['Hour']       = [i[4] for i in grouped.index]
    agg_df['AQI_median'] = grouped['median'].values
    agg_df['AQI_mean']   = grouped['mean'].values
    agg_df['AQI_max']    = grouped['max'].values
    agg_df['AQI_min']    = grouped['min'].values

    agg_df['Date']       = pd.to_datetime(agg_df[['Year', 'Month', 'Day', 'Hour']])
    agg_df['AQI_median'] = agg_df['AQI_median'].astype(np.int64)
    agg_df['AQI_mean']   = agg_df['AQI_mean'].astype(np.int64)
    agg_df['AQI_max']    = agg_df['AQI_max'].astype(np.int64)
    agg_df['AQI_min']    = agg_df['AQI_min'].astype(np.int64)

    return agg_df

def get_city_aggregate(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function takes a pd DataFrame containing air quality data for various cities in India and aggregates the data by state, year, month, day, and hour.
    
    Args:
    - df: pd DataFrame containing air quality data
    
    Returns:
    - pd DataFrame containing aggregated air quality data by state, year, month, day, and hour
    """

    df['State'] = df['State'].ffill()
    df['City']  = df['City'].ffill()
    df = df.rename(columns={'Current AQI value': 'AQI'})
    
    # create a new dataframe to hold the aggregated data
    agg_df = pd.DataFrame(columns=['City', 'Date','Year', 'Month', 'Day', 'Hour', 'AQI_median', 'AQI_mean', 'AQI_max', 'AQI_min'])
    
    # drop records with non-numeric or missing data in the 'AQI' column
    df = df[pd.to_numeric(df['AQI'], errors='coerce').notnull()]

    # group the data by state, year, month, day, and hour and calculate the median, mean, max, and min AQI values
    grouped = df.groupby(['City', 'Year', 'Month', 'Day', 'Hour'])['AQI'].agg(['median', 'mean', 'max', 'min'])
    
    # populate the new dataframe with the aggregated data
    agg_df['City']      = [i[0] for i in grouped.index]
    agg_df['Year']       = [i[1] for i in grouped.index]
    agg_df['Month']      = [i[2] for i in grouped.index]
    agg_df['Day']        = [i[3] for i in grouped.index]
    agg_df['Hour']       = [i[4] for i in grouped.index]
    agg_df['AQI_median'] = grouped['median'].values
    agg_df['AQI_mean']   = grouped['mean'].values
    agg_df['AQI_max']    = grouped['max'].values
    agg_df['AQI_min']    = grouped['min'].values

    agg_df['Date']       = pd.to_datetime(agg_df[['Year', 'Month', 'Day', 'Hour']])
    agg_df['AQI_median'] = agg_df['AQI_median'].astype(np.int64)
    agg_df['AQI_mean']   = agg_df['AQI_mean'].astype(np.int64)
    agg_df['AQI_max']    = agg_df['AQI_max'].astype(np.int64)
    agg_df['AQI_min']    = agg_df['AQI_min'].astype(np.int64)

    return agg_df


def concat_and_sort(df_list: List[pd.DataFrame]) -> pd.DataFrame:
    
    """
    Concatenates a list of dataframes of same column structure and sorts the concatenated dataframe by state, year, month, day.
    It also calls the get_state_aggregate function on each of the dataframes in the input list.
    
    Args:
    df_list (List[pd.DataFrame]): The list of dataframes to be concatenated and sorted.
    
    Returns:
    pd.DataFrame: The concatenated and sorted dataframe.
    
    Raises:
    ValueError: If the dataframes in the list have different column structures.
    """
    # check if the column structures are the same
    for i in range(len(df_list)-1):
        if not df_list[i].columns.equals(df_list[i+1].columns):
            raise ValueError("DataFrames have different column structures.")
    
    # call the get_state_aggregate function on each dataframe in the list
    agg_df_list = []
    if 'States' in df_list[0].columns:
        for df in df_list:
            agg_df = get_state_aggregate(df)
            agg_df_list.append(agg_df)
    elif 'City' in df_list[0].columns:
        for df in df_list:
            agg_df = get_city_aggregate(df)
            agg_df_list.append(agg_df)    
    # concatenate the dataframes
    concat_df = pd.concat(agg_df_list)
    
    # sort the concatenated dataframe by state, year, month, day
    sorted_df = concat_df.sort_values(by=['Date'], ascending=True)
    
    return sorted_df

def out_filename_india_aqi_state(extension='.mp4'):
    if extension not in ['.mp4', '.gif', '.mkv']:
        raise ValueError("Invalid extension. Must be one of '.mp4', '.gif', or '.mkv'.")
    return 'india_aqi_states' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + extension

def out_filename_india_aqi_city(extension='.mp4'):
    if extension not in ['.mp4', '.gif', '.mkv']:
        raise ValueError("Invalid extension. Must be one of '.mp4', '.gif', or '.mkv'.")
    return 'india_aqi_cities' + datetime.datetime.now().strftime('%Y%m%d_%H%M%S') + extension