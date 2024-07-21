from controller.LoadModel import LoadModel
from controller.GetPredection import GetPredection
import streamlit as st

st.title('Iris Flower Prediction App')
st.write('Enter the characteristics of the iris flower:')

sepal_length = st.number_input('Sepal Length (cm)', min_value=0.0, max_value=10.0, step=0.1)
sepal_width = st.number_input('Sepal Width (cm)', min_value=0.0, max_value=10.0, step=0.1)
petal_length = st.number_input('Petal Length (cm)', min_value=0.0, max_value=10.0, step=0.1)
petal_width = st.number_input('Petal Width (cm)', min_value=0.0, max_value=10.0, step=0.1)

model = LoadModel('model/Iris_Model.pkl')

if st.button('Predict'):

    predection = GetPredection(model, [sepal_length, sepal_width, petal_length, petal_width])

    st.write(f'The predicted class of the iris flower is: {predection}')

