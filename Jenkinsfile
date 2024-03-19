DOCKER_IMAGE_NAME = "juangarciamontero/app25"
pipeline {
    agent any

    stages {
        stage('Despliegue en AWS Elastic Beanstalk') {
            when {
                anyOf {
                    branch 'Ops'; branch 'main';
                }
            }
            environment {
                AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
                AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
                AWS_DEFAULT_REGION = 'eu-west-1' // Cambia esto a tu región AWS
                EB_ENVIRONMENT_NAME = 'App-Flask-Postgresql' // Cambia esto al nombre de tu entorno EB
                VERSION = "1.0.1"
            }
            steps {
                script {
                    withAWS(credentials: 'aws-credentials', region: AWS_DEFAULT_REGION) {
                        sh "aws elasticbeanstalk create-application-version --application-name \${EB_ENVIRONMENT_NAME} --version-label \${VERSION} --source-bundle S3Bucket=elasticbeanstalk-eu-west-1-1234567890,S3Key=\${DOCKER_IMAGE_NAME}:\${VERSION}"
                        sh "aws elasticbeanstalk update-environment --application-name \${EB_ENVIRONMENT_NAME} --environment-name \${EB_ENVIRONMENT_NAME} --version-label \${VERSION}"
                    }
                }
            }
        }
    }
}