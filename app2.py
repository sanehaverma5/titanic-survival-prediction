import streamlit as st
import pandas as pd 
import pickle

with open("Titanic_model.pkl","rb") as file:
    model= pickle.load(file)

st.set_page_config(page_title="Titanic Survival Prediction", page_icon="🚢")

st.title("🚢 Titanic Survival Prediction")
st.write("Enter Passenger Details to Predict Survival")

st.markdown("---")


col1, col2 = st.columns(2)

with col1:
    pclass = st.selectbox(
        "Passenger Class",
        [1,2,3]
    )

    age = st.number_input(
        "Age",
        min_value = 0,
	    max_value = 100,
	    value = 25
    )

   
    sibsp = st.number_input(
	    "Siblings/Spouse",
	        min_value = 0,
	        max_value = 10,
	        value = 0
        )

    Fare = st.number_input(
	    "Fare",
	    min_value = 0.0,
	    value = 50.0
    )

with col2:
    sex = st.selectbox(
        "Gender",
        ["Male","Female"]
    )

    Parch = st.number_input(
	    "Parent/children",
	    min_value = 0,
	    max_value = 10,
	    value = 0
    )

    family_size = sibsp + Parch+ 1
    st.number_input(
        "Family Size",
        value=family_size,
        disabled=True
    )

    embarked = st.selectbox(
	    "Embarked",
	    ["S","C","Q"]
    )

st.markdown("---")

#Encode categorial columns
sex=1 if sex=='Male' else 0


embarked_dict={
	"S":0,
	"C":1,
	"Q":2
}
embarked = embarked_dict[embarked]

#Predict Button
predict = st.button(
    "🚢 Predict Survival",
    use_container_width=True
)

#prediction

if predict:
    input_data=pd.DataFrame({
        "Pclass": [pclass],
        "Sex": [sex],
        "Age": [age],
        "Sibsp": [sibsp],
        "Parch": [parch],
        "Fare": [fare],
        "Embarked": [embarked],
        "FamilySize": [familysize]
    })

    prediction = model.predict(input_data)

    st.markdown("---")

    if prediction[0] == 1:
        st.success("✅ Passenger is likely to Survive.")
        st.balloons()
    else:
        st.error("❌ Passenger is not likely to Survive.") 
    
