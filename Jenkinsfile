pipeline {
    agent any

    environment {
        DOCKERHUB = "2023bcs0220gsrishtiksekar"
        FRONTEND_IMAGE = "${DOCKERHUB}/2023bcs0220_frontend"
        BACKEND_IMAGE = "${DOCKERHUB}/2023bcs0220_backend"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/SrishtikSekar/FullStack-Devops.git'
            }
        }

        stage('Build Backend') {
            steps {
                sh 'docker build -t $BACKEND_IMAGE ./backend'
            }
        }

        stage('Build Frontend') {
            steps {
                sh 'docker build -t $FRONTEND_IMAGE ./frontend'
            }
        }

        stage('Login DockerHub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'USER',
                    passwordVariable: 'PASS')]) {

                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                }
            }
        }

        stage('Push Images') {
            steps {
                sh 'docker push $BACKEND_IMAGE'
                sh 'docker push $FRONTEND_IMAGE'
            }
        }
    }
}