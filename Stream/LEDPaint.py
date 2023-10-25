import streamlit as st

# Define the number of rows and columns
num_rows = 16
num_cols = 16

# Create the grid using Streamlit columns
for i in range(num_rows):
    col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14, col15, col16 = st.columns(num_cols)
    for j in range(num_cols):
        with eval(f'col{j + 1}'):
            button_label = f'{i + 1}{j + 1}'
            if st.button(button_label):
                st.write(f'Button in Row {i + 1}, Col {j + 1} clicked')

# You can customize the button label and the action taken when the button is clicked.
