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

        stage('Trust Git Directory') {
            steps {
                dir('health-monitoring-django') {
                    bat 'git config --global --add safe.directory "%cd%"'
                }
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
                dir('health-monitoring-django') {
                    bat '''
                        python -m venv %VENV%
                        call %VENV%\\Scripts\\activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Migrations') {
            steps {
                dir('health-monitoring-django') {
                    bat '''
                        call %VENV%\\Scripts\\activate
                        python manage.py makemigrations
                        python manage.py migrate
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir('health-monitoring-django') {
                    bat '''
                        call %VENV%\\Scripts\\activate
                        python manage.py test
                    '''
                }
            }
        }

        stage('Collect Static Files') {
            steps {
                dir('health-monitoring-django') {
                    bat '''
                        call %VENV%\\Scripts\\activate
                        python manage.py collectstatic --noinput
                    '''
                }
            }
        }

        stage('Success Notification') {
            steps {
                echo '✅ Build, Test, and Static Collection Completed Successfully'
            }
        }
    }
}
