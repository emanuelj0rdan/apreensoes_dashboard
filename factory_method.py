import streamlit as st
import plotly.express as px
from abc import ABC, abstractmethod

# Interface base para as drogas
class DrugFormatter(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def format_data(self):
        pass

    @abstractmethod
    def generate_diario(self):
        pass

    @abstractmethod
    def generate_mensal(self):
        pass

    @abstractmethod
    def generate_anual(self):
        pass

# Implementação para cada droga
# Basicamente cria um gráfico de barra pra cada período(diário, mensal e anual)
class CrackFormatter(DrugFormatter):
    def format_data(self):
        return self.data[self.data['Tipo de Entorpecente'] == 'Crack']
        
    def generate_diario(self):
        daily_data = self.format_data().groupby('Dia')['Quantidade (Kg)'].sum().reset_index()
        fig = px.bar(daily_data, x='Dia', y='Quantidade (Kg)', 
                 title='Apreensões de Crack ☠️: Total acumulado por dia do mês',
                 labels={'Dia': 'Datas', 'Quantidade (Kg)': 'Kilos apreendidos'},
                 color_discrete_sequence=['#acb255'])
        st.plotly_chart(fig, theme="streamlit")
        
    def generate_mensal(self):
        daily_data = self.format_data().groupby('Mês')['Quantidade (Kg)'].sum().reset_index()
        fig = px.bar(daily_data, x='Mês', y='Quantidade (Kg)', 
                 title='Apreensões de Crack ☠️: Total acumulado por meses do ano',
                 labels={'Mês': 'Datas', 'Quantidade (Kg)': 'Kilos apreendidos'},
                 color_discrete_sequence=['#acb255'])
        st.plotly_chart(fig, theme="streamlit")
        
    def generate_anual(self):
        daily_data = self.format_data().groupby('Ano')['Quantidade (Kg)'].sum().reset_index()
        fig = px.bar(daily_data, x='Ano', y='Quantidade (Kg)', 
                 title='Apreensões de Crack ☠️: Total acumulado ao longo dos anos',
                 labels={'Ano': 'Datas', 'Quantidade (Kg)': 'Kilos apreendidos'},
                 color_discrete_sequence=['#acb255'])
        st.plotly_chart(fig, theme="streamlit")

class MaconhaFormatter(DrugFormatter):
    def format_data(self):
        return self.data[self.data['Tipo de Entorpecente'] == 'Maconha']

    def generate_diario(self):
        daily_data = self.format_data().groupby('Dia')['Quantidade (Kg)'].sum().reset_index()
        fig = px.bar(daily_data, x='Dia', y='Quantidade (Kg)', 
                 title='Apreensões de Maconha 🍁: Total acumulado por dia do mês',
                 labels={'Dia': 'Dia', 'Quantidade (Kg)': 'Kilos apreendidos'},
                 color_discrete_sequence=['#219607'])
        st.plotly_chart(fig, theme="streamlit")
        
    def generate_mensal(self):
        daily_data = self.format_data().groupby('Mês')['Quantidade (Kg)'].sum().reset_index()
        fig = px.bar(daily_data, x='Mês', y='Quantidade (Kg)', 
                 title='Apreensões de Maconha 🍁: Total acumulado por meses do ano',
                 labels={'Mês': 'Meses', 'Quantidade (Kg)': 'Kilos apreendidos'},
                 color_discrete_sequence=['#219607'])
        st.plotly_chart(fig, theme="streamlit")
        
    def generate_anual(self):
        daily_data = self.format_data().groupby('Ano')['Quantidade (Kg)'].sum().reset_index()
        fig = px.bar(daily_data, x='Ano', y='Quantidade (Kg)', 
                 title='Apreensões de Maconha 🍁: Total acumulado ao longo dos anos',
                 labels={'Ano': 'Ano', 'Quantidade (Kg)': 'Kilos apreendidos'},
                 color_discrete_sequence=['#219607'])
        st.plotly_chart(fig, theme="streamlit")

class CocainaFormatter(DrugFormatter):
    def format_data(self):
        return self.data[self.data['Tipo de Entorpecente'] == 'Cocaína']

    def generate_diario(self):
        daily_data = self.format_data().groupby('Dia')['Quantidade (Kg)'].sum().reset_index()
        fig = px.bar(daily_data, x='Dia', y='Quantidade (Kg)', 
                 title='Apreensões de Cocaína 👃: Total acumulado por dia do mês',
                 labels={'Dia': 'Dia', 'Quantidade (Kg)': 'Kilos apreendidos'},
                 color_discrete_sequence=['#c5b693'])
        st.plotly_chart(fig, theme="streamlit")
        
    def generate_mensal(self):
        daily_data = self.format_data().groupby('Mês')['Quantidade (Kg)'].sum().reset_index()
        fig = px.bar(daily_data, x='Mês', y='Quantidade (Kg)', 
                 title='Apreensões de Cocaína 👃: Total acumulado por meses do ano',
                 labels={'Mês': 'Meses', 'Quantidade (Kg)': 'Kilos apreendidos'},
                 color_discrete_sequence=['#c5b693'])
        st.plotly_chart(fig, theme="streamlit")
        
    def generate_anual(self):
        daily_data = self.format_data().groupby('Ano')['Quantidade (Kg)'].sum().reset_index()
        fig = px.bar(daily_data, x='Ano', y='Quantidade (Kg)', 
                 title='Apreensões de Cocaína 👃: Total acumulado ao longo dos anos',
                 labels={'Ano': 'Ano', 'Quantidade (Kg)': 'Kilos apreendidos'},
                 color_discrete_sequence=['#c5b693'])
        st.plotly_chart(fig, theme="streamlit")

class HaxixeFormatter(DrugFormatter):
    def format_data(self):
        return self.data[self.data['Tipo de Entorpecente'] == 'Haxixe']

    def generate_diario(self):
        daily_data = self.format_data().groupby('Dia')['Quantidade (Kg)'].sum().reset_index()
        fig = px.bar(daily_data, x='Dia', y='Quantidade (Kg)', 
                 title='Apreensões de Haxixe 🟤: Total acumulado por dia do mês',
                 labels={'Dia': 'Dia', 'Quantidade (Kg)': 'Kilos apreendidos'},
                 color_discrete_sequence=['#b98c1e'])
        st.plotly_chart(fig, theme="streamlit")
        
    def generate_mensal(self):
        daily_data = self.format_data().groupby('Mês')['Quantidade (Kg)'].sum().reset_index()
        fig = px.bar(daily_data, x='Mês', y='Quantidade (Kg)', 
                 title='Apreensões de Haxixe 🟤: Total acumulado por meses do ano',
                 labels={'Mês': 'Meses', 'Quantidade (Kg)': 'Kilos apreendidos'},
                 color_discrete_sequence=['#b98c1e'])
        st.plotly_chart(fig, theme="streamlit")
        
    def generate_anual(self):
        daily_data = self.format_data().groupby('Ano')['Quantidade (Kg)'].sum().reset_index()
        fig = px.bar(daily_data, x='Ano', y='Quantidade (Kg)', 
                 title='Apreensões de Haxixe 🟤: Total acumulado ao longo dos anos',
                 labels={'Ano': 'Ano', 'Quantidade (Kg)': 'Kilos apreendidos'},
                 color_discrete_sequence=['#b98c1e'])
        st.plotly_chart(fig, theme="streamlit")

# Factory para os formatadores
def drug_formatter_factory(drug_type, data):
    if drug_type == 'Crack':
        return CrackFormatter(data)
    elif drug_type == 'Maconha':
        return MaconhaFormatter(data)
    elif drug_type == 'Cocaína':
        return CocainaFormatter(data)
    elif drug_type == 'Haxixe':
        return HaxixeFormatter(data)
    else:
        raise ValueError("Tipo de droga não suportado")
