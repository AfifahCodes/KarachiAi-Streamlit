import streamlit as st
import pandas as pd 
data = pd.read_csv('AirPassengers.csv')
#Convert it into years:
# data['Year'] = data['Month'].apply(lambda x:x.spllit('-')[0])
def main():
    st.title('Air Passengers by year')
    year = st.selectbox( 'Select Year', data['Year'].drop_duplicates())
    filtered = data[data['Year']== year]
    button = st.button('Display data')
    if button:
        st.table(data =filtered)
 

if __name__ == "__main__":
    main()
