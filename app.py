import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import preprocessor, helper
import openpyxl

us_mass_shooting = pd.read_excel('USMassShootings.xlsx')

# load preprocessor.py
us_mass_shooting = preprocessor.preprocess(us_mass_shooting)

# sidebar ui
st.sidebar.title('USA Mass Shooting Analysis')

# sidebar components
user_menu = st.sidebar.radio(
    'Select an Option', (
        'Victims Per Gender', 'SHOOTING TYPE', 'Mass Shooting per Race', 'Count of Victims per State', 'Count of Victims per Year', 'Summary of Killers/Shooters',
        'MENTAL HEALTH SOURCES', 'Information Sources', 'Weapons Used to Shoot/Kill', 'ASSAULT', 'Number of Weapons Used', 'Type of Weapons Used',
        'Where Weapons were Obtained', 'weapons obtained legally', 'Mental Health Notes', 'Prior Signs of Mental Illness', 'Location Type', 'Cases Reported',
        'Fatalities Per Gender', 'Shooting Type Per Prior Signs of Mental Illness'
))

if user_menu == 'Victims Per Gender':
    st.title('Victims of Mass Shooting Per Gender')
    gender = helper.Gender(us_mass_shooting)
    st.table(gender)
    
    # A Bar Graph showing Gender Distributions
    st.subheader('A Bar Graph Displaying Victims of Mass Shooting Per Gender')
    fig = px.bar(us_mass_shooting.GENDER.value_counts(), color=['Male', 'Female'], title='Victims of Mass Shooting Per Gender',
                    template='presentation')
    st.plotly_chart(fig)
    
    # A Pie chart Displaying Victims of Mass Shooting Per Gender
    st.subheader('A Pie Chart Displaying Victims of Mass Shooting Per Gender')
    fig = fig = px.pie(values= us_mass_shooting.GENDER.value_counts(), names=['Male','Female'], 
                    title='Victims of Mass Shooting Per Gender',
                    template='presentation',hole=0.55,
                    color_discrete_sequence=['#891336','#009277'],
                    data_frame=us_mass_shooting)
    st.plotly_chart(fig)

if user_menu == 'SHOOTING TYPE':
    st.title('Shooting Types per Victim')
    s_type = helper.ShootingType(us_mass_shooting)
    st.table(s_type)
    
    # A Bar Graph showing Shooting Types per Victim
    st.subheader('A Bar Graph Displaying Shooting Types per Victim')
    fig = px.bar(us_mass_shooting.SHOOTINGTYPE.value_counts(),color=['Mass', 'Spree'], title='Shooting Types',template='presentation')
    st.plotly_chart(fig)
    
    # A Pie chart Displaying Shooting Types per Victim
    st.subheader('A Pie Chart Displaying Shooting Types per Victim')
    fig = px.pie(values= us_mass_shooting.SHOOTINGTYPE.value_counts(),hole=0.67 ,names=['Mass','Spree'], 
            title='Shooting Types',
            template='presentation',
            color_discrete_sequence=['#809936','#123777'],
            data_frame=us_mass_shooting)
    st.plotly_chart(fig)

if user_menu == 'Mass Shooting per Race':
    st.title('Mass Shooting per Race')
    us_mass_race = helper.Race(us_mass_shooting)
    st.table(us_mass_race)
    
    # A Bar Graph showing Mass Shooting per Race
    st.subheader('A Bar Graph Displaying Mass Shooting per Race')
    fig = px.bar(us_mass_shooting.RACE.value_counts(), color={'White':'red', 'Black':'yellow', 'Asian':'green', 
                                                                    'Latino':'#004332', 'Native American':'#546332', 'Middle Eastern':'#722190',
                                                                    'Other':'#477000'}, title='Race')
    st.plotly_chart(fig)
    
    # A Pie chart Displaying showing Mass Shooting per Race
    st.subheader('A Pie Chart Displaying Percentage of Mass Shooting per Race')
    fig = px.pie(values= us_mass_shooting.RACE.value_counts(), names=['White','Black', 'Asian', 'Latino', 'Native American', 'Middle Eastern', 'Other'], 
            title='RACE', hole=0.55,
            color_discrete_sequence=['#560390','yellow', 'green', '#004332', '#000144', '#090090','#477000'],
            data_frame=us_mass_shooting)
    st.plotly_chart(fig)

