import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load('mlp_model.pkl')
scaler = joblib.load('scaler.pkl')

# Initialize session state
if 'student_data' not in st.session_state:
    st.session_state.student_data = []

# Page 1: Input student data
def input_student_data():
    st.title('Input Student Data')
    name = st.text_input('Student Name')
    semester_grades = []
    for i in range(1, 9):  # Assuming 8 semesters
        grade = st.number_input(f'Semester {i} Grade', min_value=0.0, max_value=4.0, step=0.01)
        semester_grades.append(grade)
    
    if st.button('Submit'):
        student_data = {
            'name': name,
            'grades': semester_grades
        }
        st.session_state.student_data.append(student_data)
        st.success('Student data added successfully!')

# Page 2: List students and predict grades
def list_students_and_predict():
    st.title('Student Grades and Predictions')
    
    if not st.session_state.student_data:
        st.warning('No student data available. Please add student data on the input page.')
        return
    
    for student in st.session_state.student_data:
        st.subheader(student['name'])
        grades = student['grades']
        df = pd.DataFrame([grades], columns=[str(i) for i in range(1, 9)])
        st.table(df)

        # Prepare the data for prediction
        input_data = np.array(grades[:-1]).reshape(1, -1)
        input_data_scaled = scaler.transform(input_data)
        prediction = model.predict(input_data_scaled)
        st.write(f'Predicted Grade for Next Semester: {prediction[0]:.2f}')

# Streamlit navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Input Student Data', 'List Students and Predict Grades'])

if page == 'Input Student Data':
    input_student_data()
elif page == 'List Students and Predict Grades':
    list_students_and_predict()