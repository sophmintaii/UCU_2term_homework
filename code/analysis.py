"""
The main module of the program.
Contains analysis of data from databases and API.
"""
import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from psyanalyser import PsyAnalyser
from psystudentanalyser import PsyStudentAnalyser
from agegroup import AgeGroup
from studentgroup import StudentGroup
from people import Person, Student


def count_resp(data):
    """
    dict -> dict
    Counts sum of respondents in particulat year.
    """
    years = dict()
    for record in data:
        if record["Year"] not in years:
            years[record["Year"]] = record["Suicides"]
        else:
            years[record["Year"]] += record["Suicides"]
    return years


def analyse_suicide_by_age(path):
    """
    str -> plotly line graphs
    Analyses middle death from suicide age in different years.
    """
    # read data from csv file to pandas data frame
    with open(path, "r", encoding="utf-8") as file:
        data = pd.read_csv(file).to_dict(orient="records")
    # create PsyAnalyser object
    analyser = PsyAnalyser(1981)
    years_resp = count_resp(data)
    result = []
    for i, record in enumerate(data):
        year = record["Year"]
        year_prev = data[i - 1]["Year"] if i > 0 else record["Year"]
        if year == year_prev:
            analyser.add_group(AgeGroup(age=record["Age"],
                                        suicide=record["Suicides"],
                                        suicide_resp=years_resp[year]))
        else:
            result.append(analyser)
            analyser = PsyAnalyser(year)

    res_df = pd.DataFrame(columns=["year", "age", "suicides"])
    for analysis in result:
        df = pd.DataFrame(analysis.get_suicide().get_df_for_line(
            analysis.year), columns=["year", "age", "suicides"])
        res_df = res_df.append(df, ignore_index=True)
    figure1 = px.line(res_df, x="age", y="suicides",
                      color="year", line_group="year", hover_name="year")

    middle_ages = []
    for analysis in result:
        age = 0
        counter = 0
        for group in analysis.groups:
            age += group * analysis.groups[group].suicide
            counter += analysis.groups[group].suicide
        middle_ages.append((analysis.year, age / counter))
    middle_df = pd.DataFrame(middle_ages, columns=["year", "middle age"])
    figure2 = px.line(middle_df, x="year", y="middle age")

    return figure1, figure2


def get_from_google_sheets(sheets):
    """
    list -> list
    Returns list of responses from all the workplaces listed.
    """
    # get data using API
    # (client_secret.json is a file you get when you enable Google Sheets API)
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'client_secret.json', scope)
    # create a client who will have access to Google Sheets
    # remember to give to your client email edit rights
    client = gspread.authorize(creds)
    data = []
    # open first sheet of each workbook by name and return records from it
    for workbook in sheets:
        sheet = client.open(workbook).sheet1
        uni = sheet.get_all_records()
        data.extend(uni)
    return data


def analyse_students_merge(path, ukrainian):
    """
    str, list -> plotly line graphs
    Merges data from API and data from databases to analyse
    students' depression, doctor and suicide parameters.
    """
    # read data from csv file to pandas data frame
    with open(path, "r", encoding="utf-8") as file:
        data = pd.read_csv(file, usecols=["Age", "Dep", "Doctor", "Suicide"]).to_dict(
            orient="records")

    data.extend(ukrainian)

    #create an analyser for all the students
    student_analyser = PsyStudentAnalyser()
    for record in data:
        if str(record["Age"]) != "nan":
            record["Dep"] = 1 if str(record["Dep"]) in ["Yes", "1"] else 0
            record["Doctor"] = 1 if record["Doctor"] != 0 else 0
            record["Suicide"] = 1 if str(record["Suicide"]) in [
                "Yes", "1"] else 0
            student = Student(age=int(
                record["Age"]), depression=record["Dep"], suicide=record["Suicide"], doctor=record["Doctor"])
        student_analyser.add_person(student)

    df_dep = pd.DataFrame(sorted(student_analyser.get_depression(
    ).get_df_for_line(), key=lambda t: t[0]), columns=["age", "depression%"])
    figure_dep = px.line(df_dep, x="age", y="depression%")

    df_doc = pd.DataFrame(sorted(student_analyser.get_doctor().get_df_for_line(
    ), key=lambda t: t[0]), columns=["age", "doctor visits%"])
    figure_doc = px.line(df_doc, x="age", y="doctor visits%")

    df_sui = pd.DataFrame(sorted(student_analyser.get_suicide().get_df_for_line(
    ), key=lambda t: t[0]), columns=["age", "suicide attempts%"])
    figure_sui = px.line(df_sui, x="age", y="suicide attempts%")

    return figure_dep, figure_doc, figure_sui


