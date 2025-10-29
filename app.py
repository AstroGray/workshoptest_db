import sqlite3
import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px
from dash_auth import BasicAuth
import os  # For environment variables (optional for security)

# Connect to database
conn = sqlite3.connect('data.db')

# Load maintenance data
query = "SELECT WorkshopID, DateIn, Issue, Cost FROM MaintenanceRecord;"
df = pd.read_sql_query(query, conn)

# If your dates are strings, convert them to datetime
try:
    df['DateIn'] = pd.to_datetime(df['DateIn'])
except Exception:
    pass

# Initialize the app
app = Dash(__name__)

# Define credentials as a list of tuples (username, plaintext password)
# For security, load from env vars: e.g., [('admin', os.environ.get('DASH_PASSWORD', 'password123'))]
VALID_USERNAME_PASSWORD_PAIRS = [
    ('admin', 'password123')  # Replace with your desired credentials; add more tuples if needed
]

# Apply basic authentication (correct parameters only)
BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS,  # This is the required username_password_list
    secret_key=os.environ.get("SECRET_KEY", "your_random_secret_key_here")  # Generate a strong, random key (at least 32 chars)
)

# Create a visualization (cost over time by workshop)
fig = px.bar(df, x='Issue', y='Cost', color='WorkshopID', title='Maintenance Cost Over Time')

# Format y-axis as currency with dollars and commas
fig.update_layout(
    yaxis=dict(
        tickprefix='$',  # Adds $ before each tick value
        tickformat=',.0f'  # Adds commas for thousands and 0 decimal places
    ),
    xaxis_title='Issue'  # Changes the x-axis label to "Issue"
)

fig2 = px.pie(df, names='WorkshopID', values='Cost', title='Cost Breakdown by Workshop')

# Format pie slices to show workshop name, dollar-formatted cost, and percentage
fig2.update_traces(
    texttemplate='%{label}<br>$%{value:,.0f}<br>(%{percent})',
    textposition='inside',
    textinfo='label+text'  # Ensures the template is used
)

# Dashboard layout
app.layout = html.Div([
    html.H1('Workshop Maintenance Overview'),
    dcc.Graph(figure=fig),
    dcc.Graph(figure=fig2)
])

if __name__ == '__main__':
    app.run(debug=True)
