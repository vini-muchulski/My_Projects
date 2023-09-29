# Circles and Arcs in Python

## English

This repository contains two Python scripts for generating and plotting circles and circular arcs:

### circles.py

This script defines a `Circulo` class that can be used to create a circle with given radius and angle. It contains methods to calculate properties like the arc length and x,y coordinates. 

An example usage is shown, creating a circle with radius 4 and angle 30, and plotting it using Matplotlib.

### circle_intervalos.py

This script is similar, but the `Circulo` class takes a start and end angle rather than a single angle. This allows generating circles, semicircles, or circular arcs.

The key part is using `np.linspace()` to generate multiple angles between the start and end, which provides enough points to plot a smooth curve.

Examples are shown for full circles, arcs, and semicircles.

## Português 

Este repositório contém dois scripts Python para gerar e plotar círculos e arcos circulares:

### circles.py

Este script define uma classe `Circulo` que pode ser usada para criar um círculo com raio e ângulo dados. Ele contém métodos para calcular propriedades como o comprimento do arco e coordenadas x, y.

É mostrado um exemplo de uso, criando um círculo com raio 4 e ângulo 30, e plotando-o usando Matplotlib.

### circle_intervalos.py

Este script é semelhante, mas a classe `Circulo` recebe um ângulo inicial e final em vez de um único ângulo. Isso permite gerar círculos, semicírculos ou arcos circulares. 

A parte chave é o uso de `np.linspace()` para gerar múltiplos ângulos entre o início e o fim, o que fornece pontos suficientes para plotar uma curva suave.

São mostrados exemplos de círculos completos, arcos e semicírculos.
