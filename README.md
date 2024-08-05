# Proyecto01-DS
Se proporciona una forma interactiva de seleccionar, leer y procesar archivos CSV utilizando una interfaz gráfica de usuario (GUI). Utiliza la librería `pandasgui` para mostrar datos, `pandas` para manejar datos y la biblioteca `tkinter` para los componentes de la GUI.

## PandasGUI
PandasGUI es una interfaz gráfica de usuario para analizar datos en Python utilizando DataFrames de pandas. Proporciona una manera interactiva de visualizar y manipular datasets, facilitando el análisis de datos de forma más visual.
- **Ver DataFrames:** PandasGUI muestra los DataFrames  de pandas en un formato tabular, similar a cómo se podrían ver datos en Excel.
- **Filtrar y ordenar datos:** Es posible aplicar filtros a subconjuntos específicos. Ordenar por columnas también permite organizar los datos en orden numérico o alfabético.
- **Editar datos:** La interfaz permite la edición directa de los datos en la cuadrícula, sin necesidad de volver al script.
- **Creación de gráficos:** PandasGUI se inegra con matplotlib y seaborn para graficar directamente desde la interfaz. Esto permite seleccionar las variables que desean mostrarse para crear histogramas, diagramas de dispersión, gráficos de barras, gráficos circulares y más.
- **Herramientas de análisis de datos:** Incluye herramientas para realizar análisis estadísticos comunes, como calcular medias, medianas, modas y otras estadísticas descriptivas.
- **Queries:** Esta función permite a los usuarios construir queries arrastrando columnas a un constructor de queries, simplificando el proceso de filtrar y buscar a través de grandes conjuntos de datos.
- **Generación de scripts:** A medida que se interactúa con la GUI, PandasGUI puede generar código que representa las transformaciones o análisis que se realicen.
- **Exportación de datos:** PandasGUI ofrece funcionalidades integradas para exportar DataFrames a varios formatos de archivo comúnmente utilizados. Además de exportar DataFrames a diferentes formatos de archivo, PandasGUI también permite guardar las gráficas creadas dentro de la interfaz. 


## Características
- **Selección de archivo:** Los usuarios pueden seleccionar un archivo CSV desde su sistema utilizando un diálogo de archivo. El archivo de ejemplo está nombrado como "penguins.csv"
- **Especificación de delimitador:** Los usuarios tienen la opción de especificar un delimitador para el archivo CSV o dejarlo en blanco para su detección automática.
- **Procesamiento de datos:**
  - Convierte las columnas correspondientes a tipos numéricos
  - Identifica y categoriza columnas basadas en los valores faltantes o desconocidos.
- **Análisis de columnas:** Muestra un resumen de las columnas numéricas y categóricas, junto con información detallada sobre valores nulos o desconocidos.
- **Visualización:** Utiliza "PandasGUI" para proporcionar una vista interactiva del DataFrame procesado, permitiendo una exploración específica de los datos.


## Requisitos
- Python 3
- pandas
- pandasgui
- tkinter

Instalar las librerías usando pip:
`pip install pandas pandasgui`


