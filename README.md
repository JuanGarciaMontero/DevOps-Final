# DevOps-Final
## Proyecto Final DevOps Beca Qualentum

En cuanto a la estructura del documento, este deberá estar compuesto de tres grandes secciones: 

• Una descripción de la arquitectura del sistema.
    Nos interesa definir qué servicios, métodos y tecnologías se necesitan para poder ofrecer una solución productiva moderna y competente. 
      • Balanceadores de carga. Docker y Kubernetes 
	  • Terminadores SSL. Clave pública y clave privada. Certificados 503, HTTPS
	  • Bases de datos. Mysql
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
	 
# Bloques de desarrollo:

1- Creación de un entorno local de desarrollo.
    Clonar a un repositorio git la aplicación ejemplo.
	Realizar test unitarios a nuevas características incorporadas en nuestra aplicación
	Documentación de: arquitectura de software, como se ejecutan los test, como se ejecutan localmente el entorno de prueas y el modelo de ramas GIT.
	Test de cobertura de al menos el 80% de las líneas de código
2- Creación de pipelen de CI. Jenkins.
    Clonado de código fuente
    Ejecución de test
	Proceso de linting
	Creación imagen Docker para ejecutar software en un contenedor
	Subida el resultadoa algún Registro (privado,EC2, Docker Hub, ...) siempre que sea la rama des o main.
	Documentar que hace Jenkins y Git, y en cada push se realice un job en Jenkins.
3- Infraestructura como código
    El código generado debe estar en un repositorio de Git, que puede ser el mismo que el de la aplicación o no (está decisión debe ser justificada).
	Se debe acompañar al código de IaC de instrucciones precisas sobre cómo conseguimos ejecutar la creación/actualización de la infraestructura, incluyendo si es necesario qué valores o variables de entorno debemos tener en cuenta.
	Tampoco debemos olvidar que puede haber más de un entorno de despliegue y que nos podría interesar regenerar la misma infraestructura, con un diferente set de recursos, en otro VPC.
4- Despliegue
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
    - git checkout -b Dev
      git add Dev/
      git commit -m "Agrego archivos Dev"
      git push --set-upstream origin Dev
    - git checkout -b Ops
      git add Ops/
      git commit -m "Agrego archivos Ops"
      git push --set-upstream origin Ops
    - git checkout -b QA
      git add QA/
      git commit -m "Agrego archivos QA"
      git push --set-upstream origin QA

## Pruebas en local de la App

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
