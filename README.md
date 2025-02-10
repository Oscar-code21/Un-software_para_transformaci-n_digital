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

## Seguridad y regulación (5i)

### ¿Qué medidas de seguridad implementaste para proteger los datos o procesos en tu proyecto?
  - Para proteger los datos y procesos en mi proyecto, se podrían implmentar medidas de seguridad como el cifrado de datos en tránsito y en reposo, autenticación de usuarios y control de acceso basado en roles.

### ¿Qué normativas (e.g., GDPR) podrían afectar el uso de tu software y cómo las has tenido en cuenta?

  - El proyecto podría verse afectado por normativas como el GDPR si se maneja información personal del usuario. Para cumplir con estas normativas, se deberían implementar políticas de privacidad claras, obtener el consentimiento de los usuarios para el procesamiento de sus datos y proprocionar mecanismos para que los usuarios acceder,rectificar y elimir datos.

### Si no implementaste medidas de seguridad, ¿qué riesgos potenciales identificas y cómo los abordarías en el futuro?
  - Si no implemento mediad de seguridad, lso riesgos potenciales incluye el acceso no autorizado a los datos , la pérdida de datos y la manipulación de datos. Para abordar estos riesgos, se podrían  implementar medidas de seguridad como el cifrado, la autenticación de usuarios y control de acceso.

## Implicación de las THD en negocio y planta (2e)

### ¿Qué impacto tendría tu software en un entorno de negocio o en una planta industrial?

 - El software podría tener un impacto significativo en entorno de negocio o plantas industriales al mejorar la planificación y ejecución de operaciones tácticas y balísticas. Por ejemplo, en una planta industrial, el software podría utilziarse para simular y optimizar rutas de transporte de materiales, reduciendo costos y mejorando la eficiencia operativa.

### ¿Cómo crees que tu solución podría mejorar procesos operativos o la toma de decisiones?
  
  - La solución podría mejorar los procesos operativos al proporcionar simulaciones precisas y en tiempo real, lo que permitiria una mejor toma de decisiones. Ademas
