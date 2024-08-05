from pandasgui import show
import pandas as pd
from tkinter import Tk, filedialog, simpledialog, messagebox
import csv

def seleccionar_archivo():
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal

    # Abrir el diálogo de selección de archivos
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
    root.destroy()
    if not file_path:  # Si no se selecciona ningún archivo, salir de la función
        messagebox.showinfo("Info", "No se seleccionó un archivo.")
        return None
    return file_path

def pedir_delimitador():
    # Preguntar al usuario por el delimitador o proporcionar una opción para la detección automática
    delimiter = simpledialog.askstring("Input", "Ingrese un delimitador o deje en blanco para detectar automáticamente (e.g., ',', ';', '\\t'): ")
    return delimiter

def leer_csv(file_path, delimiter):
    try:
        if delimiter:
            df = pd.read_csv(file_path, delimiter=delimiter, engine='python')
        else:
            with open(file_path, 'r') as file:
                sniffer = csv.Sniffer()
                dialect = sniffer.sniff(file.read(1024))
                file.seek(0)
                df = pd.read_csv(file_path, delimiter=dialect.delimiter)
        return df
    except csv.Error as e:
        messagebox.showerror("Error", f"Error de CSV: {e}")
    except pd.errors.ParserError as e:
        messagebox.showerror("Error", f"Error de análisis: {e}")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")
    return None


def procesar_dataframe(df):
    # Inferir automáticamente los nombres de las columnas si no se proporcionan
    if df.columns[0] == 0:
        df.columns = [f"Column_{i}" for i in range(df.shape[1])]

    # Procesar el DataFrame
    null_values = {}
    for column in df.columns:
        converted_column = pd.to_numeric(df[column], errors='coerce')
        if not converted_column.isnull().all():  # Verificar si la conversión fue al menos parcialmente exitosa
            unique_ratio = len(pd.unique(converted_column.dropna())) / len(converted_column.dropna())
            # Si los valores únicos son menos del 5% del total, considerarlo categórico
            if unique_ratio < 0.05:
                df[column] = converted_column.astype('category')
            else:
                df[column] = converted_column

        # Contar valores nulos y añadir al diccionario
        null_values[column] = df[column].isnull().sum() + (df[column] == '?').sum()

    # Identificar columnas numéricas y categóricas
    numerical_columns = df.select_dtypes(include=['float64', 'int64']).columns
    categorical_columns = df.select_dtypes(include=['category']).columns

    # Preparar mensaje para mostrar
    message = f"Columnas numéricas: {list(numerical_columns)}\nColumnas categóricas: {list(categorical_columns)}\n\n"
    message += "Cantidad de valores nulos o desconocidos por columna:\n" + "\n".join(
        [f"{col}: {null_values[col]}" for col in df.columns])
    return message


def mostrar_resultado(df, message):
    # Mostrar el cuadro de mensaje con la información de las columnas
    messagebox.showinfo("Análisis de columnas", message)
    # Mostrar el DataFrame usando PandasGUI
    show(df)

def select_file_and_process():
    file_path = seleccionar_archivo()
    if not file_path:
        return

    delimiter = pedir_delimitador()
    df = leer_csv(file_path, delimiter)
    if df is not None:
        message = procesar_dataframe(df)
        mostrar_resultado(df, message)

# Llamar a la función
select_file_and_process()
