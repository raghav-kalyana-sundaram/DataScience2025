import pandas as pd
import plotly.express as px

# Load the dataset (replace 'your_file_path.csv' with the path to your CSV file)
file_path = 'Files/incomebystate.csv'
data = pd.read_csv(file_path)

# Dictionary to map full state names to their postal abbreviations
state_abbreviations = {
    "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR", "California": "CA",
    "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE", "Florida": "FL", "Georgia": "GA",
    "Hawaii": "HI", "Idaho": "ID", "Illinois": "IL", "Indiana": "IN", "Iowa": "IA",
    "Kansas": "KS", "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
    "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS", "Missouri": "MO",
    "Montana": "MT", "Nebraska": "NE", "Nevada": "NV", "New Hampshire": "NH", "New Jersey": "NJ",
    "New Mexico": "NM", "New York": "NY", "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH",
    "Oklahoma": "OK", "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
    "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT", "Vermont": "VT",
    "Virginia": "VA", "Washington": "WA", "West Virginia": "WV", "Wisconsin": "WI", "Wyoming": "WY"
}

data['State'] = data['State'].map(state_abbreviations)

# Aggregate income data by State
state_income = data.groupby('State')['IncomePerCap'].median().reset_index()

# Create a choropleth map using Plotly
fig = px.choropleth(
    state_income,
    locations="State",
    locationmode="USA-states",
    color="IncomePerCap",
    scope="usa",
    color_continuous_scale="YlOrRd",
    title="Heatmap of Median Income by State",
    labels={"IncomePerCap": "Median Income"}
)

# Show the interactive plot
fig.show()
