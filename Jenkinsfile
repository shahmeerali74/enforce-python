pipeline {
    agent any
    environment {
        repoLink = "${env.enforce_repoLink}"
        repoName = "${env.enforce_repoName}"
    }
    stages {
        stage('Checkout') {
            steps {
                script {
                    git branch: 'master',
                        credentialsId: 'github-credential',
                        url: "${repoLink}/${repoName}.git"
                }
            }
        }

       stage('Checkout') {
            steps {
                script {
                    git branch: 'master',
                        credentialsId: 'github-credential',
                        url: "${repoLink}/${repoName}.git"
                }
            }
        }
    }
}
