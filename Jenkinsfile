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
        stage('Despliegue en AWS Elastic Beanstalk') {
            when {
                anyOf {
                    branch 'QA'; branch 'main';
                }
            }
            environment {
                AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
                AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
                AWS_DEFAULT_REGION = 'us-east-1' // Cambia esto a tu región AWS
                EB_ENVIRONMENT_NAME = 'nombre-del-entorno' // Cambia esto al nombre de tu entorno EB
                VERSION = "1.0.1"
            }
            steps {
                script {
                    withAWS(credentials: 'aws-credentials', region: AWS_DEFAULT_REGION) {
                        sh "aws elasticbeanstalk create-application-version --application-name \${EB_ENVIRONMENT_NAME} --version-label \${VERSION} --source-bundle S3Bucket=elasticbeanstalk-us-east-1-1234567890,S3Key=\${DOCKER_IMAGE_NAME}:\${VERSION}"
                        sh "aws elasticbeanstalk update-environment --application-name \${EB_ENVIRONMENT_NAME} --environment-name \${EB_ENVIRONMENT_NAME} --version-label \${VERSION}"
                    }
                }
            }
        }
    }
}