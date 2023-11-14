from flask import Flask, render_template
from flask_cors import CORS
from waitress import serve
from decouple import config
import seaborn as sns
import mpld3
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__)
cors = CORS(app)

@app.route('/index')
def inicio():
    return render_template('index.html') 

@app.route('/informes')
def informes():
    return render_template('informes.html') 

@app.route('/grafica')
def grafica():
    # Leer los datos del CSV
    data = pd.read_csv('EconomiaEmpresa.csv')

    # Crear una gráfica con Seaborn
    sns.histplot(data=data, x = "producción")

    # Convertir la gráfica a formato HTML con mpld3
    html_grafica = mpld3.fig_to_html(plt.gcf())

    return html_grafica

if __name__ == '__main__':
    print("Server running: "+"http://"+config('URL_BACKEND')+":"+config('PORT'))
    serve(app, host = config('URL_BACKEND'), port = config('PORT'))