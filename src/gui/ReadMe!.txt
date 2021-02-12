Estructura de una ventana en Python:
- Raiz --> Es la ventana. Tambien se le llama organizador. En java seria el JFrame
- Frame --> Es el panel de la raiz. En java seria el JPanel del JFrame
- Widgets --> Dentro de la raiz, tenemos cuadros de texto, botones... A la raiz se le considera un widget también

Debemos poner siempre al final el metodo .mainLoop() para que se mantenga en ejecución

Pasos a seguir para crear un ventana en Python:
1. Crear la raiz
2. Crear el Frame y meterlo en la raiz
3. Empaquetar el Frame en la raiz para que se pueda mostrar
4. Dar tamaño al Frame, no a la raiz. Ya que la raiz se adapta al tamaño de sus widgets

IMPORTANTE:
El método pack() adapta la raiz a las dimensiones del widget. Con el método place() debemos indicar en que
coordenadas queremos posicionarlo, la raiz no se adaptara al widget