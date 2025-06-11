pipeline {
    agent any

    environment {
        VENV = 'venv'
        DJANGO_SETTINGS_MODULE = 'healthmonitor.settings'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/ManasaCheeku/health-monitoring-django'
            }
        }

        stage('Trust Git Directory') {
            steps {
                bat 'git config --global --add safe.directory "%cd%"'
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                bat '''
                    python -m venv %VENV%
                    call %VENV%\\Scripts\\activate
                    %VENV%\\Scripts\\python.exe -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Migrations') {
            steps {
                bat '''
                    call %VENV%\\Scripts\\activate
                    python manage.py makemigrations
                    python manage.py migrate
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call %VENV%\\Scripts\\activate
                    python manage.py test
                '''
            }
        }

        stage('Collect Static Files') {
            steps {
                bat '''
                    call %VENV%\\Scripts\\activate
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
