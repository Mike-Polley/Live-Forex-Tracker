import matplotlib.animation as animation
from matplotlib import style
import reader as rd
import scraper as sc
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import matplotlib.pyplot as plt

style.use('ggplot')
f = Figure (figsize=(5,4),dpi=100)
a = f.add_subplot(111)
reader = rd.reader()


def animate(i):
	scraper = sc.scraper()
	site = scraper.scrapeWebsite('https://www1.oanda.com/currency/live-exchange-rates/')
	parsed = scraper.parserHTML(site)
	scraper.writer(parsed,'data.json')
	df = reader.readFile('data.json')
	newDF = reader.createData(df)
	a.clear()
	max = newDF[['GBP_USD']].max()
	min = newDF[['GBP_USD']].min()
	a.set_title('Current $ to £ Exchange Rates')
	newDF.plot(kind='line',x='TIME',y='GBP_USD',ax=a,ylim=[1.30,1.32])

root = tk.Tk()
canvas = FigureCanvasTkAgg(f,root)
canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)

	
ani = animation.FuncAnimation(f,animate, interval=10000)
root.mainloop()
