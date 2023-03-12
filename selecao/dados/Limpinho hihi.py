#!/usr/bin/env python
# coding: utf-8

# # Declarações

# In[2]:


get_ipython().system('pip install basedosdados')
import basedosdados as bd
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# # ENEM para IDEP

# ## Importando base de dados

# In[ ]:


enem_2019 = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\enem_2019.csv', sep = ',',
                        usecols = ['treineiro', 'nota_lc', 'nota_mt', 'nota_redacao', 'estado'],
                        skiprows = lambda i: i > 0 and random.random() > 0.1)


# ## Removendo treineiros

# In[ ]:


enem_2019 = enem_2019.drop(enem_2019[enem_2019.treineiro == 1].index) #removendo os treineiros ;)
enem_2019.query('treineiro == 1')


# In[ ]:


enem_2019.drop(columns = 'treineiro', inplace = True)
enem_2019.sample(10)


# ## Exportando a base de dados tratada

# In[ ]:


enem_2019.dropna(inplace = True)
enem_2019.describe()
enem_2019.to_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\enem_2019_idep.csv',
                           sep=';', index=False, encoding='utf-8-sig')


# ## Importando base de dados tratada

# In[ ]:


enem_2019_idep = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\enem_2019_idep.csv',
                           sep=';', encoding='utf-8-sig')


# ## Organizando por estado e deixando apropriado para comparar com a base do IDEP

# In[ ]:


enem_2019_idep_uf = enem_2019_idep.groupby('estado')
enem_2019_idep_uf.mean()


# In[ ]:


df_enem_2019_idep_uf = enem_2019_idep_uf.mean().reset_index()
df_enem_2019_idep_uf.rename(columns={'estado': 'sigla_uf'}, inplace=True)
df_enem_2019_idep_uf


# # IDEP
# 

# ## Importando a base do IDEP

# In[ ]:


idep_uf = bd.read_table(dataset_id='br_inep_ideb', table_id='uf', billing_project_id="analytica-desigualdade")


# ## Tratando os dados

# In[ ]:


idep_uf.drop(columns = "indicador_rendimento", inplace = True) #é a mesma coisa que a taxa de aprovação!


# In[ ]:


idep_uf_2019 = idep_uf.query("ano == 2019").drop(columns = 'ano')
idep_2019_total = idep_uf_2019.query("rede == 'total'").drop(columns = 'rede')
idep_2019_fundamentalI = idep_2019_total.query("anos_escolares == 'finais (6-9)'").drop(columns = ['anos_escolares', 'ensino'])
idep_2019_fundamentalII = idep_2019_total.query("anos_escolares == 'iniciais (1-5)'").drop(columns = ['anos_escolares', 'ensino'])
idep_2019_medio = idep_2019_total.query("anos_escolares == 'todos (1-4)'").drop(columns = ['anos_escolares', 'ensino'])


# ## Exportando as base de dados tratadas

# In[ ]:


idep_2019_fundamentalI.to_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\idep_fundamentalI_2019.csv',
                           sep=';', index=False, encoding='utf-8-sig')
idep_2019_fundamentalII.to_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\idep_fundamentalII_2019.csv',
                           sep=';', index=False, encoding='utf-8-sig')
idep_2019_medio.to_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\idep_medio_2019.csv',
                           sep=';', index=False, encoding='utf-8-sig')


# ## Importando as bases de dados tratadas

# In[ ]:


idep_2019_fundamentalI = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\idep_fundamentalI_2019.csv',
                                     sep=';')
idep_2019_fundamentalII = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\idep_fundamentalII_2019.csv',
                           sep=';')
idep_2019_medio = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\idep_medio_2019.csv',
                           sep=';')


# # Unindo os datasets

# In[ ]:


