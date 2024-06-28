import streamlit as st
import pandas as pd
import base64
from predict import predict as predict_supervised
from predict_unsupervised import predict_unsupervised
from data_fetcher import DataFetcher
import warnings
warnings.filterwarnings("ignore")

def app():
    # Load the dataset
    df = pd.read_csv("D:/Heritage Institute of Technology,Kolkata/Omdena/Omdena-Milan-Web-App/dataset/Merged_2014.csv")

    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    def set_background_image():
        image_path = "D:/Heritage Institute of Technology,Kolkata/Omdena/Omdena-Milan-Web-App/image/img2.jpeg"
        encoded_image = get_base64_of_bin_file(image_path)
        image_css = f"""
            <style>
            body {{
                background-image: url('data:image/jpeg;base64,{encoded_image}');
                background-size: cover;
            }}
            </style>
        """
        st.markdown(image_css, unsafe_allow_html=True)

    set_background_image()
    st.title("Agriculture Suitability Prediction")
    st.write("This is the Sustainability page.")
    
    # Introduction and user instructions
    st.write("""
    Enter the latitude and longitude to predict whether the area is suitable for agriculture.
    """)
    
    # Input fields for latitude and longitude
    latitude = st.number_input("Latitude", format="%.6f")
    longitude = st.number_input("Longitude", format="%.6f")
    
    # Display the entered latitude and longitude (optional)
    st.write("Entered Latitude:", latitude)
    st.write("Entered Longitude:", longitude)
    
    # Optionally, you can add a map to visualize the entered location
    map_data = pd.DataFrame({'lat': [latitude], 'lon': [longitude]})
    st.write("Location on Map:")
    st.map(map_data)
    
    # Define a tolerance range
    tolerance = 0.0001  # Adjust this value based on the required precision

    # Find the row that is within the tolerance range
    selected_row = df[(abs(df['Latitude'] - latitude) <= tolerance) & (abs(df['Longitude'] - longitude) <= tolerance)]
    
    if not selected_row.empty:
        st.write("Additional Data for the Entered Location:")
        st.write(f"Zone: {selected_row['Zone'].values[0]}")
        st.write(f"NDVI: {selected_row['NDVI'].values[0]}")
        st.write(f"landuse: {selected_row['landuse'].values[0]}")
        st.write(f"LST: {selected_row['LST'].values[0]}")
        st.write(f"NDBI: {selected_row['NDBI'].values[0]}")
        st.write(f"NDWI: {selected_row['NDWI'].values[0]}")
        st.write(f"SAVI: {selected_row['SAVI'].values[0]}")
        st.write(f"SMI: {selected_row['SMI'].values[0]}")
    else:
        st.write("No data found for the entered latitude and longitude.")
    
    if st.button("Predict using Supervised Model"):
        st.experimental_set_query_params(page="supervised", latitude=latitude, longitude=longitude)
    
    if st.button("Predict using Unsupervised Model"):
        st.experimental_set_query_params(page="unsupervised", latitude=latitude, longitude=longitude)

if __name__ == "__main__":
    app()

