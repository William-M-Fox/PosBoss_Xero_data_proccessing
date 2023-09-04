# PosBoss_Xero_data_proccessing
Python Scripts for combining Posboss and Xero reporting for buisness analysis

add_date_season_temp_hours.py 
Usage: python3 add_date_season_temp.py <cash_ups_csv>  <output_file>
- used to add a consistent date to a xero "cash up" summary for further analysis
- Defines a day as a cafe only or, cafe and bar day based on cash up time
- adds a season identifer and automatically identifes the average daily temperature based on OpenWeather API accessability
- api key has to be added

remove_commas.py
Usage: python3 remove_commas.py <input_csv> <output_csv>
- Removes comma from numerical values for proper proccessing
  
add_outgoing_loop.py
Usage: python process_outgoings.py <input_csv>
- Run in a directory containing xero transation reports csv files
- input csv is the turnover summaries obtained from PosBoss
- Adds xero reports to turnover summaries for further analysis

fix_date.py
- used to standardise date format from input_format = "%d/%m/%y" to '%Y-%m-%d'

moving_average.py
Usage: python3 moving_average.py <input_csv> <output_csv> <window_size>
- requires a "Turnover" Column, which is orginally available ferom PosBoss reporting
