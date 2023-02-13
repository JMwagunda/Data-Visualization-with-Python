import seaborn as sns  
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("my_data.csv")

#Function to plot the violin plots
def violinplots(df):
    sns.set_style('White grid')
    plt.figure(figsize=(10, 5))
    
    plt.subplot(120)
    sns.violinplot(x='lifeExp', data=df)
    plt.title('LIFE EXPECTANCY')
    
    plt.subplot(121)
    sns.violinplot(x='pop', data=df)
    plt.title('POPULATION')
    
    plt.subplot(122)
    sns.violinplot(x='gdppercap', data=df)
    plt.title('GDP per Capita')
    
    plt.tight_layout()
    plt.show()
    
    #Streamlit Representation
    #Andika admission yako apo kwa brackets
    st.title("Kenneth Ruto\nSCT211-0744/2021\nData Visualization with Violin Plots")
    violinplots(df)