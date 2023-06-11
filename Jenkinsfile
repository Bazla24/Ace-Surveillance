pipeline {
    agent any

    environment {
        PATH = "${PATH}:${HOME}/.local/bin"
    }

    stages {
        stage('Cloning Apache Airflow repo') {
            steps {
                git branch: 'main', url: 'https://github.com/Bazla24/Ace-Surveillance.git'
                bat 'echo "Apache Airflow Version:"'
                bat 'airflow version'
            }
        }

        stage('Cloning DVC repo') {
            steps {
                dir('examples/intro-example/dags') {
                    git branch: 'main', url: 'https://github.com/Bazla24/Ace-Surveillance.git'
                    bat 'echo "DVC Version:"'
                    bat 'dvc --version'
                }
            }
        }

        stage('Cloning mlFlow repo') {
            steps {
                dir('examples/intro-example/dags/models') {
                    git branch: 'main', url: 'https://github.com/Bazla24/Ace-Surveillance.git'
                    bat 'echo "mlFlow Version:"'
                    bat 'mlflow --version'
                }
            }
        }

        stage('Running Airflow') {
            steps {
                bat 'echo "Running Airflow..."'
                bat 'docker-compose up -d'
            }
        }
    }
}