idep_2019_fundamentalI_mat  = idep_2019_fundamentalI.loc[:, ['sigla_uf', 'nota_saeb_matematica']].reset_index().drop(columns = 'index')
idep_2019_fundamentalII_mat = idep_2019_fundamentalII.loc[:, ['sigla_uf', 'nota_saeb_matematica']].reset_index().drop(columns = 'index')
idep_2019_medio_mat         = idep_2019_medio.loc[:, ['sigla_uf', 'nota_saeb_matematica']].reset_index().drop(columns = 'index')
df_enem_2019_cat_renda_por_uf_mat = df_enem_2019_cat_renda_por_uf.loc[:, ['sigla_uf', 'nota_mt']]
matematica_2019 = pd.merge(idep_2019_fundamentalI_mat, idep_2019_fundamentalII_mat, on='sigla_uf')
matematica_2019 = pd.merge(matematica_2019, idep_2019_medio_mat, on='sigla_uf')
matematica_2019 = pd.merge(matematica_2019, df_enem_2019_cat_renda_por_uf_mat, on='sigla_uf')
matematica_2019.rename(columns = {'nota_saeb_matematica_x': 'nota_saeb_fundamentalI', 'nota_saeb_matematica_y': 'nota_saeb_fundamentalII',
                                 'nota_saeb_matematica': 'nota_saeb_medio', 'nota_mt': 'enem'}, inplace=True)
matematica_2019


# In[ ]:


idep_2019_fundamentalI_por  = idep_2019_fundamentalI.loc[:, ['sigla_uf', 'nota_saeb_lingua_portuguesa']].reset_index().drop(columns = 'index')
idep_2019_fundamentalII_por = idep_2019_fundamentalII.loc[:, ['sigla_uf', 'nota_saeb_lingua_portuguesa']].reset_index().drop(columns = 'index')
idep_2019_medio_por         = idep_2019_medio.loc[:, ['sigla_uf', 'nota_saeb_lingua_portuguesa']].reset_index().drop(columns = 'index')
df_enem_2019_cat_renda_por_uf_port = df_enem_2019_cat_renda_por_uf.loc[:, ['sigla_uf', 'nota_lc']]
portugues_2019 = pd.merge(idep_2019_fundamentalI_por, idep_2019_fundamentalII_por, on='sigla_uf')
portugues_2019 = pd.merge(portugues_2019, idep_2019_medio_por, on='sigla_uf')
portugues_2019 = pd.merge(portugues_2019, df_enem_2019_cat_renda_por_uf_port, on='sigla_uf')
portugues_2019.rename(columns = {'nota_saeb_lingua_portuguesa_x': 'nota_saeb_fundamentalI', 'nota_saeb_lingua_portuguesa_y': 'nota_saeb_fundamentalII',
                                 'nota_saeb_lingua_portuguesa': 'nota_saeb_medio', 'nota_lc': 'enem'}, inplace=True)
portugues_2019


# In[ ]:


idep_2019_fundamentalI_por  = idep_2019_fundamentalI.loc[:, ['sigla_uf', 'nota_saeb_lingua_portuguesa']].reset_index().drop(columns = 'index')
idep_2019_fundamentalII_por = idep_2019_fundamentalII.loc[:, ['sigla_uf', 'nota_saeb_lingua_portuguesa']].reset_index().drop(columns = 'index')
idep_2019_medio_por         = idep_2019_medio.loc[:, ['sigla_uf', 'nota_saeb_lingua_portuguesa']].reset_index().drop(columns = 'index')
df_enem_2019_cat_renda_por_uf_red = df_enem_2019_cat_renda_por_uf.loc[:, ['sigla_uf', 'nota_redacao']]
portugues_2019 = pd.merge(idep_2019_fundamentalI_por, idep_2019_fundamentalII_por, on='sigla_uf')
portugues_2019 = pd.merge(portugues_2019, idep_2019_medio_por, on='sigla_uf')
redacao_2019 = pd.merge(portugues_2019, df_enem_2019_cat_renda_por_uf_red, on='sigla_uf')
redacao_2019.rename(columns = {'nota_saeb_lingua_portuguesa_x': 'nota_saeb_fundamentalI', 'nota_saeb_lingua_portuguesa_y': 'nota_saeb_fundamentalII',
                                 'nota_saeb_lingua_portuguesa': 'nota_saeb_medio', 'nota_redacao': 'enem'}, inplace=True)
