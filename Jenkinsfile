pipeline {
    agent any

    environment {
        POSTGRES_DB = 'ejer_final'
        POSTGRES_USER = 'postgres'
        POSTGRES_PASSWORD = 'postgres'
        POSTGRES_CONTAINER_NAME = 'postgres-container'
        APP_CONTAINER_NAME = 'app-container'
    }

    stages {
        stage('Iniciar contenedor de PostgreSQL') {
            steps {
                script {
                    def postgresCommand = """
                        docker run -d \
                        -p 5432:5432 \
                        -e POSTGRES_DB=${env.POSTGRES_DB} \
                        -e POSTGRES_USER=${env.POSTGRES_USER} \
                        -e POSTGRES_PASSWORD=${env.POSTGRES_PASSWORD} \
                        --name ${env.POSTGRES_CONTAINER_NAME} \
                        postgres:13
                    """

                    def postgresContainerId = sh(script: postgresCommand, returnStdout: true).trim()

                    sh 'sleep 20'

                    env.POSTGRES_CONTAINER_ID = postgresContainerId
                }
            }
        }

        stage('Iniciar contenedor con Python y app') {
            steps {
                script {
                    def appCommand = """
                        docker run -d -it \
                        -p 5000:5000 \
                        --name ${env.APP_CONTAINER_NAME} \
                        juangarciamontero/app15:1.0.75
                    """

                    def appContainerId = sh(script: appCommand, returnStdout: true).trim()
                    
                    sh 'sleep 20'
                    sh "docker logs ${appContainerId}"
                    sh "docker exec ${appContainerId} python --version"

                    // Obtiene la ruta actual dentro del contenedor
                    def currentDir = sh(script: "docker exec ${appContainerId} pwd", returnStdout: true).trim()

                    // Muestra la ruta actual en los logs de Jenkins
                    echo "Ruta actual en el contenedor: ${currentDir}"

                    sh "docker exec ${appContainerId} ls -l /"

                    // Otorga permisos de ejecución al script manage.sh
                    sh "docker exec ${appContainerId} chmod +x /manage.sh"

                    // Muestra el contenido de manage.sh
                    sh "docker exec ${appContainerId} cat /manage.sh"

                    // Ejecuta manage.sh directamente
                    sh "docker exec ${appContainerId} /bin/bash -c 'manage.sh'"         
                    sh "docker exec ${appContainerId} python run.py"
                    sh 'sleep 20'
                    sh "docker exec ${appContainerId} curl -X POST -H \"Content-Type: application/json\" -d '{\"name\": \"Juan\"}' http://127.0.0.1:5000/data"
                    sh "docker exec ${appContainerId} curl -X POST -H \"Content-Type: application/json\" -d '{\"name\": \"Pedro\"}' http://127.0.0.1:5000/data"
                    sh "docker exec ${appContainerId} curl -X POST -H \"Content-Type: application/json\" -d '{\"name\": \"Luis Manuel\"}' http://127.0.0.1:5000/data"
                    sh "docker exec ${appContainerId} curl http://127.0.0.1:5000/data"
                    sh "docker exec ${appContainerId} curl -X DELETE http://127.0.0.1:5000/data/1"

                    def isAppContainerRunning = sh(script: "docker inspect -f '{{.State.Running}}' ${appContainerId}", returnStatus: true).toInteger()

                    if (isAppContainerRunning == 0) {
                        error "El contenedor de la aplicación NO está en ejecución."
                    }

                    env.APP_CONTAINER_ID = appContainerId
                }
            }
        }
    }

    post {
        always {
            script {
                sh "docker stop ${env.APP_CONTAINER_ID}"
                sh "docker rmi ${env.APP_CONTAINER_ID}"

                sh "docker stop ${env.POSTGRES_CONTAINER_ID}"
                sh "docker rmi ${env.POSTGRES_CONTAINER_ID}"
            }
            echo "Fin del pipeline"
        }
    }
}
