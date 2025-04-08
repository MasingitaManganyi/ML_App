import streamlit as st
import joblib

joblib.load('linear_regression.pkl')
joblib.load('scaler.pkl')

st.title('MetaBrains student test predictor')
st.write('Please enter the number of hours to predict test score: ')

hours = st.number_input('Hours Studied:', min_value = 0.0, step = 1.0)

if st.button('Predict'):
    try:
        data = [[hours]]
        scaled_data = scaler.transform(data)
        prediction = model.predict(scaled_data)
        st.write(f'Predicted Test Score {prediction[0]:0.2f}')
    except Exception as e:
        st.error(f'Error: {e}')
