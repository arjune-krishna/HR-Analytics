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

## Objective
### Department Page - (Page 1)
> <b>"Select a Department" Dropdown Menu:</b>
We're presented with the option to select the department for analysis from a list of departments in the organizations.
- `Customer Service`
- `Development`
- `Finance`
- `Human Resources`
- `Marketing`
- `Production`
- `Quality Management`
- `Research`
- `Sales`

> <b>Active Employees:</b> Gives us the total number of active employees in the organization

> <b>Median Salary:</b> Calculates the median salary of all the employees in the department

> <b>Department Salary in %:</b> `(Total Salary Paid to All The Employees in the Department / Total Salary) * 100`

> <b>Employees Gender (in %):</b> % of Male and Female Employees in the Department ("Doughnut Chart")

> <b>Average Hike vs Working Year:</b> YoY Average Hike in Salary of all the Employees in the Department ("Line Chart")

> <b>Churn Rate per Year:</b> % of Employees churning each year. ("Line Chart")

> <b>Employee's Experience When Churned:</b> Average Employees Experience (in yrs) when churned. ("Bar Chart")

</br>

### Employee Page - (Page 2)
> <b>"Enter a Employee Number" Input field:</b> We can enter a employee number
- `Employees number range between 10001 and 499999`

> <b>Name:</b> Name of the employee

> <b>Gender:</b> Gender of the employee

> <b>Department:</b> Department of the employee

> <b>Date of Birth:</b> Date of Birth of the employee

> <b>Current Salary:</b> Current Salary of the employee

> <b>Salary Chart:</b> Employee's salary YoY ("Line Chart")

> <b>Employee's Work History:</b> List of all the departments where the employee worked previously with their respective from and to dates.
- `Department Name `
- `From`
- `To`

> <b>Employee's Salary Records:</b> List of all the salary records of the employee since joining the organization and YoY Hike.
- `Salary` 
- `From`
- `To`
- `Salary Growth`
- `Salary Growth in %`



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
> **Departments Page**
- ![Dashboard Screenshot](https://i.ibb.co/VYGGhHd/screencapture-arjune-krishna-hr-analytics-main-gu5bi5-streamlitapp-2022-09-29-22-18-43.png)
> **Employees Page**
- ![Dashboard Screenshot 2](https://i.ibb.co/7pjPJ1F/screencapture-arjune-krishna-hr-analytics-main-gu5bi5-streamlitapp-Employees-2022-10-01-12-37-34.png)

## Author
- <b> Arjune Krishna TS </b>
- <b> LinkedIn </b> - https://www.linkedin.com/in/arjune-krishna/
- <b> Twitter </b> - https://twitter.com/bce3227
