import streamlit as st
import requests

# call parameters
country = st.text_input('Country')
cdd_18 = st.number_input('Cooling Degree Days above 18', format='%.4f')
cdd_21 = st.number_input('Cooling Degree Days above 21', format='%.4f')
irradiance = st.number_input('Global Horizontal Irrandiance', format='%.4f')
hdd_16 = st.number_input('Heating Degree Days below 16', format='%.4f')
hdd_18 = st.number_input('Heating Degree Days below 18', format='%.4f')
heat_index = st.number_input('Heat Index', format='%.4f')
humidity = st.number_input('Relative humidity', format='%.4f')
temp = st.number_input('Avergage temperature', format='%.4f')
precipitation = st.number_input('Total precipitaiton', format='%.4f')


url_ = 'placeholder' # TODO

params_ = {
    "Country": country,
    "value_CDD_18": cdd_18,
    "value_CDD_21": cdd_21,
    "value_Global_Horizontal_Irrandiance": irradiance,
    "value_HDD_16": hdd_16,
    "value_HDD_18": hdd_18,
    "value_Heat_index": heat_index,
    "value_Relative_Humidty": humidity,
    "value_Temperature": temp,
    "value_Total_Precipitation": precipitation
    }

if st.button('Get Renewable Energy prediction'):
    res = requests.get(url=url_,
                       params=params_)

    if res.status_code != 200:
        st.error('Error in API connection')

    else:
        prediction = res.json()['total target (wind, solar, hydro)']

st.success(f'Prediction: {prediction}')
