import pandas as pd
import plotly.graph_objs as go
df = pd.read_csv('Morocco-2022.csv')
print(df.shape)
print(df.head(10))
#asign the the columns to variables in order to get the age in the Y axis and gender in the x axis
y=df['Age']
x1=df['M']
x2=df['F']*-1

#create the instance of the figure
fig = go.Figure()
#add trace to figure and specify the type of the chart
fig.add_trace(go.Bar(
    y=y,
    x=x1,
    name='MALE',
    orientation='h'
))
#add trace to the figure the female part

fig.add_trace(go.Bar(
    y=y,
    x=x2,
    name='FEMALE',
    orientation='h'
))

#update the figure layout
fig.update_layout(
    template='plotly_white',
    title='Population Pyramid Morocco 2022',
    title_font_size=24,
    barmode='relative',
    bargap=0.0,
    bargroupgap=0,
    xaxis=dict(
        tickvals=[-1500000,-1000000,-500000,0,500000,1000000,1500000],
        ticktext=['1.5M','1M','0.5M','0','0.5M','1M','1.5M'],
        title='Population',
        title_font_size=14
    )
)

#plot the chart
fig.show()