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
  
  - La solución podría mejorar los procesos operativos al proporcionar simulaciones precisas y en tiempo real, lo que permitiria una mejor toma de decisiones. Además, la integración de tecnologías como la inteligencia artificial podria automatizar la detección de obstáculos y la planificación de rutas, aumentando la eficiencia y reduciendo errores humanos.

### Si tu proyecto no aplica directamente a negocio o planta, ¿qué otros entornos podrían beneficiarse?

  - Otros entornos que podria beneficiarse es la educación, donde ell software podría utilizarse para enseñar conceptos de fisíca y matemáticas, y el sector militar, donde se prodria utilizar para entrenar a personal en tácticas y estrategias.


## Mejoras en IT y OT (2f)

### ¿Cómo puede tu software facilitar la integración entre entornos IT y OT?

  - El software podría facilitar la integración entre entornos IT Y OT al proporcionar una plataforma unificada para la simulación y análisis de datos. Esto permitiria una mejor coordinación entr los sistemas de información y los sistemas opertivos, mejorando la eficiencia y reduciendo la redundancia de datos.


### ¿Qué procesos específicos podrían beneficiarse de tu solución en términos de automatización o eficiencia?

  - Procesos específicos como la planificación de rutas y gestión de inventarios podrían beneficiarse de la solución al proporcionar simulaciones precisas y optimizadas. Esto permitiría una mejor asignación de recursos y una reducción de tiempos de inactividad.

### Si no aplica a IT u OT, ¿cómo podrías adaptarlo para mejorar procesos tecnológicos concretos?

  - Para adaptarlo a mejorar procesos tecnologicos concretos, se podrían integrar con sistemas de gestión de recursos empresariales (ERP) y sistemas de ejecución de manufactura (MES) para proporcionar datos en tiempo real y mejorar la toma de decisiones.

## Tecnologías Habilitadoras Digitales (2g)

### ¿Qué tecnologías habilitadoras digitales (THD) has utilizado o podrías integrar en tu proyecto?

  - El proyecto podría integrar tecnologías habilitadoras digitales como la inteligencia artificial y el aprendizaje automático para mejorar la precisión de las simulaciones y la detección de obstáculos. Además, el uso de sensores IoT podría proporcionar datos en tiempo real para ajustar las simulaciones y mejorar la toma de decisiones.


### ¿Cómo mejoran estas tecnologías la funcionalidad o el alcance de tu software?

  - Las tecnologías habilitadoras digitales mejorarían la funcionalidad del software al proporcionar simulaciones más precisas y en tiempo real. Esto tendría un impacto positivo en el entorno al permitir una mejor planificación y ejecución de operaciones, reduciendo costos y mejorando la eficiencia operativa.
