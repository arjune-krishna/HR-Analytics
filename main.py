import streamlit as st
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly.subplots import make_subplots

departments = pd.read_csv('departments.csv')
dept_emp = pd.read_csv('dept_emp.csv')
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
st.sidebar.header("Filters")
department = st.sidebar.selectbox(
    "Select a Department:",
    tuple(departments['dept_name'].unique())
)

#title
st.title('🎯 HR Analytics')
# -----------------------------------------------
#------------------------------------------------    
dept_emp = dept_emp.merge(departments, left_on='dept_no', right_on='dept_no')
filtered = dept_emp[dept_emp['dept_name'].isin([department])].merge(employees, left_on='emp_no', right_on='emp_no')


active_filtered = filtered[filtered['to_date'].astype(str).str.contains('9999')].merge(titles, left_on=['emp_no', 'to_date'], right_on=['emp_no', 'to_date'])
active_filtered.drop(['to_date', 'dept_no'], axis=1, inplace=True)
active_filtered.set_axis(['emp_no', 'work_in_dept_from_date', 'dept_name', 'birth_date', 'first_name', 'last_name',	'gender', 'hire_date', 'current_title',	'current_title_from_date'], axis=1, inplace=True)


inactive_filtered = filtered[~(filtered['to_date'].astype(str).str.contains('9999'))].reset_index().drop(['index'], axis=1)

salaries1 = salaries[salaries['to_date'].astype(str).str.contains('9999')]

# -----------------------------------------------
#------------------------------------------------ 

#KPI 
column1, column2, column3 = st.columns(3)
with column1:
    #Active Employees
    active_employees = active_filtered.shape[0]
    st.metric(label='✅ Active Employees', value=f"{active_employees}")
with column2:
    #Avg Salary
    avg_salary = round(salaries1[salaries1.emp_no.isin(active_filtered['emp_no'].unique())]['salary'].median(),2)
    st.metric(label='💰 Median Salary', value=f"${avg_salary}")
with column3:
    dept_manager= dept_manager.merge(departments, left_on='dept_no', right_on='dept_no')
    dept_manager1=dept_manager[dept_manager['to_date'].astype(str).str.contains('9999')]
    dept_manager1=dept_manager1[dept_manager1["dept_name"] == department].merge(employees, on="emp_no")
    dept_manager1 = dept_manager1["first_name"][0] + " " + dept_manager1["last_name"][0]
    st.metric(label='👤 Department Manager', value=f"{dept_manager1}")

st.markdown("---")
# -----------------------------------------------
#------------------------------------------------ 


#Gender Pie Chart
gender = active_filtered.gender.value_counts().to_frame().reset_index().set_axis(['gender', 'employees'], axis=1)
data = go.Pie(labels=['Male', 'Female'], values=gender['employees'], hole=.4, marker={'colors': ['rgb(12, 102, 254)', 'rgb(179, 207, 255)']}, \
            name='', hovertemplate='<br>Gender: %{label}<br> %{value} Employees<br>')
fig = go.Figure(data)
fig.update_layout(
        title = "Active Employees: Gender in %",
        title_x=0.5,
        autosize=True,
        paper_bgcolor="#00172B",
        plot_bgcolor="#00172B")

# -----------------------------------------------
#------------------------------------------------

#Avg Hike
salaries = salaries[salaries['emp_no'].isin(active_filtered['emp_no'].unique())]
salaries['from_date'] = pd.to_datetime(salaries['from_date'], format="%d-%m-%Y") 
#applying rank for each employee and their salary hike
salaries['rank'] = salaries.groupby(['emp_no'])['from_date'].rank(ascending=True)
#calculating the diff between the current salary and previous salary
salaries['diff'] = salaries.sort_values(by=['emp_no', 'rank']).groupby(['emp_no'])['salary'].diff()
old_salary = (salaries['salary'] - salaries['diff'])
new_salary = salaries['salary']
salaries['yoy'] = round(((new_salary - old_salary)/old_salary)*100, 2)
s = salaries.groupby('rank')['yoy'].mean().round(2).to_frame().reset_index().set_axis(['working_period', 'hike'], axis=1).fillna(0)