def analyser_ukrainian_students(ukrainian):
    """
    list -> PsyStudentAnalyser
    Returns Analyser to analyse Ukrainian students mental health.
    """
    # create an analyser for all the students:
    ukrainian_analyser = PsyStudentAnalyser()
    for student in ukrainian:
        new_student = Student(age=student["Age"], depression=student["Dep"],
                              anxiety=student["anxiety"],
                              suicide=student["Suicide"],
                              doctor=student["Doctor"],
                              study=student["study"],
                              suicidal_thoughts=student["suicidal_thoughts"],
                              self_harm=student["self_harm"],
                              dep_diagnosed=student["dep_diagnosed"],
                              behavior=student["behavior"],
                              anx_diagnosed=student["anx_diagnosed"],
                              list_dep=student["list_dep"].split(", "),
                              list_anx=student["list_anx"].split(", "))
        ukrainian_analyser.add_person(new_student)
    return ukrainian_analyser


def analyse_ukrainian(ukrainian_analyser):
    """
    PsyStudentAnalyser -> plotly diagrams.
    Returns pie and line diagrams for possible parameters
    of ukrainian students.
    """
    # study
    pie_study = px.pie(pd.DataFrame(ukrainian_analyser.get_study(
    ).get_df_for_pie(), columns=["students"]),
        values="students")

    # suicidal_thoughts
    pie_suicidal_thoughts = px.pie(pd.DataFrame(ukrainian_analyser.get_suicidal_thoughts(
    ).get_df_for_pie(), columns=["students"]),
        values="students")

    # self_harm
    pie_self_harm = px.pie(pd.DataFrame(ukrainian_analyser.get_self_harm(
    ).get_df_for_pie(), columns=["students"]),
        values="students")

    # dep_diagnosed
    pie_dep_daignosed = px.pie(pd.DataFrame(ukrainian_analyser.get_dep_diagnosed(
    ).get_df_for_pie(), columns=["students"]),
        values="students")

    # behavior
    pie_behavior = px.pie(pd.DataFrame(ukrainian_analyser.get_behavior(
    ).get_df_for_pie(), columns=["students"]),
        values="students")

    # anx_diagnosed
    pie_anx_diagnosed = px.pie(pd.DataFrame(ukrainian_analyser.get_anx_diagnosed(
    ).get_df_for_pie(), columns=["students"]),
        values="students")

    # list_dep
    df_list_dep = pd.DataFrame(sorted(ukrainian_analyser.get_list_dep().get_df_for_line(
    ), key=lambda t: t[0]), columns=["disorder", "%"])
    line_list_dep = px.line(df_list_dep, x="disorder", y="%")

    # list_anx
    df_list_anx = pd.DataFrame(sorted(ukrainian_analyser.get_list_anx().get_df_for_line(
    ), key=lambda t: t[0]), columns=["disorder", "%"])
    line_list_anx = px.line(df_list_anx, x="disorder", y="%")

    return pie_study, pie_suicidal_thoughts, pie_self_harm, pie_dep_daignosed, \
        pie_behavior, pie_anx_diagnosed, line_list_dep, line_list_anx


def get_countries_data(path_percent, path_total, col):
    """
    str, str, str -> plotly diagram
    Returns line diagram based on files that contain
    name of the country, percent of people suffering from d/o's
    and total population of the country for every year.
    """
    # read data from csv file to pandas data frame
    with open(path_percent, "r", encoding="utf-8") as file:
        data = pd.read_csv(file, usecols=["Entity", "Year", col]).to_dict(
            orient="records"
        )
    with open(path_total, "r", encoding="utf-8") as file:
        data_total = pd.read_csv(
            file, usecols=["Entity", "Year", "Population"]).to_dict(orient="records")
    
    for record in data:
        record["cy"] = record["Entity"] + str(record["Year"])
    
    cy = dict()
    for record in data_total:
        cy[record["Entity"] + str(record["Year"])] = record["Population"]
    
    result = []
    result_world = []
    for record in data:
        if record["cy"] in cy:
            record["Population"] = cy[record["cy"]]
            record["Number of ill"] = record["Population"] * record[col] / 100
            if record["Entity"] != "World":
                result.append(record)
            else:
                result_world.append(record)
    
    df = pd.DataFrame(result, columns=["Entity", "Year", "Number of ill"])
    figure = px.line(df, x="Year", y="Number of ill",
                      color="Entity", line_group="Entity", hover_name="Entity")

    df_world = pd.DataFrame(result_world, columns=["Entity", "Year", "Number of ill"])
    figure_world = px.line(df_world, x="Year", y="Number of ill")
    
    return figure, figure_world