if user_menu == 'Count of Victims per State':
    st.title('Count of Victims per State')
    us_mass_state = helper.State(us_mass_shooting)
    st.table(us_mass_state)
    
    # A Bar Graph showing Victims per State
    st.subheader('A Bar Graph Displaying Count of Victims per State')
    fig = px.bar(us_mass_shooting.STATE.value_counts(), color=['Tennessee', 'South Carolina', 'Washington', 'California', 'D.C.',
    'Florida', 'New York', 'Connecticut', 'Minnesota', 'Wisconsin',
    'Colorado', 'Georgia', 'Nevada', 'Arizona', 'Texas',
    'North Carolina', 'Kentucky', 'Illinois', 'Missouri', 'Nebraska',
    'Virginia', 'Utah', 'Pennsylvania', 'Ohio', 'Mississippi',
    'Massachusetts', 'Hawaii', 'Oregon', 'Arkansas', 'Michigan',
    'Iowa', 'Oklahoma'], title='Count of Victims per State')
    st.plotly_chart(fig)
    
    # A Pie chart Displaying showing Victims per State
    st.subheader('A Pie Chart Displaying showing Percentage Victims per State')
    fig = px.pie(values=us_mass_shooting.STATE.value_counts(), names=[
    'Tennessee', 'South Carolina', 'Washington', 'California', 'D.C.',
    'Florida', 'New York', 'Connecticut', 'Minnesota', 'Wisconsin',
    'Colorado', 'Georgia', 'Nevada', 'Arizona', 'Texas',
    'North Carolina', 'Kentucky', 'Illinois', 'Missouri', 'Nebraska',
    'Virginia', 'Utah', 'Pennsylvania', 'Ohio', 'Mississippi',
    'Massachusetts', 'Hawaii', 'Oregon', 'Arkansas', 'Michigan',
    'Iowa', 'Oklahoma'
    ], hole=0.4, color_discrete_sequence=['#560390','yellow', 'green', '#004332', '#000144', '#090090','#477000', '#000077', '#898000', '#755123',
                                    '#000000','#999933', '#129955', '#345666', '#660777', 'indigo','violet', 'red', '#901100', '#790323',
                                    '#222999','#438111', '#707070', '#004332', '#099933', '#474712','#166590', '#233478', '#898989', '#777977',
                                    '#317888','#872907'
                                    ], title='Count of Victims per State', data_frame=us_mass_shooting)
    st.plotly_chart(fig)

if user_menu == 'Count of Victims per Year':
    st.title('Count of Victims per Year')
    year = helper.Year(us_mass_shooting)
    st.table(year)
    
    # A Bar Graph showing Count of Victims per Year
    st.subheader('A Bar Graph Displaying Count of Victims per Year')
    fig = px.bar(us_mass_shooting.YEAR.value_counts(), color=['2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005',
    '2004', '2003', '2001', '2000', '1999', '1998', '1997', '1996', '1995', '1994', '1993',
    '1992', '1991', '1990', '1989', '1988', '1987', '1986', '1984', '1982'], title='Count of Victims per Year')
    st.plotly_chart(fig)
    
    # A Pie chart Displaying showing Count of Victims per Year
    st.subheader('A Pie Chart Displaying showing Percentage of Victims per Year')
    fig = px.pie(values= us_mass_shooting.YEAR.value_counts(), names=['2015', '2014', '2013', '2012', '2011', '2010', '2009', '2008', '2007', '2006', '2005',
    '2004', '2003', '2001', '2000', '1999', '1998', '1997', '1996', '1995', '1994', '1993',
    '1992', '1991', '1990', '1989', '1988', '1987', '1986', '1984', '1982'], hole=0.3,
            title='Count of Victims per Year',
            color_discrete_sequence=['red','yellow', 'green', '#004332', '#000144', '#090090','#477000', '#000077', '#898000', '#755123',
                                    '#000000','#999933', '#129955', '#345666', '#660777', 'indigo','violet', '#560390', '#901100', '#790323',
                                    '#222999','#438111', '#707070', '#004332', '#099933', '#474712','#166590', '#233478', '#898989', '#777977',
                                    '#317888',],
            data_frame=us_mass_shooting)
    st.plotly_chart(fig)

