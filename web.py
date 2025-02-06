import os 
import pickle  # load pretrained model
import streamlit as st   # web app
from streamlit_option_menu import option_menu  # Use to create option menu

# Configure Streamlit app
st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon='🩺')

# Load models using relative paths
def load_model(model_path):
    if os.path.exists(model_path):
        with open(model_path, "rb") as model_file:
            return pickle.load(model_file)
    else:
        st.error(f"Model file not found: {model_path}")
        return None 

# Load models (Ensure these files exist in your GitHub repo)
diabetes_model = load_model("saved_models/diabetes_model.sav")
heart_model = load_model("saved_models/heart_model.sav")
parkinson_model = load_model("saved_models/parkinson_model.sav")

with st.sidebar:
    selected= option_menu('Prediction of disease outbreak system',
                          ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                          menu_icon='hospital-fail',icons=['activity','heart','person'],default_index=0)
    
if selected =='Diabetes Prediction':
    st.title('Diabetes Pridiction on Your Report Data')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
    with col2:
         Glucose= st.text_input('Glucose level')
    with col3:
        Bloodpressure= st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin= st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreefunction = st.text_input('Diabetes Predigree Function Value')
    with col2:
        Age= st.text_input('Age of the Person')

diab_diagnosis = ''
advice = ''

if st.button('Diabetes Test Result'):
    user_input = [Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin, BMI, DiabetesPedigreefunction, Age]
    user_input = [float(x) for x in user_input]
    diab_prediction = diabetes_model.predict([user_input])

    if diab_prediction[0] == 1:
        diab_diagnosis = '🛑 The person is diabetic.'
        advice = """  
        **Immediate Steps:**  
        - Consult a doctor immediately.  
        - Monitor blood sugar levels regularly.  
        - Follow a balanced diet and exercise routine.  

        **Diet & Lifestyle Recommendations:**  
        - Avoid sugary and processed foods.  
        - Eat fiber-rich foods and maintain portion control.  
        - Stay physically active for at least 30 minutes daily.  

        **Medication & Monitoring:**  
        - Take prescribed medications or insulin as advised.  
        - Schedule regular health check-ups.  
        """
    else:
        diab_diagnosis = '✅ The person is not diabetic.'
        advice = ''

    st.success(diab_diagnosis)
    
    if advice:
        st.warning(advice)


#HEART DISEASE DIGNOSIS 
if selected =='Heart Disease Prediction':
    st.title="Pridict the Heart Disease"
    col1,col2,col3=st.columns(3)
    with col1:
        age= st.text_input('Age of Person')
    with col2:
        sex=st.text_input('Enter the sex')
    with col3:
        cp=st.text_input('constrictive pericarditis(CP)')
    with col1:
        trestbps=st.text_input('Value of trestbps')
    with col2:
        chol=st.text_input('Value of Cholesterol')
    with col3:
        fbs=st.text_input('Fasting blood sugar Level(FBS)')
    with col1:
        restecg= st.text_input('resting electrocardiographic result(restecg)')
    with col2:
        thalach=st.text_input('measurement of thalach')
    with col3:
        exang=st.text_input('exercise-induced angina(exang)')
    with col1:
        oldpeak=st.text_input('oldpeak value')
    with col2:
        slope=st.text_input('ST/HR slope')
    with col3:
        ca=st.text_input('coronary artery calcification(ca)')
    with col1:
        thal=st.text_input('level of Thalassemia(thal)')
        
heart_diagnosis = ''
if st.button('Heart Test Result'):
    user_input= [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    user_input= [float(x) for x in user_input]
    heart_prediction= heart_model.predict([user_input])
   # Heart Disease Prediction Result
    if heart_prediction[0] == 1:
        heart_diagnosis = '🛑 The person has heart disease.'
        advice = """  
        **Heart Disease Management:**  
        - Consult a cardiologist.  
        - Maintain a low-fat, high-fiber diet.  
        - Exercise regularly but avoid overexertion.  
        - Monitor blood pressure and cholesterol levels.  
        - Take prescribed medications.  
        \n"""
    else:
        heart_diagnosis = '✅ The person does not have heart disease.'
    st.success(heart_diagnosis)
    
# Show Advice if Any Disease is Detected
    if advice:
        st.warning(advice)
    

#PARKINSON'S DISEASE DIGNOSIS MODEL
if selected=='Parkinsons Prediction':
    st.title='PARKINSON DISEASE PREDINCT ON YOUR DATA'
    col1,col2,col3=st.columns(3)
    with col1:
       MDVP_Fo =st.text_input('MDVP:Fo(Hz)')
    with col2:
        MDVP_Fhi=st.text_input('MDVP:Fhi(Hz)')
    with col3:
        MDVP_Flo=st.text_input('MDVP:Flo(Hz)')
    with col1:
        MDVP_Jitter_percentage =st.text_input('MDVP:Jitter(percentage)')
    with col2:
        MDVP_Jitter_Abs=st.text_input('MDVP:Jitter(Abs)')
    with col3:
        MDVP_Jitter_RAP=st.text_input('MDVP:JitterRAP')
    with col1:
        MDVP_PPQ=st.text_input('MDVP:PPQ')
    with col2:
        Jitter_DDP=st.text_input('MDVP:DDP')
    with col3:
        MDVP_Shimmer=st.text_input('MDVP:Shimmer')
    with col1:
        MDVP_Shimmer_dB=st.text_input('MDVP:Shimmer(dB)')
    with col2:
        Shimmer_APQ3=st.text_input('Shimmer:APQ3')
    with col3:
        Shimmer_APQ5=st.text_input('Shimmer:APQ5')
    with col1:
        MDVP_APQ=st.text_input('Shimmer:APQ')     
    with col2:
        Shimmer_DDA=st.text_input('Shimmer:DDA')
    with col3:
        NHR=st.text_input('NHR')
    with col1:
        HNR=st.text_input('HNR')
    with col2:
        RPDE=st.text_input('RPDE')
    with col3:
        DFA=st.text_input('DFA')
    with col1:
        spread1=st.text_input('spread1')
    with col2:
        spread2=st.text_input('spread2')
    with col3:
        D2=st.text_input('D2')
    with col1:
        PPE=st.text_input('PPE')
        
park_dignosis=''
if st.button('Parkison Disease Result'):
    user_input=[MDVP_Fo,MDVP_Fhi,MDVP_Flo,MDVP_Jitter_percentage,MDVP_Jitter_Abs,MDVP_Jitter_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA ,NHR, HNR, RPDE, DFA,spread1,spread2,D2,PPE]
    user_input=[float(x) for x in user_input]
    park_Prediction=parkinson_model.predict([user_input])
    # Parkinson’s Disease Prediction Result
    if parkinson_prediction[0] == 1:
        parkinson_diagnosis = '🛑 The person has Parkinson’s disease.'
        advice = """  
        **Parkinson’s Management:**  
        - Consult a neurologist for early treatment.  
        - Engage in physiotherapy and movement exercises.  
        - Take prescribed medications.  
        - Join a Parkinson’s support group.  
        \n"""
    else:
        parkinson_diagnosis = '✅ The person does not have Parkinson’s disease.'
    st.success(park_dignosis)
    if advice:
        st.warning(advice)
        