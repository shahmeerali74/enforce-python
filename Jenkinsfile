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
                    // Print variables to verify they are correctly set
                    echo "Repository Link: ${repoLink}"
                    echo "Repository Name: ${repoName}"

                    // Correct syntax for the git step
                    git branch: 'master',
                        credentialsId: 'github-credential',
                        url: "${repoLink}/${repoName}.git"
                }
            }
        }
        
       stage('Checkout') {
            steps {
                script {
                    // Print variables to verify they are correctly set
                    echo "Repository Link: ${repoLink}"
                    echo "Repository Name: ${repoName}"

                    // Correct syntax for the git step
                    git branch: 'master',
                        credentialsId: 'github-credential',
                        url: "${repoLink}/${repoName}.git"
                }
            }
        }
    }
}
