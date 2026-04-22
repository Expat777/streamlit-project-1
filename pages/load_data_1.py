import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


uploaded_file = st.file_uploader(
    'load file on format CSV',
    type=['csv']
    )

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    dfs = {
        'male': df[df['customer_gender'] == 'male'],
        'female':df[df['customer_gender'] == 'female'],
    }
    
    for title, data in dfs.items():
        data.drop(columns=['customer_gender'], inplace=True)
        st.subheader(f'SData {title}:')

        st.dataframe(data)
    

    fig, ax = plt.subplots()
    ax.hist(dfs['male']['customer_age'])
    ax.set_title('распределение по возрасту у мужчин')


    st.pyplot(fig)

    st.bar_chart(data=dfs['male'], x='country', y='customer_age')

    f_df = dfs['female']

    st.line_chart(data=f_df[f_df['revenue'] > 1000], y='revenue', x='customer_age')