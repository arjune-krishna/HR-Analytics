import streamlit as st
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly.subplots import make_subplots

departments = pd.read_csv('departments.csv')
dept_employees = pd.read_csv('dept_emp.csv')
dept_manager = pd.read_csv('dept_manager.csv')
employees = pd.read_csv('employees.csv')
salaries = pd.read_csv('salaries.csv')
titles = pd.read_csv('titles.csv')

# -----------------------------------------------
#------------------------------------------------

st.set_page_config(page_title='HR Analytics', page_icon='🎯', layout='wide')

# -----------------------------------------------
#------------------------------------------------
#sidebar
# st.sidebar.header("Filters")
# department = st.sidebar.selectbox(
#     "Select a Department:",
#     tuple(departments['dept_name'].unique())
# )

#title
st.title('🎯 HR Analytics')

col1, col2, col3 = st.columns(3)
with col1:
    department = st.selectbox(
        "Select a Department:",
        tuple(departments['dept_name'].unique()))
# st.markdown("")
# st.markdown("")
# -----------------------------------------------
#------------------------------------------------ 
#Salaries of Active Employees   
salaries_active_employees = salaries[salaries['to_date'].astype(str).str.contains('9999')]

#adding department name to department_employees and department_manager tables
dept_employees = dept_employees.merge(departments, left_on='dept_no', right_on='dept_no')
dept_manager= dept_manager.merge(departments, left_on='dept_no', right_on='dept_no')


filtered_df = dept_employees[dept_employees['dept_name'].isin([department])].merge(employees, left_on='emp_no', right_on='emp_no')
#active_employees in the dept
active_employees = filtered_df[filtered_df['to_date'].astype(str).str.contains('9999')].merge(titles, left_on=['emp_no', 'to_date'], right_on=['emp_no', 'to_date'])
#inactive employees in the dept
inactive_employees = filtered_df[~(filtered_df['to_date'].astype(str).str.contains('9999'))].reset_index().drop(['index'], axis=1)

#cleaning active_employees
active_employees.drop(['to_date', 'dept_no'], axis=1, inplace=True)
active_employees.set_axis(['emp_no', 'work_in_dept_from_date', 'dept_name', 'birth_date', 
                         'first_name', 'last_name',	'gender', 'hire_date', 
                         'current_title', 'current_title_from_date'], axis=1, inplace=True)
                    

# -----------------------------------------------
#------------------------------------------------ 


#KPI 
column1, column2, column3 = st.columns(3)
with column1:
    #Active Employees
    active_emp = active_employees.shape[0]
    st.metric(label='✅ Active Employees', value=f"{active_emp}")
with column2:
    #Avg Salary
    avg_salary = round(salaries_active_employees[salaries_active_employees.emp_no.isin(active_employees['emp_no'].unique())]['salary'].median(),2)
    st.metric(label='💰 Median Salary', value=f"${avg_salary}")
with column3:
    #department_salary_percent
    total_salary = salaries_active_employees.salary.sum()
    department_salary = salaries_active_employees[salaries_active_employees.emp_no.isin(active_employees['emp_no'].unique())]['salary'].sum()
    salary_percent = ((department_salary/total_salary)*100).round(2)
    st.metric(label='👤 Department Salary in %', value=f"{salary_percent}%")

st.markdown("---")
# -----------------------------------------------
#------------------------------------------------ 

#Gender Pie Chart
gender = active_employees.gender.value_counts().to_frame().reset_index().set_axis(['gender', 'employees'], axis=1)

#gender of employees in the department - Pie Chart
data = go.Pie(labels=['Male', 'Female'], values=gender['employees'], 
                hole=.4, marker={'colors': ['rgb(12, 102, 254)', 'rgb(179, 207, 255)']},  name='')

fig1 = go.Figure(data)
fig1.update_layout(
        title = "Active Employees: Gender in %",
        title_x=0.5,
        autosize=True,
        paper_bgcolor="#00172B",
        plot_bgcolor="#00172B")

# -----------------------------------------------
#------------------------------------------------

#Avg Hike
salaries = salaries[salaries['emp_no'].isin(active_employees['emp_no'].unique())]

#cleanup from_date column
salaries['from_date'] = pd.to_datetime(salaries['from_date'], format="%d-%m-%Y") 

#applying rank for each employee and their salary hike
salaries['rank'] = salaries.groupby(['emp_no'])['from_date'].rank(ascending=True)

#calculating the diff between the current salary and previous salary
salaries['diff'] = salaries.sort_values(by=['emp_no', 'rank']).groupby(['emp_no'])['salary'].diff()

#creating yoy column
old_salary = (salaries['salary'] - salaries['diff'])
new_salary = salaries['salary']
salaries['yoy'] = round(((new_salary - old_salary)/old_salary)*100, 2)

