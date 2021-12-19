import plotly.express as px #For interactive map functionality
import pandas as pd #For reading the CSV file

if __name__ == '__main__':
    df = pd.read_csv("routes2.csv") #Creates a dataframe of the climbing routes from mountainproject.com
    states = list()
    for i in range(len(df['Location'])):
        state = df['Location'][i].split('>')
        states.append(state[-1])
    df['states'] = states #Adds a new column of the state to the dataframe of the last item in the location data
    df['displays'] = df['Route'] + ' , ' + df['Rating'] + ' , ' + df['states'] #Combining the route name, rating, and state
    fig = px.scatter_geo(df,lat='Lat',lon='Lon', hover_name='displays') #Plots the locations on a map with data when hovered over
    fig.update_layout(title = 'Climbing Routes', title_x=0.5)
    fig.show()