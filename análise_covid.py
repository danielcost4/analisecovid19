# -*- coding: utf-8 -*-
"""Análise Covid

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e9BkD73RaCBC0k53W00qobHRYdJ1Gyiu
"""

#Importando as bibliotecas a serem utilizadas
import pandas as pd
import matplotlib.pyplot as mtplt

#Importando as bases de dados a serem utilizadas
data_deaths = pd.read_csv('/COVID DEATHS.csv')
data_vaccinations = pd.read_csv('/COVID_VACCINATIONS.csv')

# 1. Países que testaram mais pessoas tiveram mais ou menos casos positivos de Covid-19?
correlation_tests_cases = data_vaccinations['new_tests'].corr(data_deaths['new_cases'])
print("Correlação entre novos testes e novos casos:", correlation_tests_cases)

# 2. Os países com maior densidade populacional tiveram maior número de incidências, internações ou mortes?
correlation_density_cases = data_vaccinations['population_density'].corr(data_deaths['new_cases_smoothed'])
correlation_density_hosp = data_vaccinations['population_density'].corr(data_deaths['hosp_patients'])
correlation_density_deaths = data_vaccinations['population_density'].corr(data_deaths['total_deaths'])
print("Correlação entre densidade populacional e novos casos:", correlation_density_cases)
print("Correlação entre densidade populacional e pacientes hospitalizados:", correlation_density_hosp)
print("Correlação entre densidade populacional e total de mortes:", correlation_density_deaths)

# 3. A quantidade de pessoas hospitalizadas diminuiu quando o total de vacinação aumentou?
correlation_hosp_vacc = data_deaths['hosp_patients'].corr(data_vaccinations['total_vaccinations'])
print("Correlação entre pacientes hospitalizados e total de doses de vacinas:", correlation_hosp_vacc)

# Gráfico: Relação entre novos testes e novos casos
mtplt.figure(figsize=(10, 6))
mtplt.scatter(data_vaccinations['new_tests'], data_deaths['new_cases'])
mtplt.xlabel('Novos Testes')
mtplt.ylabel('Novos Casos')
mtplt.title('Relação entre Novos Testes e Novos Casos')
mtplt.tight_layout()
mtplt.show()

# Gráfico: Relação entre densidade populacional e novos casos
mtplt.figure(figsize=(10, 6))
mtplt.scatter(data_vaccinations['population_density'], data_deaths['new_cases_smoothed'])
mtplt.xlabel('Densidade Populacional')
mtplt.ylabel('Novos Casos (suavizados)')
mtplt.title('Relação entre Densidade Populacional e Novos Casos')
mtplt.tight_layout()
mtplt.show()

# Gráfico: Relação entre pacientes hospitalizados e total de doses de vacinas
mtplt.figure(figsize=(10, 6))
mtplt.scatter(data_vaccinations['total_vaccinations'], data_vaccinations['hosp_patients'])
mtplt.xlabel('Total de Doses de Vacinas')
mtplt.ylabel('Pacientes Hospitalizados')
mtplt.title('Relação entre Total de Vacinações e Pacientes Hospitalizados')
mtplt.tight_layout()
mtplt.show()

