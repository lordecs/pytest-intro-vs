pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/lordecs/pytest-intro-vs.git']]])
            }
        }
        stage('Install Python') {
            steps {
                sh 'sudo apt install python3 -y'
            }
        }
        stage('Build') {
            steps {
                git branch: 'main', url: 'https://github.com/lordecs/pytest-intro-vs.git'
                sh 'python ops.py'
            }
        }
        stage('Test') {
            steps {
                sh '''
                    python -m pytest
                '''
            }
        }
    }
}
