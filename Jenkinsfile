pipeline {
    agent any

    stages {

        stage('Iniciar contenedor con Python y app') {
            steps {
                script {
                    // Crear y ejecutar el contenedor con la aplicación Python
                    def appContainerId = sh(script: "docker run -d -it -p 5000:5000 --name app-container python:3.9-slim", returnStdout: true).trim()

                    // Esperar a que la aplicación esté lista (ajustar según tus necesidades)
                    sh 'sleep 10'

                    // Ejecutar comandos dentro del contenedor de la aplicación
                    script {
                        docker.image("${appContainerId}").inside {
                            sh "python --version"
                            sh "pytest ./tests"
                            sh "pytest --cov=app ./tests"
                        }
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
            }
            echo "Fin del pipeline"
        }
    }
}