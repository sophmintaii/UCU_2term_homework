"""
Contains example of usage of ResponseList ADT and
PsyAnalyser, PsyStudentAnalyser classes.
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
from ..modules.psyanalyser import PsyAnalyser
from ..modules.psystudentanalyser import PsyStudentAnalyser
from ..modules.agegroup import AgeGroup
from ..modules.studentgroup import StudentGroup
from ..modules.people import Person, Student

def main():
    """
    Creates and runs web app based on information from the created age
    and student groups
    """
    # create age groups
    group1 = AgeGroup(age=16, suicide=2, suicide_resp=20, depression=5,
                    depression_resp=30, anxiety=10, anxiety_resp=30)
    group2 = AgeGroup(age=17, suicide=3, suicide_resp=28, depression=7,
                    depression_resp=30, anxiety=11, anxiety_resp=30)
    group3 = AgeGroup(age=18, suicide=6, suicide_resp=30, depression=8,
                    depression_resp=31, anxiety=8, anxiety_resp=20)

    # create student groups
    sgroup1 = StudentGroup(age=17, depression=13, anxiety=15, suicide=5, study=20,
                        suicidal_thoughts=10, self_harm=6, dep_diagnosed=2,
                        behavior=15, anx_diagnosed=4, doctor=10, total=30,
                        list_anx=["GAD"])
    sgroup2 = StudentGroup(age=19, depression=11, anxiety=16, suicide=2, study=21,
                        suicidal_thoughts=9, self_harm=5, dep_diagnosed=4,
                        behavior=17, anx_diagnosed=3, doctor=12, total=34,
                        list_anx=["PD", "PD"])

    # create people & students
    person = Person(age=18, depression=1, suicide=0, anxiety=0, doctor=1)
    student = Student(age=16, depression=0, anxiety=1, suicide=0, doctor=1,
                    study=1, suicidal_thoughts=1, self_harm=1, dep_diagnosed=0,
                    behavior=1, anx_diagnosed=1, list_dep=[], list_anx=["GAD",
                                                                        "PD"])

    # create PsyAnalyser and PsyStudentAnalyser
    analyser = PsyAnalyser()
    analyser.add_group(group1)
    analyser.add_group(group2)
    analyser.add_group(group3)
    analyser.add_person(person)

    student_analyser = PsyStudentAnalyser()
    student_analyser.add_group(sgroup1)
    student_analyser.add_group(sgroup2)
    student_analyser.add_person(student)

    # create pandas data frames and graph for depression parameter
    figure1 = px.line(pd.DataFrame(analyser.get_depression().get_df_for_line(),
                                columns=["age", "depression%"]),
                    x="age",
                    y="depression%")

    # create pandas data frames and graph for anxiety disorders list parameter
    figure2 = px.line(pd.DataFrame(student_analyser.get_list_anx(
    ).get_df_for_line(), columns=["d/o", "number of students"]),
        x="d/o", y="number of students")

    # create graph for suicidal_thoughts parameter
    figure3 = px.pie(pd.DataFrame(student_analyser.get_suicidal_thoughts(
    ).get_df_for_pie(), columns=["students"]),
        values="students",
        color_discrete_sequence=px.colors.sequential.RdBu)

    # run web app for data
    external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    app.layout = html.Div(children=[
        html.H1(children="Deprssion"),
        html.Div(children="""
            Statistics on depression.
            """),
        dcc.Graph(
            id="depr-graph",
            figure=figure1
        ),
        html.H1(children="Anxiety d/o's"),
        html.Div(children="""
            Statistics on anxiety disorders.
            """),
        dcc.Graph(
            id="anxdo-graph",
            figure=figure2
        ),
        html.H1(children="Suicidal thoughts"),
        html.Div(children="""
            How many students had or have suicidal thoughts?
            """),
        dcc.Graph(
            id="suithoughts-graph",
            figure=figure3
        ),
    ])
    app.run_server(debug=True)


if __name__ == "__main__":
    main()
