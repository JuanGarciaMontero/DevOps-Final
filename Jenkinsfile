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
                                script {
                                    dir('devops-final') {
                                        sh "pip install -r /home/juan/devops-final/requirements.txt"
                                    }
                                 }
                            }
                        }
                        stage('Linting') {
                            steps {
                                dir('devops-final') {
                                    script {
                                        sh "flake8"
                                    }
                                }
                            }
                        }
                        stage('Coverage') {
                            steps {
                                dir('devops-final') {
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
                        dir('devops-final') {
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
