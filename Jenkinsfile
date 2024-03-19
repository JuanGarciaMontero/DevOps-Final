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
            when {
                anyOf {
                    branch 'QA'; branch 'main';
                }
            }
            environment {
                DOCKER = credentials('dockerhub-credentials')
                VERSION = "1.0.1"
                AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
                AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
                AWS_DEFAULT_REGION = 'eu-west-1' // Cambia esto al region donde esté tu bucket de S3
                S3_BUCKET_NAME = 'app_s3'
            }
            steps {
                script {
                    // Loguearse en DockerHub
                    sh "docker login -u \${DOCKER_USER} -p \${DOCKER_PASS}"

                    // Construir y subir la imagen de Docker
                    sh """
                    docker tag image \${DOCKER_IMAGE_NAME}:\${VERSION}
                    docker push \${DOCKER_IMAGE_NAME}:\${VERSION}
                    """

                    // Subir la imagen a AWS S3
                    sh "aws s3 cp \${DOCKER_IMAGE_NAME}:\${VERSION} s3://\${S3_BUCKET_NAME}/\${DOCKER_IMAGE_NAME}-\${VERSION}.tar.gz"
                }
            }
        }

    }
}
