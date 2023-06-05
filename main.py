import streamlit as st
import pandas as pd
import numpy as np
import joblib
from streamlit_option_menu import option_menu

# Sidebar to select Page
with st.sidebar:
    page = option_menu('Multiple Disease Prediction System',
                       ['Home',
                        'Diabetes',
                        'Heart Disease',
                        'Parkinson',
                        'Breast Cancer'],
                       icons=['house','bandaid','activity','bandaid-fill','lungs'])
# till here

# Home page function
def home():
    st.title("""
            Welcome to this multi-disease predictor project""")
    st.write("""
             #### You can check diseases such as : 
                 
                > Diabetes
                
                > Heart Disease
                
                > Parkinson 
                
                > Breast Cancer
                
                """)
    st.warning("You should not 100% believe the results here, if you can, then getting checked by a proper doctor is suggested!")

# Diabetes Predictor function
def diabetes():
    st.title("Diabetes Predictor")  

    # look at dataset
    if st.button('Dataset Used'):
        df = pd.read_csv('diabetes.csv')
        st.dataframe(df.sample(1))
    # till here
    
    model = joblib.load('diabetes_model.pkl')  
    
    # input for prediction
    col1, col2, col3, col4 =  st.columns(4)
    
    with col1:
        pregnancy = st.number_input('Enter pregnancies: ',0)
    with col2:
        glucose = st.number_input('Enter glucose : ',0)
    with col3:
        bloodpressure = st.number_input('Enter bloodpressure: ',0)
    with col4:
        skinthickness = st.number_input('Enter skinthickness: ',0)  
        
    with col1:
        insulin = st.number_input('Enter insulin: ',0)
    with col2:
        bmi = st.number_input('Enter bmi : ',0)
    with col3:
        diabetespredigreefunction = st.number_input('Enter Diabetes predigree: ',0)
    with col4:
        age = st.number_input('Enter age: ',0)
    # till here
    
    # predict button
    if st.button('Predict'):
        input_data = np.array([pregnancy,glucose, bloodpressure, skinthickness,insulin, bmi, diabetespredigreefunction, age]).reshape(1,-1)
        prediction = model.predict(input_data)
        if (prediction[0] == 0):
            st.success('Not Diabetic')
        else:
            st.warning('Diabetic')              
    # till here    

# Heart Disease Predictor
def heart_disease():
    st.title("Heart Disease Predictor")  
    
    # look at dataset
    if st.button('Dataset Used'):
        df = pd.read_csv('heart_disease_data.csv')
        st.dataframe(df.sample(1))
    # till here
    
    model = joblib.load('heart_disease_model.pkl')  
    
    # input for prediction
    col1, col2, col3 =  st.columns(3)
    
    with col1:
        age = st.number_input('Enter age: ',0)
    with col2:
        sex = st.number_input('Enter sex : ',0)
    with col3:
        cp = st.number_input('Enter cp: ',0)
        
    with col1:
        trestbps = st.number_input('Enter trestbps: ',0)              
    with col2:
        chol = st.number_input('Enter chol: ',0)
    with col3:
        fbs = st.number_input('Enter fbs : ',0)
        
    with col1:
        restecg = st.number_input('Enter restecg: ',0)
    with col2:
        thalach = st.number_input('Enter thalach: ',0)
    with col3:
        exang = st.number_input('Enter exang: ',0)
        
    with col1:
        oldpeak = st.number_input('Enter oldpeak: ',0)
    with col2:
        slope = st.number_input('Enter slope: ',0)
    with col3:
        ca = st.number_input('Enter ca: ',0)
        
    with col2:
        thal = st.number_input('Enter thal: ',0)
    # till here
    
    # predict button
    if st.button('Predict'):
        input_data = np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]).reshape(1,-1)
        prediction = model.predict(input_data)
        if (prediction[0] == 0):
            st.success('No Heart Disease detected')
        else:
            st.warning('Heart Disease detected')           
    # till here    

# Parkinson Disease Predictor
def parkinson():
    st.title("Parkinsson Predictor")      
    
    # look at dataset
    if st.button('Dataset Used'):
        df = pd.read_csv('Parkinsson disease.csv')
        st.dataframe(df.sample(1))
    # till here
    
    model = joblib.load('parkinsson_model.pkl')  
    
    # input for prediction
    col1, col2, col3, col4 =  st.columns(4)
    
    with col1:
        Fo = st.text_input('Enter Fo(Hz): ',0)
    with col2:
        Fhi = st.text_input('Enter Fhi : ',0)
    with col3:
        Flo = st.text_input('Enter Flo: ',0)
    with col4:
        Jitter = st.text_input('Enter Jitter: ',0)
        
    with col1:
        Jitter_abs = st.text_input('Enter Jitter_abs: ',0)              
    with col2:
        rap = st.text_input('Enter RAP: ',0)
    with col3:
        ppq = st.text_input('Enter ppq : ',0)
    with col4:
        ddp = st.text_input('Enter ddp : ',0)
        
    with col1:
        Shimmer = st.text_input('Enter Shimmer: ',0)
    with col2:
        Shimmer_dB = st.text_input('Enter Shimmer_dB : ',0)
    with col3:
        Shimmer_APQ3 = st.text_input('Enter Shimmer_APQ3: ',0)
    with col4:
        Shimmer_APQ5 = st.text_input('Enter Shimmer_APQ5: ',0)
        
    with col1:
        apq = st.text_input('Enter apq: ',0)              
    with col2:
        Shimmer_DDA = st.text_input('Enter Shimmer_DDA: ',0)
    with col3:
        nhr = st.text_input('Enter nhr : ',0)
    with col4:
        hnr = st.text_input('Enter hnr : ',0)
        
    with col1:
        rpde = st.text_input('Enter rpde: ',0)              
    with col2:
        dfa = st.text_input('Enter dfa: ',0)
    with col3:
        spread1 = st.text_input('Enter spread1 : ',0)
    with col4:
        spread2 = st.text_input('Enter spread2 : ',0)
        
    with col2:
        d2 = st.text_input('Enter d2: ',0)
    with col3:
        ppe = st.text_input('Enter ppe : ',0)
    # till here
    
    # predict button
    if st.button('Predict'):
        input_data = np.array([Fo,Fhi, Flo, Jitter,
       Jitter_abs, rap, ppq, ddp,
       Shimmer, Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5,
       apq, Shimmer_DDA, nhr, hnr, rpde, dfa,
       spread1, spread2, d2, ppe]).reshape(1,-1)
        prediction = model.predict(input_data)
        if (prediction[0] == 0):
            st.success('No Parkinsson detected')
        else:
            st.warning('Parkinsson detected')           
    # till here    

