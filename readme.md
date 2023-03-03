# Control de Acceso basado en reconocimiento facial con Raspberry Pi 4 y OpenCV

se tiene como objetivo implementar un sistema de control de acceso. El sistema se encarga de reconocer el rostro de una persona y permitir o denegar el acceso a una determinada área según las credenciales del usuario.

# Componentes
#### -Raspberry Pi 4
#### -PiCamera
#### -LCD 16*2
#### -Protoboard
#### -Adaptador I2C
#### -3 Leds (Verde, Amarillo, Rojo)
#### -Buzzer
#### -Boton
#### -Carcasa personalizada para Raspberry Pi

# Funcionamiento
## Conexiones de la Raspberry pi
Led verde= GPIO 22

Led amarillo=GPIO 27

Led rojo= GPIO 17

Buzzer= GPIO 23

LCD= GPIO 2 & 3

Boton= GPIO 24

## Instalación

Clone el repositorio en su Raspberry Pi 4.
Dependencias
Python 3.8 o superior
OpenCV
numpy
imutils
keyboard
RPi.GPIO
I2C_LCD_driver
Instalación
Para instalar las dependencias, se recomienda utilizar pip, el administrador de paquetes de Python. Para instalar OpenCV, puedes ejecutar el siguiente comando en la terminal:


```bash
pip install opencv-python
```

```bash
pip install numpy imutils keyboard RPi.GPIO I2C_LCD_driver
```


## Uso
Antes de ejecutar el código, es necesario conectar una cámara web al dispositivo y conectar una pantalla LCD al GPIO de la Raspberry Pi como se explico anteriormente.

Si las conexiones estan correctas y las dependencias ejecuta el archivo tecla.py

```bash
python3 tecla.py
```


 

Forquee el repositorio.
Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.