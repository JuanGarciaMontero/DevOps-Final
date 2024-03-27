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
                    appURL = ''
                }
                steps {
                    script {
                        withAWS(credentials: 'aws-credentials', region: AWS_DEFAULT_REGION) {
                            sh "aws elasticbeanstalk create-application-version --application-name \${EB_ENVIRONMENT_NAME} --version-label \${VERSION} --source-bundle S3Bucket=elasticbeanstalk-eu-west-1-\${S3_BUCKET_NAME}/\${DOCKER_IMAGE_NAME}-\${VERSION}.tar.gz,S3Key=\${DOCKER_IMAGE_NAME}:\${VERSION}"
                            sh "aws elasticbeanstalk update-environment --application-name \${EB_ENVIRONMENT_NAME} --environment-name \${EB_ENVIRONMENT_NAME} --version-label \${VERSION}"
                        
                            // Obtener la URL de la aplicación
                            def describeEnvironmentOutput = sh(script: "aws elasticbeanstalk describe-environments --environment-names \${EB_ENVIRONMENT_NAME}", returnStdout: true).trim()
                            def environmentJson = readJSON(text: describeEnvironmentOutput)
                            appURL = environmentJson.Environments[0].CNAME

                            echo "La URL de la aplicación es: \${appURL}"
                        }
                    }
            }
            
        }
    }
}
