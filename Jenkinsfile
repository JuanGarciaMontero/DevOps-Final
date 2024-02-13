pipeline {
    agent any

    environment {
        POSTGRES_DB = 'ejer_final'
        POSTGRES_USER = 'juan'
        POSTGRES_PASSWORD = 'juan'
    }

    stages {
        stage('Iniciar contenedor de PostgreSQL') {
            steps {
                script {
                    // Crear y ejecutar el contenedor de PostgreSQL
                    def postgresContainerId = sh(script: "docker run -d -p 5432:5432 -e POSTGRES_DB=${POSTGRES_DB} -e POSTGRES_USER=${POSTGRES_USER} -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} postgres:latest", returnStdout: true).trim()

                    // Esperar a que PostgreSQL esté listo (ajusta según tus necesidades)
                    sh 'sleep 10'

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
                    def appContainerId = sh(script: "docker run -d -p 5000:5000 juangarciamontero/app13:1.0.15", returnStdout: true).trim()
                    
                    // Lista de comandos a ejecutar dentro del contenedor de la aplicación
                    def commands = [
                        "python --version",
                        "curl -X POST -H \"Content-Type: application/json\" -d '{\"name\": \"Juan\"}' http://localhost:5000/data"
                        "curl -X POST -H \"Content-Type: application/json\" -d '{\"name\": \"Pedro\"}' http://localhost:5000/data"
                        "curl -X POST -H \"Content-Type: application/json\" -d '{\"name\": \"Luis Manuel\"}' http://localhost:5000/data"

                        "curl http://localhost:5000/data"

                        "curl -X DELETE http://localhost:5000/data/1"
                        // Agrega más comandos si es necesario
                    ]

                    // Ejecuta cada comando en el contenedor de la aplicación usando 'invoke'
                    commands.each { command ->
                        invoke([command: "docker exec ${appContainerId} ${command}", pty: true])
                        
                        // Hacer una pausa opcional de 5 segundos entre comandos
                        sh 'sleep 5'
                    }

                    // Verificar si el contenedor de la aplicación está en ejecución
                    def isAppContainerRunning = sh(script: "docker inspect -f '{{.State.Running}}' ${appContainerId}", returnStatus: true).toInteger()

                    if (isAppContainerRunning == 1) {
                        error "El contenedor de la aplicación SI está en ejecución."
                    } else {
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
