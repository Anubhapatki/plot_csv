import pandas
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mpld3

data = pandas.read_csv('/Downloads/Sensorlogs_latest.txt',
                       names=['Time', 'timestamp2','devicename', 'attr1','attr2', 'attr3', 'attr4', 'attr5'],
                       header=None)

new = data['devicename'].str.split(':', n=1, expand= True)
data['device'] = new[1]
data['Temp'] = data['attr5'].apply(lambda x: int(x, base=16)/100)
data['Time'] = pandas.to_datetime(data['Time'])


myFmt = mdates.DateFormatter("%d/%m-%H:%M")
fig, ax = plt.subplots(figsize=(15,7))
ax.grid(True)
print (data['device'].unique())
print (data['Time'])


ax.set_ylabel('Temp in degree celsius')
ax.set_xlabel('Time - (Format:Date-HR:Min')
ax.xaxis.set_major_locator(mdates.HourLocator(interval=5))
ax.xaxis.set_major_formatter(myFmt)
fig.autofmt_xdate(rotation=25)


lns=[]
for device in data['device'].unique():
    data[data['device'] == device].plot(x='Time', y='Temp', ax=ax, label=device)


handles, labels = ax.get_legend_handles_labels() # return lines and labels
interactive_legend = mpld3.plugins.InteractiveLegendPlugin(handles, labels)
mpld3.plugins.connect(fig, interactive_legend)
mpld3.show()



