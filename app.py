import pandas as pd
import streamlit as st
from datetime import timedelta, datetime
from factory_method import drug_formatter_factory  # chama o Factory


st.set_page_config(page_title = "Apreensões de Entorpecentes em Fortaleza",
                   layout = "wide",
                   page_icon="https://acervo.fortaleza.ce.gov.br/assets/images/Logo_PMF_Ver_Col_Preto.svg",)

# Obtem os dados
@st.cache_data
def obtem_data():
    data = pd.read_csv("FortalezaEntorpecente_2009-2024.csv")
    data['Data'] = pd.to_datetime(data['Data'])
    data['Dia'] = data['Data'].dt.day
    data['Mês'] = data['Data'].dt.month
    data['Ano'] = data['Data'].dt.year
    return data

data = obtem_data()

st.title("Apreensões de Entorpecentes em Fortaleza")

st.logo(image="https://acervo.fortaleza.ce.gov.br/assets/images/Logo_PMF_Hor_Col_Preto.svg",
        icon_image="https://acervo.fortaleza.ce.gov.br/assets/images/Logo_PMF_Ver_Col_Preto.svg")


with st.sidebar:
    st.title("Apreensão de drogas 🧪")
    st.header("⚙️ Parâmetros")

    max_date = data['Data'].max().date()
    padrao_data_inicial = data["Data"].min().date()  # Padroniza a data inicial
    padrao_data_final = max_date
    start_date = st.date_input("Data inicial", padrao_data_inicial, min_value=data['Data'].min().date(), max_value=max_date)
    end_date = st.date_input("Data final", padrao_data_final, min_value=data['Data'].min().date(), max_value=max_date)
    time_frame = st.selectbox("Select time frame", ("Diário", "Mensal", "Anual"))

    st.markdown("---")  # Linha horizontal separando o "rodapé"
    st.markdown("📝 **Dados fornecidos pela Secretaria da Segurança Pública e Defesa Social do Estado do Ceará**")
    st.markdown("📅 **Ano de referência: 2009 - 2024**")
    st.markdown("🔗 [Fonte](https://www.sspds.ce.gov.br/estatisticas-2-3/)")
    st.markdown("🔗 [Github](https://github.com/emanuelj0rdan/apreensoes_dashboard)")

data = obtem_data()

# Converte as datas de entrada
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filtra o DataFrame pelo intervalo/período selecionado
filtered_data = data[(data['Data'] >= start_date) & (data['Data'] <= end_date)]

# Filtra pelo tipo de droga
drug_type = st.selectbox("Selecione o tipo de droga", filtered_data['Tipo de Entorpecente'].unique())

filtered_data = filtered_data[filtered_data['Tipo de Entorpecente'] == drug_type]

# Cria o formatador apropriado/"instancia" o objeto
formatter = drug_formatter_factory(drug_type, filtered_data)

# Mostra o gráfico conforme o tempo/período escolhido
if time_frame == 'Diário':
    formatter.generate_diario()
elif time_frame == 'Mensal':
    formatter.generate_mensal()
elif time_frame == 'Anual':
    formatter.generate_anual()

# Atribui os valores das variáveis que serão usadas como métricas
maior = formatter.format_data()['Quantidade (Kg)'].max()
dia_maior_valor_unico = filtered_data.loc[filtered_data['Quantidade (Kg)'].idxmax()]['Data'].date()
soma = formatter.format_data()['Quantidade (Kg)'].sum()
media_anual = formatter.format_data()['Quantidade (Kg)'].sum()/len(filtered_data["Data"].dt.year.unique())

# Métricas
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total apreendido (KG)", value=round(soma))

with col2:
    st.metric(label="Maior valor único apreendido (KG)", value=str(round(maior)), 
              delta = str(dia_maior_valor_unico), delta_color="off")
    
with col3:
    st.metric(label="Média por ano (KG)", value=round(media_anual))
