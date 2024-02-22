# DevOps-Final
## Proyecto Final DevOps Beca Qualentum

En cuanto a la estructura del documento, este deberá estar compuesto de tres grandes secciones: 

• Una descripción de la arquitectura del sistema.
    Nos interesa definir qué servicios, métodos y tecnologías se necesitan para poder ofrecer una solución productiva moderna y competente. 
      • Balanceadores de carga. Docker
	  • Terminadores SSL. Clave pública y clave privada. Certificados 503, HTTPS
	  • Bases de datos. Posgresql
	  • Tecnologías de telemetría. Prometheus y Grafana
• Definición de la arquitectura cloud.
	  • AWS. EC2, S3, Cloudformation, Terraform
• Descripción del ciclo de vida. 
   * El modelo de desarrollo que se seguirá para evolucionar el producto
    – Cómo se desarrollará localmente. IDE(Visual Studio Code) Python. ENV. 
    – Tipos de pruebas obligatorias. Pruebas unitarias, pruebas integración, pruebas de cobertura de código
    – Diferentes tipos de entornos. Dev, QA, Ops, Prod(main)
    – Modelo de ramas usado para trabajar de manera colaborativa. GIT, Github 
    – ¿Trunk-based? Main, Des, QA, Prod(main) ¿Github? ¿Algún otro modelo? CI/CD
    – ¿Cómo se decide qué se despliega y dónde? CD en AWS con Terraform o CloudFormation.
   * El modelo de operaciones
     Que se seguirá para garantizar que tu software llegue sin errores a producción y que sea capaz de dar servicio, de manera efectiva, a nuestros usuarios. Te comparto algunos ejemplos de esto: 
     – ¿Qué estrategia de despliegue usaremos en EC2 para poder dar servicio sin interrupciones? Estrategia de despliegue en EC2 como Canary.
     – ¿Usaremos algún SaaS de AWS para la gestión de las trazas y logs? Ver SaaS de AWS para observabilidad. 
	 – ¿O desplegamos el nuestro propio? Ver AWS Trazas y logs; o usar Prometheus y Grafana	 


## Bloques de desarrollo:

