pipeline {
    agent any

    stages {
        stage('Smoke Test') {
            steps {
                sh 'docker --version'
                sh 'docker ps'
            }
        }
    }
}