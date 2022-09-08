import streamlit as st
option = st.selectbox(
'What chart do you want to see?',
('Pie Chart & Bar Chart', 'Histogram', 'Box Plot & Column Chart'))

st.write('You selected:', option)