# 1- Creación de un entorno local de desarrollo.

  ![imagen Piramide Tests](https://dc722jrlp2zu8.cloudfront.net/media/uploads/2022/11/18/untitled.png)

    Clonar a un repositorio git la aplicación ejemplo.
	Realizar test unitarios a nuevas características incorporadas en nuestra aplicación
	Documentación de: arquitectura de software, como se ejecutan los test, como se ejecutan localmente el entorno de pruebas y el modelo de ramas GIT.
	Test de cobertura de al menos el 80% de las líneas de código
# 2- Creación de pipelen de CI. Jenkins.

  ![imagen Jenkins](https://miro.medium.com/v2/resize:fit:951/1*H9jHoRaRnJ0KnqmPs6xeUA.jpeg)

    Clonado de código fuente
    Ejecución de test
	Proceso de linting
	Creación imagen Docker para ejecutar software en un contenedor
	Subida el resultadoa algún Registro (privado,EC2, Docker Hub, ...) siempre que sea la rama des o main.
	Documentar que hace Jenkins y Git, y en cada push se realice un job en Jenkins.
# 3- Infraestructura como código

  ![imagen AWS CludFormation](https://www.inbest.cloud/hs-fs/hubfs/Alondra/que%20es%20aws%20cloud%20formation.jpg)

    El código generado debe estar en un repositorio de Git, que puede ser el mismo que el de la aplicación o no (está decisión debe ser justificada).
	Se debe acompañar al código de IaC de instrucciones precisas sobre cómo conseguimos ejecutar la creación/actualización de la infraestructura, incluyendo si es necesario qué valores o variables de entorno debemos tener en cuenta.
	Tampoco debemos olvidar que puede haber más de un entorno de despliegue y que nos podría interesar regenerar la misma infraestructura, con un diferente set de recursos, en otro VPC.
# 4- Despliegue

  ![imagen Ansible Architecture](https://www.exevi.com/wp-content/uploads/2021/04/ansible-automation-engine-768x450.png)

    El objetivo es el de generar un playbook de Ansible que sepa desplegar una nueva versión de una imagen Docker en la infraestructura que nosotros mismos hemos declarado y generado.
	El único input que deberíamos necesitar es la versión por desplegar o una URL al artefacto/imagen.
	Ten en cuenta aquellas estrategias de despliegue que permitan minimizar el tiempo de indisponibilidad, así como la posibilidad de que el proceso falle y haya que volver atrás.

  # Implementación de la Solución

    Creación de un Entorno Local de Desarrollo:
    Para crear un entorno local de desarrollo, sigue estos pasos:
      1. Configuración del Entorno:
         - python -m venv env
         - source env/Scripts/activate
      2. Instalación de Dependencias:
         - Instala las dependencias del proyecto: pip install -r requirements.txt.
      3. Ejecución Local:
         - Ejecuta la aplicación localmente: python run.py.
         - Accede a la aplicación en tu navegador: http://localhost:5000.
      4. Pruebas Locales:
         - Asegúrate de que todas las funcionalidades se ejecuten correctamente en el entorno local.
    
# Crear Repositorio e GitHub con usuario JuanGarciaMontero con nombre "DevOps-Final"

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

    Instalar PostgreSQL para Windows. Levatar servicio y abrir "pgAdmin4".
      Crear acceso a postgres con el usuario "juan" en local por el puerto "5432"
      Crear base de datos "ejer_final"

    app/config.py -> configurar para conectar a postgreSQL. 
       SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:juan@127.0.0.1:5432/ejer_final'

    * Ejecutar "python run.py"

    curl -X POST -H "Content-Type: application/json" -d '{"name": "Juan"}' http://localhost:5000/data
    curl -X POST -H "Content-Type: application/json" -d '{"name": "Pedro"}' http://localhost:5000/data
    curl -X POST -H "Content-Type: application/json" -d '{"name": "Luis Manuel"}' http://localhost:5000/data

    curl http://localhost:5000/data

    curl -X DELETE http://localhost:5000/data/1

***************************************************************

# TEST UNITARIOS:

pip install Flask-Testing psycopg2 pytest

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

pip install coverage

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

## CREACIÓN DE PIPELINE DE CI. JENKINS

 Desde Jenkins se configura pipeline para ejecutar las pruebas unitarias, pruebas de covertura y linting; de forma
 automática. Lo primero es realizar un dockerfile donde estará la app, tests y dependencias (requirements.txt), y lo
 se publica en Docker Hub. Desde Jenkins y apuntando al repositorio en Github donde se encuantra el Jenkisfile se
 ejecuta la CI de Jenkins y nos encontramos con error en los test debido a no tener la base de datos Postgresql.

Para test(dockerfile)

docker build -t juangarciamontero/app15:1.0.1 .
docker images
docker tag juangarciamontero/app15:1.0.1 juangarciamontero/app15:1.0.1
docker push juangarciamontero/app15:1.0.1

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
con más de un 80 porciento crea un pull-request a la rama.

Se puede ver en https://github.com/JuanGarciaMontero/DevOps-Final/

****************************************************************************************

## INFRAESTRUCTURA COMO CÓDIGO

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

Ejecutamos: aws cloudformation deploy --stack-name "qualentum-aws-iac-test" --template-file main.yml --parameter-overrides "MyIpAddress=88.12.12.1"

Despues de optener la salida de cloudformation: qualentum-LoadBala-QYRTZQATUF4F-1646991560.eu-west-1.elb.amazonaws.com

curl -X POST -H "Content-Type: application/json" -d '{"name": "Juan"}' "http://qualentum-LoadBala-QYRTZQATUF4F-1646991560.eu-west-1.elb.amazonaws.com:5000/data" ERROR 503 Servidor

curl "http://qualentum-LoadBala-QYRTZQATUF4F-1646991560.eu-west-1.elb.amazonaws.com:5000/data" ERROR 503 Servidor

*********************************************************************************************************************************

# DESPLIEGUE
 APROVISIONAMIENTO Y CONFIGURACIÓN DE HOSTS. PRUEBAS EN LOCALHOST. WSL

* Ejecutar Ansible en Linux en desarrollo, dev. (aprovisionamiento para app e imagen de postgresql)

	Crea archivo secrets.yml -> ansible-vault encrypt secrets.yml

	ansible-playbook -i inventory.yml playbook-dev.yml --ask-vault-pass -> contraseña=juan

* Ejecutar Ansible en Linux en producción, prod.(aprovisionamiento para app y base de dato postpresql)

	Crea archivo secrets.yml -> ansible-vault encrypt secrets.yml

	ansible-playbook -i inventory.yml playbook-prod.yml ->

TASK [Crear base de datos y usuario en PostgreSQL] **************************************************************************fatal: [localhost]: FAILED! => {"changed": false, "msg": "unable to connect to database: connection to server on socket "/var/run/********ql/.s.PGSQL.5432" failed: fe_sendauth: no password supplied\n"} ...ignoring
