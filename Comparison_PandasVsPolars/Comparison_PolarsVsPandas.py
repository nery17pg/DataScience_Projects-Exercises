import pandas as pd
import polars as pl
import matplotlib.pyplot as plt
import time

"""1. Reading time of the dataset"""
# Pandas
inicio = time.perf_counter()
pd_df = pd.read_csv("[Dataset File]", nrows=1000)
runtime_pd_read = time.perf_counter() - inicio

# Polars
inicio = time.perf_counter()
pl_df = pl.read_csv("[Dataset File]", n_rows=1000)
runtime_pl_read = time.perf_counter() - inicio

"""2. Selected data columns"""
# Pandas
inicio = time.perf_counter()
pd_df_selected = pd_df[['Severity', 'Start_Time', 'End_Time', 'Station', 'Stop', 'Traffic_Signal']]
runtime_pd_select = time.perf_counter() - inicio

# Polars
inicio = time.perf_counter()
pl_df_selected = pl_df[['Severity', 'Start_Time', 'End_Time', 'Station', 'Stop', 'Traffic_Signal']]        
runtime_pl_select = time.perf_counter() - inicio

"""3. Filtering data"""
# Pandas
inicio = time.perf_counter()
filter_pd_df = pd_df[pd_df['Traffic_Signal']==True]
runtime_pd_filter = time.perf_counter() - inicio

# Polars
inicio = time.perf_counter()
filter_pl_df = pl_df.filter(pl.col('Traffic_Signal')==True)        
runtime_pl_filter = time.perf_counter() - inicio

"""4. Sorting"""
# Pandas
inicio = time.perf_counter()
sorted_pd_df = pd_df.sort_values(by='Humidity(%)', ascending=False)
runtime_pd_sort = time.perf_counter() - inicio

# Polars
inicio = time.perf_counter()
sorted_pl_df = pl_df.sort("Humidity(%)", descending=True)        
runtime_pl_sort = time.perf_counter() - inicio

"""5. Grouping"""
# Pandas
inicio = time.perf_counter()
grouped_pd_df = pd_df.groupby(['State'])['ID'].agg('count')
runtime_pd_groupby = time.perf_counter() - inicio

# Polars
inicio = time.perf_counter()
grouped_pl_df = pl_df.group_by('State').agg(pl.col('ID').count())        
runtime_pl_groupby = time.perf_counter() - inicio

"""Tablas de comparación"""
# Tabla de comparación - Lectura
print("Pandas:", runtime_pd_read)
print("Polars:", runtime_pl_read)

packages = ['pandas', 'polars']
runtimes = [runtime_pd_read, runtime_pl_read]

plt.bar(packages, runtimes)

plt.xlabel('package')
plt.ylabel('runtime')
plt.title("Comparación Pandas vs. Polars - Lectura")

plt.show()

# Tabla de comparación - Selección
print("Pandas: ", runtime_pd_select)
print("Polars: ", runtime_pl_select)

packages = ['pandas', 'polars']
runtimes = [runtime_pd_select, runtime_pl_select]

plt.bar(packages, runtimes)

plt.xlabel('package')
plt.ylabel('runtime')
plt.title("Comparación Pandas vs. Polars - Selección")

plt.show()

# Tabla de comparación - Filtrado
print("Pandas: ", runtime_pd_filter)
print("Polars: ", runtime_pl_filter)

packages = ['pandas', 'polars']
runtimes = [runtime_pd_filter, runtime_pl_filter]

plt.bar(packages, runtimes)

plt.xlabel('package')
plt.ylabel('runtime')
plt.title("Comparación Pandas vs. Polars - Filtrado")

plt.show()

# Tabla de comparación - Sorting
print("Pandas: ", runtime_pd_sort)
print("Polars: ", runtime_pl_sort)

packages = ['pandas', 'polars']
runtimes = [runtime_pd_sort, runtime_pl_sort]

plt.bar(packages, runtimes)

plt.xlabel('package')
plt.ylabel('runtime')
plt.title("Comparación Pandas vs. Polars - Sorting")

plt.show()

# Tabla de comparación - Group by
print("Pandas: ", runtime_pd_groupby)
print("Polars: ", runtime_pl_groupby)

packages = ['pandas', 'polars']
runtimes = [runtime_pd_groupby, runtime_pl_groupby]

plt.bar(packages, runtimes)

plt.xlabel('package')
plt.ylabel('runtime')
plt.title("Comparación Pandas vs. Polars - Groupby")

plt.show()