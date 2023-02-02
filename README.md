# Rutgers Salaries

## Overview
### Frequency of All Salaries 
![Frequency of All Salaries](/images/Histogram%20All.png)

### Boxplot of All Salaries Sorted by Campus
![Boxplot of All Salaries Sorted by Campus](/images/Boxplot%20By%20Campus%20All.png)

### Boxplot of Professor Salaries Sorted by Campus
![Boxplot of Professor Salaries Sorted by Campus](/images/Boxplot%20By%20Campus%20Professors%20Only.png)

## Collection

This data was scraped from [DataUniverse - Asbury Park Press](https://content-static.app.com/datauniverse/caspio/bundle/Rutgers_salaries.html)

You can find how I did it in [rutgers_salaries_async.py](/rutgers_salaries_async.py)
* This takes ~300 seconds to run
* Creates a .csv file that is ~25k lines
* Includes Name, Campus, Department, and Total Pay

## Graphing
Used Python Plotly code is viewable in [main.py](/main.py)
