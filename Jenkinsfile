DOCKER_IMAGE_NAME = "juangarciamontero/app25"
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
        stage('Pre') {
            parallel {
                stage('Test') {
                    agent {
                        docker {
                            image 'python:3.9-slim'
                        }
                    }
                    stages {
                        stage('Instalar Dependencias + Test Covertura') {
                            steps {
                                script {
                                    dir('./') {
                                        sh "python -m venv env"
                                        sh ". env/bin/activate && pip install -r requirements.txt && python run.py && pytest --cov=app tests/"
                                    }
                                 }
                            }
                        }
                    
                    }
                }
                stage('Imagen') {
                    agent any
                    steps {
                        dir('./') {
                            script {
                                sh "docker build --tag image -f Dockerfile .."
                            }
                        }
                    }
                }
            }
        }

        stage('Image') {
            when {
                anyOf {
                    branch 'main'; branch 'QA'
                }
            }
            environment {
                DOCKER = credentials('dockerhub-credentials')
                VERSION = "1.0.1"
            }
            steps {
                script {
                    sh """
                    docker login -u \${DOCKER_USER} -p \${DOCKER_PASS}
                    docker tag image \${DOCKER_IMAGE_NAME}:\${VERSION}
                    docker push \${DOCKER_IMAGE_NAME}:\${VERSION}
                    """
                }
            }
        }
    }
}
