
# Interfaz Estación de Control

Programas para conectar el Rover a través de MQTT y mostrar los datos obtenidos mediante una interfaz de usuario.


## Instalar librerías necesarias

Para la conexión de MQTT, es necesario instalar la libreía paho-mqtt

```bash
  pip install paho-mqtt
```

## Levantar un broker propio

Para levantar un broker propio en una Raspberry Pi, se deben de correr los siguientes comandos en una terminal

#### 1. Update de repositorios y upgrade del sistema

```bash
  sudo apt-get update && sudo apt-get upgrade -y
```
#### 2. Instala Docker

```bash
  curl -sSL https://get.docker.com | sh
```
#### 3. Agrega usuario al grupo de docker

```bash
  sudo usermod -aG docker [usuario] 
```
#### 4. Verifica que el usuario está en el grupo

```bash
  groups [usuario]
```
#### 5. Reinicia la raspberry

```bash
  sudo reboot now 
```
#### 6. Instala pip 3 (en caso de que no lo tengas)

```bash
  sudo apt install python3-pip
```
#### 7. Instala docker-compose

```bash
  sudo pip3 install docker-compose
```
#### 8. Configura docker para que se ejecute al arranque del OS

```bash
  sudo systemctl enable docker 
```
## Ya que instalaste Docker y docker-compose

#### 1. Crea una carpeta para el broker

#### 2. Crea un manifiesto (debe llamarse docker-compose.yml)

```bash
  nano docker-compose.yml
```
#### 3. Escribe o copia el texto de abajo en el archivo

```bash
version: '3'
services:
    Mosquitto:
        container_name: Mosquitto
        image: 'eclipse-mosquitto:2.0.14'
        ports:
            - '1883:1883'
        command: mosquitto -c /mosquitto-no-auth.conf
        tty: true
```
## Para correr/ejecutar cualquier contenedor

#### 1. Navega hasta la carpeta en donde está ubicado el archivo docker-compose.yml que deseas

#### 2. Ejecuta el manifiesto

```bash
  docker-compose up -d
```
#### 3. Para detener el contenedor

```bash
  docker-compose down
```
## Instalar Node-RED

#### 1. Instalar Node.js a través de este link: https://nodejs.org/es

#### 2. Ejecutar el siguiente comando en una terminal (Sin sudo si estás en Windows)

```bash
  sudo npm install -g --unsafe-perm node-red
```
#### 3. Para correr Node-RED, correr el siguiente comando en una terminal

```bash
  node-red

## Para usar Node-RED, escribir la dirección que se muestra en la terminal al correrlo

![App Screenshot](https://github.com/SaulA01745146/Quantum/blob/main/Node-RED.jpg)
```
