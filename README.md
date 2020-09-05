# ValueArray

Ordena Arreglos de datos anidados en una estructura Unica API REST.

  - Recorre Arreglos anidados de numeros y genera un estructura Unica
  - Ordena el arreglo resultante
  - Almacena el ordenamiento para consultas fururas


### Tecnologias 

Desarrollado usando tecnologias:

* [Python] - Django Rest Framework - Gunicorn.
* [Docker] - Gestion de contenedores y despliegue.
* [PostgreSql] - Base de datos relacional.
* [Nginx] - Servidor de aplicaciones.

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

### Instalación

Para la instalación requiere [Docker](https://www.docker.com/) y [Docker Compose](https://docs.docker.com/compose/).

Clonar el proyecto e ingresar al directorio creado

```sh
$ git clone https://github.com/profefonso/ValuesArray.git
$ cd Values Array
```

Descargar y construir las imagenes necesarias

```sh
$ docker-compose build
$ docker-compose up 
```

### Probar App

Ingrese a la direccion para ver la documentacion del API en swagger
[http://localhost:1337/api/](http://localhost:1337/api/)

Ordenamiento de Array Anidado.

```sh
$ curl -X POST -H "Content-Type: application/json" \
 -d '{"items":[9,8,[3,4,[5,6],1],8]}' \
 http://localhost:1337/value_array/
```

Ver los Arrays creados [http://localhost:1337/value_array/](http://localhost:1337/value_array/):
```sh
$ curl -X GET "http://localhost:1337/value_array/" -H  "accept: application/json"
```


License
----

MIT
