# DevOps-Final
## Proyecto Final DevOps Beca Qualentum

    1. Descripción de la Arquitectura del Sistema

       Introducción:

        La aplicación es una aplicación web escrita en Python con el framework Flask,
         diseñada para gestionar nombres de usuarios en una base de datos.

       Arquitectura de Capas:

         La aplicación sigue una arquitectura de dos capas, ya que el frontend no se 
         implementa en esta solución:

           - Backend: Lógica de la aplicación implementada en Flask.
           - Base de Datos: PostgreSQL utilizada para almacenar nombres de usuario.
		   
       Componentes Principales:

         - Servidor Flask: Gestiona las solicitudes HTTP, maneja la lógica de la aplicación y
          conecta con la base de datos.
         - Base de Datos PostgreSQL: Almacena los nombres de usuarios.
		 
       Manejo de Datos:

         La base de datos contiene una base de datos "ejer_final" con campos como id y name. 
         La interacción con la base de datos se realiza a través de consultas SQL utilizando 
         el ORM de Flask-SQLAlchemy.

     2. Definición de la Arquitectura Cloud

        Elección de Proveedor Cloud:

          Se ha elegido AWS como proveedor de servicios en la nube debido a su amplia variedad
          de servicios, escalabilidad y confiabilidad.

        Despliegue en la Nube:

          La aplicación se despliega utilizando el ciclo de despliegue continuo (CD), en el que
          se utiliza Elastic-Beanstilk de AWS.

        Escalabilidad y Tolerancia a Fallos:

          La aplicación es escalable horizontalmente con instancias de EC2 adicionales para 
          garantizar disponibilidad. Para automatizar el escalado se implementa Elastic Beanstalk.

      3. Descripción del Ciclo de Vida

        Desarrollo:

        Se sigue una metodología ágil con sprints de dos semanas. El código se gestiona a través 
        de un repositorio Git, y las tareas se gestionan con Jira.

         Pruebas:

           Las pruebas unitarias y de covertura se ejecutan automáticamente en cada confirmación 
          a través de un pipeline action de Github.

  ![imagen GitHub Jenkins o Actions Github -> Elastic Beanstalk](https://assets-global.website-files.com/62b1b25a5edaf66f5056b068/62d1343221adea5442f119cd_Deployment-processes-of-Elastic-Beanstalk.png)

         Despliegue y Mantenimiento:

          El despliegue se realiza automáticamente desde el repositorio Git a través de 
          AWS Elastic Beanstalk. Las actualizaciones se implementan con mínimo tiempo de inactividad.


         Monitorización y Registro:

           Se utiliza AWS CloudWatch para la monitorización de métricas y logs. 
           Las alertas se configuran para notificar eventos críticos.

         Seguridad:

           Se aplican prácticas de seguridad, como el cifrado de datos en reposo y en tránsito, 
          y se gestionan los accesos a los recursos mediante roles IAM.

         Ciclo de Vida Completo:

           Integración continua, pruebas automáticas, despliegue y monitorización están 
           completamente integrados en un ciclo de vida continuo.

  ![imagen Ciclo de Vida](https://i.ytimg.com/vi/x2IN28DKK3o/sddefault.jpg)
           

## Implementación de la Solución

# 1- CREACIÓN DE UN ENTORNO LOCAL DE DESARROLLO:

  IDE elegido es Visual Studio Code por ser muy versatil al poder utilizar multiples 
  lenguajes y tener plugins adaptados a ellos, se puede utilizar cualquier otro IDE del mercado.
  Necesidad de tener instalado Python en version igual o superior a la 3, de forma global 
  en la máquina local, ya que es el lenguaje utilizado en la aplicación sobre la que tenemos 
  que desarrollar la solución.
  
  Una vez elegido la ruta y nombre de la carpeta que llevará nuestro proyecto " DevOps-Final",
	lo primero es clonar el repositorio público creado en github https://github.com/JuanGarciaMontero/DevOps-Final/ a nuestra carpeta proyecto.

  A continuación copiamos los archivos y carpetas de la aplicación en nuestro proyecto.
  Despues tenemos que aislar nuestro proyecto del resto del equipo, para poder utilizar
  la versión deseada de dependencias o librerias en nuestra aplicación. Para ellos creamos 
  un entorno virtual y cargamos las dependencias en su versión necesarias para nuestro proyecto. 
  a aplicación en local podemos arrancarla con "python run.py".

  Para crear un entorno local de desarrollo, sigue estos pasos:

  1. Configuración del Entorno:
      - python -m venv env
      - source env/Scripts/activate
  2. Instalación de Dependencias:
      - Instala las dependencias del proyecto: pip install -r requirements.txt.
  3. Ejecución Local:
      - Ejecuta la aplicación localmente: python run.py.
      - Accede a la aplicación en tu navegador: http://localhost:5000/data
    
# Crear Repositorio en GitHub con usuario JuanGarciaMontero con nombre "DevOps-Final"

  ## Crear en local una carpeta por cada rama. Dev, Ops y QA.

  Crear ramas: 

    ** git checkout -b Dev
      * git add *
      * git commit -m "Agrego archivos Dev"
      * git push --set-upstream origin Dev

    ** git checkout -b Ops
      * git add *
      * git commit -m "Agrego archivos Ops"
      * git push --set-upstream origin Ops

    ** git checkout -b QA
      * git add *
      * git commit -m "Agrego archivos QA"
      * git push --set-upstream origin QA
	  
 Explicación de las Ramas:
 
 1/ La rama "main" es la rama de producción que llevará el código de la aplicación preparado para producción y los 
 archivos que prepara la infrastructura como código y su despliegue en AWS(Cloudformation.yml)(Nube pública elegida). 
 El despliegue automatico o CD se realiza mediante el archivo Jenkinsfile de la rama main.
    
2/ La rama "Dev" tendrá el código de la aplicación en Flask además el archivo Docker (Dockerfile), que permitiran a los desarrolladores
poder evolucionar la aplicación contra la imagen docker de una base de datos postgresql. En esta fase no se permite que falle la aplicación
contra la base de datos. Se consigue pasando CI action de Github a esta rama.
	   
3/* La rama "QA" tendrá el código de la aplicación además de las modificaciones en el código para 
pasar test unitarios y de covertura. Los test se pueden pasar localmente (Dockerfile1 y Docker-compose.yml), pero se pretende que el código pase
a una canalizacion o pipeline de integración continua. Esto lo conseguimos a través de CI action de Github (no permitiendo errores al subir
código en esta rama, ya que debe pasar 80% de test de covertura), o on Jenkins. Tenemos elavorado un archivo Jenkinsfile.yml que recoge Jenkins
cuando hay cambios en el repositorio Github(configuración de webhook en Github y activar la recogidas de esos hooks y a que rama afecta "QA"), arranca
la canalización: primero vá elaborando un contenedor docker de la aplicación actual, y por la otra rama levanta una imagen docker con los archivos
de la aplicación y pasa los test de covertura; estos deben teneruna covertura mayor al 80% sino dará error el pipeline. Si todo va bien y pasa el
80% de los test de covertura, y estamos en la rama "main" o "QA"; continua con el push de la imagen docker generada a un repositorio, como Docker Hub o S3 de AWS.
  
4/* La rama "Ops" tendrá el código de la infractructura como código, será un entorno preproduccion.
Se pretende elaborar una plantilla en Cloudformation.yml para que elabore un entorno con la imagen de una base de datos postgresql y recoja del 
repositorio Docker Hub o S3 de AWS la imagen docker de nuestra aplicación. La construcción del archivo Cloudformation.yml tambien elaborará el servicio
de Elastic-Beanstalk de AWS. Si todo vá bien la salida de la plantilla Cloudformation.yml nos dará la url con la aplicación funcionando.
En esta rama se crea un Jenkinsfile que realizará el despliegue continuo en Elastic-Beanstalk de AWS.
	   
## PRUEBAS EN LOCAL DE LA APP

  Nos situamos en la rama Dev(Desarrollo). 
  Si todo vá bien clonamos con la rama main(producción).

## 1- Arrancamos una imagen docker posgresql: 
  docker run --name ejer_final_postgres -e POSTGRES_DB=ejer_final -e POSTGRES_USER=postgres -e 		POSTGRES_PASSWORD=postgres -d postgres
	  (de esta forma nos aislamos del sistema operativo local)
	
	 Ó
	
  ## 2- Instalar PostgreSQL para Windows. Levatar servicio y abrir "pgAdmin4".
    Crear acceso a postgres con el usuario "juan" en local por el puerto "5432"
    Crear base de datos "ejer_final"

   	app/config.py -> configurar para conectar a postgreSQL. 
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:juan@127.0.0.1:5432/ejer_final'
	(de esta forma no nos aislamos del sistema operativo local, ya que la instalación de postresql se
	 realizado en un sistema operativo Windows).

  * Ejecutar "python run.py"

    Pruebas del funcionamiento de la aplicación sobre la base de datos PostgreSQL.

    Pruebas de inserción:
    curl -X POST -H "Content-Type: application/json" -d '{"name": "Juan"}' http://localhost:5000/data
    curl -X POST -H "Content-Type: application/json" -d '{"name": "Pedro"}' http://localhost:5000/data
    curl -X POST -H "Content-Type: application/json" -d '{"name": "Luis Manuel"}' http://localhost:5000/data

    Prueba de recuperar todo:
    curl http://localhost:5000/data
    

    Prueba de borrado:
    curl -X DELETE http://localhost:5000/data/1

***************************************************************

# TEST UNITARIOS:

Nos situamos dentro de la rama QA(pruebas). Clonamos la rama Dev en QA.
Creamos los archivos Dockerfile1 y Docker-compose.yml. Con "Docker-compose up" levantamos la app con 
una base de datos postgresql.
En la rama QA incluimos la carpetas tests y dentro creamos el archivo "test_routes.py",
necerarias para realizar pruebas unitarias con "pytest". A continuación instalamos pytest.

pip install Flask-Testing psycopg2 pytest

Ejecutamos test unitarios:
Acer@Portatil-Juan MINGW64 ~/Desktop/DevOps-Qualentum/Proyecto_Final/reto_final_python1/reto_final_python (main)
$ pytest tests/
====================================================== test session starts =======================================================
platform win32 -- Python 3.7.16, pytest-7.4.4, pluggy-1.0.0
rootdir: C:\Users\Acer\Desktop\DevOps-Qualentum\Proyecto_Final\reto_final_python1\reto_final_python
collected 1 item

tests\test_routes
py .                                                                                                      [100%]

======================================================= 1 passed in 3.51s ======================================================== 

*********************************************************

# TEST COVERTURA:

Instalamos el repositorio "coverage" para realizar pruebas de cobertura. Incluimos dentro de requirements.txt
tanto unitest como coverage.

pip install coverage

Ejecutamos test de covertura. Antes modificamos archivo run.py para que si realiza test de covertura grabe
los resultado en un archivo.html

pytest --cov=app tests/
================================================================== test session starts ==================================================================
platform win32 -- Python 3.7.16, pytest-7.4.4, pluggy-1.0.0
rootdir: C:\Users\Acer\Desktop\DevOps-Qualentum\DevOps-Final\QA
plugins: cov-4.1.0
collected 1 item

tests\test_routes.py .                                                                                                                             [100%]

---------- coverage: platform win32, python 3.7.16-final-0 -----------
Name              Stmts   Miss  Cover
-------------------------------------
app\__init__.py      12      0   100%
app\config.py        19      0   100%
app\models.py         6      1    83%
app\routes.py        23      9    61%
-------------------------------------
TOTAL                60     10    83%


=================================================================== 1 passed in 2.61s =================================================================== 


# 2- CREACIÓN DE PIPELINE DE CI. JENKINS

Desde Jenkins (instalado en wsl(Windows)) se configura pipeline para ejecutar las pruebas unitarias, pruebas de covertura y linting; de forma automática. Se configura en Jenkins para que recoja el Jenkinsfile de Github en la rama "QA" y ejecute la canalización o pipeline. Al ejecutarse se crean dos ramas: la primera vá creando una imagen de la aplicación que recoge de "Dokerfile", y en la otra rama levanta un imagen docker con python ("python:3.9-slim"), ejecuta un entorno virtual y lo levanta, despues instala las librerias que necesita nuestra aplicación y a continuación pasa los test de
covertura. Si pasa el 80% de los test de covertura continua y pertenece a la rama "QA" o "main" crea un push a Docker Hub y S3 de AWS.


## CREACIÓN DE PIPELINE DE CI. GITHUB ACTIONS

Pruebas automaticas en actions de Github. Creamos carpeta .github/workflows/ci.yaml
Ponemos estas carpetas en las ramas main, Dev y QA. Cuando se realiza un push sobre
alguna de ellas reliza las actions en las que contruye una imagen linux, con python, 
las librerias de pytest y coverage, y ejecuta las pruebas.
En main y Dev se realizan pruebas de conexión a la base de datos despues de realizar
curl a funciones de crear, borrar o devolver todo.
En QA se realizan los test unitarios y test de covertura. Si pasa los test de covertura
con más de un 80% crea un pull-request a la rama principal o "main"(producción).

Se puede ver en https://github.com/JuanGarciaMontero/DevOps-Final/

****************************************************************************************


# 3- INFRAESTRUCTURA COMO CÓDIGO

Nos situamos en la rama "QA". Creamos un clon a la rama nueva llamada "Ops".

## 1./ Prueba Cloudformation.yml

Creación de cloudformation(Cloudformation.yml) donde se pide crear una instancia EC2 "t2.small" y que coja una ami de linux de amazon. Instanciamos EC2 más la imagen de la ami linux y un segurity group, y ejecutamos dentro libreria "http" para para poder tener un servidor web que arrancamos permitiendo que
escuche por el puerto 8080, creamos un index.html donde dentro escribimos el texto
"Hello from EC2". En el segurity group habilitamos el puerto 8080 para que conecte a través
de ssh a través de un rango de ips.
Como salida tendremos la instancia EC2 en AWS y una ip pública.

Despues de formar .yml pasamos "cfn-lint" para no tener errores en la estructura del yaml.
Debemos estar en linux.

Creamos acceso a cloudformation:

aws ec2 create-key-pair --key-name qualentum_cfn-keypair --query 'KeyMaterial' --output text > qualentum_cfn-keypair.pem

Ejecutamos: aws cloudformation deploy --stack-name "qualentum-aws-iac-test" --template-file Cloudformation.yml --parameter-overrides "MyIpAddress=88.12.12.1"

Despues de optener la salida de cloudformation: qualentum-LoadBala-QYRTZQATUF4F-1646991560.eu-west-1.elb.amazonaws.com

curl -X POST -H "Content-Type: application/json" -d '{"name": "Juan"}' "http://qualentum-LoadBala-QYRTZQATUF4F-1646991560.eu-west-1.elb.amazonaws.com:5000/data" ERROR 503 Servidor

curl "http://qualentum-LoadBala-QYRTZQATUF4F-1646991560.eu-west-1.elb.amazonaws.com:5000/data" ERROR 503 Servidor

## 2./ Prueba Cloudfomation_new.yml

Creamos Cloudformation_new.yml que creará una aplicación en Elastic Beanstalk con nuestra app y una
base de datos postgresql, y nos dará como resultado la url de la aplicación en preproducción.

## 3./ Prueba despliegue continuo "CD". Jenkinsfile. Rama Ops o preproducción.

Continuamos con las pruebas en la rama Ops. Creamos un Jenkinsfile para realizar las pruebas de despliegue continuo (CD), este recoje la imagen S3 del la aplicación y crea una aplicación en elasticbeanstalk, se finaliza con la creación del entorno en elasticbeanstalk. Si todo va bien nos devolvera la url de la aplicación en preproducción.

## 4./ Prueba despliegue continuo "CD". Jenkinsfile. Rama main o producción.

En la rama "main" o producción, preparamos la app para producción sin los test y el servidor Flask que arranque con Gurnicorn.

Creamos un Dockerfile para empaquetar la aplicación en un docker y si pasa las pruebas de covertura, que se guarde en Docker Hub y S3 de AWS.

A continuación creamos un Jenkinsfile que realice los mismo pasos que en "QA" pero ahora tambien debe
realizar el CD. Si son las ramas Ops o main se conecta a AWS y crea una aplicación en Elastibeanstalk
con un entorno virutal; dandonos la url de la aplicación en producción.



*********************************************************************************************************************************

# 4- DESPLIEGUE

 APROVISIONAMIENTO Y CONFIGURACIÓN DE HOSTS. PRUEBAS EN LOCALHOST. WSL(Windows)

* Ejecutar Ansible en Linux en desarrollo, dev. (aprovisionamiento para app e imagen de postgresql)

	ansible-playbook -i inventory.yml playbook.yml

Este script Ansible realiza varias tareas para la instalación y configuración de un entorno de aplicación Flask con Nginx como servidor web y PostgreSQL como base de datos. Está dividido en tres secciones, cada una dirigida a un grupo específico de servidores:

1./ Instalación y Configuración del Servidor Nginx con Flask:
  - Instala Nginx.
  - Crea un usuario llamado nginx.
  - Instala Python 3 y pip.
  - Instala virtualenv globalmente.
  - Crea un entorno virtual en /code/mlvenv e instala los paquetes requeridos para Flask y PostgreSQL en   este entorno.
  - Activa el entorno virtual.

2./ Instalación y Configuración de la Base de Datos PostgreSQL:
  - Instala PostgreSQL.
  - Configura la autenticación md5 en PostgreSQL modificando pg_hba.conf.
  - Reinicia PostgreSQL para aplicar los cambios.
  - Instala psycopg2 para la conexión entre Python y PostgreSQL.
  - Incluye variables desde un archivo Vault (secrets.yml) para configurar la base de datos.
  - Crea la base de datos y el usuario en PostgreSQL utilizando las variables del archivo Vault.
  
3./ Tareas Comunes:
  -En el servidor localhost (donde se ejecuta Ansible), crea un archivo de marcador de posición para indicar que la instalación está completa.
  -Actualiza la marca de tiempo del archivo de marcador de posición para reflejar la última provisión.

Además, se define un handler para recargar PostgreSQL en caso de cambios en su configuración.

Este script está estructurado para automatizar la instalación y configuración de los componentes necesarios para ejecutar una aplicación Flask con Nginx como servidor web y PostgreSQL como base de datos en un entorno Linux.

****************************************************************************************************

# Conlusiones de la elección de Elastic-Beanstealk:

## 1: Ofrece una forma rápida y sencilla de implementar y administrar aplicaciones web. Abstrae gran parte de la infraestructura subyacente, lo que facilita la implementación y el escalado de aplicaciones sin preocuparse por la infraestructura subyacente.

## 2: Proporciona escalado automático para aplicaciones web basadas en la carga de tráfico. Puedes escalar automáticamente la capacidad de computación, el equilibrio de carga y otros recursos en función de la demanda de la aplicación.

## 3: Es ideal para aplicaciones web tradicionales que se ejecutan en entornos preconfigurados (como PHP, Python, Java, etc.). Proporciona opciones limitadas de configuración para el entorno de ejecución.

## 4: Suele ser más fácil de administrar y puede ser más económico para aplicaciones simples o en etapas iniciales, ya que AWS se encarga de gran parte de la infraestructura subyacente.

## 5: Es más adecuado si tu equipo tiene poca experiencia con Kubernetes o desea una solución rápida y sencilla para implementar aplicaciones web.