#avg yoy hike of employees
salaries = salaries.groupby('rank')['yoy'].mean().round(2).to_frame().reset_index().set_axis(['working_period', 'hike'], axis=1).fillna(0)

#plotting
fig2 = go.Figure([go.Scatter(x=salaries.loc[1:]['working_period'], y=salaries.loc[1:]['hike'], 
                            mode='lines+markers', marker={'color': 'rgb(12, 102, 254)'}, 
                            name='', hovertemplate='<br>Year: %{x}<br>Avg Hike: %{y}%<br>')])


fig2.update_layout(
        title = "Average Hike vs Working Year",
        xaxis=dict(title='Working Year', showgrid=False),
        yaxis=dict(title='Hike', showgrid=False),
        title_x=0.5,
        autosize=True,
        paper_bgcolor="#00172B",
        plot_bgcolor="#00172B")


# -----------------------------------------------
#------------------------------------------------

#Churn Rate
##churn rate chart --inactive_employees

#inactive_employees. to_date column cleaning
inactive_employees['to_date'] = pd.to_datetime(inactive_employees.loc[:,'to_date'], format="%d-%m-%Y").to_frame().reset_index().drop(['index'], axis=1)

#year-churned_employees
churn = inactive_employees['to_date'].dt.year.value_counts().to_frame().sort_index().reset_index().set_axis(['year', 'churned_employees'], axis=1)

#hired_employees
hired_employees = pd.to_datetime(filtered_df['hire_date'], format="%d-%m-%Y") \
                    .dt.year.value_counts().sort_index().to_frame().reset_index().set_axis(['year', 'hired_employees'], axis=1)

#joining churned and hired dfs
churn = churn.merge(hired_employees, on='year')

#creating a shift and creating cumilativesum of hired employees
churn['hired_employees'] = churn['hired_employees'].shift()
churn['cum_hired_employees'] = churn['hired_employees'].cumsum()

#yoy churn
churn['yoy'] = ((churn['churned_employees'] / churn['cum_hired_employees'])*100).round(2).fillna(0)


#plotting
fig3 = go.Figure([go.Scatter(x=churn['year'], y=churn['yoy'], mode='lines+markers', marker={'color': 'rgb(12, 102, 254)'}, 
    customdata = churn['yoy'], name='', hovertemplate='<br>Year: %{x}<br>Churn Rate: %{y}%<br>')])


fig3.update_layout(
    title = "Employee Churn Rate",
    xaxis=dict(title='Year', showgrid=False),
    yaxis=dict(title='Churn Rate', showgrid=False),
    title_x=0.5,
    autosize=True,
    paper_bgcolor="#00172B",
    plot_bgcolor="#00172B")

# -----------------------------------------------
#------------------------------------------------
#Avg Exp of Employees when Churned
#experience of employees when churned
exp_when_churned = (pd.to_datetime(inactive_employees['to_date'], format="%d-%m-%Y") - pd.to_datetime(inactive_employees['hire_date'], format="%d-%m-%Y")).dt.days


#exp in yrs when churned
exp_when_churned=(exp_when_churned/365).round(2).to_frame()
#year of churn
exp_when_churned = exp_when_churned.set_axis(['yoe'], axis=1)

#plotting histogram for exp of employees when churned
fig4 = go.Figure(go.Histogram(x=exp_when_churned['yoe'],  xbins=dict(start='0', end='18', size= '1'), customdata=[i for i in range(1,19)],
hoverinfo = ('y'), name='', marker_color='rgb(12, 102, 254)',
hovertemplate='<br>Experience in yrs: %{customdata}<br>Number of Employees: %{y}<br>'))

fig4.update_layout(
    title = "Employee Experience when Churned",
    xaxis=dict(title='Years of Experience', showgrid=False),
    yaxis=dict(title='Number of Employees', showgrid=False),
    bargap=0.2,
    title_x=0.5,
    autosize=True,
    paper_bgcolor="#00172B",
    plot_bgcolor="#00172B")



left_column, right_column = st.columns(2)
left_column.plotly_chart(fig1, use_container_width=True)
#center_column.plotly_chart(fig1, use_container_width=True)
right_column.plotly_chart(fig2, use_container_width=True)

left_column1, right_column1 = st.columns(2)
left_column1.plotly_chart(fig3, use_container_width=True)
#center_column.plotly_chart(fig1, use_container_width=True)
right_column1.plotly_chart(fig4, use_container_width=True)


# with st.expander(f"View all Employees in the {department} Department 👥"):
#     num = st.slider("Number of Records to view?", 0, active_filtered.shape[0], 5)
#     st.table(active_filtered.loc[:num,['emp_no', 'first_name', 'last_name', 'gender', 'birth_date', 'current_title']])

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
