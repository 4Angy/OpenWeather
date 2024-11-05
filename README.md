Una vez terminado el proyecto ,definido las librerías a utilizar y establecido las variables de entorno procedemos a crear la imagen de Docker ,obviamente teniendo en cuenta que Docker esté activo.

<<<<<<< HEAD
El comando para ejecutar la imagen es: "docker build -t open_weather_app ." en nuestro caso fue open_weather_app pero en general ahí va el nombre del proyecto a ejecutar. A continuación debemos ejecutar el siguiente comando para hacer correr nuestro contenedor Docker: "docker run --env-file .env -it open_weather_app". Este último comando retornará en nuestra terminal una serie de direcciones donde la API no está operativa , en nuestro caso no pudimos lograr que devuelva el localhost en la terminal pero sí esta operativo cuando se le buscó por URL.
=======
El comando para ejecutar la imagen es: "docker build -t open_weather_api ." en nuestro caso fue open_weather_api pero en general ahí va el 
nombre del proyecto a ejecutar. 
A continuación debemos ejecutar el siguiente comando para hacer correr 
nuestro contenedor Docker: "". 
Este último comando retornará en nuestra terminal una serie de direcciones donde la API 
no está operativa , en nuestro caso no pudimos lograr que devuelva el localhost en la terminal 
pero sí esta operativo cuando se le buscó por URL.
>>>>>>> ff56966e5470ac65f5254087ffe161f3a167e323

Quedamos a disposición de cualquier duda, consulta o corrección.

Grupo Guido Van Rossum.
docker run --env-file .env -p 5000:5000 -ti open_weather_api