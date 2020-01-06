# Live-Forex-Tracker
Tracks Live Forex Prices and Displays in Desktop App

Provides a destop application based overview of current Forex GBP - USD prices (although this is configurable).

Uses BeautifulSoup to scrape the data and save locally as a json file. 
Pandas parses json into a DataFrame object where data is manipulated.
Matplotlib is used to plot the data.
Tkinter displays the plot within a desktop app.

Data is refreshed every ten seconds to give rolling overview of currency prices.
