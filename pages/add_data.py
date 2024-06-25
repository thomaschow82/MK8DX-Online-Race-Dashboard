from datetime import datetime
import pandas as pd
import pytz
import streamlit as st
import sqlite3
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

def get_date():
    # Step 1: Define the PST timezone
    pst_timezone = pytz.timezone('US/Pacific')

    # Step 2: Get the current time in UTC
    utc_now = datetime.now(pytz.utc)

    # Step 3: Convert the current UTC time to PST
    pst_now = utc_now.astimezone(pst_timezone)

    # Step 4: Extract the date part and format it as YYYY-MM-DD
    return pst_now.strftime('%Y-%m-%d')

def get_race_id(conn):
    return int(pd.read_sql_query('SELECT MAX(race_id) AS max_id FROM races;', conn)['max_id'][0]) + 1


with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

st.write("A way for me to add data from my mario kart races... sorry!")

name, authentication_status, username = authenticator.login()

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')

    conn = sqlite3.connect('mk8dx.db')

    character = st.selectbox(label='Character',
                             options=['Mario', 'Luigi', 'Peach', 'Daisy', 'Yoshi', 'Toad', 'Toadette', 'Koopa Troopa', 'Bowser', 'Donkey Kong', 'Wario', 'Waluigi', 'Rosalina', 'Metal Mario', 'Pink Gold Peach', 'Lakitu', 'Shy Guy', 'Baby Mario', 'Baby Luigi', 'Baby Peach', 'Baby Daisy', 'Baby Rosalina', 'Larry', 'Lemmy', 'Wendy', 'Ludwig', 'Iggy', 'Roy', 'Morton', 'Mii', 'Tanooki Mario', 'Link', 'Villager (male)', 'Isabelle', 'Cat Peach', 'Dry Bowser', 'Villager (female)', 'Gold Mario', 'Dry Bones', 'Bowser Jr.', 'King Boo', 'Inkling Girl', 'Inkling Boy', 'Birdo', 'Wiggler', 'Petey Piranha', 'Kamek', 'Diddy Kong', 'Funky Kong', 'Peachette', 'Pauline'])
    
    kart = st.selectbox(label='Kart',
                        options=['Standard Kart', 'Pipe Frame', 'Mach 8', 'Steel Driver', 'Cat Cruiser', 'Circuit Special', 'Tri-Speeder', 'Badwagon', 'Prancer', 'Biddybuggy', 'Landship', 'Sneeker', 'Sports Coupe', 'Gold Standard', 'Standard Bike', 'Comet', 'Sport Bike', 'The Duke', 'Flame Rider', 'Varmint', 'Mr. Scooty', 'Jet Bike', 'Yoshi Bike', 'Standard ATV', 'Wild Wiggler', 'Teddy Buggy', 'GLA', 'W 25 Silver Arrow', '300 SL Roadster', 'Blue Falcon', 'Tanooki Kart', 'B Dasher', 'Master Cycle', 'Streetle', 'P-Wing', 'City Tripper', 'Bone Rattler', 'Koopa Clown', 'Splat Buggy', 'Inkstriker'])
    
    wheel = st.selectbox(label='Wheel',
                         options=['Standard', 'Monster', 'Roller', 'Slim', 'Slick', 'Metal', 'Button', 'Off-Road', 'Sponge', 'Wood', 'Cushion', 'Blue Standard', 'Hot Monster', 'Azure Roller', 'Crimson Slim', 'Cyber Slick', 'Retro Off-Road', 'Gold Tires', 'GLA Tires', 'Triforce Tires', 'Leaf Tires'])
    
    glider = st.selectbox(label='Glider',
                          options=['Super Glider', 'Cloud Glider', 'Wario Wing ', 'Waddle Wing', 'Peach Parasol', 'Parachute', 'Parafoil', 'Flower Glider  ', 'Bowser Kite', 'Plane Glider  ', 'MKTV Parafoil', 'Gold Glider', 'Hylian Kite', 'Paper Glider'])
    
    track = st.selectbox(label='Track',
                         options=['SNES Mario Circuit 3', 'SNES Bowser Castle 3', 'SNES Donut Plains 3', 'SNES Rainbow Road', 'N64 Kalimari Desert', "N64 Toad's Turnpike", 'N64 Choco Mountain', 'N64 Royal Raceway', 'N64 Yoshi Valley', 'N64 Rainbow Road', 'GBA Riverside Park', 'GBA Mario Circuit', 'GBA Boo Lake', 'GBA Cheese Land', 'GBA Sky Garden', 'GBA Sunset Wilds', 'GBA Snow Land', 'GBA Ribbon Road', 'GCN Baby Park', 'GCN Dry Dry Desert', 'GCN Daisy Cruiser', 'GCN Waluigi Stadium', 'GCN Sherbet Land', 'GCN Yoshi Circuit', 'GCN DK Mountain', 'DS Cheep Cheep Beach', 'DS Waluigi Pinball', 'DS Shroom Ridge', 'DS Tick-Tock Clock', 'DS Mario Circuit', 'DS Wario Stadium', 'DS Peach Gardens', 'Wii Moo Moo Meadows', 'Wii Mushroom Gorge', 'Wii Coconut Mall', 'Wii DK Summit', "Wii Wario's Gold Mine", 'Wii Daisy Circuit', 'Wii Koopa Cape', 'Wii Maple Treeway', 'Wii Grumble Volcano', 'Wii Moonview Highway', 'Wii Rainbow Road', '3DS Toad Circuit', '3DS Music Park', '3DS Rock Rock Mountain', '3DS Piranha Plant Slide', '3DS Neo Bowser City', '3DS DK Jungle', "3DS Rosalina's Ice World", '3DS Rainbow Road', 'Mario Kart Stadium', 'Water Park', 'Sweet Sweet Canyon', 'Twomp Ruins', 'Mario Circuit', 'Toad Harbor', 'Twisted Mansion', 'Shy Guy Falls', 'Sunshine Airport', 'Dolphin Shoals', 'Electrodrome', 'Mount Wario', 'Cloudtop Cruise', 'Bone-Dry Dunes', "Bowser's Castle", 'Rainbow Road', 'Excitebike Arena', 'Dragon Driftway', 'Mute City', 'Ice Ice Outpost', 'Hyrule Circuit', 'Wild Woods', 'Animal Crossing', 'Super Bell Subway', 'Big Blue', 'Tour New York Minute', 'Tour Tokio Blur', 'Tour Paris Promenade', 'Tour London Loop', 'Tour Vancouver Velocity', 'Tour Los Angeles Laps', 'Merry Mountain', 'Tour Berlin Byways', 'Ninja Hideaway', 'Tour Sidney Sprint', 'Tour Singapore Speedway', 'Tour Amsterdam Drift', 'Tour Bangkok Rush', 'Sky-High Sundae', 'Piranha Plant Cove', "Yoshi's Island", 'Tour Athens Dash', 'Tour Rome Avanti', 'Squeaky Clean Sprint', 'Tour Madrid Drive'])
    
    place = st.number_input(label="Place", step=1, min_value=1, max_value=12)

    vr_gain = st.number_input(label="VR Gain", step=1, min_value=-100, max_value=100, value=0)

    if st.button('Insert Race Into Database'):
        cursor = conn.cursor()
        cursor.execute("""
                       INSERT INTO races (race_id, date, character, kart, wheel, glider, track, place, vr_gain)
                       VALUES (?,?,?,?,?,?,?,?,?)
                       """, (get_race_id(conn=conn), get_date(), character, kart, wheel, glider, track, place, vr_gain))
        conn.commit()



elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')