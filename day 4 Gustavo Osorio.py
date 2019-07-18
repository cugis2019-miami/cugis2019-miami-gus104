import pandas
import plotly
dir(pandas)
dir(plotly)


student = [["Steve",32,"male"],["Lia",28,"female"],["Vin",45,"male"],["Katie",38,"female"]]
studentdf = pandas.DataFrame(student, columns = ["Name","Age","Gender"], index = ["First","Second","Third","Fourth"])

print(studentdf)

from plotly.offline import plot

agename = plotly.graph_objs.Bar(x=studentdf["Name"], y=studentdf["Age"])
plot([agename])


#reading data files into python
import pandas as pd
from plotly.offline import plot
import plotly.graph_objs as go


#We read the data into a dataset or data frame called df
df = pd.read_excel("GISdata.xlsx", sheet_name = "cancercases",marker = {"color": cancercasesdf["CancerType"], "colorscale" : "Portland"})
#source:Bureau of Labor Statistics

#We use the bar graph option of the graph_objs function from the plotly library
cancercases = go.Bar(x= df["CancerType"], y=df["Number"],)

#we call the plot function from the plotly.offline library
plot([cancercases])

#or we use figure option of the graph_objs function from the plotly library
fig = go.Figure(data=[cancercases])

plot(fig)

#we use the layout option of the graph_objs function from the plotly library
titles = go.Layout(
                    #Define title of the graph
                    title = "Amount of Women With Cancer in 2018",
                    
                    #define title for x-axis
                    xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="CancerType",
                        )
                    ),
                    
                    #Define title for y-axis
                    yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Number",
                            )
                        )
                    )

fig = go.Figure(data=[cancercases], layout = titles)

plot(fig)



#presenting your project

#introduction/condext: setting the stage 

#objective of your project: what is the purpose of your project

#methodology/approach: what methods or tools did you use to help you achieve your objective?

#results: make sure to interpret your results
































































































