with open('/home/rakshith/Desktop/CHAOSCT/adver/arch1_waac.json') as json_file:  
    data = json.load(json_file)
    psnr,bpp=[],[]
    new_bpp=[]
    mean_x,mean_y=[],[]
    
    
    for p in data:
        psnr.append(p['psnr'])
        bpp.append((p['bpp']))
        
    for row in bpp:

        row[:]=([16 / x for x in row])
        new_bpp.append(row[:])

    
    i=0

    while(i<len(psnr)):

        mean_y.append(statistics.mean(psnr[i]))
        mean_x.append(statistics.mean(new_bpp[i]))
        i=i+1
        
    trace0 = go.Scatter(
    x = mean_x,
    y = mean_y,marker={'symbol': 'star', 'size': 10},
    mode = 'lines+markers',
    name = 'Arch1')
    
data=[trace0]
layout = go.Layout(
xaxis=dict(
    type='log'
    )
)
fig = dict(data=data,layout=layout)
plotly.offline.iplot(fig, filename='Mean_graph')
