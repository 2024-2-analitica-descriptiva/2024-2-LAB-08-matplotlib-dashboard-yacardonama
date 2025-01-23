# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import matplotlib.pyplot as plt
import pandas as pd
import os

#Carga datos
ruta_datos='./files/input/shipping-data.csv'
def load_data():
    df= pd.read_csv(ruta_datos)
    return df

#Crea carpeta de salida
ruta_carpeta= './docs/'
def carpeta():
    try:
        os.makedirs(os.path.dirname(ruta_carpeta))
    except FileExistsError:
        pass

#Gráfico Warehouse_block
colors1 = [
    'maroon',
    'firebrick',
    'brown',
    'indianred',
    'lightcoral',
]
def graf_Warehouse_block(df):
    df= df.copy()
    plt.Figure()
    counts=df.Warehouse_block.value_counts()
    counts.plot.bar(
        title = 'Shipping per Werehouse',
        xlabel = 'Werehouse block',
        ylabel = 'Record count',
        color = colors1, #'maroon',
        fontsize = 10
    )
    
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_color('gray')
    plt.gca().spines['bottom'].set_color('gray')
    plt.savefig('./docs/shipping_per_warehouse.png')


#Gráfica Mode_of_Shipment
colors2 = [
    'green',
    'mediumseagreen',
    'mediumaquamarine'
]
def graf_Mode_of_Shipment(df):
    df = df.copy()
    plt.figure()
    counts = df.Mode_of_Shipment.value_counts()
    counts.plot.pie(
        title = 'Mode of shipment',
        wedgeprops = dict(width=0.55),
        ylabel= '',
        colors=colors2,
        autopct='%1.1f%%'
    )
    plt.savefig('./docs/mode_of_shipment.png')


#Gráfica Customer_rating
def graf_Customer_rating(df):
    df = df.copy()
    plt.figure()
    df = (
        df[['Mode_of_Shipment','Customer_rating']]
        .groupby('Mode_of_Shipment')
        .describe()
    )
    df.columns = df.columns.droplevel()
    df = df[['mean', 'min','max']]
    plt.barh(
        y= df.index.values,
        width=df['max'].values - 1,
        left= df['min'].values,
        height=0.9,
        color='gainsboro'
    )
    colors3 = [
        'tab:green' if value >= 3.0 else 'darkorange' for value in df['mean'].values
    ]
    plt.barh(
        y= df.index.values,
        width=df['mean'].values - 1,
        left= df['min'].values,
        height=0.5,
        color=colors3,        
    )
    plt.title('Average costumer rating')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_color('gray')
    plt.gca().spines['bottom'].set_color('gray')
    plt.savefig('./docs/average_customer_rating.png')  

#Gráfica Weight_in_gms
def graf_Weight_in_gms(df):
    df= df.copy()
    plt.figure()
    df.Weight_in_gms.plot.hist(
        title='Shipped weight distribution',
        color='navy',
        edgecolor='White'
    )
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_color('gray')
    plt.gca().spines['bottom'].set_color('gray')
    plt.savefig('./docs/weight_distribution.png') 

#Archivo HTML
def create_dashboard_html(output_file="docs/index.html"):
    """
    Genera un archivo HTML para mostrar el dashboard con los gráficos generados.
    
    Parámetros:
    - output_file: Nombre o ruta del archivo HTML a generar.
    """
    html_content = """<!DOCTYPE html>
<html>
    <head>
    <style>
        h1 {
        font-family: Arial, sans-serif; 
        font-size: 24px;
        font-weight: bold;
        color: #333; /* Color gris oscuro */
        }
    </style>
    </head>

    <body>
        <h1>Shipping Dashboard Example</h1>
        <div style="width:45%;float:left">
            <img src="docs/shipping_per_warehouse.png" alt="Fig 1">
            <img src="docs/mode_of_shipment.png" alt="Fig 2">
        </div>
        <div style="width:45%;float:left">
            <img src="docs/average_customer_rating.png" alt="Fig 3">
            <img src="docs/weight_distribution.png" alt="Fig 4">
        </div>
    </body>
</html>"""

    # Crear el archivo HTML
    with open(output_file, "w") as file:
        file.write(html_content)

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    df=load_data()
    carpeta()

    graf_Warehouse_block(df)
    graf_Mode_of_Shipment(df)
    graf_Customer_rating(df)
    graf_Weight_in_gms(df)

    os.makedirs("docs", exist_ok=True)
    create_dashboard_html("docs/index.html")

pregunta_01()
