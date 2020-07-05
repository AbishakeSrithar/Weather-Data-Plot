# Data visualisation project. I used the MET's data, recorded at Heathrow, to plot a visualisation
# of temperatures over the last 70 years. Guided by the Project 2 section of Python Crash Course
# by Eric Matthes.

import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Downloaded from https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/heathrowdata.txt
# Manually got rid of the top paragraph when saving .txt. Could call next(reader) 5 more times instead.
filename = 'data/heathrowdata.txt'
outfile = 'data/heathrowdata2.txt'

with open(filename) as h, open(outfile, 'w') as out:
	reader = csv.reader(h)
	header_row = next(reader)
	# Split function with no arguements uses white space as seperation point. 
	print(header_row[0].split())
	# Skips the line with the units of measurements.
	second_row = next(reader)
	# Writes our data in comma seperated value form into a new text document.
	o=csv.writer(out)
	
	for line in h:
		o.writerow(line.split())

with open(outfile) as h:
	reader = csv.reader(h)
	# Store values needed for plot.
	date, highs, lows = [], [], []

	for row in reader:
		# Combines the first 2 elements of each row to give %Y-%m format.
		combine_date = f"{row[0]}-{row[1]}"
		current_date = datetime.strptime(combine_date, '%Y-%m')
		date.append(current_date)
		highs.append(float(row[2]))
		lows.append(float(row[3]))
		# Skips the empty line.
		x = next(reader)

	plt.style.use('dark_background')
	fig, ax = plt.subplots()
	ax.plot(date, highs, c='red')
	ax.plot(date, lows, c='blue')

	ax.set_title('Monthly High/Low Mean Temperatures', fontsize=18)
	ax.set_xlabel('Year', fontsize=14)
	ax.set_ylabel('Temperature (C)', fontsize=16)
	ax.tick_params(axis='both', which='major', labelsize=12)

	plt.show()

