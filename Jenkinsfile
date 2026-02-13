pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t sentiment-api .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop sentiment-api || true'
                sh 'docker rm sentiment-api || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 8000:8000 --name sentiment-api sentiment-api'
            }
        }
    }
}