# Breast Cancer Predictor
def breast_cancer():
    st.title("Breast Cancer Predictor")  
    
    # look at dataset
    if st.button('Dataset Used'):
        df = pd.read_csv('breast_cancer.csv')
        st.dataframe(df.sample(1))
    # till here
    
    model = joblib.load('breast_cancer_model.pkl')  
    
    # input for prediction
    col1, col2, col3 =  st.columns(3)
    
    with col1:
        radius_mean = st.number_input('Enter radius_mean: ',0.00)
    with col2:
        texture_mean = st.number_input('Enter texture_mean : ',0.00)
    with col3:
        texture_mean = st.number_input('Enter texture_mean: ',0.00)

    with col1:
        area_mean = st.number_input('Enter area_mean: ',0.00)
    with col2:
        smoothness_mean = st.number_input('Enter smoothness_mean: ',0.00)
    with col3:
        compactness_mean = st.number_input('Enter compactness_mean: ',0.00)

    with col1:
        concavity_mean = st.number_input('Enter concavity_mean: ',0.00)
    with col2:
        concave_points_mean = st.number_input('Enter concave_points_mean: ',0.00)
    with col3:
        symmetry_mean = st.number_input('Enter symmetry_mean: ',0.00)
        
    with col1:
        fractal_dimension_mean = st.number_input('Enter fractal_dimension_mean: ',0.00)
    with col2:
        radius_se = st.number_input('Enter radius_se: ',0.00)
    with col3:
        texture_se = st.number_input('Enter texture_se: ',0.00)
        
    with col1:
        perimeter_se = st.number_input('Enter perimeter_se: ',0.00)
    with col2:
        area_se = st.number_input('Enter area_se: ',0.00)
    with col3:
        smoothness_se = st.number_input('Enter smoothness_se: ',0.00)
        
    with col1:
        compactness_se = st.number_input('Enter compactness_se: ',0.00)
    with col2:
        concavity_se = st.number_input('Enter concavity_se: ',0.00)
    with col3:
        concave_points_se = st.number_input('Enter concave_points_se: ',0.00)
        
    with col1:
        symmetry_se = st.number_input('Enter symmetry_se: ',0.00)
    with col2:
        fractal_dimension_se = st.number_input('Enter fractal_dimension_se: ',0.00)
    with col3:
        radius_worst = st.number_input('Enter radius_worst: ',0.00)
        
    with col1:
        texture_worst = st.number_input('Enter texture_worst: ',0.00)
    with col2:
        perimeter_worst = st.number_input('Enter perimeter_worst: ',0.00)
    with col3:
        area_worst = st.number_input('Enter area_worst: ',0.00)
        
    with col1:
        smoothness_worst = st.number_input('Enter smoothness_worst: ',0.00)
    with col2:
        compactness_worst = st.number_input('Enter compactness_worst: ',0.00)
    with col3:
        concavity_worst = st.number_input('Enter concavity_worst: ',0.00)
        
    with col1:
        concave_points_worst = st.number_input('Enter concave_points_worst: ',0.00)
    with col2:
        symmetry_worst = st.number_input('Enter symmetry_worst: ',0.00)
    with col3:
        fractal_dimension_worst = st.number_input('Enter fractal_dimension_worst: ')        
    # till here
    
    # predict button
    if st.button('Predict'):
        input_data = np.array([radius_mean, texture_mean, texture_mean,
       area_mean, smoothness_mean, compactness_mean, concavity_mean,
       concave_points_mean, symmetry_mean, fractal_dimension_mean,
       radius_se, texture_se, perimeter_se, area_se, smoothness_se,
       compactness_se, concavity_se, concave_points_se, symmetry_se,
       fractal_dimension_se, radius_worst, texture_worst,
       perimeter_worst, area_worst, smoothness_worst,
       compactness_worst, concavity_worst, concave_points_worst,
       symmetry_worst, fractal_dimension_worst]).reshape(1,-1)
        prediction = model.predict(input_data)
        if (prediction[0] == 0):
            st.success('Breast Cancer is Malignant')
        else:
            st.warning('Breast Cancer is Benign')           
    # till here    


# Page function caller
if page == 'Home':
    home()    
elif page == 'Diabetes':
    diabetes()
elif page == 'Heart Disease':
    heart_disease()
elif page == 'Parkinson':
    parkinson()
elif page == 'Breast Cancer':
    breast_cancer()
# till here