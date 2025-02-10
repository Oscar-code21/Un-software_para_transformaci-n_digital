# Preguntas Sobre el Proyecto


## Ciclo de Vida del dato (5b):

### ¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?
  - En mi proyecto, los datos se generan principalmente atraves de la simulación de trayectorias balísticas y la generación de mapas con obstaculos. Estos datos se procesan en tiempo real durante la ejecución
    del programa y se eliminan al finalizar la simulación. No se almacena información persistente.

### ¿Qué estrategia sigues para garantizar la consistencia e integridad de los datos?
  - Para garantizar la consistencia e integridad de los datos, se podría implemetar una base de datos para almacenar los resultados de las simulaciones y mapas generados. Ademas, se podria utilizar tecnicas de comprensión y cifrado para optimziar el almacenamiento y la seguridad de los datos.

### Si no trabajas con datos, ¿cómo podrías incluir una funcionalidad que los gestione de forma eficiente?
  - Para incluir datos en este proyecto, se podria implementar una base de datos para almacenar los resultados de las simulaciones y los mapas generados. Además, se podria utilizar técnicas de comprensión y cifrado para optimizar el almacenamiento y la seguridad de datos.

## Almacenamiento en la nube (5f)

### Si tu software utiliza almacenamiento en la nube, ¿cómo garantizas la seguridad y disponibilidad de los datos?
  - Mi proyecto, no utiliza almacenamiento en la nube. Sin embargo podria implementar un servicio del almacenamiento en la nube como Google Cloud Storage para almacenar los resultados de las simulaciones y los mapas generados. Esto te garantizara la seguridad y disponbibilidad de los datos mediante el uso de cifrado y copias de seguridad automaticas.

### ¿Qué alternativas consideraste para almacenar datos y por qué elegiste tu solución actual? 
  - Si hubiera utilizado, pdoria considerar alternativas como base de datos relacionales o base de datos NoSQL. Mi elección dependeria de la naturaleza de los datos y los requisitos de rendimiento y escabilidad.   La nube lo elegiria por la capacidad de escalado automatico y su facilidad de integración con otros servicios.

### Si no usas la nube, ¿cómo podrías integrarla en futuras versiones?
  - Podria utilizar servicios de almacenamientos en la nube como Google Coud Strorage como antes e dicho o AWS S3. Además, se podrían implementar APis para interectuar con estos servicios y asegurar la transferencia segura de datos.
