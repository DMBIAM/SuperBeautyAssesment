# Super Beauty Assessment

## Control de Inventario de Computadores

### Introducción

Este proyecto consiste en una aplicación desarrollada en Django para el control de inventario de computadores. A continuación se describen los principales pasos que se ejecutan para poder utilizar la aplicación:

**Pasos**
- Se crea un proyecto Django llamado superbeautyassesment utilizando una base de datos SQLite, utilizando el siguiente comando

```bash
django-admin startproject superbeautyassesment
```
- Creación de superusuario: Se ha creado un superusuario con el nombre de usuario admin y contraseña admin para acceder al panel de administración de Django, bajo el comando 

```bash
python manage.py createsuperuser --username=admin --email=admin@example.com
```

Nota: Este paso se puede cambiar y orientar su ejecución desde docker utilizando el comando directamente en el dockerfile y pasando como argumentos variables asociadas al nombre y contraseña del usuario, los cuales estrían almacenados en archivo de entorno que sería leído por docker ofreciendo una mayor seguridad y control para este tipo de datos

- Creación de aplicación Django: Se ha creado una aplicación Django llamada inventario para gestionar el inventario de computadores, utilizando el siguiente comando

```bash
python manage.py startapp inventario
```

- Creación de modelos: Se han definido dos modelos principales:

-- Equipo: Este modelo contiene campos como referencia, marca, procesador, memoria, disco y tipo para describir cada equipo.

![Create Equipment](https://github.com/DMBIAM/SuperBeautyAssesment/blob/main/pic-evidence/add_equipment.png)

-- EquipoUsuario: Este modelo registra la asignación de equipos a usuarios, con campos como llave foránea Equipo, llave foránea usuario (de Django), fecha de asignación y fecha de entrega.

![Create forenkey equipment User](https://github.com/DMBIAM/SuperBeautyAssesment/blob/main/pic-evidence/add_equipment_user.png)

- Creación vistas de administración:

-- Vista de administración de Equipos: Permite ver una lista de equipos con campos como id, referencia, marca y tipo. También incluye filtros por tipo y un buscador por referencia.

![List Equipment](https://github.com/DMBIAM/SuperBeautyAssesment/blob/main/pic-evidence/list_equipment.png)

-- Vista de administración de EquiposUsuarios: Muestra una lista de asignaciones de equipos a usuarios, con campos como id, equipo, usuario y fecha de asignación. Incluye filtros por fecha de asignación y por usuario.

![List Equipment Users](https://github.com/DMBIAM/SuperBeautyAssesment/blob/main/pic-evidence/list_equipment_user.png)

Creación Apiview: Se ha creado una Apiview con el método GET para consultar la lista de equipos mediante una API, la cual responde en forma to json 

![List Equipment Rest](https://github.com/DMBIAM/SuperBeautyAssesment/blob/main/pic-evidence/rest_get_equipment.png)

### Ejecución de pruebas

Para el desarrollo del proyecto se ejecutaron pruebas unitarias y de análisis de código estático, las cuales fueron ejecutadas dentro del contenedor Docker dispuesto al final del presente README


-- Ejecución de prueba unitaria 

Ejemplo del comando utilizado:

```bash
python3 manage.py test
```
Resultado:

![List Equipment Rest](https://github.com/DMBIAM/SuperBeautyAssesment/blob/main/pic-evidence/test_python.png)

-- Ejecución del análisis de código estático:

Ejemplo del comando utilizado:

```bash
pylint manage.py
```
Resultado:

![List Equipment Rest](https://github.com/DMBIAM/SuperBeautyAssesment/blob/main/pic-evidence/static_code_analyser.png)


## Run Super Beauty Assessment in to Docker

### Introducción

Este segmento  contiene los archivos y pasos necesarios para ejecutar la aplicación web en Python utilizando Docker. La aplicación está basada en Django y se proporcionan instrucciones sobre cómo configurar y ejecutar el contenedor Docker para probar la aplicación.


### Archivos

1. **.env** 

Este archivo contiene las variables de entorno necesarias para la configuración de la aplicación. Incluye las siguientes variables

- REPO: URL del repositorio de GitHub donde se encuentra el código de la aplicación.
- USER_DJANGO: Nombre de usuario de Django para el superusuario.
- PWD_DJANGO: Contraseña de Django para el superusuario.
- USER_MAIL: Correo electrónico del superusuario de Django.

Ejemplo:

```bash
REPO = https://github.com/DMBIAM/SuperBeautyAssesment
USER_DJANGO = admin
PWD_DJANGO = admin
USER_MAIL = admin@admin.com
```


2. **docker-compose.yml**

Este archivo define los servicios del contenedor Docker. El servicio web es el principal y contiene la configuración para construir y ejecutar la aplicación. Se configuran las siguientes opciones:

- container_name: Nombre del contenedor Docker.
- build: Configuración para construir la imagen Docker.
- image: Nombre de la imagen Docker.
- command: Comando para ejecutar la aplicación.
- ports: Mapeo de puertos para acceder a la aplicación desde el host.


Ejemplo:

```bash
version: '3.1'

services:
  web:
    container_name: super_beauty_assesment
    build:
      dockerfile: Dockerfile
      args:
        USER_DJANGO: $USER_DJANGO
        PWD_DJANGO: $PWD_DJANGO
        USER_MAIL: $USER_MAIL
        REPO: $REPO
    image: super_beauty_assesment
    command: python manage.py runserver 0.0.0.0:8000
    ports:
      - "8000:8000"
```

NOTA: Utiliza como argumentos las variables de entornos definidos en el archivo .env

3. **Dockerfile**

Este archivo define la configuración para construir la imagen Docker. Incluye los siguientes pasos:

- Instalación de Git para clonar el repositorio de la aplicación.
- Instalación de herramientas como Pylint, Coverage, Pytest y Bandit.
- Clonación del repositorio de la aplicación.
- Instalación de las dependencias de la aplicación.
- Migración de la base de datos.
- Creación del superusuario de Django.


4. **Ejecución del contenedor**

Ejecuta el siguiente comando para construir y ejecutar el contenedor Docker:

```bash
docker-compose up --build
```

Una vez que el contenedor esté en ejecución, la aplicación estará disponible en http://localhost:8000 en su navegador web.

Para acceder al panel de administración de Django, puedes ir a http://localhost:8000/admin e iniciar sesión con las credenciales del superusuario definidas en el archivo .env del proyecto python