redacao_2019


# ## Exportando as bases de dados

# In[ ]:


portugues_2019.to_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\portugues_2019.csv',
                           sep=';', index=False, encoding='utf-8-sig')
matematica_2019.to_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\matematica_2019.csv',
                           sep=';', index=False, encoding='utf-8-sig')
redacao_2019.to_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\redacao_2019.csv',
                           sep=';', index=False, encoding='utf-8-sig')


# ## Importando as bases de dados

# In[ ]:


portugues_2019 = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\portugues_2019.csv',
                           sep=';')
matematica_2019 = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\matematica_2019.csv',
                           sep=';')
redacao_2019 = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\redacao_2019.csv',
                           sep=';')


# ## Explorando as bases de dados

# In[ ]:


portugues_2019.corr() 
#base importa muito! mas quanto mais próximo, mais correlação esses dois exames têm em português, embora menos que matemática
#em todos os casos, a correlação é forte!


# In[ ]:


plt.matshow(portugues_2019.corr())
plt.show()


# In[ ]:


matematica_2019.corr() 
#base importa muito! mas quanto mais próximo, mais correlação esses dois exames têm em matemática. 
#em todos os casos a correlação é forte!


# In[ ]:


plt.matshow(matematica_2019.corr())
plt.show()


# In[ ]:


redacao_2019.corr() #redação não tem tanta correlação com estudar português - correlação moderada (!!!)


# In[ ]:


plt.matshow(redacao_2019.corr())
plt.show()


# ### Conclusão: Estudo de base sólido tem uma correlação forte no desempenho do enem. Naturalmente, quão mais próximas temporamente elas forem, mais forte será o impacto. Vemos que isso especialmente se dá em matemática, que é uma matéria cheia de pré-requisitos, os quais sem eles, o aluno pode se perder conforme o tempo passa e não só se desinteressar na matéria, mas também não assimilar novos conhecimentos. Embora o português não tenha esse caráter, ainda é de forte correlação o quanto o estado dedica nos ensinos primários e seu desempenho no ENEM. Finalmente, o estudo de base em português tem uma correlação moderada com as notas de redação do ENEM; talvez isso se dê pelo fato da redação do ENEM ter como apenas uma competência a gramática, representando 1/5 da nota. De forma geral, o resumo é que aqueles estados que se dedicam nos ensinos de base são recompensados com boas notas no ENEM.

# # Explorando a base de dados do IDEP

# ## Importando as base de dados tratadas

# In[ ]:


idep_2019_fundamentalI = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\idep_fundamentalI_2019.csv',
                                     sep=';')
idep_2019_fundamentalII = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\idep_fundamentalII_2019.csv',
                           sep=';')
idep_2019_medio = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\idep_medio_2019.csv',
                           sep=';')


# In[ ]:


idep_2019_fundamentalI.boxplot('taxa_aprovacao')


# In[ ]:


idep_2019_fundamentalII.boxplot('taxa_aprovacao')


# In[ ]:


idep_2019_medio.boxplot('taxa_aprovacao')


# ### Não há outliers!

# In[ ]:


idep_2019_fundamentalI_sorted = idep_2019_fundamentalI.sort_values("taxa_aprovacao")

plt.rc('figure', figsize = (20, 10))

fig = plt.bar(idep_2019_fundamentalI_sorted['sigla_uf'], idep_2019_fundamentalI_sorted['taxa_aprovacao'])
plt.ylabel("Taxa de aprovação (%)", fontsize = 30)
plt.title("Taxa de aprovação do IDEP fundamental I por estado", fontsize = 40, pad = 20)


# In[ ]:


idep_2019_fundamentalII_sorted = idep_2019_fundamentalII.sort_values("taxa_aprovacao")

plt.bar(idep_2019_fundamentalII_sorted['sigla_uf'], idep_2019_fundamentalII_sorted['taxa_aprovacao'])
plt.ylabel("Taxa de aprovação (%)", fontsize = 30)
plt.title("Taxa de aprovação do IDEP fundamental II por estado", fontsize = 40, pad = 20)


