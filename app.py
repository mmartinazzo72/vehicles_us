import pandas as pd
import streamlit as st
import plotly.express as px

# lendo o arquivo de dados
car_data = pd.read_csv('data/vehicles_us.csv')

# criar um título para a página web
st.header('Análise de Anúncios de Veículos nos EUA')

# criar um botão para gerar um histograma
hist_button = st.button('Criar histograma')

# se o botão histograma for clicado
if hist_button:
    
    # mensagem para que o usuário saiba o que está acontecendo
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um histograma com os dados de odometro dos anúncios constantes no dataframe
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)


# criar um botão para gerar um gráfico de dispersão
dispersao_button = st.button('Criar gráfico de dispersão')

# se o botão gráfico de dispersão for clicado
if dispersao_button:
    
    # mensagem para que o usuário saiba o que está acontecendo
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
            
    # criar um gráfico de dispersão com os dados de odometro vs price dos anúncios constantes no dataframe
    fig = px.scatter(car_data, x="odometer", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)