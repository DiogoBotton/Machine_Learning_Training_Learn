# Para iniciar a aplicação Streamlit:
# streamlit run App.py

import streamlit as st
import pandas as pd
import joblib
import os

# Adquire todos os arquivos necessários para realizar o agrupamento dos novos dados
main_path = os.path.dirname(__file__)
encoder = joblib.load(os.path.join(main_path, 'encoder.pkl'))
scaler = joblib.load(os.path.join(main_path, 'scaler.pkl'))
kmeans = joblib.load(os.path.join(main_path, 'model_kmeans.pkl'))

st.title('Grupos de interesse para marketing')
st.write("""
         Neste projeto, aplicamos o algoritmo de clusterização K-means para identificar e prever agrupamentos de interesses de usuários, com o objetivo de direcionar campanhas de marketing de forma mais eficaz.
         Através dessa análise, conseguimos segmentar o público em bolhas de interesse, permitindo a criação de campanhas personalizadas e mais assertivas, com base nos padrões de comportamento e preferências de cada grupo.
         """)

# Planilha csv com os novos dados a serem previstos
up_file = st.file_uploader('Escolha um arquivo CSV para realizar a previsão.', type='csv')

def processar_prever(df):
    # Realiza o encoder da coluna "sexo"
    encoded_sexo = encoder.fit_transform(df[['sexo']])

    # Cria o dataframe com as colunas com os diferentes generos
    encoded_df = pd.DataFrame(encoded_sexo, columns=encoder.get_feature_names_out(['sexo']))

    # Junta os dois dataframes
    df_encoded = pd.concat([df, encoded_df], axis=1)

    # Remove a coluna "sexo"
    df_encoded.drop('sexo', axis=1, inplace=True)

    # Realiza a normalização dos dados numéricos
    scaled_data_array = scaler.fit_transform(df_encoded)

    # Converte os dados para um Dataframe novamente
    df_scaled = pd.DataFrame(scaled_data_array, columns=df_encoded.columns)

    # Faz a previsão dos clusters (agrupamentos) com os novos dados
    cluster_predict = kmeans.predict(df_scaled)

    return cluster_predict

if up_file is not None:

    st.write("""
                ### Descrição dos Grupos:
                - **Grupo 0** é focado em um público jovem com forte interesse em moda, música e aparência.
                - **Grupo 1** está muito associado a esportes, especialmente futebol americano, basquete e atividades culturais como banda e rock.
                - **Grupo 2** é mais equilibrado, com interesses em música, dança, e moda.
            """)
   
    # Lê o arquivo csv enviado
    df = pd.read_csv(up_file)

    # Envia o csv para processamento e posteriormente realizar a previsão dos agrupamentos
    cluster = processar_prever(df)

    # Adiciona no csv enviado os clusters retornados
    # 1° param. Qual o indice da coluna (no caso, no início)
    # 2° param. Nome da coluna
    # 3° param. Dados
    df.insert(0, 'grupos', cluster)

    # Exibe os 10 primeiros registros do dataframe
    st.write("Visualização dos resultados (10 primeiros registros):")
    st.write(df.head(10))

    # Converte o dataframe para um csv
    csv = df.to_csv(index=False)

    # Botão para realizar o download do csv com os dados de agrupamentos
    st.download_button(label='Baixar resultado completo', 
                       data=csv, 
                       file_name='grupos_interesse.csv', 
                       mime='text/csv')