# In[ ]:


idep_2019_medio_sorted = idep_2019_medio.sort_values("taxa_aprovacao")

fig = plt.gcf()

fig.set_size_inches(18.5, 10.5)
plt.bar(idep_2019_medio_sorted['sigla_uf'], idep_2019_medio_sorted['taxa_aprovacao'])
plt.ylabel("Taxa de aprovação (%)", fontsize = 30)
plt.title("Taxa de aprovação do IDEP no ensino médio por estado", fontsize = 35, pad = 20)


# # Explorando a base de dados do ENEM por gênero

# ## Importando base de dados

# In[3]:


enem_2019 = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\enem_2019.csv', sep = ',',
                        usecols = ['sexo', 'treineiro', 'nota_lc', 'nota_mt', 'nota_ct', 'nota_ch', 'estado'],
                        skiprows = lambda i: i > 0 and random.random() > 0.1)


# ## Removendo os treineiros e padronizando o nome das colunas

# In[4]:


enem_2019 = enem_2019.drop(enem_2019[enem_2019.treineiro == 1].index) #removendo os treineiros ;)
enem_2019 = enem_2019.drop(columns = 'treineiro').rename(columns = {'estado': 'sigla_uf'}).dropna()
enem_2019


# ## Agrupando por gênero

# In[5]:


enem_2019['media'] = (enem_2019.nota_ct + enem_2019.nota_ch + enem_2019.nota_mt + enem_2019.nota_lc)/4
enem_2019


# In[11]:


ax = sns.displot(enem_2019_genero['media'], height=8, kind='kde', hue=enem_2019_genero.sigla_uf)

ax.set(title ='Distribuição de frequência da renda mensal', 
       xlabel='Categoria da renda mensal', ylabel='Quantidade de participantes') 


# In[6]:


enem_2019_genero = enem_2019.groupby(by='sexo')


# In[8]:


for item, sexo in enem_2019_genero:
    print(enem_2019_genero.get_group(item))


# In[ ]:


ax = sns.displot(enem_2019_renda['renda_mensal_familiar'], height=8, kind='kde', )

ax.set(title ='Distribuição de frequência da renda mensal', 
       xlabel='Categoria da renda mensal', ylabel='Quantidade de participantes') 


# # Separar os datasets em M e F

# # Número médio de horas semanais dedicadas aos cuidados de pessoas e/ou afazeres domésticos das pessoas de 14 anos ou mais de idade ocupadas na semana de referência por sexo segundo Unidades da Federação

# In[12]:


trabalho_domestico = pd.read_excel(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\horas_dedicadas_trabalho_domestico.xlsx')


# In[13]:


trabalho_domestico_total = trabalho_domestico.loc[:, ['sigla_uf', 'M', 'F']].drop([27], 0).reset_index().drop(columns = 'index').set_index('sigla_uf')
trabalho_domestico_total


# # Unindo bases de dados

# In[14]:


relacao_nota_trabalho_domestico = enem_2019.merge(trabalho_domestico_total, on='sigla_uf')
relacao_nota_trabalho_domestico


# In[15]:


relacao_nota_trabalho_domestico['horas_semanais_trabalho_domestico'] = np.where(relacao_nota_trabalho_domestico['sexo'] == 'M', 
                                                                                relacao_nota_trabalho_domestico['M'], 
                                                                                relacao_nota_trabalho_domestico['F'])
relacao_nota_trabalho_domestico.drop(columns = ['M','F'], inplace=True)


# In[16]:


relacao_nota_trabalho_domestico


# In[17]:


relacao_nota_trabalho_domestico.groupby("sigla_uf").corr().query('horas_semanais_trabalho_domestico == 1.0')


# In[33]:


relacao_nota_trabalho_domestico.info()


# In[41]:


ax = sns.scatterplot(data=relacao_nota_trabalho_domestico, x='horas_semanais_trabalho_domestico', y='media', hue='sexo')

sns.set(rc={'figure.figsize':(15,10)})
ax.set(title ='Distribuição da media do ENEM com base nas horas semanais médias trabalhadas em casa por estado e gênero', 
       xlabel='Quantidade de horas dedicadas a afazeres domésticos na semana estudada', ylabel='Média simples da nota do ENEM') 


# ###  Minha hipótese era de que as notas mais baixas por parte da média das mulheres em relação aos homens era porque, no Brasil, mulheres dedicam mais horas com afazeres domésticos do que homens. Porém, como foi evidenciado no gráfico acima, a quantidade média de horas por estado não é suficiente para explicar a diferença das notas. Talvez se pudesse ser analisado individualmente a quantidade que cada pessoa levou se dedicando a afazeres doméstiocs ao invés de uma média generalista, o resultado fosse diferente. Porém, não foi o caso, então nada podemos concluir a partir disso

# # Correlacionar renda com sucesso
# 

# In[69]:


enem_2019_renda_mensal = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\enem_2019.csv',
                                     sep = ',', usecols = ['renda_mensal_familiar', 'treineiro', 'nota_lc', 'nota_mt', 'nota_ct',
                                                           'nota_ch'],
                                     skiprows = lambda i: i > 0 and random.random() > 0.1)


