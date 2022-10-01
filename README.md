## Interactive HR Analytics Dashboard with Python – Streamlit
Analytics dashboard built with Python and Streamlit.

Live - https://arjune-krishna-hr-analytics-main-gu5bi5.streamlitapp.com/



## Project Organization
```
.
├── streamlit/                              : App layout
│   └── config.toml
├── DB/                                     : DB Files
│   ├── employees-mod-db.pdf
│   ├── employees.sql
│   ├── employees_db_to_csv.py
│   └── employees_mod.sql
├── pages/                                  : Employees Page(streamlit)
│   └── Employees.py
├── departments.csv                         : List of all the departments data
├── dept_emp.csv                            : Employees and departments data
├── dept_manager.csv                        : Managers and departments data
├── employees.csv                           : Employees data
├── main.py                                 : Main Page (streamlit)  
├── requirements.txt                        : Requirements (all the necessary packages and modules)
├── salaries.csv                            : Employees Salaries data
├── titles.csv                              : Employees Titles data
└── README.md                               : Report
```

## Business Objective:
<b>Build an interative dashboard for HR department.</b> </br>
</br>
<b>Key Metrics to Report</b>
* Active Employees
* Median Salary
* Department Manager
* Employees Gender (in %)
* Average Hike vs Working Year
* Churn Rate per Year
* Employee's Experience When Churned

## Data provided:
* Employees DB file with the following table schema
![DB Schema](https://i.ibb.co/k4NpHm4/Screenshot-4.png)

## Steps:
* Dumped the DB file to MySQLWorkbench.
* `my-sql-connector` to pull data from DB and convereted it to csv files.
* Python for data cleaning 
* Plotly for Charts
* Streamlit for Deployment.

## Libraries primarily used:
* `streamlit`
* `plotly`
* `pandas`

## Screenshot
![Dashboard Screenshot](https://i.ibb.co/VYGGhHd/screencapture-arjune-krishna-hr-analytics-main-gu5bi5-streamlitapp-2022-09-29-22-18-43.png)
![Dashboard Screenshot 2](https://i.ibb.co/ySR668D/screencapture-arjune-krishna-hr-analytics-main-gu5bi5-streamlitapp-Employees-2022-09-29-22-17-12.png)

## Author
- <b> Arjune Krishna TS </b>
- <b> LinkedIn </b> - https://www.linkedin.com/in/arjune-krishna/
- <b> Twitter </b> - https://twitter.com/bce3227
