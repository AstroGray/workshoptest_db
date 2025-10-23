import sqlite3
import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Connect to database
conn = sqlite3.connect('data.db')

# Load maintenance data
query = "SELECT WorkshopID, DateIn, Cost FROM MaintenanceRecord;"
df = pd.read_sql_query(query, conn)

# If your dates are strings, convert them to datetime
try:
    df['DateIn'] = pd.to_datetime(df['DateIn'])
except Exception:
    pass

# Initialize the app
app = Dash(__name__)

# Create a visualization (cost over time by workshop)
fig = px.line(df, x='DateIn', y='Cost', color='WorkshopID', title='Maintenance Cost Over Time', markers=True)

# Format y-axis as currency with dollars and commas
fig.update_layout(
    yaxis=dict(
        tickprefix='$',  # Adds $ before each tick value
        tickformat=',.0f'  # Adds commas for thousands and 2 decimal places
    ),
    xaxis_title='Date'  # Changes the x-axis label to "Date"
)

fig2 = px.pie(df, names='WorkshopID', values='Cost', title='Cost Breakdown by Workshop')

# Dashboard layout
app.layout = html.Div([
    html.H1('Workshop Maintenance Overview'),
    dcc.Graph(figure=fig),
    dcc.Graph(figure=fig2)
])


if __name__ == '__main__':
    app.run(debug=True)
