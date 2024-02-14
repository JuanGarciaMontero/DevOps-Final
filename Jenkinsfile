pipeline {
    agent any

    environment {
        POSTGRES_DB = 'ejer_final'
        POSTGRES_USER = 'postgres'
        POSTGRES_PASSWORD = 'postgres'
    }

    stages {
        stage('Iniciar contenedor de PostgreSQL') {
            steps {
                script {
                    // Crear y ejecutar el contenedor de PostgreSQL
                    def postgresContainerId = sh(script: "docker run -d -p 5432:5432 -e POSTGRES_DB=${POSTGRES_DB} -e POSTGRES_USER=${POSTGRES_USER} -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} postgres:latest", returnStdout: true).trim()

                    // Esperar a que PostgreSQL esté listo (ajustar según tus necesidades)
                    sh 'sleep 20'

                    // Almacenar el ID del contenedor de PostgreSQL para detenerlo más tarde.
                    env.POSTGRES_CONTAINER_ID = postgresContainerId
                }
            }
        }

        stage('Iniciar contenedor con Python y app') {
            steps {
                script {
                    // Utilizar 'script' para ejecutar comandos en un bloque
                    // Dentro del contenedor Docker
                    def appContainerId = sh(script: "docker run -d -p 5000:5000 juangarciamontero/app15:1.0.50", returnStdout: true).trim()

                    sh 'sleep 20'

                    sh "docker logs ${appContainerId}"

                    sh "docker events"

                    // Lista de comandos a ejecutar dentro del contenedor de la aplicación
                    def commands = [
                        "which python",
                        "which manage.sh",
                        "python --version",
                        "sh manage.sh",
                        "python run.py",
                        "sleep 5",
                        "curl -X POST -H \"Content-Type: application/json\" -d '{\"name\": \"Juan\"}' http://127.0.0.1:5000/data",
                        "curl -X POST -H \"Content-Type: application/json\" -d '{\"name\": \"Pedro\"}' http://127.0.0.1:5000/data",
                        "curl -X POST -H \"Content-Type: application/json\" -d '{\"name\": \"Luis Manuel\"}' http://127.0.0.1:5000/data",
                        "curl http://127.0.0.1:5000/data",
                        "curl -X DELETE http://127.0.0.1:5000/data/1"
                        // Agrega más comandos si es necesario
                    ]

                    // Ejecuta cada comando en el contenedor de la aplicación usando 'invoke'
                    commands.each { command ->
                        sh "docker exec ${appContainerId} ${command}"

                        // Hacer una pausa opcional de 5 segundos entre comandos
                        sh 'sleep 5'
                    }

                    // Verificar si el contenedor de la aplicación está en ejecución
                    def isAppContainerRunning = sh(script: "docker inspect -f '{{.State.Running}}' ${appContainerId}", returnStatus: true).toInteger()

                    if (isAppContainerRunning == 0) {
                        error "El contenedor de la aplicación NO está en ejecución."
                    }

                    // Almacenar el ID del contenedor de la aplicación para detenerlo más tarde
                    env.APP_CONTAINER_ID = appContainerId
                }
            }
        }
    }

    post {
        always {
            // Detener y eliminar los contenedores después de la ejecución del pipeline
            script {
                sh "docker stop ${env.APP_CONTAINER_ID}"
                sh "docker rm ${env.APP_CONTAINER_ID}"

                sh "docker stop ${env.POSTGRES_CONTAINER_ID}"
                sh "docker rm ${env.POSTGRES_CONTAINER_ID}"
            }
            echo "Fin del pipeline"
        }
    }
}
