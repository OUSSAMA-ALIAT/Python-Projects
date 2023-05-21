


data set 



script :

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"

data = pd.read_csv("train.csv")
print(data.head())



Let’s have a look at the information about the columns in the dataset:

1
print(data.info())

Before moving forward, let’s have a look if the dataset has any null values or not:

print(data.isnull().sum())
1
print(data.isnull().sum())

The dataset doesn’t have any null values. As this dataset is labelled, let’s have a look at the Credit_Score column values:


data["Credit_Score"].value_counts()

Data Exploration
The dataset has many features that can train a Machine Learning model for credit score classification. Let’s explore all the features one by one.

I will start by exploring the occupation feature to know if the occupation of the person affects credit scores:

fig = px.box(data, 
             x="Occupation",  
             color="Credit_Score", 
             title="Credit Scores Based on Occupation", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.show()

There’s not much difference in the credit scores of all occupations mentioned in the data. Now let’s explore whether the Annual Income of the person impacts your credit scores or not:

fig = px.box(data, 
             x="Credit_Score", 
             y="Annual_Income", 
             color="Credit_Score",
             title="Credit Scores Based on Annual Income", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

According to the above visualization, the more you earn annually, the better your credit score is. Now let’s explore whether the monthly in-hand salary impacts credit scores or not:

fig = px.box(data, 
             x="Credit_Score", 
             y="Monthly_Inhand_Salary", 
             color="Credit_Score",
             title="Credit Scores Based on Monthly Inhand Salary", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()



Like annual income, the more monthly in-hand salary you earn, the better your credit score will become. Now let’s see if having more bank accounts impacts credit scores or not:

fig = px.box(data, 
             x="Credit_Score", 
             y="Num_Bank_Accounts", 
             color="Credit_Score",
             title="Credit Scores Based on Number of Bank Accounts", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

Maintaining more than five accounts is not good for having a good credit score. A person should have 2 – 3 bank accounts only. So having more bank accounts doesn’t positively impact credit scores. Now let’s see the impact on credit scores based on the number of credit cards you have:

fig = px.box(data, 
             x="Credit_Score", 
             y="Num_Credit_Card", 
             color="Credit_Score",
             title="Credit Scores Based on Number of Credit cards", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()


Just like the number of bank accounts, having more credit cards will not positively impact your credit scores. Having 3 – 5 credit cards is good for your credit score. Now let’s see the impact on credit scores based on how much average interest you pay on loans and EMIs:

fig = px.box(data, 
             x="Credit_Score", 
             y="Interest_Rate", 
             color="Credit_Score",
             title="Credit Scores Based on the Average Interest rates", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()


If the average interest rate is 4 – 11%, the credit score is good. Having an average interest rate of more than 15% is bad for your credit scores. Now let’s see how many loans you can take at a time for a good credit score:

fig = px.box(data, 
             x="Credit_Score", 
             y="Num_of_Loan", 
             color="Credit_Score", 
             title="Credit Scores Based on Number of Loans Taken by the Person",
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()

To have a good credit score, you should not take more than 1 – 3 loans at a time. Having more than three loans at a time will negatively impact your credit scores. Now let’s see if delaying payments on the due date impacts your credit scores or not:

fig = px.box(data, 
             x="Credit_Score", 
             y="Delay_from_due_date", 
             color="Credit_Score",
             title="Credit Scores Based on Average Number of Days Delayed for Credit card Payments", 
             color_discrete_map={'Poor':'red',
                                 'Standard':'yellow',
                                 'Good':'green'})
fig.update_traces(quartilemethod="exclusive")
fig.show()









