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
                    def postgresContainerId = sh(script: "docker run -d -p 5432:5432 -e POSTGRES_DB=${POSTGRES_DB} -e POSTGRES_USER=${POSTGRES_USER} -e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} --name postgres-container postgres:latest", returnStdout: true).trim()

                    // Esperar a que PostgreSQL esté listo (ajustar según tus necesidades)
                    sh 'sleep 20'

                    // Almacenar el ID del contenedor de PostgreSQL para detenerlo más tarde
                    env.POSTGRES_CONTAINER_ID = postgresContainerId
                }
            }
        }

        stage('Iniciar contenedor con Python y app') {
            steps {
                script {
                    // Crear y ejecutar el contenedor con la aplicación Python
                    def appContainerId = sh(script: "docker run -d -p 5000:5000 --name app-container --link postgres-container juangarciamontero/app15:1.0.1", returnStdout: true).trim()

                    // Esperar a que la aplicación esté lista (ajustar según tus necesidades)
                    sh 'sleep 10'

                    // Ejecutar comandos dentro del contenedor de la aplicación
                    script {
                        docker.image("${appContainerId}").inside {
                            sh "python --version"
                            sh "manage.sh"
                            sh "python run.py"
                            sh "sleep 5"
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
                sh "docker rmi ${env.APP_CONTAINER_ID}"

                sh "docker stop ${env.POSTGRES_CONTAINER_ID}"
                sh "docker rmi ${env.POSTGRES_CONTAINER_ID}"
            }
            echo "Fin del pipeline"
        }
    }
}
