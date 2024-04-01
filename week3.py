import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from urllib.request import urlopen
import json

data = pd.read_csv("/content/Police_Department_Incident_Reports__Historical_2003_to_May_2018_20240221.csv")

data_num=data.shape[0]

import plotly.express as px
filtered_df = data[(data["DayOfWeek"] == "Sunday") & (data["Category"] == "VEHICLE THEFT")]
filtered_df.head()
data_num = filtered_df.shape[0]
df_num=data.shape[0]
# 输出结果
print(df_num)
print(data_num)

theft_counts_by_district = filtered_df.groupby("PdDistrict").size().to_frame(name="Thefts")
theft_counts_by_district["Theft Rate"] = theft_counts_by_district["Thefts"] / theft_counts_by_district["Thefts"].sum() * 100
theft_counts_by_district = theft_counts_by_district.reset_index()
theft_counts_by_district.head()



with urlopen('https://raw.githubusercontent.com/suneman/socialdata2022/main/files/sfpd.geojson') as response:
    geojson_data = json.load(response)

fig = px.choropleth_mapbox(
    theft_counts_by_district,
    geojson=geojson_data,
    locations="PdDistrict",
    color="Thefts",
    mapbox_style="carto-positron",
    zoom=10,
    center={"lat": 37.7749, "lon": -122.4194},
    title="The number of vehivle in different district on sunday",
    labels={"Thefts": "Theft number"}
)

fig.show()
