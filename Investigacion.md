# Laboratorio II: Diseño de un sistema de adquisición de datos
## Taller de Instrumentación - Tecnológico de Costa Rica
### Sede Alajuela, Segundo Semestre 2023
### Profesor: Kaleb Alfaro Badilla

---

## Portada

![Tecnológico de Costa Rica](https://th.bing.com/th/id/OIP.wqe6IbLSTjEmOdbOu3S-XwHaE7?pid=ImgDet&rs=1)

- **Tecnológico de Costa Rica**
- *Escuela de Electrónica*
- *Curso: EL-5822 Taller de Instrumentación*
- *Sede: Alajuela*
- *Segundo Semestre, 2023*

---

### Realizado por:

- Alexander Castro 2017153854
- Andrés Carrillo 2017106733
- Douglas Kopper 2017220194
- Steven Arias 2017097670

---

# Parte I: Solución del Cuestionario Previo

## Pregunta 1:
¿Cuales son los tipos de sensores de temperatura más populares? ¿Cuáles son sus ventajas y desventajas en función de los requisitos del diseño?

### Respuesta:
Termistores:
Los termistores son sensores económicos y compactos que responden rápidamente a los cambios de temperatura. Son sensibles pero su precisión puede ser limitada en algunos rangos. Son ideales para aplicaciones que requieren respuestas rápidas a cambios de temperatura.

Termopares:
Los termopares son versátiles y duraderos, especialmente en entornos de alta temperatura. Sin embargo, su precisión es relativamente baja en comparación con otros sensores. No requieren una fuente de alimentación externa, lo que los hace adecuados para aplicaciones en las que se necesita medir temperaturas extremas.

RTD (Resistencia Térmica de Detracción):
Los RTD ofrecen alta precisión y estabilidad en un rango amplio de temperaturas. Son ideales cuando se requieren mediciones muy precisas. Sin embargo, pueden ser más costosos que otros sensores y tienen una respuesta más lenta a los cambios de temperatura.

Termómetros de infrarrojos (IR):
Los termómetros de infrarrojos miden la temperatura superficial sin contacto. Son rápidos y útiles para medir objetos a distancia. Sin embargo, pueden verse afectados por la emisividad de la superficie y otros factores, lo que podría afectar su precisión.

IC de sensor de temperatura:
Los sensores de temperatura integrados son pequeños y precisos. Algunos ofrecen interfaces digitales, lo que los hace fáciles de usar en sistemas electrónicos. Sin embargo, pueden ser más costosos y tener limitaciones en ciertos rangos de temperatura.

Sensores de temperatura basados en diodos:
Estos sensores utilizan diodos de silicio para medir la temperatura. Son precisos y convenientes para aplicaciones electrónicas. Sin embargo, su precisión puede ser menor que la de otros sensores más especializados.

![Sensores Populares](Imagenes_CuestionarioPrevio/Imagen1.jpg)




## Pregunta 2:
¿Cuales son los tipos de termocuplas? ¿Cuales son sus rangos de temperatura y tensión?

### Respuesta:
Las termocuplas son sensores de temperatura que funcionan en base al principio de que cuando dos metales diferentes se unen en un extremo y se exponen a una diferencia de temperatura, se genera una diferencia de potencial (fuerza electromotriz) en el otro extremo de la termocupla. Existen varios tipos de termocuplas, designados por letras y combinaciones de metales que las componen.

**Algunos Tipos de Termocuplas Comunes**
1. - Tipo K (Cromel-Alumel):
   - Rango de Temperatura: Aproximadamente -270°C a 1372°C (-454°F a 2502°F).
   - Tensión Generada: Alrededor de 41 μV/°C.
2. - Tipo J (Hierro-Constantán):
   - Rango de Temperatura: Aproximadamente -210°C a 1200°C (-346°F a 2192°F).
   - Tensión Generada: Alrededor de 52 μV/°C.
3. - Tipo T (Cobre-Constantán):
   - Rango de Temperatura: Aproximadamente -270°C a 400°C (-454°F a 752°F).
   - Tensión Generada: Alrededor de 43 μV/°C.
4. - Tipo E (Cromel-Constantán):
   - Rango de Temperatura: Aproximadamente -270°C a 1000°C (-454°F a 1832°F).
   - Tensión Generada: Alrededor de 68 μV/°C.
5. - Tipo N (Nicrosil-Nisil):
   - Rango de Temperatura: Aproximadamente -270°C a 1300°C (-454°F a 2372°F).
   - Tensión Generada: Alrededor de 39 μV/°C.
6. - Tipo B (Platino-Rodio/Platino):
   - Rango de Temperatura: Aproximadamente 0°C a 1820°C (32°F a 3308°F).
   - Tensión Generada: Varía, alrededor de 10 μV/°C a 25 μV/°C.

**Notas sobre Rangos y Tensiones**
- Los rangos de temperatura y las tensiones generadas pueden variar ligeramente según las fuentes y las normas específicas utilizadas en la industria.
- Las termocuplas son adecuadas para diferentes aplicaciones en función de sus rangos de temperatura y sus propiedades específicas. La elección de la termocupla adecuada depende de los requisitos del diseño y el entorno de operación.
- Las tensiones generadas por las termocuplas son pequeñas y requieren amplificación para su lectura precisa.

![Título de la imagen](Imagenes_CuestionarioPrevio/imagen2.jpg)




## Pregunta 3:
¿Qué es una señal balanceada y una no balanceada? ¿Qué aplicación tiene el uso de señales balanceadas?

### Señal No Balanceada:

Una señal no balanceada, también conocida como señal no diferencial o señal de un solo extremo, se transmite a través de un solo conductor en relación a una referencia de tierra (nivel de referencia). En este caso, la señal se mide respecto a un punto de referencia en el circuito. Un ejemplo común es un cable coaxial en el que el conductor central lleva la señal y el conductor exterior y la tierra actúan como referencia.

### Señal Balanceada:

Una señal balanceada, también conocida como señal diferencial, se transmite a través de dos conductores: uno lleva la señal original y el otro lleva la misma señal pero invertida (opuesta en fase). Ambas señales tienen la misma amplitud pero polaridades opuestas. Esto significa que cualquier interferencia o ruido que afecte ambos conductores será rechazado en el receptor debido a la propiedad diferencial de la señal. [3]

### Aplicaciones del Uso de Señales Balanceadas:

Las señales balanceadas tienen varias ventajas que las hacen ideales para muchas aplicaciones:

1. **Rechazo de Ruido:** Debido a su naturaleza diferencial, las señales balanceadas son altamente inmunes al ruido y las interferencias. Cualquier interferencia que afecte ambos conductores se cancelará cuando se resta la señal invertida.

2. **Transmisión a Largas Distancias:** Las señales balanceadas son menos susceptibles a la degradación a lo largo de distancias largas debido a su rechazo de ruido. Esto las hace ideales para aplicaciones como transmisiones de audio y video profesional.

3. **Audio Profesional:** Los sistemas de audio profesional a menudo utilizan conexiones balanceadas para minimizar el ruido y garantizar una transmisión de alta calidad.

4. **Redes y Comunicaciones:** En sistemas de redes y comunicaciones, las señales balanceadas ayudan a prevenir las interferencias electromagnéticas, mejorando la integridad de la señal en transmisiones de larga distancia.

5. **Instrumentación y Medición:** En entornos en los que se necesita una alta precisión en la medición, las señales balanceadas reducen la interferencia y mejoran la exactitud de las mediciones.




## Pregunta 4:
¿Qué es el aislamiento eléctrico entre dos tierras? ¿En los diseños electrónicos que ventajas tiene el aislamiento entre señales?

### Respuesta:
El aislamiento eléctrico entre dos tierras se refiere a la práctica de separar dos partes de un sistema eléctrico o electrónico para evitar que las corrientes eléctricas fluyan entre ellas. Se logra utilizando materiales aislantes o dispositivos como transformadores o optoacopladores para evitar la conexión directa de las tierras.

**Ventajas del Aislamiento entre Señales en Diseños Electrónicos**
    1. **Prevención de Corrientes Parásitas:** El aislamiento evita la circulación de corrientes parásitas o fugas eléctricas entre diferentes partes del sistema. Esto es especialmente útil en circuitos sensibles o de alta impedancia.
    2. **Eliminación de Bucles de Tierra:** Los bucles de tierra pueden generar ruido y interferencias en los circuitos. El aislamiento entre señales evita la formación de bucles de tierra, mejorando la integridad de la señal.
    3. **Protección contra Descargas y Sobretensiones:** En sistemas donde puede haber diferencias de potencial significativas, el aislamiento protege contra descargas eléctricas y sobretensiones que podrían dañar componentes.
    4. **Mejora del Aislamiento Galvánico:** En sistemas que requieren aislamiento galvánico (aislamiento entre partes con diferentes potenciales), el aislamiento eléctrico asegura que no se establezcan conexiones conductivas no deseadas.
    5. **Reducción de Ruido y Interferencias:** El aislamiento minimiza la transferencia de ruido electromagnético entre circuitos, lo que mejora la calidad de las señales y la precisión de las mediciones.
    6. **Compatibilidad de Potencia:** Permite la interconexión de componentes o sistemas con diferentes niveles de potencia sin el riesgo de cortocircuitos.
    7. **Seguridad:** En sistemas donde hay interacción con usuarios, el aislamiento eléctrico puede mejorar la seguridad al evitar el riesgo de descargas eléctricas.

![Título de la imagen](Imagenes_CuestionarioPrevio/imagen4.png)




## Pregunta 5:
Investigue diseños electrónicos para aislar eléctricamente señales DC o de baja frecuencia (<100Hz).

### Respuesta:
 Optoacopladores (Optoaisladores):
Los optoacopladores son dispositivos que utilizan un LED en una parte del circuito y un fototransistor en la otra. La señal de entrada se convierte en una señal de luz por el LED, que luego se detecta en el fototransistor y se convierte de nuevo en una señal eléctrica. Esto proporciona aislamiento galvánico, ya que no hay conexión eléctrica directa entre las dos partes del circuito. Los optoacopladores son ideales para señales de baja frecuencia y DC, y son comunes en aplicaciones de control y monitoreo.

 Transformadores:
Los transformadores son otra opción para lograr el aislamiento eléctrico. Consisten en dos bobinas enrolladas alrededor de un núcleo de ferrita. La señal de entrada se induce en la primera bobina y se acopla magnéticamente a la segunda bobina, creando así una señal aislada eléctricamente en la salida. Los transformadores son efectivos para señales de baja frecuencia y pueden manejar niveles de potencia más altos que los optoacopladores.

![Optoacoplador](Imagenes_CuestionarioPrevio/Imagen5.jpg)




## Pregunta 6:
6. Investigue diseños de amplificadores con ganancia programable.
   
###Respuesta:

- Los Amplificadores con Ganancia Programable podrían clasificarse en 4 grupos:
    1. Amplificadores con resistencia interna con los que añadiendo resistencia externas se varia la ganancia.
    2. Amplificadores que incorporan todas las resistencias y la variación se logra haciendo cortocircuitos en la terminales.
    3. Amplificadores en los que la ganancia se consigue modificando la tensión analógica.
    4. Dispositivos que en los que la ganancia se consigue aplicando un código digital a la entrada.

- Tenemos el MCP6221 que correspondería el 4 grupo de Ganancia Programable, ya que se controla de manera digital ya que viene con un periférico SPI el cual puede ser controlado usando un microcontrolador. Al igual tenemos el AD7710 que también se controla atraves SPI.


![Título de la imagen](Imagenes_CuestionarioPrevio/img_5.png)

- En la empresa Analog Divice tenemos el AD8421 que un ruido muy bajo, tiene resistencias internas y ademas se acompaña con un MUX para controlar las ganancias, ya que tiene diferentes resistencias para variar la ganancia, este se podría considerar del grupo 1. El problema que se tiene es que la ganancia es no lineal lo cual no es deseado.

![Título de la imagen](Imagenes_CuestionarioPrevio/img_6.png)


## Pregunta 7:
7. Investigue como se mide el rechazo de modo común para una señal diferencial, y el rechazo de crosstalk entre dos canales.

### Rechazo de modo comun:

*Razón de rechazo en modo común (CMRR):* El texto se centra en la importancia de la medida de la capacidad de un amplificador para rechazar señales no deseadas que afectan ambas entradas por igual, es decir, señales en modo común. Esto se conoce como la Razón de Rechazo en Modo Común (CMRR).

$$ CMRR = 20*\log_{10}(\frac{A_{ol}}{A_{cm}}) $$

*Señales deseadas y no deseadas:* En un amplificador diferencial, las señales deseadas pueden aparecer en una sola entrada o en ambas con polaridades opuestas. Por otro lado, las señales no deseadas (ruido) que tienen la misma polaridad en ambas entradas son eliminadas por el amplificador diferencial y no se reflejan en las salidas.

*Objetivo del amplificador diferencial:* El objetivo ideal de un amplificador diferencial es tener una alta ganancia con las señales deseadas y ganancia cero con señales en modo común. Sin embargo, en la práctica, existe una pequeña ganancia en modo común, que generalmente es mucho menor que 1, mientras que se logra una alta ganancia de voltaje diferencial.

*Relación entre ganancia diferencial y en modo común:* Se resalta que cuanto mayor sea la relación entre la ganancia de voltaje diferencial (Av(d)) y la ganancia en modo común (Amc), mejor será el desempeño del amplificador diferencial en términos de rechazar señales en modo común.

*CMRR como medida de desempeño:* Se sugiere que una medida efectiva del desempeño de un amplificador diferencial en la capacidad de rechazar señales no deseadas en modo común es el cociente entre la ganancia de voltaje diferencial y la ganancia en modo común, que es precisamente la Razón de Rechazo en Modo Común (CMRR).

Un CMRR más alto indica una mejor capacidad del sistema para rechazar las interferencias comunes. Los sistemas con un CMRR alto son deseables en aplicaciones sensibles en las que se necesita minimizar las interferencias, como en sistemas biomédicos o de audio profesional. [7]

![Título de la imagen](Imagenes_CuestionarioPrevio/Imagen7.png)

### Crosstalk:

El rechazo de crosstalk (también conocido como diafonía) se refiere a la capacidad de un sistema para rechazar las interferencias provenientes de señales en canales adyacentes o cercanos. Por lo general, se utiliza para medir la interferencia que se produce entre dos canales cercanos cuando están transmitiendo señales simultáneamente.

Para medir el rechazo de crosstalk, se puede calcular el Crosstalk Ratio (CTR):

$$ CTR = 20*\log_{10}(\frac{V_{senal principal}}{V_{crosstalk}}) $$

Un CTR más alto indica una mejor capacidad del sistema para minimizar la interferencia entre canales. Los sistemas con un buen rechazo de crosstalk son esenciales en entornos donde múltiples canales de transmisión están cercanos y necesitan operar sin afectarse mutuamente, como en sistemas de redes de datos y comunicaciones. En ambos casos, un valor más alto en las mediciones de rechazo indica un mejor rendimiento del sistema en términos de minimizar interferencias y ruidos no deseados. Estas mediciones son fundamentales para garantizar una transmisión de señal confiable y de alta calidad en aplicaciones críticas.


---

# Bibliografía

1. Kulwicki, B. M. (1991). Humidity sensors. Journal of the American Ceramic Society, 74(4), 697-708. [Enlace a la fuente](https://ceramics.onlinelibrary.wiley.com/doi/abs/10.1111/j.1151-2916.1991.tb06911.x).

2.  National Institute of Standards and Technology (NIST). "Thermocouples Calibrations Services". [Enlace a la fuente](https://www.nist.gov/pml/sensor-science/thermodynamic-metrology/thermocouples-calibrations-services).

3. C. K. Alexander, Fundamentals of Electric Circuits, McGraw-Hill Education, 2006. ISBN 978-607-15-0948-2.

4. Texas Instruments. "Isolation: Understanding Signal and Power Isolation in Digital Systems". [Enlace de la fuente](https://www.ti.com/lit/an/slla197/slla197.pdf).

5. Scherz, P., & Monk, S. (2013). Practical electronics for inventors. McGraw-Hill Education.. [Enlace a la fuente](https://www.accessengineeringlibrary.com/content/book/9780071771337).

6. Microchip. "Programmable Gain Amplifiers (PGAs), Operational Amplifiers and Comparators Design Guide".[Enlace de la fuente](http://ww1.microchip.com/downloads/en/devicedoc/21861b.pdf).

7. Thomas L. Floyd, Dispositivos Electrónicos, 8ª ed., PEARSON EDUCACION, 2008. ISBN 978-970-26-1193-6.

---
