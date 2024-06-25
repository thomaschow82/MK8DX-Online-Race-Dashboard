import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Establish a connection to the database
conn = sqlite3.connect('mk8dx.db')

st.write("""
         # super64guy's MK8DX Online Race Dashboard

         Use this site to browse my statistics for my race data online in Mario Kart 8 Deluxe

         ### Testing
         """)
st.table(pd.read_sql_query('SELECT * FROM races', conn))

st.write("### General Statistics")

general_filter = st.radio(label='Frequency', options=['Latest 1 Day', 'All Time'], key=1)

if general_filter == 'Latest 1 Day':
    st.table(pd.read_sql_query(
        '''
        SELECT AVG(place) as avg_place, AVG(vr_gain) as avg_vr_gain
        FROM races
        WHERE date = (SELECT MAX(date) FROM races);
        ''',
        conn
        ))
elif general_filter == 'All Time':
    st.table(pd.read_sql_query(
        '''
        SELECT AVG(place) as avg_place, AVG(vr_gain) as avg_vr_gain
        FROM races;
        ''',
        conn
        ))

st.write("### VR Gain Chart")

vr_gain_filter = st.radio(label='Frequency', options=['Latest 1 Day', 'All Time'], key=2)

if vr_gain_filter == 'Latest 1 Day':
    vr_gain_df = pd.read_sql_query(
        '''
        SELECT vr_gain
        FROM races
        WHERE date = (SELECT MAX(date) FROM races);
        ''',
        conn
    )
elif vr_gain_filter == 'All Time':
    vr_gain_df = pd.read_sql_query(
        '''
        SELECT vr_gain
        FROM races;
        ''',
        conn
    )

st.line_chart(vr_gain_df)

st.write("### Place Distribution")

place_filter = st.radio(label='Frequency', options=['Latest 1 Day', 'All Time'], key=3)

if place_filter == 'Latest 1 Day':
    place_df = pd.read_sql_query(
        '''
        SELECT place, COUNT(*) as count
        FROM races
        WHERE date = (SELECT MAX(date) FROM races)
        GROUP BY place;
        ''',
        conn
    )
elif place_filter == 'All Time':
    place_df = pd.read_sql_query(
        '''
        SELECT place, COUNT(*) as count
        FROM races
        GROUP BY place;
        ''',
        conn
    )

st.bar_chart(data=place_df, x='place', y='count')
