#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PRIMER PASO: IMPORTAR LIBERIAS
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#PARA MODIFICAR LOS ESTILOS DE MATPLOTLIB
mpl.style.use('bmh')


# In[2]:


#SEGUNDO PASO: IMPORTAR BASE DE DATOS DE ARCHIVO EXCEL
#donde debemos crear una variable en el que se almacenara ducho archivo

basedatos=pd.read_excel(r'C:\Users\garro\OneDrive\Escritorio\DATA SCIENCE\TRABAJO PRACTICO\ViolenciaGenero2.0.xlsx', sheet_name='casos')
basedatos['FECHA'] = pd.to_datetime(basedatos['FECHA'], format = '%Y-%m-%d %H:%M')


# In[3]:


#TERCER PASO: VERFICAMOS SI SE REALIZÓ LA CARGA A PARTIR DE M0STRAR LOS PRIMEROS CINCO DATOS
#(donde la primer fila son los nombres de las columnas, por lo que se mstraran cuatro filas con datos)

basedatos.head()


# In[4]:


#CUARTO PASO
#DETERMINAMOS LA COLUMNA "FECHA" COMO INDEX
basedatos.index=basedatos['FECHA']
#ELIMINAMOS LA COLUMNA INDEX ORIGINAL
basedatos=basedatos.drop('FECHA',axis='columns')
basedatos


# In[5]:


#APLICAMOS FORMATO DATE A LA COLUMNA 'FECHA'
basedatos.index = pd.to_datetime(basedatos.index, errors='coerce')
basedatos.head


# In[6]:


#QUINTO PASO:REALIZAMOS LOS PRIMEROS TRES GRAFICOS CON MATPLOTLIT
#REALIZAMOS UN GRÁFICO DE TORTA PARA ANLIZAR LOS PORCENTAJES

vinculo=basedatos.groupby('VINCULO_PERSONA_AGRESORA')
cant=basedatos.groupby(basedatos.VINCULO_PERSONA_AGRESORA)['CASO'].count()
cant 


# In[7]:


suma=sum(cant)
porcentaje=(cant*100)/suma
porcentaje


# In[8]:


fig1, ax1 = plt.subplots()
#Creamos el grafico, añadiendo los valores
ax1.pie(porcentaje,labels=cant, autopct='%1.1f%%', shadow=True, startangle=90)
#señalamos la forma, en este caso 'equal' es para dar forma circular
ax1.axis('equal')
plt.title('Distribución de vinculo de agresor')
plt.legend()
plt.savefig('grafica_pastel.png')
plt.show()


# #SEGUNDO GRAFICO: ANALIZAMOS LA VARIACIÓN DE LA CANTIDAD DE CASOS EN FUNCION DEL TIEMPO (en meses) 
# #DEFINIMOS NUESTROS EJES
# x = basedatos.groupby(basedatos.index)
# 
# #cantcasos= basedatos.groupby(basedatos.index).size() #CANTIDAD DE CASOS MENSUALES
# cantcasos=basedatos.groupby(basedatos.index)['CASO'].count()
# cantcasos

# #DEFINIMOS LOS OBJETOS
# fig, ax= plt.subplots(figsize=(12,4))
# ax.plot(x, cantcasos, label='Cantidad de casos mensuales')
# 
# #DETERMINAMOS NOMBRE A EJES, INSERTAMOS TITULO Y LEYENDA
# ax.set_xlabel('Año')                  
# ax.set_ylabel('Cantidad de casos')
# ax.set_title('Cantidad de casos según el año')
# ax.legend() 

# In[9]:


#SEGUNDO GRAFICO: REALIZAMOS UNA CATEGORIZACIÓN DE GÉNERO DE LAS VICTIMAS
genero=basedatos.groupby('GENERO_PERSONA_SIT_VIOLENCIA').count()
genero_cant=basedatos.groupby(basedatos.GENERO_PERSONA_SIT_VIOLENCIA)['CASO'].count()
genero_cant


# In[10]:


total=sum(genero_cant)
porcentaje_genero=(genero_cant*100)/total
porcentaje_genero


# In[11]:


fig1, ax1 = plt.subplots()
#Creamos el grafico, añadiendo los valores
desfase = (0, 0.5, 0.5, 0.5)
ax1.pie(porcentaje_genero, labels=genero_cant, autopct='%1.1f%%',  startangle=90, explode=desfase)
#señalamos la forma, en este caso 'equal' es para dar forma circular
ax1.axis('equal')
plt.title('Distribución de vinculo de agresor')
plt.legend()
plt.savefig('grafica_pastel.png')
plt.show()


# In[12]:


#TERCER GRAFICO: ANALIZAMOS LA CANTIDAD DE CASOS EN FUNCION A LA EDAD DE LAS VICTIMAS
#CALCULAMOS LAS VARIABLES
#primero armamos rangos de edades
    # '1': niños (0-5)
    # '2':pre-adolescentes(6-12)
    # '3': adolescentes (13-18)
    # '4': jovenes (19-30)
    # '5': adultos (31-60)
    # '6': mayores (61-100)
    
bins=[0,5,12,18,30,60,100]
#names=('0-5','6-12','13-18','19-30','31-60','61-100')
names=('1','2','3','4','5','6')
basedatos['EDAD']=pd.cut(basedatos['EDAD'], bins, labels=names)


