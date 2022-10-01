## HR Analytics Dashboard with Python – Streamlit
In this project, I've analyzed the data of employees, managers, titles and their respective salaries, departments in the organization and built a dashboard to display key metrics for the HR department.

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

## HR Analytics:

Human resources (HR) is the division of a business that is charged with finding, screening, recruiting, and training job applicants. It also administers employee-benefit programs.

HR plays a key role in helping companies deal with a fast-changing business environment and a greater demand for quality employees in the 21st century.

I've built a dashboard for the HR department where they can get a summary of each department and each employee in the organization.

<b>Objective</b>
</br>
1. Department Page
    - Active Employees 
    - Median Salary 
    - Department Salary in % 
    - Employees Gender (in %) 
    - Average Hike vs Working Year 
    - Churn Rate per Year 
    - Employee's Experience When Churned 

2. Employee Page
    - Name 
    - Gender 
    - Department 
    - Date of Birth 
    - Current Salary 
    - Salary Chart 
    - Employee's Work History 
    - Employee's Salary Records 



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
