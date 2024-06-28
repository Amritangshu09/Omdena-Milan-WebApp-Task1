import streamlit as st
from predict_unsupervised import predict_unsupervised

def app():
    st.title("Unsupervised Model Prediction")
    
    # Get query parameters
    query_params = st.experimental_get_query_params()
    latitude = float(query_params.get("latitude", [0.0])[0])
    longitude = float(query_params.get("longitude", [0.0])[0])

    st.write("Entered Latitude:", latitude)
    st.write("Entered Longitude:", longitude)
    
    prediction = predict_unsupervised(latitude, longitude)
    st.write("Prediction Result (Unsupervised Model):")
    st.write(prediction)

if __name__ == "__main__":
    app()

