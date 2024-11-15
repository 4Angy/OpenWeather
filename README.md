Comandos con Docker compose:

<<<<<<< HEAD
<<<<<<< HEAD
El comando para ejecutar la imagen es: "docker build -t open_weather_app ." en nuestro caso fue open_weather_app pero en general ahí va el nombre del proyecto a ejecutar. A continuación debemos ejecutar el siguiente comando para hacer correr nuestro contenedor Docker: "docker run --env-file .env -it open_weather_app". Este último comando retornará en nuestra terminal una serie de direcciones donde la API no está operativa , en nuestro caso no pudimos lograr que devuelva el localhost en la terminal pero sí esta operativo cuando se le buscó por URL.
=======
El comando para ejecutar la imagen es: "docker build -t open_weather_api ." en nuestro caso fue open_weather_api pero en general ahí va el 
nombre del proyecto a ejecutar. 
A continuación debemos ejecutar el siguiente comando para hacer correr 
nuestro contenedor Docker: "docker run --env-file .env -p 5000:5000 -ti open_weather_api". 
Este último comando retornará en nuestra terminal una serie de direcciones donde la API 
no está operativa , en nuestro caso no pudimos lograr que devuelva el localhost en la terminal 
pero sí esta operativo cuando se le buscó por URL.
>>>>>>> ff56966e5470ac65f5254087ffe161f3a167e323
=======
docker-compose up -d
>>>>>>> 7ad0bd242cf78efbcd4e5ce0015453237c9bec9f



docker compose run weather_app
