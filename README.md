# Escáner de Puertos en Python 🔍

Un script básico desarrollado en Python para identificar puertos abiertos en una dirección IP objetivo, utilizando la librería `socket`. Este es mi primer proyecto de automatización enfocado en ciberseguridad.

## 🛠️ Tecnologías usadas
* Python 3
* Librerías nativas: `socket`, `datetime`, `sys`

## 🧠 Conceptos de Ciberseguridad aplicados
* **Reconocimiento de red (Information Gathering):** Identificación de vectores de ataque potenciales.
* **Protocolo TCP/IPv4:** Entendimiento del *Three-way handshake*.
* **Manejo de conexiones a bajo nivel:** Creación y gestión de *sockets*.

## 🚀 Futuras mejoras planificadas
* Implementar *Multithreading* (hilos) para que el escaneo sea asíncrono y mucho más rápido.
* Añadir paso de argumentos por terminal para que el usuario elija la IP a escanear dinámicamente.
* Detección de servicios (Banner grabbing) para saber qué hay detrás de cada puerto abierto.