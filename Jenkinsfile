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
                        stage('Instalar Dependencias') {
                            steps {
                                dir('DEVOPS-FINAL') {
                                    script {
                                        // Ajustar los permisos del directorio de caché de pip en un entorno virtual
                                        sh "chmod -R 777 venv/lib/python*/site-packages/pip/_vendor/requests/cacert.pem"
                                        sh "chown -R $USER venv/lib/python*/site-packages/pip/_vendor/requests/cacert.pem"


                                        // Instalar dependencias
                                        sh "pip install -r requirements.txt"
                                    }
                                }
                            }
                        }
                        stage('Linting') {
                            steps {
                                dir('DEVOPS-FINAL') {
                                    script {
                                        sh "flake8"
                                    }
                                }
                            }
                        }
                        stage('Coverage') {
                            steps {
                                dir('DEVOPS-FINAL') {
                                    script {
                                        sh """
                                        pytest --cov=app tests/
                                        """
                                    }
                                }
                            }
                        }
                    }
                }
                stage('Imagen') {
                    agent any
                    steps {
                        dir('DEVOPS-FINAL') {
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
                    branch 'main'; branch 'Dev'
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
