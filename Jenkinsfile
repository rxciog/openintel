pipeline {
    agent any

    environment {
        COMPOSE_FILE = 'docker-compose.yml'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Images') {
            steps {
                sh 'docker-compose up --build'
            }
        }

        stage('Backend Tests') {
            steps {
                sh 'docker compose run --rm backend pytest'
            }
        }

        stage('Integration Tests') {
            steps {
                sh '''
                    docker compose up -d
                    sleep 5
                    docker compose exec backend pytest tests/integration
                '''
            }
        }
    }

    post {
        always {
            sh 'dcoker-compose down -v'
        }
        failure {
            echo 'CI failed'
        }
        success {
            echo 'CI passed'
        }
    }

}