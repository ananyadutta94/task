import pandas as pd
import plotly.express as px
import streamlit as st

# Title of the app
st.title("Interactive Data Visualization Tool")

# Step 1: Upload Dataset
st.sidebar.header("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    # Load the dataset
    df = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview")
    st.write(df.head())

    # Step 2: Select Visualization Type
    st.sidebar.header("Visualization Options")
    chart_type = st.sidebar.selectbox("Choose a visualization type", 
                                       ["Scatter Plot", "Bar Chart", "Histogram", "Line Plot", "Box Plot"])

    # Step 3: Select Columns for Visualization
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    categorical_columns = df.select_dtypes(include=['object']).columns

    if chart_type in ["Scatter Plot", "Bar Chart", "Line Plot"]:
        x_axis = st.sidebar.selectbox("Select X-Axis", df.columns)
        y_axis = st.sidebar.selectbox("Select Y-Axis", numeric_columns)

        if chart_type == "Scatter Plot":
            fig = px.scatter(df, x=x_axis, y=y_axis)
        elif chart_type == "Bar Chart":
            fig = px.bar(df, x=x_axis, y=y_axis)
        elif chart_type == "Line Plot":
            fig = px.line(df, x=x_axis, y=y_axis)
    elif chart_type == "Histogram":
        x_axis = st.sidebar.selectbox("Select Column", numeric_columns)
        fig = px.histogram(df, x=x_axis)
    elif chart_type == "Box Plot":
        x_axis = st.sidebar.selectbox("Select X-Axis (Categorical)", categorical_columns)
        y_axis = st.sidebar.selectbox("Select Y-Axis (Numeric)", numeric_columns)
        fig = px.box(df, x=x_axis, y=y_axis)

    # Display the visualization
    st.write("### Visualization")
    st.plotly_chart(fig)

else:
    st.write("Please upload a dataset to get started.")

