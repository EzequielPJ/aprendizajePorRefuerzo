**Estructura del código fuente**

El código implementado del proyecto está dividido en dos archivos.py:

Por un lado, encontramos el Environment.py en que están los métodos relacionados con la carga los parámetros iniciales, el reinicio de los parámetros en cada iteración y 
la toma de una acción en el mapa. También los métodos encargados de generar los mapas de pruebas, ya sea el mapa del problema predeterminado que se nos pide o uno aleatorio. 
Finalmente, encontramos los métodos que actualizan y finalizan los mapas en la consola de comandos y en la venta de Tkinter.

Por otro lado, tenemos el Algorithm.py donde encontramos la implementación del algoritmo de aprendizaje modificado conforme a nuestras necesidades junto a la implementación 
de la interfaz con la que puedes seleccionar qué tipo de mapa va a recorrer el algoritmo.

**Cómo usar la interfaz de usuario**

1ºPaso: Tras importar el proyecto al IDE deseado, se debe de buscar el botón de Run, pulsarlo y así ejecutar el archivo Algorithm.py

2ºpaso: A continuación aparecerán dos ventanas, una en blanco y otra con un formulario. Desplazas la ventana en blanco donde posteriormente 
aparecerá el mapa generado y nos centramos en la del formulario.

3ºPaso: En la ventana del formulario se pueden hacer dos cosas:
	- Introducir los datos de altura y anchura del mapa en el formulario y darle al botón de "Start". Esto generará un mapa aleatorio con los parámetros introducidos
	- Pulsar el botón de "Utilizar el mapa predeterminado" que genera el mapa que se nos pide en el problema a resolver po el algoritmo.

4ºpaso: Tras realizar una de las 2 anteriores acciones, después de un tiempo de carga, aparecerá el mapa dibujado en la ventana en blanco. 
Esto solo muestra el mapa mientras que se realizan las iteraciones del código. No se ha podido mostrar el camino de cada una de las iteraciones 
porque suponía mucha carga del procesador para los ordenadores. *se puede ver como se está ejecutando el algoritmo en la consola del IDE*.

5ºPaso: Después de un largo periodo el algoritmo completará todas sus iteraciones y el mapa seleccionado se actualizará. En este aparecerá el recorrido más óptimo que ha encontrado 
el algoritmo en 100 iteraciones.


**Realizar pruebas con parametros**

Al poder seleccionar la altura y el ancho en la interfaz de usuario se puede hacer la prueba de meter datos variados para realizar pruebas. Si se desea tocar otro parámetro 
como por ejemplo el número de iteraciones, se puede realizar modificando el código directamente en el IDE. El código está debidamente comentado para que sea más fácil de localizar.
Dejamos por escrito los más comunes:
	-Iteraciones/Epochs: método empezar() (mapa aleatorio) y empezarPrueba() (mapa predeterminado) en el Algorithm.py
	-Gamma: método empezar() (mapa aleatorio) y empezarPrueba() (mapa predeterminado) en el Algorithm.py
	-Reward/Recompensas: método step() en el Environment.py
	
***Hay que instalar las librerías de tkinter y numpy para el correcto funcionamiento del código fuente