if user_menu == 'Summary of Killers/Shooters':
    st.title('Summary of Killers/Shooters')
    us_mass_summary = helper.Summary(us_mass_shooting)
    st.table(us_mass_summary)

if user_menu == 'MENTAL HEALTH SOURCES':
    st.title('MENTAL HEALTH SOURCES')
    us_mass_mentalsources = helper.MentalHealthSources(us_mass_shooting)
    st.table(us_mass_mentalsources)

if user_menu == 'Information Sources':
    st.title('Shooting Information Sources')
    us_mass_Information_Sources = helper.InfoSources(us_mass_shooting)
    st.table(us_mass_Information_Sources)

if user_menu == 'Weapons Used to Shoot/Kill':
    st.title('Weapon details Used to Shoot/Kill')
    us_mass_weapons = helper.Weapons(us_mass_shooting)
    st.table(us_mass_weapons)

if user_menu == 'ASSAULT':
    st.title('Assaulted Victims')
    us_mass_assault = helper.Assault(us_mass_shooting)
    st.table(us_mass_assault)
    
    # A Bar Graph showing Count of assaulted Victims 
    st.subheader('A Bar Graph Displaying Count of Assaulted Victims')
    fig = px.bar(us_mass_shooting.ASSAULT.value_counts(), color=['No','Yes'], title='Assaulted Victims')
    st.plotly_chart(fig)
    
    # A Pie chart Displaying showing Count of assaulted Victims 
    st.subheader('A Pie Chart Displaying showing Percentage of assaulted Victims')
    fig = px.pie(values= us_mass_shooting.ASSAULT.value_counts(), names=['No', 'Yes'], 
            title='ASSAULT',
            color_discrete_sequence=['#560390', '#477000'],
            data_frame=us_mass_shooting)
    st.plotly_chart(fig)

if user_menu == 'Number of Weapons Used':
    st.title('Number of Weapons Used')
    us_mass_numweapons = helper.NumberOfWeapons(us_mass_shooting)
    st.table(us_mass_numweapons)
    
    # A Bar Graph showing Count of Weapons used to AssaultVictims
    st.subheader('A Bar Graph Displaying of Weapons used to Assault Victims')
    fig = px.bar(us_mass_shooting.NUMWEAPONS.value_counts(), color=[3, 1, 2, 4, 5, 9, 7], title='Number of Weapons')
    st.plotly_chart(fig)
    
    # A Pie chart Displaying showing Percentage of Number of weapons used to assault Victims
    st.subheader('A Pie Chart Displaying showing Percentage of Number of weapons used to assault Victims')
    fig = px.pie(values= us_mass_shooting.NUMWEAPONS.value_counts(), names=[3, 1, 2, 4, 5, 9, 7], 
            title='Number of Weapons',hole=0.47,
            color_discrete_sequence=['#000000','#999933', '#129955', '#345666', '#660777', 'indigo','violet'],
            data_frame=us_mass_shooting)
    st.plotly_chart(fig)

if user_menu == 'Type of Weapons Used':
    st.title('Type of Weapons Used')
    us_mass_typesofweapons = helper.TypesOfWeapons(us_mass_shooting)
    st.table(us_mass_typesofweapons)

if user_menu == 'Where Weapons were Obtained':
    st.title('Where Weapons were Obtained')
    us_mass_weaponsobtained = helper.WeaponsObtained(us_mass_shooting)
    st.table(us_mass_weaponsobtained)

if user_menu == 'weapons obtained legally':
    st.title('weapons obtained legally')
    weapons_obtained_legally = helper.WeaponsObtainedLegally(us_mass_shooting)
    st.table(weapons_obtained_legally)
    
    # A Bar Graph showing weapons obtained legally
    st.subheader('A Bar Graph Weapons Obtained Legally')
    fig = px.bar(us_mass_shooting.WEAPONSOBTAINEDLEGALLY.value_counts(), color=['Yes', 'No'], title='weapons obtained legally')
    st.plotly_chart(fig)
    
    # A Pie Chart showing weapons obtained legally
    st.subheader('A Pie Chart showing Weapons Obtained Legally')
    fig = px.pie(values= us_mass_shooting.WEAPONSOBTAINEDLEGALLY.value_counts(), names=['Yes', 'No'], 
            title='weapons obtained legally',
            color_discrete_sequence=['#433987','#999933'],
            data_frame=us_mass_shooting)
    st.plotly_chart(fig)

