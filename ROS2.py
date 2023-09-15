#Equipo 3
#Nodo que envía los datos recibidos al broker de MQTT

#Importar librerías necesarias
import rclpy
from rclpy.node import Node
from mensaje.msg import Mensaje
from geometry_msgs.msg import Twist
import random
import paho.mqtt.client as mqttClient
import json
import time

def on_connect(client, userdata, flags, rc):
    """Función que establece la conexión
   
    """
    if rc==0:
        print("Conectado al broker")
        global Connected
        Connected = True
    else:
        print("Falla en la conexión")
    return

Connected = False  #variable para verificar el estado de la conexión
broker_address= "10.48.60.51" #dirección del Broker
port= 1883 #puerto por defecto de MQTT
#tag1 = "/Equipo3/IMU"  #tag, etiqueta o tópico
#tag2 = "/Equipo3/Cámara"  #tag, etiqueta o tópico
#tag3 = "/Equipo3/Velocidad"  #tag, etiqueta o tópico
tag4 = "/Equipo3/Rover" #tag, etiqueta o tópico

client = mqttClient.Client("identificador") #instanciación
client.on_connect = on_connect #agregando la función
client.connect(broker_address, port)
client.loop_start() #inicia la instancia

#Crear nodo
class Centro(Node):

    #Función que inicia el modo suscriptor al tópico deseado
    def __init__(self):
        super().__init__('centro')
        self.sub = self.create_subscription(Twist, 'cmd_vel', self.chatter_callback, 10)

    #Función que envía los datos recibidos al broker de MQTT, en formato JSON
    def chatter_callback(self, msg):
      sen = msg.velocidad.linear.x
      try:
          #val1=json.dumps({"Posicion_x": nom})
          #val2=json.dumps({"Posicion_y": can})
          val3=json.dumps({"Velocidad": sen})
          #val4=json.dumps({"Posicion_x": nom,"Posicion_y": can,"Velocidad": sen})
          print(tag3,val3)
          #client.publish(tag1,val1,qos=0)
          #client.publish(tag2,val2,qos=0)
          client.publish(tag3,val3,qos=0)
          #client.publish(tag4,val4,qos=0)
          time.sleep(2)
      except KeyboardInterrupt: #cuando presionas Ctrl +C
          print("Envío de datos detenido por el usuario")
          client.disconnect()
          client.loop_stop()


def main(args=None):
    rclpy.init(args=args)

    node = Centro()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()