fig1 = go.Figure([go.Scatter(x=s.loc[1:]['working_period'], y=s.loc[1:]['hike'], mode='lines+markers', marker={'color': 'rgb(12, 102, 254)'}, 
    name='', hovertemplate='<br>Year: %{x}<br>Avg Hike: %{y}%<br>')])


fig1.update_layout(
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
inactive_filtered['to_date'] = pd.to_datetime(inactive_filtered.loc[:,'to_date'], format="%d-%m-%Y").to_frame().reset_index().drop(['index'], axis=1)

churn = inactive_filtered['to_date'].dt.year.value_counts().to_frame().sort_index().reset_index().set_axis(['year', 'churned_employees'], axis=1)
hired_employees = pd.to_datetime(filtered['hire_date'], format="%d-%m-%Y") \
                        .dt.year.value_counts().sort_index().to_frame().reset_index().set_axis(['year', 'hired_employees'], axis=1)
churn = churn.merge(hired_employees, on='year')
churn['hired_employees'] = churn['hired_employees'].shift()

churn['yoy'] = ((churn['churned_employees'] / churn['hired_employees'])*100).round(2).fillna(0)
churn = churn.loc[1:]

fig2 = go.Figure([go.Scatter(x=churn['year'], y=churn['yoy'], mode='lines+markers', marker={'color': 'rgb(12, 102, 254)'}, 
        customdata = churn['yoy'], name='', hovertemplate='<br>Year: %{x}<br>Churn Rate: %{y}%<br>')])


fig2.update_layout(
        title = "Churn Rate Per Year",
        xaxis=dict(title='Year', showgrid=False),
        yaxis=dict(title='Churn Rate', showgrid=False),
        title_x=0.5,
        autosize=True,
        paper_bgcolor="#00172B",
        plot_bgcolor="#00172B")

# -----------------------------------------------
#------------------------------------------------
#Avg Exp of Employees when Churned
exp_when_churned = (pd.to_datetime(inactive_filtered['to_date'], format="%d-%m-%Y") - pd.to_datetime(inactive_filtered['hire_date'], format="%d-%m-%Y")).dt.days
exp_when_churned=(exp_when_churned/365).round(2).to_frame()
exp_when_churned = exp_when_churned.set_axis(['yoe'], axis=1)

fig3 = go.Figure(go.Histogram(x=exp_when_churned['yoe'],  xbins=dict(start='0', end='18', size= '1'), customdata=[i for i in range(1,19)],
hoverinfo = ('y'), name='', marker_color='rgb(12, 102, 254)',
hovertemplate='<br>Experience in yrs: %{customdata}<br>Number of Employees: %{y}<br>'))

fig3.update_layout(
    title = "Employee's Experience when Churned",
    xaxis=dict(title='Years of Experience', showgrid=False),
    yaxis=dict(title='Number of Employees',showgrid=False),
    autosize=True,
    bargap=0.2,
    title_x=0.5,
    paper_bgcolor="#00172B",
    plot_bgcolor="#00172B")



left_column, right_column = st.columns(2)
left_column.plotly_chart(fig, use_container_width=True)
#center_column.plotly_chart(fig1, use_container_width=True)
right_column.plotly_chart(fig1, use_container_width=True)

left_column1, right_column1 = st.columns(2)
left_column1.plotly_chart(fig2, use_container_width=True)
#center_column.plotly_chart(fig1, use_container_width=True)
right_column1.plotly_chart(fig3, use_container_width=True)


with st.expander(f"View all Employees in the {department} Department 👥"):
    num = st.slider("Number of Records to view?", 0, active_filtered.shape[0], 5)
    st.table(active_filtered.loc[:num,['emp_no', 'first_name', 'last_name', 'gender', 'birth_date', 'current_title']])

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)