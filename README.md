# Campus Energy Monitoring System

## Project Description

A web application that updates dynamically the data collected
from the smart meters, every 5 minutes, Machine learning is used to predict the future
energy consumption and graphs are displayed which are useful for the administration
department to know about the energy consumption of various blocks in the campus and
also detect anomalies if they exist.

## Process Flow

Smart meters were set up at GNITS in collaboration with IIT-H which are connected to a Raspberry Pi and used to send data that can be stored. The raspberry pi is programmed in such a way that the data is read and synced into dropbox every minute. In dropbox, a new file is created every day at 12:00 with the name as the date. Every minute the data is read from corresponding meters and stored in the file line by line in comma-separated values. The data includes information about time, meter id, power, voltage, and current values. A task is created in the Task scheduler such that it runs a file every 5 minutes.This file contains the code which reads the newly updated data and adds it to the database. This file takes the help of another file, which contains the last read line.The website is created to view and analyze real-time and historic data using the database which is updated every 5 minutes. Machine learning algorithms like regression analysis which predict the output values based on input features from the data fed in the system have been used to predict the future energy consumption. 9 months data has been used for machine learning.LightGBM, short for Light Gradient Boosting Machine which is a distributed gradient boosting framework for machine learning has also been used. It is based on decision tree algorithms and used for ranking, classification and other machine learning tasks. The data collected is analyzed and pre-processed before it is used for model training and testing. The performance of each of the methods is compared based on RMSE metrics.

## Technologies Used: 

* Node.js
* Raspbian OS
* MySQL Server
* Python
* HTML
*  CSS
* Javascript

## Overview of the website

### Microgrid of the campus

Microgrid displays the grid structure which depicts how the different meters are connected to the main meter and how it is connected to the grid. It also shows
the corresponding block of each meter.

<img  src="https://github.com/spurithareddy/CampusEnergyMonitoring/blob/5dc7910aca903b2db81138c33ec0e0e02b73cbd9/Results/microgrid.png" width="595"/>

### Realtime data

Realtime data displays the detailed energy consumption before 5 minutes for the selected meter as wells lets the user visualize the energy consumption with the
help of real-time graphs.

<img  src="https://github.com/spurithareddy/CampusEnergyMonitoring/blob/master/Results/realtimedata.png" width="595"/>

####  Total energy (Cumulation of all meters consumption)

<img  src="https://github.com/spurithareddy/CampusEnergyMonitoring/blob/master/Results/totalenergy.png" width="595"/>

#### Total energy consumption of selected meter

<img  src="https://github.com/spurithareddy/CampusEnergyMonitoring/blob/master/Results/totalofmeter.png" width="595"/>

#### Graph representation of selected meter’s total energy consumption

<img  src="https://github.com/spurithareddy/CampusEnergyMonitoring/blob/master/Results/graphmeter.png" width="595"/>


### Historic Data


Historic data is further divided into meter data of the day, monthly report, day-wise
comparison.

#### Graph representation of Historic data of the selected meter on a selected date

<img  src="https://github.com/spurithareddy/CampusEnergyMonitoring/blob/master/Results/graphhistoric.png" width="595"/>

#### Graph representation of day wise meters total energy consumption 

<img  src="https://github.com/spurithareddy/CampusEnergyMonitoring/blob/master/Results/graph%20daywise.png" width="595"/>

####  Monthly report of selected month

<img  src="https://github.com/spurithareddy/CampusEnergyMonitoring/blob/master/Results/monthlyreport.png" width="595"/>

### User validation to access the Predict Energy page

<img  src="https://github.com/spurithareddy/CampusEnergyMonitoring/blob/master/Results/user%20validatio.png" width="595"/>

### Energy prediction for the selected date and meter

<img  src="https://github.com/spurithareddy/CampusEnergyMonitoring/blob/master/Results/energyprediction.png" width="595"/>

###  Daily energy consumption report sent via Email

<img  src="https://github.com/spurithareddy/CampusEnergyMonitoring/blob/master/Results/emailreport.jpg" width="295"/>




