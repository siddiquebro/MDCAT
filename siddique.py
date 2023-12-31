import streamlit as st

def calculate_mdcat_merit(mdcat_score, total_mdcat_marks, intermediate_percentage, matriculation_percentage):
    if not (0 <= mdcat_score <= total_mdcat_marks) or not (0 <= intermediate_percentage <= 100):
        raise ValueError("Invalid input values. Please ensure MDCAT score is between 0 and total MDCAT marks, and intermediate percentage is between 0 and 100.")
    
    mdcat_merit = (mdcat_score / total_mdcat_marks) * 50 + (intermediate_percentage * 0.4) + (matriculation_percentage * 0.1)
    return mdcat_merit

st.title("🎓MERIT CALCULATOR FOR MDCAT")
#merit= st.text_input("Enter this years MERIT")
st.write('This app is created and deployed by Siddique_Ali khan for just Educational Purpose All Rights Are Reserved ✔️ for the year of 🔴2k23-2k24🔴')
total_mdcat_marks = st.text_input("Enter TOTAL MDCAT Marks")
matriculation_percentage = st.text_input("Enter Your Matriculation Percentage")
intermediate_percentage = st.text_input("Enter Your Intermediate PERCENTAGE")
mdcat_score = st.text_input("Enter Your MDCAT Marks")
merit= 89.00


if st.button("CALCULATE"):
    MDCAT_MERIT = calculate_mdcat_merit(float(mdcat_score), float(total_mdcat_marks), float(intermediate_percentage), float(matriculation_percentage))
    st.success("MERIT Caluculatioin COMPLETE")
    st.success(f"YOUR MERIT : {MDCAT_MERIT:.2f}")
    if MDCAT_MERIT>=merit:
        st.success("CONGRATULATIONS YOU ARE ON MERIT")