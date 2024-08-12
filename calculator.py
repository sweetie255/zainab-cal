import streamlit as st
import addition
import subtraction
import multiplication
import divide

# Title of the app
st.title("Zainab Calculator")

# Input fields for numbers
num1 = st.number_input("Enter the first number:", value=0.0)
num2 = st.number_input("Enter the second number:", value=0.0)

# Dropdown for operator selection
operator = st.selectbox("Choose an operator:", ["+", "-", "*", "/"])

# Perform the calculation based on the selected operator
if operator == '+':
    result = addition.add(num1, num2)
elif operator == '-':
    result = subtraction.subtract(num1, num2)
elif operator == '*':
    result = multiplication.multiply(num1, num2)
elif operator == '/':
    result = divide.divide(num1, num2)

# Display the result
st.write(f"The result is: {result}")

# Option to quit
if st.button("Quit"):
    st.stop()
