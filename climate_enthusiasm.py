# https://blog.mafr.de/2012/12/30/matplotlib-bar-diagrams/
# https://software-carpentry.org/blog/2012/05/an-exercise-with-matplotlib-and-numpy.html
# https://matplotlib.org/2.1.2/gallery/ticks_and_spines/date_index_formatter.html
# https://stackoverflow.com/questions/47298022/fixing-date-labels-when-plotting-bar-chart-of-resampled-pandas-time-series-data

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

student_data = {
    "10-01-2019":  3000,
    "17-01-2019": 12500,
    "24-01-2019": 35000
}

people_data = {
    "30-11-2015": 60,
    "06-12-2015": 14000,
    "02-12-2018": 65000,
    "27-01-2019": 70000
}

student_dates = [dt.datetime.strptime(d, '%d-%m-%Y') for d in student_data.keys()]
people_dates = [dt.datetime.strptime(d, '%d-%m-%Y') for d in people_data.keys()]
plt.bar(student_dates, student_data.values(), label='Students')
plt.bar(people_dates, people_data.values(), label='People')

hfmt = mdates.DateFormatter('%d-%m-%Y')

#plt.bar(range(len(student_data)), list(student_data.values()), color='b', align='center')
#plt.xticks(range(len(student_data)), list(student_data.keys()))
# plt.bar(range(len(people_data)), list(people_data.values()), color='g', align='center')
# plt.xticks(range(len(people_data)), list(people_data.keys()))

# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
# plt.gca().xaxis.set_major_locator(mdates.DayLocator())
# plt.gcf().autofmt_xdate()

plt.ylabel('Number of students/people')
plt.title('Belgian climate enthusiasm in numbers')

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.xaxis.set_major_formatter(hfmt)
plt.show()
