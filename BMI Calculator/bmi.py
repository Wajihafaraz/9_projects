import streamlit as st


# 🎨 Add Custom Styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #f0f8ff;  /* Light Blue Background */
        }
        h1 {
            color: #0077b6;  /* Dark Blue Heading */
            text-align: center;
        }
        div.stButton > button {
            background-color: #0077b6;
            color: white;
            border-radius: 10px;
            font-size: 18px;
            padding: 10px;
            width: 100%;
        }
        div.stButton > button:hover {
            background-color: #005f8a;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🦾BMI CALCUTAOR WEB APP")


height=st.slider("Select your height (cm)", 50,200,170, step=1)
weight=st.slider("Select your weight (kg)" , 10,100,70, step=1)

# convert height from cm to m
height = height/100 # 170cm -> 1.70 m

# calculate bmi on button click

if st.button("Calculate BMI"):
       if weight > 0 and height> 0:
            #   calculate bmi formula
            bmi=weight / (height ** 2)
            st.success(f"Your BMI is {bmi: .2f}")

            # category check for bmi

            if bmi < 18.5:
             st.warning("You are underweight 🧍‍♂️")

            elif 18.5<=bmi< 24.9:  
             st.warning("Your weight is normal 🧍‍♀️")

            elif 25 <= bmi< 29.9:
               st.warning("You are overweight 👳‍♂️")   

            else:
               st.warning("you are obess")   
       else:
        st.write("please select a valid weight and height")               

