import pandas as pd
import dash
from dash import dcc, html,Dash,Input,Output
import plotly.express as px

# Load data
df = pd.read_csv("output.csv")

df.head()

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values(by="date")

# Create Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div(
    style={"backgroundColor": "#f5f5f5", "padding": "20px"},
    children=[

        html.H1(
            "Pink Morsel Sales Dashboard",
            id = "header",
            style={"textAlign": "center", "color": "#2c3e50"}
        ),

        # Radio buttons
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "South", "value": "south"},
                {"label": "East", "value": "east"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={"textAlign": "center", "marginBottom": "20px"}
        ),

        # Graph
        dcc.Graph(id="sales-chart")
    ]
)

# Callback (dynamic update)
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"].str.lower() == selected_region]

    filtered_df = filtered_df.sort_values(by="date")

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title="Sales Over Time",
        labels={"date": "Date", "sales": "Sales"}
    )

    # Add vertical line 
    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        line_color="red"
    )

    return fig

# Run app
if __name__ == "__main__":
    app.run(debug=True)
