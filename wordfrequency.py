import dash
import csv
import random
import pandas as pd
from dash.dependencies import Input,Output,State
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader as dr
import datetime


def wordcount(filename, listwords):
    count = 0
    try:
        file = open(filename, "r")
        read = file.readlines()
        file.close()

        for word in listwords:
            lower = word.lower()


            for sentence in read:
                line = sentence.split()
                for each in line:
                    line2 = each.lower()
                    line2 = line2.strip("!@#$%^&*()_+=-[]\';/.,<>?:{}|")
                    if lower == line2:
                        count += 1

            #print(filename, ":", count)

    except FileExistsError:
        print("no file")
    return count







csv_file=pd.read_csv('data1.csv')
x=csv_file.iloc[:,:].values
xaxis=[]
yaxis=[]
c=[]
for row in x:
    xaxis.append(row[0])
    yaxis.append(row[1])

app=dash.Dash()

colors={
    'background':'#111111',
    'text':'#7ffaff'
}
app.layout=html.Div(style={'backgroundColor':colors['background']},children=[
        html.H1("Word Frequency Analyzer",style={'textAlign':'center','color':colors['text']}),
        html.H2("Enter the word",style={'font_size': 10,'color':colors['text']}),
        dcc.Input(id='input', value='', type='text'),
        dcc.Input(id='input2',value='',type='text'),
        html.Button(id='searchbutton',n_clicks=0,children='search'),
        html.Div(id='outputgraph')

    ]
)
@app.callback(
    Output(component_id='outputgraph',component_property='children'),
        [Input('searchbutton','n_clicks')],
        [State(component_id='input',component_property='value'),
         State(component_id='input2',component_property='value')
         ]


)
def update_graph(n_clicks,input_data,input_data2):
    # start = datetime.datetime(2015, 1, 1)
    #end = datetime.datetime(2018, 2, 8)
    #df = dr.data.get_data_yahoo(input_data, start, end)
    #df2=dr.data.get_data_yahoo(input_data2,start,end)
    #'x':df.index,'y':df.Close
    list=["2012.txt","2013.txt","2014.txt","2015.txt","2016.txt",]
    a=[]
    b=[]
    yr=[2012,2013,2014,2015,2016]
    for line in list:
        a.append(wordcount(line,input_data))
    for line1 in list:
        b.append(wordcount(line1,input_data2))
    print(a)
    print(b)

    return dcc.Graph(id='example',figure={'data':[{'x':yr,'y':a,'type':'line','name':input_data},
                                                  {'x':yr,'y':b,'type':'line','name':input_data2}
                                               ],
                                       'layout':{'title':'The Frequency of {} vs {}'.format(input_data,input_data2),
                                                 'plot_bgcolor':colors['background'],
                                                 'paper_bgcolor':colors['background'],

                                                 'font':{'color':colors['text']},
                                                 'xaxis': {
                                                     'title': 'Year'
                                                 },
                                                 'yaxis': {
                                                     'title': 'Number of words per year'
                                                 }
                                                 }


                                       }

                  )


if __name__=="__main__":
    app.run_server(debug=True)