if user_menu == 'Mental Health Notes':
    st.title('Mental Health Notes')
    Mental_health_notes = helper.MentalNotes(us_mass_shooting)
    st.table(Mental_health_notes)

if user_menu == 'Prior Signs of Mental Illness':
    st.title('Prior Signs of Mental Illness')
    Prior_Signs_of_Mental_Illness = helper.PriorSignsOfMentalIllness(us_mass_shooting)
    st.table(Prior_Signs_of_Mental_Illness)
    
    # A Bar Graph showing Prior Signs of Mental Illness
    st.subheader('A Pie Chart showing Prior Signs of Mental Illness')
    fig = px.bar(us_mass_shooting.PRIORSIGNSOFMENTALILLNESS.value_counts(), color=['Yes', 'No'], title='weapons obtained legally')
    st.plotly_chart(fig)
    
    # A Pie Chart showing Prior Signs of Mental Illness
    st.subheader('A Pie Chart Prior Signs of Mental Illness')
    fig = px.pie(values= us_mass_shooting.PRIORSIGNSOFMENTALILLNESS.value_counts(), names=['Yes', 'No'], 
            title='Prior Signs of Mental Illness',hole=0.7,
            color_discrete_sequence=['#974360','#273077'],
            data_frame=us_mass_shooting)
    st.plotly_chart(fig)

if user_menu == 'Location Type':
    st.title('Location where the Victim was Shot')
    LocationType = helper.LocationType(us_mass_shooting)
    st.table(LocationType)
    
    # A Bar Graph showing the Location where the Victim was Shot
    st.subheader('A Bar Graph showing the Location where the Victim was Shot')
    fig = px.bar(us_mass_shooting.LOCATIONTYPE.value_counts(), color=['Military', 'Religious', 'School', 'Other', 'Workplace'], title='Location where the Victim was Shot')
    st.plotly_chart(fig)
    
    # A Pie Chart showing the Location where the Victim was Shot
    st.subheader('A Pie Chart showing the Location where the Victim was Shot')
    fig = px.pie(values= us_mass_shooting.LOCATIONTYPE.value_counts(), names=['Military', 'Religious', 'School', 'Other', 'Workplace'], 
            title='Location where the Victim was Shot', hole=0.6,
            color_discrete_sequence=['#974360','#273077','#129955', '#345666', '#660777'],
            data_frame=us_mass_shooting)
    st.plotly_chart(fig)

if user_menu == 'Cases Reported':
    st.title('Cases Reported')
    case = helper.Case(us_mass_shooting)
    st.table(case)

if user_menu == 'Fatalities Per Gender':
    st.title('Sum of Fatalities Per Gender')
    us_mass_gender_fatalities = helper.GenderFatalities(us_mass_shooting)
    st.table(us_mass_gender_fatalities)
    
    st.subheader('A Bar Graph showing Sum of Fatalities Per Gender')
    fig = px.bar(us_mass_shooting.groupby('GENDER')[['FATALITIES']].sum(), color=['blue','red'])
    st.plotly_chart(fig)

if user_menu == 'Shooting Type Per Prior Signs of Mental Illness':
    st.title('Shooting Type Per Prior Signs of Mental Illness')
    prior_signs_shooting_type = helper.ShootingTypePerPRIORSIGNSOFMENTALILLNESS(us_mass_shooting)
    st.table(prior_signs_shooting_type)
    
    st.subheader('A Bar Graph showing Sum of Prior Signs OF Mental Illness per Shooting Type')
    fig = px.bar(us_mass_shooting.groupby('SHOOTINGTYPE')['PRIORSIGNSOFMENTALILLNESS'].size(), color=['blue','red'])
    st.plotly_chart(fig)