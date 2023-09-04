# PosBoss_Xero_data_proccessing
Python Scripts for combining Posboss and Xero reporting for buisness analysis

add_date_season_temp_hours.py 
Usage: python3 add_date_season_temp.py <cash_ups_csv>  <output_file>
- used to add a consistent date to a xero "cash up" summary for further analysis
- Defines a day as a cafe only or, cafe and bar day based on cash up time
- adds a season identifer and automatically identifes the average daily temperature based on OpenWeather API accessability

add_outgoing_loop.py
