import plotly.graph_objects as go
import pandas as pd

fig = go.Figure()

fig.update_layout(
    height=450,
    autosize=True,
    margin=dict(t=0, b=0, l=100, r=100),
    #tickfont=dict(size=35, family = "Balto"),
    template="seaborn",
)


def add_trace(fig, x, y, method, visible = False, i = 0):
    fig.add_trace(
       go.Scatter(
          x = x, y = y,  name = method, mode='markers+lines', visible = visible, marker = dict(symbol="circle")
       )
    )
    
x = list(range(1,9))
y1 = [614656, 1229312, 1843968, 2458624, 3073280, 3687936, 4302592, 4917248]
y2 = [1592, 19674794, 39347996, 59021198, 78694400, 104908800, 131123200]

for v, method in [(y1, "FCN"), (y2, "CNN")]:
    add_trace(fig, x, v, method, visible = True)

# Add dropdown
fig.update_layout(
    #title = "Testaccuracy (%): General (Coarses-grained)",
    
    updatemenus=[
        dict(
            buttons=list([
                     dict(label="Linear",  
                          method="relayout", 
                          args=[{"yaxis.type": "linear"}]),
                     dict(label="Log", 
                          method="relayout", 
                          args=[{"yaxis.type": "log"}]),
                                  ]),type="buttons",
            direction="right",
            showactive=True,
            xanchor="left",
            yanchor="top",
            y = 1.15,
            
            
        ),
    ]
)
fig.update_yaxes(title_text = "# parameters", fixedrange = True)
fig.update_xaxes(title_text = "# layers", fixedrange = True)

fig.write_html("plot.html", config = {'displayModeBar': False})