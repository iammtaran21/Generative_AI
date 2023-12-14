import LC_
import streamlit as st 
st.title("Restos & Appetite")
cousine=st.sidebar.selectbox('Pick a cousine',options=('Indian','Mexican','French','Indori','South Indian'))

if cousine:
    response=LC_.resto_names_items(cousine)
    st.header(response['resto_name'].strip())
    resto_items=response['resto_items'].strip().split(',')
    st.write("**Items**")
    for i in resto_items:
        st.write('-',i)
    