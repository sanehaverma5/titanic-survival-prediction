#pip install streamlit
import streamlit as st
import pandas as pd
import pickle 

#Load the Saved Model
with open("Titanic_model.pkl","rb") as file:
    model = pickle.load(file)

#App Title
st.title("Titanic Survival Prediction")
st.write("Enter Passenger Details")

#Passenger Class
pclass = st.selectbox("Passenger Class",[1,2,3])

#Gender
sex = st.selectbox("Gender",["Male","Female"])

#Age
age = st.number_input(
    "Age",
    min_value = 0,
    max_value=100,
    value=25
)

#sibling count
sibsp = st.number_input(
    "Siblings/Spouse",
    min_value = 0,
    max_value=10,
    value=0
)

#Parent/children count
parch = st.number_input(
    "Parents/children",
    min_value = 0,
    max_value=10,
    value=0
)

#Family Size
family_size=sibsp+parch+1
st.number_input('Family_Size',value=family_size,disabled=True)


#Fare
fare = st.number_input(
    "Fare",
    min_value = 0.0,
    value=50.0
)

#Embarked
embarked = st.selectbox(
    "Embarked",
    ["S","C","Q"]
)

#Encode categorical columns
sex=1 if sex=='Male' else 0


embarked_dict={
    "S":2,
    "C":0,
    "Q":1
}
embarked=embarked_dict[embarked]

#Predict Button
if st.button("Predict"):

    input_data = pd.DataFrame({
        "Pclass": [pclass],
        "Sex": [sex],
        "Age": [age],
        "SibSp": [sibsp],
        "Parch": [parch],
        "Fare": [fare],
        "Embarked": [embarked],
        "FamilySize": [family_size]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Passenger is likely to Survive.")
    else:
        st.error("❌ Passenger is not likely to Survive.")