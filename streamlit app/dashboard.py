import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
@st.cache_data  # This decorator helps to cache the data to speed up re-runs after the first load
def load_data():
    df = pd.read_csv('waris.csv')
    return df

df = load_data()

# Title of the dashboard
st.title('Kenya Water Utility Performance Dashboard')

# Sidebar for user input features
st.sidebar.header('User Input Features')
selected_zone = st.sidebar.selectbox('Select a Zone', df['Zone'].unique())
selected_metric = st.sidebar.selectbox('Select a Metric', ['Total Collection', 'Collection Efficiency', 'Total Personnel Expenditures'])

# Filtering data based on selection
filtered_data = df[df['Zone'] == selected_zone]

# Displaying selected metrics
st.header(f'Data for {selected_zone} Zone')
st.write(filtered_data[['Year', 'Month', selected_metric]])

# Plotting
st.header(f'Visualization for {selected_metric} in {selected_zone} Zone')
fig, ax = plt.subplots()
sns.lineplot(data=filtered_data, x='Month', y=selected_metric, hue='Year', marker='o', ax=ax)
ax.set_ylabel(selected_metric)
ax.set_title(f'{selected_metric} over Months for {selected_zone} Zone')
st.pyplot(fig)
