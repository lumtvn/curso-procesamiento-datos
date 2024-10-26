Trabajo Practico 2

Objetivo: Crear un pipeline de Machine Learning para predecir la variable PRECIO, que conste de las siguientes etapas:
    1. Preproceso de los datos
        a. Limpieza y curacion de variables de interes: PRICE, BEDS, BATH, PROPERTYSQFT, etc. Elegir mas variables de verlo necesario
    3. Entrenamiento
    4. Validacion cruzada


- Las operaciones de entrenamiento y validacion del modelo deben ser realizadas usando librerias de Spark MLlib y hacerse sobre un DataFrame Spark
- El pipeline tiene que estar conformado por modulos ejecutables. Estos modulos pueden ser funciones o archivos ejecutables en python. Deberia haber un programa que ejecute esos modulos en orden para cada etapa. 
- Se va a aceptar un programa que ejecute los modulos en orden, sin tener necesariamente un manejo de error cuando algun modulo falla. No hace falta mas orquestacion que esa.
- El entregable deberia estar conformado por el directorio con todos los modulos, similar al que se entrega como template. Se pueden modificar y agregar los modulos como les parezca necesario y a gusto personal, solo cuidar la arquitectura de codigo de tener un modulo principal que corre el resto, y un modulo helpers que tenga funciones comunes.
