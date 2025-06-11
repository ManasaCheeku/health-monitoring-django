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
<<<<<<< HEAD
                dir('health-monitoring-django') {
                    bat 'git config --global --add safe.directory "%cd%"'
                }
=======
                bat 'git config --global --add safe.directory "%cd%"'
>>>>>>> f1804cb (Save local changes before pull)
            }
        }

        stage('Set Up Virtual Environment') {
            steps {
<<<<<<< HEAD
                dir('health-monitoring-django') {
                    bat '''
                        python -m venv %VENV%
                        call %VENV%\\Scripts\\activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
=======
                bat '''
                    python -m venv %VENV%
                    call %VENV%\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r health_monitoring_project\\requirements.txt
                '''
>>>>>>> f1804cb (Save local changes before pull)
            }
        }

        stage('Run Migrations') {
            steps {
<<<<<<< HEAD
                dir('health-monitoring-django') {
                    bat '''
                        call %VENV%\\Scripts\\activate
                        python manage.py makemigrations
                        python manage.py migrate
                    '''
                }
=======
                bat '''
                    call %VENV%\\Scripts\\activate
                    cd health_monitoring_project
                    python manage.py makemigrations
                    python manage.py migrate
                '''
>>>>>>> f1804cb (Save local changes before pull)
            }
        }

        stage('Run Tests') {
            steps {
<<<<<<< HEAD
                dir('health-monitoring-django') {
                    bat '''
                        call %VENV%\\Scripts\\activate
                        python manage.py test
                    '''
                }
=======
                bat '''
                    call %VENV%\\Scripts\\activate
                    cd health_monitoring_project
                    python manage.py test
                '''
>>>>>>> f1804cb (Save local changes before pull)
            }
        }

        stage('Collect Static Files') {
            steps {
<<<<<<< HEAD
                dir('health-monitoring-django') {
                    bat '''
                        call %VENV%\\Scripts\\activate
                        python manage.py collectstatic --noinput
                    '''
                }
=======
                bat '''
                    call %VENV%\\Scripts\\activate
                    cd health_monitoring_project
                    python manage.py collectstatic --noinput
                '''
>>>>>>> f1804cb (Save local changes before pull)
            }
        }

        stage('Success Notification') {
            steps {
                echo '✅ Build, Test, and Static Collection Completed Successfully'
            }
        }
    }
}
