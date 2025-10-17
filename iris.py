import streamlit as st
import pandas as pd
import numpy as np
import pickle
#from PTL import Image
model = pickle.load(open('model/model.pkl', 'rb'))


st.title('Iris Prediction App')

st.subheader('Enter Your Data Below')

# st.text_input('sepal length')
# st.text_input('sepal width')
# st.text_input('petal length')
# st.text_input('petal width')
#
# st.button('Click Here')

with st.form(key='iris species prediction form'):
    pl=st.number_input('enter petal length')
    pw=st.number_input('enter petal width')
    sl=st.number_input('enter sepal length')
    sw=st.number_input('enter sepal width')
    submit=st.form_submit_button('predict species')



    if submit:
        input_data = np.array([[pl, pw, sl, sw]])
        prediction = model.predict(input_data)

        # species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

        species_map = {
            0: {
                'name': 'Iris Setosa',
                'emoji': '🌸',
                'class': 'species-setosa',
                'image_path': 'image/setosa.jpg',  # You'll need to add these images
                'description': "Known for its bright colors and early blooming. Native to North America."
            },

        1: {
        'name': 'Iris Versicolor',
        'emoji': '🌺',
        'class': 'species-versicolor',
        'image_path': 'image/versicolor.jpg',
        'description': "Also called 'Blue Flag Iris', commonly found in wetlands."
    },
    2: {
    'name': 'Iris Virginica',
    'emoji': '💮',
    'class': 'species-virginica',
    'image_path': 'image/virginica.jpg',
    'description': "Larger flowers, typically found in the southeastern United States."
}
}

        # Convert numpy array to list and get first element
        predicted_class = species_map.get(prediction.tolist()[0], "unknown species")

        st.success(f'Prediction Result: {prediction[0]}')
        st.success(f'Predicted Species: {predicted_class}')

