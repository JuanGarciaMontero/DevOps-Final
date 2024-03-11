DOCKER_IMAGE_NAME = "juangarciamontero/app25"
pipeline {
    agent any
    stages {
        stage(Pre) {
            parallel {
                stage('Test') {
                    agent {
                        docker {
                            image 'python:3.9-slim'
                        }
                    }
                    stages {
                        stage('Instalar Dependencias') {
                            dir('Devops-Final') {
                                sh "pip install -r requirements.txt"
                            }
                        }
                        stage('Linting') {
                            steps{
                                dir('Devops-Final') {
                                    sh "flake8"
                                }
                            }
                        }
                        stage('Coverage') {
                            steps{
                                dir('Devops-Final') {
                                    sh """
                                    pytest --cov=app tests/
                                    """
                                }
                            }
                        }
                    }

                }
                stage('Imagen') {
                    agent: any
                    steps {
                        dir('Devops-Final') {
                            sh "docker build --tag image -f Dokerfile .."
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
            sh """
                docker login -u ${DOCKER_USER} -p ${DOCKER_PASS}
                docker tag image ${DOCKER_IMAGE_NAME}:${VERSION}
                docker push ${DOCKER_IMAGE_NAME}:${VERSION}
            """
        }
    }
    }
}
