LANGUAGE="" LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 jupyter notebook

Transfer Learning + Fine-Tunning

https://www.kaggle.com/code/pestipeti/getting-started-with-keras

"The ImageNet project is a large visual database designed for use in visual object recognition software research. More than 14 million images have been hand-annotated by the project to indicate what objects are pictured and in at least one million of the images, bounding boxes are also provided" Wikipedia

Las arquitecturas más comunes hoy en día para las técnicas de transfer learning y fine-tuning son:

VGG16 y VGG19: esta arquitectura, que fue una de las primeras en aparecer, fue introducida por Simonyan y Zisserman en 2014 con su artículo titulado Very Deep Convolutional Networks for Large Scale Image Recognition.
ResNet: la arquitectura de ResNet la desarrolló He en 2015 para el transfer learning y fine tuning. El artículo se llama Deep Residual Learning for Image Recognition.
Inception V3: este tipo de arquitectura lo introdujo en 2014 Szegedy en su artículo llamado Going Deeper with Convolutions.
Xception: esta arquitectura la propuso François Chollet (el creador de Keras) y lo único que aporta respecto a Inception es que realiza las convoluciones de una forma óptima para que tarden menos tiempo.

https://keepcoding.io/blog/transfer-learning-fine-tuning/

Model loss and accuracy
https://machinelearningmastery.com/display-deep-learning-model-training-history-in-keras/ 
https://stackoverflow.com/questions/72991225/how-can-i-print-the-training-and-validation-graphs-and-training-and-validation
-------------------------------

En uno se usa el optimizador RMSprop y en otro el ADAM. Ambos con el mismo learning rate 1e-4.
En uno se entrena con 100 épocas con EarlyStopping=10 monitorizando la función de pérdida, en el otro con 10 épocas y EarlyStopping=5 monitorizando el accuracy.
En ambos se usa el callback ReduceLROnPlateau pero en el primero con persistencia=5, factor=0.2, learning_rate>=1e-6 mientras que en el segundo con persistencia=3, factor=0.2, learning_rate>=1e-7.
En ambos se monitoriza la métrica accuracy durante entrenamiento y validación.
( añadimos observación)
En ambos se grafican las accuracy, loss con la curva de entrenamiento y la curva de validación.
En ambos se evalúa el modelo con la pérdida y exactitud finales sobre los datos del dataset.

----------------------

Este es un hiperparámetro trainicionero, puesto que un learning rate muy pequeño puede hacer que la red demore siglos aprendiendo, mientras que uno muy grande le conferirá un comportamiento errático, similar al de una pelota de pinball, la cual rebota en las paredes de la máquina, difícilmente (o nunca) llegando a su destino (es decir, la red no aprendería nada)