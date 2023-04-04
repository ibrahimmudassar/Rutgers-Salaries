# Rutgers Salaries

## Overview
### Treemap of All Salaries > 500k
![Treemap of All Salaries > 500k](/images/Treemap%20Salaries%20More%20Than%20500k.png)

### Frequency of All Salaries 
![Frequency of All Salaries](/images/Histogram%20All.png)

### Boxplot of All Salaries Sorted by Campus
![Boxplot of All Salaries Sorted by Campus](/images/Boxplot%20By%20Campus%20All.png)

### Boxplot of Professor Salaries Sorted by Campus
![Boxplot of Professor Salaries Sorted by Campus](/images/Boxplot%20By%20Campus%20Professors%20Only.png)

## Conclusions

[This data can be viewed here](https://ibrahimmudassar.github.io/Rutgers-Salaries/)

* Some of the departments that are most well paid are at the NJ Medical School and Robert Wood Johnson
* Other well paid departments include Mens Basketball and Football

## Collection

This data was scraped from [DataUniverse - Asbury Park Press](https://content-static.app.com/datauniverse/caspio/bundle/Rutgers_salaries.html)

You can find how I did it in [rutgers_salaries_async.py](/rutgers_salaries_async.py)
* This takes ~300 seconds to run
* Creates a .csv file that is ~25k lines
* Includes Name, Campus, Department, and Total Pay

## Graphing
Used Python Plotly code is viewable in [main.py](/main.py)

## Other Graphs
![Rutgers New Brunswick Salaries Sorted by Department](/images/rutgers_salaries_by_depart.png)
