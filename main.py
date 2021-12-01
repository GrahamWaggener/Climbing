import plotly.express as px
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv("r2.csv")
    states = list()
    for i in range(len(df['Location'])):
        state = df['Location'][i].split('>')
        states.append(state[-1])
    df['states'] = states
    df['displays'] = df['Route'] + ' , ' + df['Rating'] + ' , ' + df['states']
    fig = px.scatter_geo(df,lat='Lat',lon='Lon', hover_name='displays')
    fig.update_layout(title = 'World map', title_x=0.5)
    fig.show()