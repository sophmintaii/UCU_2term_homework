import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px


def read_csv_to_dict(path):
    """
    str -> dict(int, dict(str: int))
    Returns dictionary with data from the csv file
    """
    with open(path, "r", encoding="utf-8") as file:
        data = pd.read_csv(file).to_dict(orient="records")

    res = {}
    for item in data:
        res[item["number"]] = dict(
            zip(list(item.keys())[1:], list(item.values())[1:]))
    return res


def data_to_plot(data):
    """
    dict(int, dict(str: int)) -> pandas DataFrame
    Returns data in format it can be plotted
    """
    data_lst = []
    for item in data:
        data_lst.append((item, data[item]["end"] - data[item]["start"]))
    res = pd.DataFrame(data_lst, columns=["number", "difference"])
    return res


def plot(data):
    """
    pandas DataFrame -> NoneType
    Plots the line diagram
    """
    fig = px.line(data, x="number", y="difference")
    return fig


def create_app(path):
    """
    str -> Dash application
    Creates a dash application based on csv file
    """
    external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    app.layout = html.Div(children=[
        html.H1(children="Difference graph"),
        html.Div(children="""
            Here's my first Dash application.
            """),
        dcc.Graph(
            id="diff-graph",
            figure=plot(data_to_plot(read_csv_to_dict(path)))
        )
    ])
    return app


if __name__ == "__main__":
    diff_app = create_app("../docs/test.csv")
    diff_app.run_server(debug=True)
