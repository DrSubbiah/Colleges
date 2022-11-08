import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

df = pd.read_csv('D:\Varun\Data\daata.csv')

fac = df.Faculty.drop_duplicates()
typ = df.Type.drop_duplicates()

df1 = df.groupby('Type', as_index = 0)['Faculty'].count()
fig1 = px.bar(df1, y = 'Faculty', x='Type')

df2 = df.groupby('Faculty', as_index = 0)['Type'].count()
fig2 = px.bar(df2, x = 'Faculty', y='Type')


def plot_fac(fa):
    fa = str(fa)
    df_fac = df.loc[df['Faculty'] == fa]
    df3 = df_fac.groupby('Type', as_index = 0)['Faculty'].count()
    fig3 = px.bar(df3, x='Type' , y='Faculty')
    return fig3
def plot_type(ty):
    ty = str(typ_sel)
    df_type = df.loc[df['Type'] == ty]
    df4 = df_type.groupby('Faculty', as_index = 0)['Type'].count()
    fig4 = px.bar(df4, x='Faculty', y='Type')
    return fig4
def map(fa):
    fa = str(fa)
    df_fac = df.loc[df['Faculty'] == fa]
    fig = px.scatter_mapbox(df_fac, lat='Lattitude', lon='Longitude', color='Type', hover_name='Name')
    fig.update_layout(mapbox_style="open-street-map")
    return fig
st.title('COLLEGES')
tab1, tab2 = st.tabs(["Plots", "Map Plot"])
with tab1:
    fac_sel = st.selectbox("Select course type: ", fac, key="1")
    st.write('Graphical output for course type selected')
    st.plotly_chart(plot_fac(fac_sel))
    typ_sel = st.selectbox("Select college type: ", typ)
    st.write('Graphical output for college type selected')
    st.plotly_chart(plot_type(typ_sel))
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe.head())
with tab2:
    select1 = st.selectbox("Select course type: ", fac, key="2")
    st.plotly_chart(map(select1))
