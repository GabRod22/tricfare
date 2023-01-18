import streamlit as st
import plotly.graph_objs as go
import pandas as pd

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1519705129143-43afdfe43ac7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=737&q=80");
background-size: cover;
}

[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs(["Calculator", "Data Transparency", "About"])

with tab1:
    st.header('Tricycle Fare Rate :green[Calculator] :pager:')

    col1, col2 = st.columns(2)
    col1.metric("Average Gas Price Last Week", "PHP66.45")
    col2.metric("Average Gas Price Currently", "PHP65.70", "-1.14%")

    f = st.form(key='my_form')
    data_set1 = f.selectbox("Select the number of passenger/s:", [
        "1", "2", "3",
        "4", "5"
    ])

fare = 0
if data_set1 == "1":
  fare += 18
elif data_set1 == "2":
  fare += 26
elif data_set1 == "3":
  fare += 33
elif data_set1 == "4":
  fare += 39
elif data_set1 == "5":
  fare += 44

# Create a dropdown menu for the number of passengers
data_set5 = f.selectbox("Select your classification:", [
    "Ordinary", "Student", "Senior Citizen/PWD"
])

if data_set5 == "Ordinary":
  fare -= 0
elif data_set5 == "Student":
  fare -= 10
elif data_set5 == "Senior Citizen/PWD":
  fare -= 13

# Create a dropdown menu for Landmarks
data_set2 = f.selectbox("Select where you are going::", [
    "All-Homes Cabanatuan", "Cabanatuan City Hall", "Cabanatuan Terminal",
    "Freedom Park", "N.E. Crossing", "Plaza Lucero",
    "Robinsons Townville", "SM City Cabanatuan", "SM Mega Center",
    "Waltermart Cabanatuan"
])


if data_set2 == "All-Homes Cabanatuan":
  fare += 16
elif data_set2 == "Cabanatuan City Hall":
  fare += 32
elif data_set2 == "Cabanatuan Terminal":
  fare += 25
elif data_set2 == "Freedom Park":
  fare += 19
elif data_set2 == "N.E. Crossing":
  fare += 19
elif data_set2 == "Plaza Lucero":
  fare += 21
elif data_set2 == "Robinsons Townville":
  fare += 40
elif data_set2 == "SM City Cabanatuan":
  fare += 34
elif data_set2 == "SM Mega Center":
  fare += 17
elif data_set2 == "Waltermart Cabanatuan":
  fare += 9

fare -= 1

submitted = f.form_submit_button("Compute!")
if submitted:
    st.success(f'Your fare should be ₱{fare}', icon="✅")

with tab2:
    st.header('This is our :blue[Algorithm] :bar_chart:')
    option = st.selectbox(
        'Which data would you like to view?',
        ('Passenger', 'Landmark', 'Gas Price Increase', 'Gas Price Decrease', 'Classification', 'Fare Matrix', 'DOE Gas Price'))

    if 'Passenger' in option:

        one = [0, 10, 15, 10, 20, 10, 5, 0, 15, 10, 25, 20, 15, 10, 15, 10, 20, 20, 20, 5, 10, 10, 20, 10, 30, 30, 30, 30, 30, 20, 20, 30, 20, 10, 30, 30, 25, 30, 20, 15, 20, 15, 0, 10, 30, 10, 10, 30, 10, 10, 20, 20, 10, 30, 30, 5, 20, 20, 15, 20, 20, 20, 20, 20, 20, 15, 20, 25, 20, 30, 20, 30, 15, 20, 20, 30, 20, 20, 20, 30, 30, 20, 20, 15, 20, 10, 15, 20, 15, 15, 25, 30, 15, 25, 15, 10, 15]
        two = [5, 15, 30, 20, 20, 15, 10, 5, 30, 15, 30, 30, 20, 20, 20, 20, 30, 25, 20, 10, 15, 20, 30, 15, 40, 40, 40, 40, 40, 30, 30, 40, 30, 20, 40, 40, 30, 35, 30, 20, 20, 20, 10, 15, 30, 15, 20, 40, 20, 20, 30, 30, 20, 30, 35, 15, 30, 30, 30, 30, 30, 30, 30, 30, 30, 25, 30, 30, 30, 35, 25, 35, 25, 25, 25, 35, 25, 30, 25, 35, 40, 25, 30, 30, 25, 15, 20, 30, 30, 25, 30, 35, 30, 40, 25, 20, 25]
        three = [10, 15, 35, 25, 30, 20, 15, 10, 40, 20, 35, 30, 25, 30, 25, 30, 40, 30, 30, 15, 20, 30, 40, 20, 45, 45, 45, 45, 45, 30, 40, 45, 45, 35, 45, 45, 35, 40, 35, 30, 30, 25, 20, 20, 40, 20, 30, 50, 30, 30, 30, 40, 30, 35, 40, 20, 40, 40, 30, 40, 40, 30, 35, 40, 40, 35, 40, 35, 50, 40, 30, 40, 30, 30, 30, 40, 30, 40, 30, 40, 40, 30, 35, 40, 30, 20, 30, 35, 40, 30, 35, 40, 45, 50, 35, 30, 35]
        four = [10, 20, 40, 30, 40, 25, 20, 15, 45, 25, 40, 40, 30, 40, 30, 40, 40, 35, 40, 20, 25, 35, 50, 25, 50, 50, 50, 50, 50, 40, 45, 45, 40, 40, 50, 50, 40, 45, 45, 40, 40, 30, 30, 25, 40, 25, 40, 50, 40, 40, 40, 45, 40, 40, 45, 25, 45, 45, 40, 45, 45, 40, 40, 45, 40, 45, 45, 40, 50, 45, 35, 45, 40, 35, 35, 45, 35, 45, 35, 45, 50, 35, 40, 45, 35, 20, 40, 40, 45, 35, 40, 45, 50, 50, 45, 40, 45]
        five = [15, 20, 50, 35, 50, 30, 25, 15, 50, 30, 50, 50, 30, 50, 35, 50, 50, 40, 50, 25, 30, 40, 50, 30, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50]

        count_one = [one.count(0), one.count(5), one.count(10), one.count(15), one.count(20), one.count(25), one.count(30), one.count(35), one.count(40), one.count(45), one.count(50)]
        count_two = [two.count(0), two.count(5), two.count(10), two.count(15), two.count(20), two.count(25), two.count(30), two.count(35), two.count(40), two.count(45), two.count(50)]
        count_three = [three.count(0), three.count(5), three.count(10), three.count(15), three.count(20), three.count(25), three.count(30), three.count(35), three.count(40), three.count(45), three.count(50)]
        count_four = [four.count(0), four.count(5), four.count(10), four.count(15), four.count(20), four.count(25), four.count(30), four.count(35), four.count(40), four.count(45), four.count(50)]
        count_five = [five.count(0), five.count(5), five.count(10), five.count(15), five.count(20), five.count(25), five.count(30), five.count(35), five.count(40), five.count(45), five.count(50)]


        x = ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50']

        trace1 = go.Scatter(x=x, y=count_one, name='1 Passenger')
        trace2 = go.Scatter(x=x, y=count_two, name='2 Passengers')
        trace3 = go.Scatter(x=x, y=count_three, name='3 Passengers')
        trace4 = go.Scatter(x=x, y=count_four, name='4 Passengers')
        trace5 = go.Scatter(x=x, y=count_five, name='5 Passengers')


        data = [trace1, trace2, trace3, trace4, trace5]

        layout = go.Layout(title='Count of Price Range in the Number of Passenger/s',
                        xaxis=dict(title='Price Range (₱)'),
                        yaxis=dict(title='Count'))

        fig = go.Figure(data=data, layout=layout)

        st.plotly_chart(fig)

    elif 'Landmark' in option:

    # Chart 2
        one = [20,30,20,10,20,20,25,30,20,25,20,20,30,20,20,30,25,20,20,10,10,15,15,10,10,10,10,10,10,25,10,10,15,15,10,10,15,15,20,25,20,15,30,20,0,20,30,15,20,30,10,25,20,0,10,25,15,20,15,10,20,20,5,10,15,15,10,15,10,10,20,10,15,10,20,0,20,20,10,10,10,10,10,15,10,10,15,20,15,15,15,10,25,20,15,15,25]
        two = [40,50,45,20,30,50,30,50,35,30,35,40,25,35,30,40,45,40,40,40,30,20,30,40,30,30,30,30,30,30,30,35,15,20,30,35,30,35,30,45,40,40,50,40,20,40,40,20,35,40,20,30,40,10,20,35,25,30,35,30,30,30,25,30,30,35,40,35,30,20,30,30,40,30,30,20,30,30,30,20,20,30,30,35,30,20,35,30,25,35,25,30,30,40,20,25,30]
        three = [40,35,50,20,30,40,35,40,40,35,30,40,30,30,20,45,45,30,40,40,20,25,40,15,20,20,20,20,20,20,20,10,20,35,20,15,15,15,25,35,25,25,30,30,10,30,30,15,30,30,15,20,30,10,10,25,15,20,35,10,30,20,20,20,30,25,30,35,20,20,20,30,35,20,20,10,30,30,20,10,10,20,20,25,20,15,25,20,15,25,10,20,40,30,25,30,30]
        four = [30,30,50,10,40,30,35,30,30,25,40,25,25,20,20,40,35,20,15,30,20,15,25,20,10,10,10,10,10,20,10,0,20,25,10,15,15,15,25,35,30,30,30,30,0,20,30,5,20,30,10,10,30,5,10,25,10,20,15,20,20,5,15,20,10,15,20,15,20,10,10,10,15,10,10,10,10,30,10,10,10,10,10,15,10,15,15,20,15,15,10,10,30,20,25,25,20]
        five = [30,30,25,10,40,30,35,40,20,20,35,20,20,25,30,30,40,30,20,30,20,10,30,15,10,10,10,10,10,30,10,0,20,20,10,10,15,15,30,40,25,35,30,30,10,20,35,5,20,30,10,20,20,10,10,30,10,10,15,25,10,15,15,10,10,15,20,15,20,10,20,10,15,10,10,10,10,20,10,10,10,10,10,15,10,15,15,20,15,10,10,10,20,20,25,35,30]
        six = [30,40,35,15,50,30,35,40,15,25,40,30,20,25,35,40,35,30,30,20,30,15,30,30,10,10,10,10,10,20,10,0,20,30,20,10,25,25,30,40,30,35,30,30,10,30,25,10,30,30,15,10,35,10,15,30,20,10,15,10,20,10,15,20,10,25,30,15,20,10,15,10,20,10,10,10,10,30,10,10,10,10,10,15,10,15,15,20,15,15,10,10,30,30,25,25,35]
        seven = [40,50,50,20,50,50,45,50,50,35,50,45,35,35,50,50,50,50,50,40,40,20,40,50,40,40,40,40,40,30,40,35,25,50,40,40,45,45,35,45,30,45,50,50,30,50,50,25,50,40,30,40,50,20,30,45,40,40,35,40,40,40,30,40,40,40,40,35,40,20,30,40,45,45,40,30,50,30,40,30,30,40,40,45,40,25,45,35,35,45,35,40,40,50,40,45,40]
        eight = [40,45,50,20,50,50,45,50,50,35,50,40,40,30,50,40,45,45,40,40,30,25,25,40,30,30,30,30,20,30,30,20,25,45,40,40,35,40,35,45,30,45,50,50,20,40,40,20,40,40,20,30,40,15,20,40,30,30,35,30,30,30,20,35,40,35,40,25,30,20,20,40,40,40,35,20,40,40,30,25,20,30,30,35,30,25,35,30,25,35,25,30,35,50,35,40,30]
        nine = [30,35,15,10,40,35,30,30,30,25,30,25,30,15,25,30,30,25,20,20,20,15,20,30,0,0,0,0,0,20,10,10,5,35,0,15,15,5,30,20,25,35,30,20,10,20,25,10,30,30,10,10,20,10,5,20,20,10,25,20,20,10,10,20,10,15,20,5,10,10,10,10,20,10,10,10,10,10,10,10,0,10,10,15,10,20,15,10,10,15,10,10,25,25,25,25,25]
        ten = [20,25,10,10,40,20,25,20,10,20,10,10,10,15,20,10,20,10,10,5,10,10,15,10,0,0,0,0,0,20,0,0,0,10,0,5,5,5,15,15,15,15,20,20,0,10,20,5,20,20,5,5,10,0,0,15,10,0,15,0,10,0,0,10,10,15,10,5,10,0,0,0,10,0,0,0,0,0,0,0,0,0,0,5,0,5,5,10,5,5,0,0,15,20,15,10,15]

        count_one = [one.count(0), one.count(5), one.count(10), one.count(15), one.count(20), one.count(25), one.count(30), one.count(35), one.count(40), one.count(45), one.count(50)]
        count_two = [two.count(0), two.count(5), two.count(10), two.count(15), two.count(20), two.count(25), two.count(30), two.count(35), two.count(40), two.count(45), two.count(50)]
        count_three = [three.count(0), three.count(5), three.count(10), three.count(15), three.count(20), three.count(25), three.count(30), three.count(35), three.count(40), three.count(45), three.count(50)]
        count_four = [four.count(0), four.count(5), four.count(10), four.count(15), four.count(20), four.count(25), four.count(30), four.count(35), four.count(40), four.count(45), four.count(50)]
        count_five = [five.count(0), five.count(5), five.count(10), five.count(15), five.count(20), five.count(25), five.count(30), five.count(35), five.count(40), five.count(45), five.count(50)]
        count_six = [six.count(0), six.count(5), six.count(10), six.count(15), six.count(20), six.count(25), six.count(30), six.count(35), six.count(40), six.count(45), six.count(50)]
        count_seven = [seven.count(0), seven.count(5), seven.count(10), seven.count(15), seven.count(20), seven.count(25), seven.count(30), seven.count(35), seven.count(40), seven.count(45), seven.count(50)]
        count_eight = [eight.count(0), eight.count(5), eight.count(10), eight.count(15), eight.count(20), eight.count(25), eight.count(30), eight.count(35), eight.count(40), eight.count(45), eight.count(50)]
        count_nine = [nine.count(0), nine.count(5), nine.count(10), nine.count(15), nine.count(20), nine.count(25), nine.count(30), nine.count(35), nine.count(40), nine.count(45), nine.count(50)]
        count_ten = [ten.count(0), ten.count(5), ten.count(10), ten.count(15), ten.count(20), ten.count(25), ten.count(30), ten.count(35), ten.count(40), ten.count(45), ten.count(50)]

        x = ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50']

        trace1 = go.Scatter(x=x, y=count_one, name='All-Homes Cabanatuan')
        trace2 = go.Scatter(x=x, y=count_two, name='Cabanatuan City Hall')
        trace3 = go.Scatter(x=x, y=count_three, name='Cabanatuan Terminal')
        trace4 = go.Scatter(x=x, y=count_four, name='Freedom Park')
        trace5 = go.Scatter(x=x, y=count_five, name='N.E. Crossing')
        trace6 = go.Scatter(x=x, y=count_one, name='Plaza Lucero')
        trace7 = go.Scatter(x=x, y=count_two, name='Robinsons Townville')
        trace8 = go.Scatter(x=x, y=count_three, name='SM City Cabanatuan')
        trace9 = go.Scatter(x=x, y=count_four, name='SM Mega Center')
        trace10 = go.Scatter(x=x, y=count_five, name='Waltermart Cabanatuan')

        data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10]

        layout = go.Layout(title='Count of Price Range in Various Landmarks',
                        xaxis=dict(title='Price Range (₱)'),
                        yaxis=dict(title='Count'))

        fig = go.Figure(data=data, layout=layout)

        st.plotly_chart(fig)

    elif 'Gas Price Increase' in option:

    # Chart 3
        one = [0,10,5,10,0,0,5,0,0,5,5,5,0,5,0,5,5,0,5,0,0,5,5,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,5,10,0]
        two = [5,15,10,10,0,5,10,5,0,5,10,5,5,5,5,5,5,5,10,5,0,10,5,0,0,0,0,0,0,5,0,0,5,0,5,5,0,5,0,0,5,0,5,0,0,5,10,0,5,0,0,10,5,5,5,5,0,5,5,0,0,5,0,0,0,5,0,0,5,0,5,5,5,0,0,5,5,0,5,5,5,0,5,5,0,0,0,5,0,0,5,0,5,5,5,15,5]
        three = [10,15,10,10,5,10,15,10,5,10,10,10,5,10,10,10,10,10,15,10,5,10,10,5,0,0,0,0,0,10,5,5,10,5,10,5,5,10,5,5,10,5,10,5,5,10,15,5,10,0,5,10,10,10,10,10,5,10,10,5,0,10,5,5,5,10,5,0,5,0,5,5,10,5,5,10,10,5,10,10,5,5,10,10,5,0,5,5,5,5,10,5,10,5,10,20,5]
        four = [10,20,10,10,5,15,20,15,10,10,15,15,5,10,15,10,10,10,15,15,5,15,10,5,0,0,0,0,0,15,10,10,15,10,10,10,10,15,10,10,15,10,15,5,5,15,20,5,15,0,5,10,15,10,10,15,5,15,15,5,5,15,5,5,5,15,5,5,10,5,10,10,15,5,10,15,15,5,15,15,10,5,10,10,5,0,10,10,5,5,15,5,10,5,10,25,10]
        five = [10,20,10,10,5,20,25,15,10,15,20,20,10,15,20,15,20,15,20,20,10,15,15,10,0,0,0,0,0,20,15,15,20,15,10,15,15,20,15,15,20,15,20,10,5,20,25,10,20,0,10,10,20,15,15,20,10,20,20,10,5,20,10,10,10,20,10,10,10,10,10,10,20,10,10,20,20,10,20,20,10,10,15,10,10,5,15,15,10,10,20,10,15,10,15,30,10]
        six = [15,25,10,10,5,25,30,15,15,15,20,20,10,15,25,15,20,15,20,25,10,20,15,10,0,0,0,0,0,25,20,20,25,20,20,20,20,25,20,20,25,20,25,10,10,25,30,10,25,0,10,10,25,15,15,25,10,25,25,15,10,25,10,10,10,25,10,10,15,15,15,15,25,10,15,25,25,10,25,25,15,10,15,15,10,5,15,15,10,10,25,10,15,15,15,35,15]
        seven = [15,30,15,10,10,30,35,20,15,20,20,25,10,15,30,20,25,20,25,30,15,20,20,15,0,0,0,0,0,30,25,25,30,25,20,20,20,30,25,25,30,25,30,15,10,30,35,15,30,0,15,15,30,20,15,30,15,30,30,20,15,30,15,15,15,25,15,15,15,20,20,20,30,15,15,30,30,10,30,30,20,15,20,20,15,5,15,15,15,15,30,15,20,20,15,40,15]

        count_one = [one.count(0), one.count(5), one.count(10), one.count(15), one.count(20), one.count(25), one.count(30), one.count(35), one.count(40), one.count(45), one.count(50)]
        count_two = [two.count(0), two.count(5), two.count(10), two.count(15), two.count(20), two.count(25), two.count(30), two.count(35), two.count(40), two.count(45), two.count(50)]
        count_three = [three.count(0), three.count(5), three.count(10), three.count(15), three.count(20), three.count(25), three.count(30), three.count(35), three.count(40), three.count(45), three.count(50)]
        count_four = [four.count(0), four.count(5), four.count(10), four.count(15), four.count(20), four.count(25), four.count(30), four.count(35), four.count(40), four.count(45), four.count(50)]
        count_five = [five.count(0), five.count(5), five.count(10), five.count(15), five.count(20), five.count(25), five.count(30), five.count(35), five.count(40), five.count(45), five.count(50)]
        count_six = [six.count(0), six.count(5), six.count(10), six.count(15), six.count(20), six.count(25), six.count(30), six.count(35), six.count(40), six.count(45), six.count(50)]
        count_seven = [seven.count(0), seven.count(5), seven.count(10), seven.count(15), seven.count(20), seven.count(25), seven.count(30), seven.count(35), seven.count(40), seven.count(45), seven.count(50)]


        x = ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50']

        trace1 = go.Scatter(x=x, y=count_one, name='₱0-2')
        trace2 = go.Scatter(x=x, y=count_two, name='₱3-5')
        trace3 = go.Scatter(x=x, y=count_three, name='₱6-8')
        trace4 = go.Scatter(x=x, y=count_four, name='₱9-11')
        trace5 = go.Scatter(x=x, y=count_five, name='₱12-14')
        trace6 = go.Scatter(x=x, y=count_six, name='₱15-17')
        trace7 = go.Scatter(x=x, y=count_seven, name='₱18-20')


        data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7]

        layout = go.Layout(title='Count of Price Range in Gas Price Increase',
                        xaxis=dict(title='Price Range (₱)'),
                        yaxis=dict(title='Count'))

        fig = go.Figure(data=data, layout=layout)

        st.plotly_chart(fig)

    elif 'Gas Price Decrease' in option:

    # Chart 4
        one = [0,10,5,5,0,0,5,0,0,5,5,0,0,5,0,5,5,0,5,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0,0,0,0,0,5,0,0,5,0,0,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,5,0,5,10,0]
        two = [5,15,10,5,0,5,10,5,0,5,5,0,5,5,5,5,5,5,10,5,0,5,5,0,0,0,0,0,0,5,0,0,5,0,5,5,0,5,0,0,5,0,5,0,0,5,10,0,5,5,0,5,10,5,5,5,0,5,5,0,5,5,0,0,0,5,0,0,5,0,5,5,5,0,0,5,5,0,5,5,5,0,5,5,0,5,0,5,0,0,5,0,5,0,5,15,5]
        three = [5,15,15,5,5,10,15,10,5,10,10,5,5,10,10,10,10,5,10,10,5,10,5,5,0,0,0,0,0,10,5,5,10,5,5,5,5,10,5,5,10,5,10,5,5,10,15,5,10,5,5,10,15,10,10,10,5,10,10,5,10,10,5,5,5,10,5,0,5,0,5,5,10,5,5,10,10,5,10,10,5,5,10,10,5,5,5,5,5,5,10,5,10,0,10,20,5]
        four = [5,15,20,5,5,15,20,15,5,10,15,5,5,10,15,10,10,10,15,15,5,10,10,5,0,0,0,0,0,15,10,5,15,10,5,10,10,15,10,10,15,10,15,5,5,15,20,5,15,10,5,15,20,10,10,15,5,15,15,5,15,15,5,5,5,15,5,5,10,5,10,10,15,5,10,15,15,5,15,15,10,5,10,10,5,5,10,10,5,5,15,5,10,5,10,20,10]
        five = [5,20,20,5,5,20,25,15,5,15,15,10,10,10,20,15,20,15,15,20,10,15,15,10,0,0,0,0,0,20,15,5,20,15,10,15,15,20,15,15,20,15,20,10,5,20,25,10,20,10,10,20,25,15,15,20,10,20,20,10,20,20,10,10,10,20,10,10,10,10,10,10,20,10,10,20,20,10,20,20,10,10,15,10,10,10,15,15,10,10,20,10,15,5,15,25,10]
        six = [10,25,20,5,5,25,30,15,10,15,20,10,10,10,25,15,20,15,20,25,10,15,20,10,0,0,0,0,0,25,20,10,25,20,10,20,20,25,20,20,25,20,25,10,10,25,30,10,25,15,10,25,30,15,15,25,10,25,25,15,25,25,10,10,10,25,10,10,15,15,15,15,25,10,15,25,25,10,25,25,15,10,15,15,10,10,15,15,10,10,25,10,15,10,15,30,15]
        seven = [10,25,25,5,10,30,35,20,10,20,20,10,10,10,25,20,25,20,20,30,15,15,20,15,0,0,0,0,0,30,25,10,30,25,10,20,20,30,25,25,30,25,30,15,10,30,35,15,30,15,15,30,35,20,15,30,15,30,30,20,30,30,15,15,15,25,15,15,15,20,20,20,30,15,15,30,30,10,30,30,20,15,20,20,15,10,15,15,15,15,30,15,20,15,15,35,15]

        count_one = [one.count(0), one.count(5), one.count(10), one.count(15), one.count(20), one.count(25), one.count(30), one.count(35), one.count(40), one.count(45), one.count(50)]
        count_two = [two.count(0), two.count(5), two.count(10), two.count(15), two.count(20), two.count(25), two.count(30), two.count(35), two.count(40), two.count(45), two.count(50)]
        count_three = [three.count(0), three.count(5), three.count(10), three.count(15), three.count(20), three.count(25), three.count(30), three.count(35), three.count(40), three.count(45), three.count(50)]
        count_four = [four.count(0), four.count(5), four.count(10), four.count(15), four.count(20), four.count(25), four.count(30), four.count(35), four.count(40), four.count(45), four.count(50)]
        count_five = [five.count(0), five.count(5), five.count(10), five.count(15), five.count(20), five.count(25), five.count(30), five.count(35), five.count(40), five.count(45), five.count(50)]
        count_six = [six.count(0), six.count(5), six.count(10), six.count(15), six.count(20), six.count(25), six.count(30), six.count(35), six.count(40), six.count(45), six.count(50)]
        count_seven = [seven.count(0), seven.count(5), seven.count(10), seven.count(15), seven.count(20), seven.count(25), seven.count(30), seven.count(35), seven.count(40), seven.count(45), seven.count(50)]



        x = ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50']


        trace1 = go.Scatter(x=x, y=count_one, name='₱0-2')
        trace2 = go.Scatter(x=x, y=count_two, name='₱3-5')
        trace3 = go.Scatter(x=x, y=count_three, name='₱6-8')
        trace4 = go.Scatter(x=x, y=count_four, name='₱9-11')
        trace5 = go.Scatter(x=x, y=count_five, name='₱12-14')
        trace6 = go.Scatter(x=x, y=count_six, name='₱15-17')
        trace7 = go.Scatter(x=x, y=count_seven, name='₱18-20')


        data = [trace1, trace2, trace3, trace4, trace5, trace6, trace7]

        layout = go.Layout(title='Count of Price Range in Gas Price Decrease',
                        xaxis=dict(title='Price Range (₱)'),
                        yaxis=dict(title='Count'))

        fig = go.Figure(data=data, layout=layout)

        st.plotly_chart(fig)

    elif 'Classification' in option:

    # Chart 5
        one = [10,10,15,10,15,10,10,10,10,10,5,15,5,15,10,10,5,10,15,20,10,5,15,10,5,5,5,5,5,5,10,10,10,15,5,10,10,5,20,10,10,15,10,10,5,10,10,15,5,10,15,10,20,15,5,5,10,10,5,10,15,15,15,10,10,5,5,10,15,10,10,15,15,10,5,10,15,10,10,10,10,15,10,5,5,5,10,5,5,5,10,5,5,5,10,15,15]
        two = [15,15,15,10,15,10,20,15,30,20,15,20,15,15,10,20,15,15,15,20,10,10,25,10,0,0,0,0,0,5,5,15,10,10,10,10,5,10,20,15,10,10,0,5,10,20,20,15,10,10,20,10,30,15,10,10,15,20,5,15,20,15,15,10,15,5,5,10,15,15,10,20,20,15,5,15,15,15,10,15,20,15,15,5,5,10,20,5,5,10,10,10,15,5,15,20,15]

        count_one = [one.count(0), one.count(5), one.count(10), one.count(15), one.count(20), one.count(25), one.count(30), one.count(35), one.count(40), one.count(45), one.count(50)]
        count_two = [two.count(0), two.count(5), two.count(10), two.count(15), two.count(20), two.count(25), two.count(30), two.count(35), two.count(40), two.count(45), two.count(50)]


        x = ['0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50']


        trace1 = go.Scatter(x=x, y=count_one, name='Student')
        trace2 = go.Scatter(x=x, y=count_two, name='PWD/Senior Citizen')



        data = [trace1, trace2]

        layout = go.Layout(title='Count of Price Range in Classification',
                        xaxis=dict(title='Price Range (₱)'),
                        yaxis=dict(title='Count'))

        fig = go.Figure(data=data, layout=layout)

        st.plotly_chart(fig)

    elif 'Fare Matrix' in option:()