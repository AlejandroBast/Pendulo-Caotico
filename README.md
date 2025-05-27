# 🌀 Péndulo Caótico – Simulación y Aplicación en el Estudio de Sismos

## 🌍 Introducción: ¿Qué son los sismos?

Los **sismos**, o **terremotos**, son movimientos bruscos de la superficie terrestre causados por la liberación repentina de energía acumulada en la corteza terrestre. Esta liberación ocurre generalmente debido a fricción entre placas tectónicas, deslizamientos o fallas geológicas.

Comprender cómo responden las estructuras a **vibraciones complejas** es esencial en ingeniería sísmica, ya que permite desarrollar edificaciones más seguras y resistentes.

## 🎯 Objetivo del repositorio

Este repositorio presenta una simulación de un **péndulo caótico forzado** utilizando Python. El modelo permite visualizar cómo un sistema dinámico responde ante una fuerza periódica, y cómo pequeñas variaciones en las condiciones iniciales pueden desencadenar un comportamiento caótico.

El **péndulo caótico** sirve como analogía para estructuras expuestas a fuerzas externas impredecibles, como las generadas por un terremoto. A través de este modelo, se puede analizar la sensibilidad de estos sistemas y su posible inestabilidad ante ciertas frecuencias o amplitudes.

---

## 🧮 Relación con el estudio de sismos

La dinámica del sistema se basa en una **ecuación diferencial no lineal de segundo orden**, que representa el movimiento de un péndulo sometido a una fuerza periódica:

```
θ''(t) + α·θ'(t) + (g/L)·sin(θ(t)) = γ·cos(ω·t)
```

Donde:

- `θ(t)`: ángulo del péndulo respecto a la vertical  
- `α`: coeficiente de amortiguamiento  
- `g`: aceleración de la gravedad  
- `L`: longitud del péndulo  
- `γ`: amplitud de la fuerza externa  
- `ω`: frecuencia angular de la fuerza externa  
- `t`: tiempo  

Este tipo de ecuación permite modelar **vibraciones no lineales**, útiles para simular cómo una estructura reacciona ante ondas sísmicas. Cuando estas fuerzas resuenan con la estructura, el comportamiento puede volverse caótico, lo que ayuda a estudiar **escenarios de falla** o **inestabilidad estructural**.

---

## 📂 Estructura del repositorio

```
Pendulo-Caotico/
├── pendulo_caotico.py    # Simulación principal del péndulo forzado
├── README.md             # Este archivo
```

---

## 🚀 Cómo ejecutar la simulación

1. Asegúrate de tener Python 3 instalado.
2. Instala las dependencias necesarias:
   ```bash
   pip install numpy matplotlib scipy
   ```
3. Ejecuta el archivo principal:
   ```bash
   python pendulo_caotico.py
   ```

Se abrirá una ventana de simulación que permite visualizar el comportamiento dinámico del sistema. Puedes modificar los parámetros para observar diferentes respuestas.

---

## 📊 Aplicaciones prácticas

- Visualización educativa de sistemas caóticos
- Modelado preliminar de estructuras sometidas a ondas sísmicas
- Análisis de resonancia y sensibilidad estructural
- Introducción a la dinámica no lineal en física e ingeniería

---

## 📘 Referencias

- Strogatz, S. H. (2015). *Nonlinear Dynamics and Chaos: With Applications to Physics, Biology, Chemistry, and Engineering*. CRC Press.
- Nayfeh, A. H., & Balachandran, B. (2008). *Applied Nonlinear Dynamics: Analytical, Computational and Experimental Methods*. Wiley.

---

## 🧠 Contribuciones

¿Te interesa el caos o la simulación de sistemas físicos? ¡Estás invitado a contribuir! Puedes abrir issues, enviar pull requests o simplemente experimentar con los parámetros del sistema. Cada aportación es bienvenida.
