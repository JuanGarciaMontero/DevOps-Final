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
                        juangarciamontero/app15:1.0.82
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

                    // Ejecuta manage.sh directamente
                    sh "docker exec ${appContainerId} pytest --cov=app ./tests"
                    sh "docker exec ${appContainerId} python run.py"

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