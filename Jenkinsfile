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
                        stage('Install Dependencies + Test Coverage') {
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
                stage('Build Image') {
                    agent any
                    steps {
                        dir('./') {
                            script {
                                sh "docker build --tag juangarciamontero/app25:latest -f Dockerfile .."
                            }
                        }
                    }
                }
            }
        }
        stage('Push Image') {
            environment {
                DOCKER_CREDS = credentials('dockerhub-credentials')
                DOCKER_REGISTRY = 'https://index.docker.io/v1/'
                DOCKER_IMAGE_NAME = "juangarciamontero/app25"
                VERSION = "1.0.1"
            }
            steps {
                script {
                    docker.withRegistry(DOCKER_REGISTRY, DOCKER_CREDS) {
                        sh """
                        docker tag juangarciamontero/app25:latest ${DOCKER_IMAGE_NAME}:${VERSION}
                        docker push ${DOCKER_IMAGE_NAME}:${VERSION}
                        """
                    }
                }
            }
        }
    }
}
