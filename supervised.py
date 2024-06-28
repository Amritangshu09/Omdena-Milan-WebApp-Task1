import streamlit as st
from predict import predict as predict_supervised

def app():
    st.title("Supervised Model Prediction")
    
    # Get query parameters
    query_params = st.experimental_get_query_params()
    latitude = float(query_params.get("latitude", [0.0])[0])
    longitude = float(query_params.get("longitude", [0.0])[0])

    st.write("Entered Latitude:", latitude)
    st.write("Entered Longitude:", longitude)
    
    prediction = predict_supervised(latitude, longitude)
    st.write("Prediction Result (Supervised Model):")
    st.write(prediction)

if __name__ == "__main__":
    app()