# In[13]:


#CALCULAMOS CANTIDAD DE CASOS TOTALES POR PROVINCIA
serie_provincia=basedatos.PROVINCIA.value_counts()
serie_provincia


# In[14]:


#GENERAMOS UN NUEVO DATA FRAME APLICANDO UN FILTRO DE EDAD Y, ASI, OBTENER LOS CASOS 
#DE VICTIMAS MENORES DE EDAD
casos_menores= basedatos.loc[basedatos['EDAD']<'4'] 
casos_menores


# In[15]:


#OBTENEMOS UNA SERIE DE CANT DE CASOS DE VICTIMAS MENORES DE EDAD POR PROVINCIA
serie_provincia_menores=casos_menores.PROVINCIA.value_counts()
serie_provincia_menores


# In[16]:


fig, ax= plt.subplots()
#etiquetas=('0-5','6-12','13-18','19-30','31-60','61-100')
ax.barh(serie_provincia.index, serie_provincia_menores, label= 'Casos menores de edad')
ax.barh(serie_provincia.index, serie_provincia, left=0, label='Casos totales')
ax.legend(loc='upper right')
ax.set_title('Cantidad de casos en cada provincia')
ax.set_ylabel('Cantidad de casos')
ax.set_xlabel('Provincias')


# In[17]:


#SEXTO PASO: REALIZAMOS LOS OTROS TRES GRÁFICOS CON SEABORN
import pandas as pd
df=pd.read_csv('ViolenciaGenero2.0.csv', delimiter=';', encoding='latin-1')
df.head()


# In[18]:


#CUARTO GRAFICO: REALIZAMOS UN HISTOGRAMA EN DONDE SE ANALIZA LA DISTRIBUCIÓN 
#DE LAS EDADES DE LAS VICTIMAS EN CADA PROVINCIA
# AXEL-LEVEL
sns.histplot(data=df, x="EDAD", hue="PROVINCIA", multiple="stack")


# In[19]:


#QUINTO GRAFICO: ANALIZAMOS LA VARIACIÓN DE LA CANTIDAD DE CASOS EN EL TIEMPO
#REALIZAMOS UN GRÁFICO DE LINEAS 
#para facilitar en analisis agrupamos las fechas de manera mensual (no diaria)
df['FECHA'] = pd.to_datetime(df['FECHA'], errors='coerce')
df['FECHA_MES']=df.FECHA.dt.to_period('M')
df_2=df.groupby('FECHA_MES', as_index=False).sum()
df_2.head()


# In[21]:


df_2['FECHA_MES'] = df_2['FECHA_MES'].astype('str')


# In[22]:


ax = sns.lineplot(data=df_2, x="FECHA_MES", y="CASO")
ax.set(xlabel='Tiempo', ylabel='Cantidad de casos', title='Variación en el tiempo')


# In[23]:


#PARA FACILITAR MAS EN ANALISI REALIZAMOS UNA GRILLA DE DOS GRAFICOS COMPARANDO EL AÑO 2020 Y 2021
#POR LO QUE CREAMOS DOS DATA FRAMES PARA CADA AÑO
df_2_2020= df_2.loc[0:11,['FECHA_MES','CASO']] 
df_2_2020['FECHA_MES'] = df_2_2020['FECHA_MES'].astype('str')
df_2_2020.head()


# In[24]:


df_2_2021= df_2.loc[12:23,['FECHA_MES','CASO']] 
df_2_2021['FECHA_MES'] = df_2_2021['FECHA_MES'].astype('str')
df_2_2021.head()


# In[25]:


fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(12, 5), sharey=True)  
ax[0].plot(df_2_2020.FECHA_MES, df_2_2020.CASO, label='Casos del 2020')
ax[1].plot(df_2_2021.FECHA_MES, df_2_2021.CASO, label='Casos del 2021', color='C1')
#ax[2].plot(df.FECHA[2022], df.CASO, label='Precipitaciones de marzo', color='C2')
ax[0].set_title('Variación de casos en el tiempo') 
ax[1].set_xlabel('Año')  
ax[1].set_ylabel('Cantidad de casos')

ax[0].legend()  
ax[1].legend()
#ax[2].legend()  


# In[26]:


#SEXTO GRAFICO: ANALIZAMOS EL TIPO DE 
#CREAMOS UN FILTRO EN EL DATA FRAME PARA VER LOS CASOS DE VIOLENCIA EN MENORES DE EDAD
#PD: recordar que habiamos generado un rango de edades
    # '1': niños (0-5)
    # '2':pre-adolescentes(6-12)
    # '3': adolescentes (13-18)
    # '4': jovenes (19-30)
    # '5': adultos (31-60)
    # '6': mayores (61-100)
#Por lo que, definimos que son menores de edad los rangos del 1 al 3
casos_menores= df.loc[df['EDAD']<18] 
casos_menores


# In[27]:


plt.figure()
# Figure -level
ax = sns.displot(data=casos_menores, x='EDAD', kind='kde', hue='VINCULO_PERSONA_AGRESORA', fill=True)
ax.set(xlabel='Edad', ylabel='Densidad', title='Distribución  de edades en función a vincuo con agresor')

