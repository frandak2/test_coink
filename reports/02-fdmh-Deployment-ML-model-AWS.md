# Deployment a ML model on AWS

Ideas principales:
- Construir un modelo de ML.
- Implementación en AWS.
- Ejecución on-demand a través de un API.

La arquitectura serverless para la construcción y despliegue de modelos de ML es una opción escalable y de bajo costo. Se puede utilizar AWS Lambda, que es un servicio de computación sin servidor(con sus limitaciones), para el entrenamiento y envió de las versiones de los datos y modelos, como base de datos se puede utilizar Amazon S3, DynamoDB, etc. donde podremos almacenar los datos para el entrenamiento y el modelo listo para despliegue, para desplegar el modelo para consumo On-demand podemos usar AWS lambda de nuevo unido a AWS APIGateway para crear una API que permita a los usuarios solicitar las predicciones del modelo cuando lo deseen. Otra forma es el entrenamiento y almacenamiento del modelo en Amazon SageMaker y exponerlo con un end-point, Sin embargo, esta opción es más costosa pero práctica.

La arquitectura tradicional sería utilizar un servidor dedicado para ejecutar el modelo de ML. Se puede utilizar un servidor virtual en la nube, como Amazon EC2, para alojar el modelo y la base de datos. Se puede utilizar una aplicación web para proporcionar una interfaz para los usuarios, y una API REST para permitir que los usuarios soliciten el modelo en tiempo real. Este enfoque es más costoso que el enfoque serverless, pero ofrece un mayor control y flexibilidad en términos de cómo se ejecuta el modelo.

Cabe resaltar que lo anterior lo podemos desplegar usando AWS CloudFormation o Terraform, lo cual nos ayuda a crear infraestructura rápidamente, siempre y cuando tengamos claro los componentes que usaremos y sus respectivos roles, esto nos ayuda a la reproducibilidad de forma rápida en otras regiones o un control de nuestros componentes. 
