DOCKER_IMAGE_NAME = "juangarciamontero/app25"
pipeline {
    agent any

    stages {
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
                                        sh ". env/bin/activate && pip install -r requirements.txt && pytest --cov=app tests/"
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
            environment {
                DOCKER_REGISTRY = 'https://index.docker.io/v1/'
                DOCKER_IMAGE_NAME = "juangarciamontero/app25"
                VERSION = "1.0.1"
            }
            steps {
            script {
                    docker.withRegistry(DOCKER_REGISTRY, 'dockerhub-credentials') {
                        sh """
                        docker tag image ${DOCKER_IMAGE_NAME}:${VERSION}
                        docker push ${DOCKER_IMAGE_NAME}:${VERSION}
                        """
                    }
                }
            }
        }
    }
}