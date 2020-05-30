pipeline {
  agent {
    node {
      label 'Ferinir'
    }

  }
  stages {
    stage('Prepare environment') {
      steps {
        sh 'echo \'Copying .env files\''
        sh 'cp /home/ml/.env.prod.db .'
        sh 'cp /home/ml/.env.prod .'
        sh 'cp /home/ml/docker-compose.prod.yml .'
      }
    }
    stage('Deploy app') {
      steps {
        sh 'docker-compose -f docker-compose.prod.yml up --build -d'
      }
    }
  }
}