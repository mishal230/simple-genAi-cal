import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Create a select box for the user to choose the operation
operation = st.selectbox("Select operation:", ("Add", "Subtract", "Multiply", "Divide"))

# Input fields for the two numbers
num1 = st.number_input("Enter first number", step=1.0)
num2 = st.number_input("Enter second number", step=1.0)

# Perform calculation when the user presses the "Calculate" button
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
        st.success(f"The result of {num1} + {num2} is: {result}")
    elif operation == "Subtract":
        result = num1 - num2
        st.success(f"The result of {num1} - {num2} is: {result}")
    elif operation == "Multiply":
        result = num1 * num2
        st.success(f"The result of {num1} * {num2} is: {result}")
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
            st.success(f"The result of {num1} / {num2} is: {result}")
        else:
            st.error("Error! Division by zero.")
