import seaborn as sns  
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to plot the violin plots
def violinplots(df):
    sns.set_style('whitegrid')
    plt.figure(figsize=(10, 5))
    
    fig, ax = plt.subplots()
    sns.violinplot(x='lifeExp', data=df)
    plt.title('LIFE EXPECTANCY')
    st.pyplot(fig)
    
    fig2, ax2 = plt.subplots()
    sns.violinplot(x='pop', data=df)
    plt.title('POPULATION')
    st.pyplot(fig2)
    
    fig3, ax3 = plt.subplots()
    sns.violinplot(x='gdpPercap', data=df)
    plt.title('GDP per Capita')
    st.pyplot(fig3)
    
    plt.tight_layout()

# Read in the data
data = pd.read_csv("my_data.csv")

# Filter the data to only include data from the year 2007
data_2007 = data[data['year'] ==2007]

# Display the Streamlit app
st.title("JUDD MARC ODOYO")
st.subheader("SCT211-0744/2021")
st.subheader("Data Visualization with Violin Plots")
violinplots(data_2007)