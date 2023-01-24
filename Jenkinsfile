pipeline {
  agent any

  stages {

    stage('Branch to Staging'){ 
      steps{
        // Checkout the 'dev' branch from the Git repository
        bat 'git checkout dev'

        bat 'git pull'
        bat 'git branch -d staging'
        
        // Create a new branch named 'staging' and check it out
        bat 'git checkout -b staging && git push --set-upstream origin staging'
      }
    }

    stage('Build') {
      steps {
        // Install python dependencies
        bat 'pip install -r requirements.txt'
      }
    }

    stage('Test') {
      steps {
        // Flask unit test
        bat 'python -m unittest'
      }
    }

    stage('Run API on Local') {
      steps {
        // Build docker image
        bat 'docker build -t ml-flask-api .'
        // Run in a container
        bat 'docker run -d -p 5000:5000 ml-flask-api'
      }
    }

    stage('P : Merge & Deploy') {
      steps {
        parallel(
          merging: {
            // Checkout the 'main' branch
            bat 'git checkout main'
            // Merge the 'staging' branch into the 'main' branch
            bat 'git merge staging'
            // Push the changes to the 'main' branch on the remote 'origin' repository
            bat 'git push --set-upstream origin main'
          },
          deploying: {
            withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerhub_pwd', usernameVariable: 'dockerhub_login')]) {
              // Login to docker hub
              bat 'docker login -u %dockerhub_login% -p %dockerhub_pwd%'
              // Associate the docker image to the repo on docker hub
              bat 'docker tag ml-flask-api wvaihau/cicd:latest'
              // Push the image to docker hub
              bat 'docker push wvaihau/cicd:latest'
            }
          }
        )
      }
    }

  }

  post {
      always {
        // Delete the 'staging' branch
        bat 'git push origin --delete staging && git branch -d staging'
      }
  }

}
