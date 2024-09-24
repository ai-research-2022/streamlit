
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and introductory text
st.title('My First Streamlit App')
st.write('This is a simple Streamlit app.')

# Input Widgets
user_input = st.text_input("Enter your name")
st.write('Your name is', user_input)

age = st.slider("Choose your age", 1, 100)
st.write("You are ", age, " years old")

if st.button('Say hello'):
    st.write('Hello there!')

# Displaying Data
data = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.dataframe(data)

# Plotting Data
fig, ax = plt.subplots()
ax.hist(data['second column'], bins=5)
st.pyplot(fig)

# Layouts and Containers
col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("Hello")
with col2:
    st.header("Column 2")
    st.write("World")

with st.expander("See explanation"):
    st.write("Here you could put in some really, really explanatory stuff.")
