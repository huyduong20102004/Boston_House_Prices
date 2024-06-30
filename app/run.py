import numpy as np
import pandas as pd
import streamlit as st
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

# Load the model
model = pickle.load(open('../model/model.pkl', 'rb'))

cols =['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
       'PTRATIO', 'B', 'LSTAT', 'MEDV']



class StreamlitApp:

    def __init__(self):
        self.model = model



    def construct_sidebar(self):

        st.sidebar.markdown(
            '<p class="header-style">Boston Housing Price Prediction</p>',
            unsafe_allow_html=True
        )
        default = [0.35809,0.0,6.2,1,0.507,6.951,88.5,2.8617,8,307.0,17.4,391.7,9.71]
        crim = st.sidebar.number_input(f"{cols[0]}", min_value=0.0, max_value=100.0, step=0.1, value=default[0])
        zn = st.sidebar.number_input(f"{cols[1]}", min_value=0.0, max_value=100.0, step=0.1, value=default[1])
        indus = st.sidebar.number_input(f"{cols[2]}", min_value=0.0, max_value=100.0, step=0.1, value=default[2])
        chas = st.sidebar.selectbox(f"{cols[3]}", [0, 1], index=1)
        nox = st.sidebar.number_input(f"{cols[4]}", min_value=0.0, max_value=1.0, step=0.01, value=default[4])
        rm = st.sidebar.number_input(f"{cols[5]}", min_value=1.0, max_value=10.0, step=0.1, value=default[5])
        age = st.sidebar.number_input(f"{cols[6]}", min_value=0.0, max_value=100.0, step=0.1, value=default[6])
        dis = st.sidebar.number_input(f"{cols[7]}", min_value=0.0, max_value=100.0, step=0.1, value=default[7])
        rad = st.sidebar.number_input(f"{cols[8]}", min_value=0, max_value=24, step=1, value=default[8])
        tax = st.sidebar.number_input(f"{cols[9]}", min_value=0.0, max_value=1000.0, step=1.0, value=default[9])
        ptratio = st.sidebar.number_input(f"{cols[10]}", min_value=0.0, max_value=100.0, step=0.1, value=default[10])
        b = st.sidebar.number_input(f"{cols[11]}", min_value=0.0, max_value=1000.0, step=0.1, value=default[11])
        lstat = st.sidebar.number_input(f"{cols[12]}", min_value=0.0, max_value=100.0, step=0.1, value=default[12])
        
        values = [crim, zn, indus, chas, nox, rm, age, dis, rad, tax, ptratio, b, lstat]

        return values

    def construct_app(self):
        values = self.construct_sidebar()

        values_to_predict = np.array(values).reshape(1, -1)
        prediction = self.model.predict(values_to_predict)

        st.markdown(
            """
            <style>
            .header-style {
                font-size:25px;
                font-family:sans-serif;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <style>
            .font-style {
                font-size:20px;
                font-family:sans-serif;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            '<p class="font-style"> Please enter the values in the sidebar to get the prediction right away.</p>',
            unsafe_allow_html=True
        )
        
        column_1, column_2 = st.columns(2)
        column_1.markdown(
            """
            <style>
            .font-style {
                font-size:24px;
                font-weight:bold;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        column_1.markdown(
            f'<p class="font-style">Prediction: ${prediction[0] * 1000:.2f}</p>',
            unsafe_allow_html=True
        )

        # MEDV 
        mdev = pd.read_csv('../data/housing_comma.csv')['MEDV']
    
        # Histogram for MEDV
        plt.figure(figsize=(10, 6))
        sns.histplot(mdev, bins=30, kde=True)
        plt.title('MEDV Distribution')
        plt.xlabel('MEDV')
        plt.ylabel('Frequency')
        st.pyplot()
        
sa = StreamlitApp()
sa.construct_app()
