from flask import Flask, render_template
import pandas as pd
import time

app = Flask(__name__)
data = pd.read_csv("data/data.csv")


@app.route('/', methods=["GET", "POST"])
def index(chart1ID='chart1_ID', chart1_type='bar',
          chart2ID='chart2_ID', chart2_type='bar',
          chart3ID='chart3_ID', chart3_type='column',
          chart4ID='chart4_ID',
          chart5ID='chart5_ID', chart5_type='bar',
          chart6ID='chart6_ID', chart6_type='column'):
    # Chart1
    maleCount = data[data['Gender'] == 'M']["Gender"].count()
    femaleCount = data[data['Gender'] == 'F']["Gender"].count()
    total = maleCount + femaleCount
    malePercentage = ((maleCount / total) * 100).round(2)
    femalePercentage = ((femaleCount / total) * 100).round(2)

    chart1 = {"renderTo": chart1ID, "type": chart1_type}
    series1 = [{"name": 'Male', "data": [malePercentage], "color": "#00FFFF"},
               {"name": 'Female', "data": [femalePercentage], "color": "#DC143C"}]
    title1 = {"text": 'Male vs Female Ratio'}
    xAxis1 = {"categories": ['Gender']}
    yAxis1 = {"title": {"text": 'Percentage (%)'}}
    plotOptions1 = {"bar": {"stacking": "normal", 'dataLabels': {'enabled': 'true'}}}
    tooltip1 = {"borderRadius": "20"}
    credits = {"text": 'Made by VARUN NAGRARE', "href": 'https://www.facebook.com/Wolvarun9295',
               "style": {"fontSize": '10px', 'color': "#FF0000"}}

    ###################################################################################################################
    # Chart2
    python = []
    automation = []
    nodejs = []
    java = []
    ios = []
    devops = []
    de = []
    ml = []

    python.append(data[data['Technology'] == 'Python']["Technology"].count())
    automation.append(data[data['Technology'] == 'Automation']["Technology"].count())
    nodejs.append(data[data['Technology'] == 'NodeJs']["Technology"].count())
    java.append(data[data['Technology'] == 'Java']["Technology"].count())
    ios.append(data[data['Technology'] == 'IOS']["Technology"].count())
    devops.append(data[data['Technology'] == 'DevOps']["Technology"].count())
    de.append(data[data['Technology'] == 'Data Engineering']["Technology"].count())
    ml.append(data[data['Technology'] == 'Machine Learning']["Technology"].count())

    chart2 = {"renderTo": chart2ID, "type": chart2_type}
    series2 = [
        {"name": 'Automation', "data": automation, "color": "#FF8000"},
        {"name": 'Data Engineering', "data": de, "color": "#CD00FF"},
        {"name": 'DevOps', "data": devops, "color": "#0027FF"},
        {"name": 'IOS', "data": ios, "color": "#00FFFF"},
        {"name": 'Java', "data": java, "color": "#74FF00"},
        {"name": 'Machine Learning', "data": ml, "color": "#FF00A2"},
        {"name": 'NodeJS', "data": nodejs, "color": "#FFF300"},
        {"name": 'Python', "data": python, "color": "#FF0000"},
    ]
    title2 = {"text": 'Techwise Bar Chart'}
    xAxis2 = {"categories": ['Technology']}
    yAxis2 = {"title": {"text": 'No. of People'}}
    plotOptions2 = {"bar": {'dataLabels': {'enabled': 'true'}}}

    ###################################################################################################################
    # Chart3
    labX = data[data['Lab'] == 'Bangalore']['Lab'].count()
    labY = data[data['Lab'] == 'Mumbai']['Lab'].count()
    chart3 = {"renderTo": chart3ID, "type": chart3_type, "polar": "true", "inverted": "true"}
    series3 = [{"name": 'Bangalore', "data": [labX], "color": "#B500FE"},
               {"name": 'Mumbai', "data": [labY], "color": "#00FE7B"}]
    title3 = {"text": 'Distribution of People in Lab X and Y'}
    xAxis3 = {"categories": ['LAB']}
    yAxis3 = {"crosshair": {"enabled": "true", "color": "#333"}}
    plotOptions3 = {"column": {'dataLabels': {'enabled': 'true'}}}
    pane3 = {"size": "85%", "innerSize": "20%", "endAngle": "300"}

    ###################################################################################################################
    # Chart4
    technology = []
    people = []
    for i in data.Technology.unique():
        technology.append(i)
        people.append(data[data['Technology'] == i]["Technology"].count())
    chart4 = {"renderTo": chart4ID}
    series4 = [{"type": "areaspline", "name": 'Technologies (Areaspline Chart)', "data": people, "color": "#FF1493"},
               {"type": "column", "name": 'Technologies (Column Chart)', "data": people, "color": "#006CFE"}]
    title4 = {"text": 'Techwise Distribution Chart'}
    xAxis4 = {"categories": technology}
    yAxis4 = {"title": {"text": 'No. of People'}}
    plotOptions4 = {"areaspline": {'dataLabels': {'enabled': 'true'}}, "column": {'dataLabels': {'enabled': 'true'}}}

    ###################################################################################################################
    # Chart5
    company = []
    for i in data.Company.unique():
        company.append(i)

    company.sort()

    dataFrame = data
    dataFrame.rename(columns={'Unnamed: 0': 'id'}, inplace=True)
    dataFrame = dataFrame[['Technology', 'Company', 'id']]
    techCount = dataFrame.groupby(["Technology", "Company"])["id"].count().unstack(fill_value=0).stack().reset_index(
        name="count")
    techList = techCount["Technology"].unique().tolist()

    finalList = []
    for tech in techList:
        tech = techCount[techCount["Technology"].str.contains(tech)]
        finalList.append(tech)

    automation = finalList[0]['count'].tolist()
    de = finalList[1]['count'].tolist()
    devops = finalList[2]['count'].tolist()
    ios = finalList[3]['count'].tolist()
    java = finalList[4]['count'].tolist()
    ml = finalList[5]['count'].tolist()
    nodejs = finalList[6]['count'].tolist()
    python = finalList[7]['count'].tolist()

    chart5 = {"renderTo": chart5ID, "type": chart5_type}
    series5 = [
        {"name": 'Automation', "data": automation, "color": "#CC00FE"},
        {"name": 'Data Engineering', "data": de, "color": "#006CFE"},
        {"name": 'DevOps', "data": devops, "color": "#FE0068"},
        {"name": 'IOS', "data": ios, "color": "#FE00BD"},
        {"name": 'Java', "data": java, "color": "#00FE45"},
        {"name": 'Machine Learning', "data": ml, "color": "#FEEB00"},
        {"name": 'NodeJS', "data": nodejs, "color": "#FE8300"},
        {"name": 'Python', "data": python, "color": "#FE0000"}
    ]
    title5 = {"text": 'Company vs Technologies Stacked Bar Chart'}
    xAxis5 = {"categories": company, "title": {"text": "Companies"}}
    yAxis5 = {"title": {"text": "No. of People"}}
    plotOptions5 = {"bar": {"stacking": "normal"}}
    tooltip2 = {"borderRadius": "20", "shared": "true"}

    ###################################################################################################################
    # Chart6
    lab = []
    for i in data.Lab.unique():
        lab.append(i)

    dataFrame = data
    dataFrame.rename(columns={'Unnamed: 0': 'id'}, inplace=True)
    dataFrame = dataFrame[['Gender', 'Lab', 'id']]
    sexCount = dataFrame.groupby(["Gender", "Lab"])["id"].count().unstack(fill_value=0).stack().reset_index(
        name="count")
    genderList = sexCount["Gender"].unique().tolist()

    finalList = []
    for sex in genderList:
        sex = sexCount[sexCount["Gender"].str.contains(sex)]
        finalList.append(sex)

    female = finalList[0]['count'].tolist()
    male = finalList[1]['count'].tolist()

    chart6 = {"renderTo": chart6ID, "type": chart6_type, "polar": "true", "inverted": "true"}
    series6 = [{"name": 'Male', "data": male, "color": "#00FFFF"},
               {"name": 'Female', "data": female, "color": "#DC143C"}]
    title6 = {"text": "Distribution of Males and Females in Lab X and Y"}
    xAxis6 = {"categories": lab}
    yAxis6 = {"crosshair": {"enabled": "true", "color": "#333"}}
    plotOptions6 = {"column": {'dataLabels': {'enabled': 'true'}}}
    pane6 = {"size": "85%", "innerSize": "20%", "endAngle": "300"}

    return render_template('index.html',
                           chart1ID=chart1ID, chart1=chart1, series1=series1, title1=title1,
                           xAxis1=xAxis1, yAxis1=yAxis1, plotOptions1=plotOptions1, tooltip1=tooltip1, credits=credits,
                           chart2ID=chart2ID, chart2=chart2, series2=series2, title2=title2, xAxis2=xAxis2,
                           yAxis2=yAxis2, plotOptions2=plotOptions2, tooltip2=tooltip2,
                           chart3ID=chart3ID, chart3=chart3, series3=series3, title3=title3, xAxis3=xAxis3,
                           yAxis3=yAxis3, plotOptions3=plotOptions3, pane3=pane3,
                           chart4ID=chart4ID, chart4=chart4, series4=series4, title4=title4, xAxis4=xAxis4,
                           yAxis4=yAxis4, plotOptions4=plotOptions4,
                           chart5ID=chart5ID, chart5=chart5, series5=series5, title5=title5, xAxis5=xAxis5,
                           yAxis5=yAxis5, plotOptions5=plotOptions5,
                           chart6ID=chart6ID, chart6=chart6, series6=series6, title6=title6, xAxis6=xAxis6,
                           yAxis6=yAxis6, plotOptions6=plotOptions6, pane6=pane6,
                           reload=time.time())


if __name__ == "__main__":
    app.run(debug=True)
