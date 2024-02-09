def call () {
    sh 'python --version'
    sh 'pytest tests/'
    sh 'pytest --cov=app tests/'
}