pipeline {
    agent any

    stages {
        stage('Build and Push to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhubCred', passwordVariable: 'DOCKERHUB_PASSWORD', usernameVariable: 'DOCKERHUB_USERNAME')]) {
                    script {
                        // Authenticate with Docker Hub using withCredentials
                        sh "docker login --username \${DOCKERHUB_USERNAME} --password \${DOCKERHUB_PASSWORD}"

                        // Build and push the Docker image
                        sh "docker build -t moelzedy/cicddemo ."
                        sh "docker push moelzedy/cicddemo"
                    }
                }
            }
        }

        stage('Deploy to EKS') {
            steps {
                script {
                    // Deploy your application using kubectl or any other deployment tool you prefer
                    sh "kubectl apply -f deployment.yaml"
                }
            }
        }
    }
}
