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

          La aplicación se despliega utilizando Cloudformation con grupos de seguridad, pares 
          de claves y balanceadores de carga.

        Escalabilidad y Tolerancia a Fallos:

          La aplicación es escalable horizontalmente con instancias de EC2 adicionales para 
          garantizar disponibilidad. Para automatizar el escalado se puede implementar Elastic Beanstalk.

      3. Descripción del Ciclo de Vida

        Desarrollo:

        Se sigue una metodología ágil con sprints de dos semanas. El código se gestiona a través 
        de un repositorio Git, y las tareas se gestionan con Jira.

  ![imagen Jira Github](https://www.bitband.com/blog/wp-content/uploads/2022/04/Jira-Git-CTA.png)

         Pruebas:

           Las pruebas unitarias y de covertura se ejecutan automáticamente en cada confirmación 
          a través de un pipeline action de Github.

  ![imagen GitHub Jenkins o Actions Github -> Elastic Beanstalk](https://assets-global.website-files.com/62b1b25a5edaf66f5056b068/62d1343221adea5442f119cd_Deployment-processes-of-Elastic-Beanstalk.png)

         Despliegue y Mantenimiento:

          El despliegue se realiza automáticamente desde el repositorio Git a través de 
          AWS Elastic Beanstalk. Las actualizaciones se implementan con mínimo tiempo de inactividad.

  ![imagen AWS Elastic Beanstalk](https://media.geeksforgeeks.org/wp-content/uploads/20230418121110/aws-beanstalk.webp)

         Monitorización y Registro:

           Se utiliza AWS CloudWatch para la monitorización de métricas y logs. 
           Las alertas se configuran para notificar eventos críticos.

  ![imagen AWS CloudWatch](https://docs.aws.amazon.com/images/AmazonCloudWatch/latest/monitoring/images/CW-default-dashboard-update.png)

         Seguridad:

           Se aplican prácticas de seguridad, como el cifrado de datos en reposo y en tránsito, 
          y se gestionan los accesos a los recursos mediante roles IAM.
      
  ![imagen AWS IAM](https://i.ytimg.com/vi/pmemtFjlApQ/maxresdefault.jpg)

         Ciclo de Vida Completo:

           Integración continua, pruebas automáticas, despliegue y monitorización están 
           completamente integrados en un ciclo de vida continuo.

  ![imagen Ciclo de Vida](https://i.ytimg.com/vi/x2IN28DKK3o/sddefault.jpg)
           

## Bloques de desarrollo:

# 1- Creación de un entorno local de desarrollo.

  ![imagen Piramide Tests](https://dc722jrlp2zu8.cloudfront.net/media/uploads/2022/11/18/untitled.png)

    - Clonar a un repositorio git la aplicación ejemplo.
    - Realizar test unitarios a nuevas características incorporadas en nuestra aplicación.
    - Documentación de: arquitectura de software, como se ejecutan los test,
      como se ejecutan localmente el entorno de pruebas y el modelo de ramas GIT.
    - Test de cobertura de al menos el 80% de las líneas de código

# 2- Creación de pipelen de CI. Jenkins.

  ![imagen Jenkins|50](https://miro.medium.com/v2/resize:fit:951/1*H9jHoRaRnJ0KnqmPs6xeUA.jpeg )

    - Clonado de código fuente
    - Ejecución de test
    - Creación imagen Docker para ejecutar software en un contenedor
    - Subida el resultadoa algún Registro (privado,EC2, Docker Hub, ...) 
      siempre que sea la rama Dev o main.
      - Documentar que hace Jenkins y Git, y en cada push se realice un job en Jenkins.

# 3- Infraestructura como código

  ![imagen AWS CludFormation](https://www.inbest.cloud/hs-fs/hubfs/Alondra/que%20es%20aws%20cloud%20formation.jpg)

    - El código generado debe estar en un repositorio de Git, que puede ser el mismo 
    que el de la aplicación o no (está decisión debe ser justificada). Utilizamos el mismo 
    repositorio Git ya que en la rama Ops tendremos la infraestructura tanto para desarrollo Dev
    como para produccion. Se diferencian en que en desarrollo utilizamos una imagen de posgresql 
    y en produccion (main) instalamos postgresql.
    - Se debe acompañar al código de IaC de instrucciones precisas sobre cómo conseguimos 
    ejecutar la creación/actualización de la infraestructura, incluyendo si es necesario 
    qué valores o variables de entorno debemos tener en cuenta.
    - Tampoco debemos olvidar que puede haber más de un entorno de despliegue y que nos podría 
    interesar regenerar la misma infraestructura, con un diferente set de recursos, en otro VPC.

# 4- Despliegue

  ![imagen Ansible Architecture](https://www.exevi.com/wp-content/uploads/2021/04/ansible-automation-engine-768x450.png)

    El objetivo es el de generar un playbook de Ansible que sepa desplegar una nueva versión 
    de una imagen Docker en la infraestructura que nosotros mismos hemos declarado y generado.
	  El único input que deberíamos necesitar es la versión por desplegar o una URL al artefacto/imagen.
	  Ten en cuenta aquellas estrategias de despliegue que permitan minimizar el tiempo de 
    indisponibilidad, así como la posibilidad de que el proceso falle y haya que volver atrás.

## Implementación de la Solución

# 1- CREACIÓN DE UN ENTORNO LOCAL DE DESARROLLO:

    IDE elegido es Visual Studio Code por ser muy versatil al poder utilizar multiples 
    lenguajes y tener plugins adaptados a ellos.
    Necesidad de tener instalado Python en version igual o superior a la 3, de forma global 
    en la máquina local. Ya que es el lenguaje utilizado en la aplicación sobre la que tenemos 
    que desarrollar la solución. Una vez elegido la ruta y nombre de la carpeta que llevará 
    nuestro proyecto " DevOps-Final", lo primero es clonar el repositorio público creado en 
    github https://github.com/JuanGarciaMontero/DevOps-Final/ a nuestra carpeta proyecto. 
    A continuación copiamos los archivos y carpetas de la aplicación en nuestro proyecto.
    A continuación tenemos que aislar nuestro proyecto del resto del equipo, para poder utilizar
     la versión deseada de dependencias o librerias en nuestra aplicación. Para ellos creamos 
     un entorno virtual y cargamos las dependencias en su versión necesarias para nuestro proyecto. 
     La aplicación en local podemos arrancarla con "python run.py".

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

## PRUEBAS EN LOCAL DE LA APP

    Nos situamos en la rama Dev(Desarrollo). 
    Si todo vá bien clonamos con la rama main(producción).

    Instalar PostgreSQL para Windows. Levatar servicio y abrir "pgAdmin4".
      Crear acceso a postgres con el usuario "juan" en local por el puerto "5432"
      Crear base de datos "ejer_final"

    app/config.py -> configurar para conectar a postgreSQL. 
       SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:juan@127.0.0.1:5432/ejer_final'

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

Nos situamos dentro de la rama QA(pruebas). Clonamos la rama main en QA.
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

 Desde Jenkins (instalado en wsl(Windows)) se configura pipeline para ejecutar las pruebas unitarias, pruebas de covertura y linting; de forma automática. Lo primero es realizar un dockerfile donde estará la app, tests y dependencias (requirements.txt), y lo se publica en Docker Hub. Desde Jenkins y apuntando al repositorio en Github donde se encuantra el Jenkisfile se ejecuta la CI de Jenkins y nos encontramos con error en los test debido a no tener la base de datos Postgresql.

Para test(dockerfile). Empaquetamos nuestra app con los requerimientos en un docker.

docker build -t juangarciamontero/app15:1.0.61 .
docker images
docker tag juangarciamontero/app15:1.0.61 juangarciamontero/app15:1.0.61
docker push juangarciamontero/app15:1.0.61

Al ejecutar Jenkinsfile desde Jenkins apuntando a un repo e Github, produce error al pasar
los test unitario y no continua, ya que no encuentra la base de datos Postgresql. Implemento la
solución con base de datos pero en Jenkins no me deja introducir comandos en el docker y lo cierra.


Ejecutando Python --version:
Print Message
0,75 Seg
0
Ejecutando Python --version:
python --version
Shell Script
6 Seg
0
+ python --version
1
Python 3.8.18
pytest
Shell Script
1 Min 25 Seg
4
collected 53 items / 14 errors
5
6
==================================== ERRORS ====================================
7
_ ERROR collecting QA/env/Lib/site-packages/greenlet/tests/test_contextvars.py _
8
ImportError while importing test module '/var/lib/jenkins/workspace/CI_DevOps-Final/QA/env/Lib/site-packages/greenlet/tests/test_contextvars.py'.

## CREACIÓN DE PIPELINE DE CI. GITHUB ACTIONS

Pruebas automaticas en actions de Github. Creamos carpeta .github/workflows/ci.yaml
Ponemos estas carpetas en las ramas main, Dev y QA. Cuando se realiza un push sobre
alguna de ellas reliza las actions en las que contruye una imagen linux, con python, 
las librerias de pytest y coverage, y ejecuta las pruebas.
En main y Dev se realizan pruebas de conexión a la base de datos despues de realizar
curl a funciones de crear, borrar o devolver todo.
En QA se realizan los test unitarios y test de covertura. Si pasa los test de covertura
con más de un 80 porciento crea un pull-request a la rama principal o "main"(producción).

Se puede ver en https://github.com/JuanGarciaMontero/DevOps-Final/

****************************************************************************************


# 3- INFRAESTRUCTURA COMO CÓDIGO

Nos situamos en la rama Dev(Desarrollo). Si todo vá bien clonamos con la rama main(producción).

Creación de cloudformation donde se pide crear una instancia EC2 "t2.small" y que coja una
ami de linux de amazon. Instanciamos EC2 más la imagen de la ami linux y un segurity group, y ejecutamos
dentro libreria "http" para para poder tener un servidor web que arrancamos permitiendo que
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

*********************************************************************************************************************************

# 4- DESPLIEGUE

 APROVISIONAMIENTO Y CONFIGURACIÓN DE HOSTS. PRUEBAS EN LOCALHOST. WSL(Windows)

* Ejecutar Ansible en Linux en desarrollo, dev. (aprovisionamiento para app e imagen de postgresql)

	Crea archivo secrets.yml -> ansible-vault encrypt secrets.yml

	ansible-playbook -i inventory.yml playbook_dev.yml --ask-vault-pass -> contraseña=juan
  
    Si el contenedor ya está creado con el mismo nombre dará error así que:
    docker ps -a
    docker stop 1353d9fab800
    docker rm 1353d9fab800

* Ejecutar Ansible en Linux en producción, prod.(aprovisionamiento para app y base de dato postpresql)

	Crea archivo secrets.yml -> ansible-vault encrypt secrets.yml

	ansible-playbook -i inventory.yml playbook_prod.yml ->

TASK [Crear base de datos y usuario en PostgreSQL] **************************************************************************fatal: [localhost]: FAILED! => {"changed": false, "msg": "unable to connect to database: connection to server on socket "/var/run/********ql/.s.PGSQL.5432" failed: fe_sendauth: no password supplied\n"} ...ignoring
