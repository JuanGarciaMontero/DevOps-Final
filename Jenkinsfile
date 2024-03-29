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
        stages {
            stage('Despliegue en AWS Elastic Beanstalk') {
                when {
                    anyOf {
                        branch 'Ops'; 
                        branch 'main';
                    }
                }
                environment {
                    AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
                    AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
                    AWS_DEFAULT_REGION = 'eu-west-1' // Cambia esto a tu región AWS
                    EB_ENVIRONMENT_NAME = 'App-Flask-Postgresql' // Cambia esto al nombre de tu entorno EB
                    VERSION = "1.0.1"
                    appURL = ''
                    DB_HOST = 'localhost'
                    DB_PORT = '5432'
                    DB_NAME = 'ejer_final'
                    DB_USER = 'postgres'
                    DB_PASSWORD = 'postgres'
                    DB_URL = 'jdbc:postgresql://<DB_HOST>:<DB_PORT>/<DB_NAME>'
                }
                steps {
                    script {
                        withAWS(credentials: 'aws-credentials', region: AWS_DEFAULT_REGION) {
                            // Despliegue en Elastic Beanstalk
                            sh "aws elasticbeanstalk create-application-version --application-name ${EB_ENVIRONMENT_NAME} --version-label ${VERSION} --source-bundle S3Bucket=elasticbeanstalk-eu-west-1-${S3_BUCKET_NAME}/${DOCKER_IMAGE_NAME}-${VERSION}.tar.gz,S3Key=${DOCKER_IMAGE_NAME}:${VERSION}"
                            sh "aws elasticbeanstalk update-environment --application-name ${EB_ENVIRONMENT_NAME} --environment-name ${EB_ENVIRONMENT_NAME} --version-label ${VERSION}"
					
			    // Configuración de la conexión a la base de datos en la aplicación
                            sh "aws elasticbeanstalk create-environment --application-name ${EB_ENVIRONMENT_NAME} --environment-name ${EB_ENVIRONMENT_NAME} --option-settings Namespace=aws:elasticbeanstalk:application:environment,OptionName=DB_HOST,Value=${DB_HOST} --option-settings Namespace=aws:elasticbeanstalk:application:environment,OptionName=DB_PORT,Value=${DB_PORT} --option-settings Namespace=aws:elasticbeanstalk:application:environment,OptionName=DB_NAME,Value=${DB_NAME} --option-settings Namespace=aws:elasticbeanstalk:application:environment,OptionName=DB_USER,Value=${DB_USER} --option-settings Namespace=aws:elasticbeanstalk:application:environment,OptionName=DB_PASSWORD,Value=${DB_PASSWORD}"
                
                            // Obtener la URL de la aplicación
                            def describeEnvironmentOutput = sh(script: "aws elasticbeanstalk describe-environments --environment-names ${EB_ENVIRONMENT_NAME}", returnStdout: true).trim()
                            def environmentJson = readJSON(text: describeEnvironmentOutput)
                            appURL = environmentJson.Environments[0].CNAME

                            echo "La URL de la aplicación es: ${appURL}"

			}
                    }
                }
	    }
}
