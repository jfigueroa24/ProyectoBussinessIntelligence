import matplotlib.pyplot as plt
import seaborn as sns
import mpld3
import pandas as pd
from flask import Flask, render_template

# Leer los datos del CSV
#data = pd.read_csv('EconomiaEmpresa.csv')

# Crear una gráfica con Seaborn
#sns.boxplot(x=data["producción"])

# Convertir la gráfica a formato HTML con mpld3
#html_grafica = mpld3.fig_to_html(plt.gcf())

app = Flask(__name__)



if __name__ == '_main_':
    app.run(debug=True)