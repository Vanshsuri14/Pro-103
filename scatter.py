import pandas as pd
import plotly.express as px

df = pd.read_csv("covid.csv")
scatter_graph = px.scatter(df,x = "date",y = "cases",title = "Covid Cases of different Countries",color = "country")
scatter_graph.show()

