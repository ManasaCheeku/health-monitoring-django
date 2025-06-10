pipeline {
    agent any

    environment {
        VENV = 'venv'
        DJANGO_SETTINGS_MODULE = 'health_monitoring_project.settings'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/ManasaCheeku/health-monitoring-django'
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV
                    source $VENV/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Migrations') {
            steps {
                sh '''
                    source $VENV/bin/activate
                    python manage.py makemigrations
                    python manage.py migrate
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source $VENV/bin/activate
                    python manage.py test
                '''
            }
        }

        stage('Collect Static Files') {
            steps {
                sh '''
                    source $VENV/bin/activate
                    python manage.py collectstatic --noinput
                '''
            }
        }

        stage('Success Notification') {
            steps {
                echo '✅ Build, Test, and Static Collection Completed Successfully'
            }
        }
    }
}