# In[70]:


enem_2019_renda_mensal = enem_2019_renda_mensal.drop(enem_2019_renda_mensal[enem_2019_renda_mensal.treineiro == 1].index)
enem_2019_renda_mensal = enem_2019_renda_mensal.drop(columns = 'treineiro').rename(columns = {'estado': 'sigla_uf'}).dropna()
enem_2019_renda_mensal


# In[60]:


enem_2019_renda_mensal.renda_mensal_familiar.unique()


# In[61]:


enem_2019_renda_mensal.renda_mensal_familiar.nunique()


# In[71]:


enem_2019_renda = enem_2019_renda_mensal.replace({'Nenhuma Renda': 0, '<= 998.00': 1, '998.00 até 1497.00': 2, 
                                                      '1497.00 até 1996.00': 3, '1996.00 até 2495.00': 4,
                                                      '2495.00 até 2994.00': 5, '2994.00 até 3992.00': 6,
                                                      '3992.00 até 4990.00': 7, '4990.00 até 5988.00': 8,
                                                      '5988.00 até 6986.00': 9, '6986.00 até 7984.00': 10,
                                                      '7984.00 até 8982.00': 11, '8982.00 até 9980.00': 12,
                                                      '9980.00 até 11976.00': 13, '11976.00 até 14970.00': 14,
                                                      '14970.00 até 19960.00': 15, '>= 19960.00': 16}
                                                    )
enem_2019_renda
enem_2019_renda.to_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\enem_2019_renda.csv',
                           sep=';', index=False, encoding='utf-8-sig')


# In[2]:


enem_2019_renda = pd.read_csv(r'C:\Users\Lenovo\OneDrive\Documentos\Ciência_da_Computação\Analytica\Dados\enem_2019_renda.csv',
                           sep=';', encoding='utf-8-sig')
enem_2019_renda


# In[21]:


ax = sns.displot(enem_2019_renda['renda_mensal_familiar'], height=8)

ax.set(title ='Distribuição de frequência da renda mensal', 
       xlabel='Categoria da renda mensal', ylabel='Quantidade de participantes') 


# In[74]:


enem_2019_renda.corr()


# ### Explicação

# # Escola pública vs privada

# In[54]:


idep_uf = bd.read_table(dataset_id='br_inep_ideb', table_id='uf', billing_project_id="analytica-desigualdade")
idep_uf.drop(columns = "indicador_rendimento", inplace = True) #é a mesma coisa que a taxa de aprovação!


# In[62]:


idep_2019


# In[69]:


idep_uf_2019 = idep_uf.query("ano == 2019").drop(columns = 'ano')
idep_2019_total = idep_uf_2019.query("anos_escolares == 'todos (1-4)'").drop(columns = ['anos_escolares', 'ensino'])
idep_2019_total = idep_2019_total.query("rede != 'total'")
idep_2019_total


# In[70]:


idep_2019_total.groupby('rede')

