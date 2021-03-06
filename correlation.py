import plotly.express as px
import csv
import numpy as np

def plot_graph(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Days Present", y="Marks In Percentage")
        fig.show()

def get_datasource(data_path):
    mark_percentage = []
    days_present = []

    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        for a in df:
            mark_percentage.append(float(a["Marks In Percentage"]))
            days_present.append(float(a["Days Present"]))

    return {
        "x" : mark_percentage, 
        "y": days_present
    }

def corr(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days present :-  \n--->",correlation[0,1])

def main():
    data_path  = "data_2_corr.csv"
    datasource = get_datasource(data_path)
    corr(datasource)
    plot_graph(data_path)

if __name__ == '__main__':
    main()