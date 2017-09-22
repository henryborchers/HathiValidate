@Library("ds-utils")
// Uses https://github.com/UIUCLibrary/Jenkins_utils
import org.ds.*

pipeline {
    agent any
    environment {
        mypy_args = "--junit-xml=mypy.xml"
        pytest_args = "--junitxml=reports/junit-{env:OS:UNKNOWN_OS}-{envname}.xml --junit-prefix={env:OS:UNKNOWN_OS}  --basetemp={envtmpdir}"
    }
    parameters {
        string(name: "PROJECT_NAME", defaultValue: "Hathi Validate", description: "Name given to the project")
        booleanParam(name: "UNIT_TESTS", defaultValue: true, description: "Run Automated Unit Tests")
        booleanParam(name: "ADDITIONAL_TESTS", defaultValue: true, description: "Run additional tests")
        booleanParam(name: "PACKAGE", defaultValue: true, description: "Create a Packages")
        booleanParam(name: "DEPLOY_SCCM", defaultValue: false, description: "Deploy SCCM")
        booleanParam(name: "DEPLOY_DEVPI", defaultValue: false, description: "Deploy to devpi on http://devpy.library.illinois.edu/hborcher/${env.BRANCH_NAME}")
        booleanParam(name: "UPDATE_DOCS", defaultValue: false, description: "Update the documentation")
        string(name: 'URL_SUBFOLDER', defaultValue: "hathi_validate", description: 'The directory that the docs should be saved under')
    }
    stages {
        stage("Cloning Source") {
            agent any

            steps {
                deleteDir()
                checkout scm
                stash includes: '**', name: "Source", useDefaultExcludes: false
                stash includes: 'deployment.yml', name: "Deployment"

            }

        }

        stage("Unit tests") {
            when {
                expression { params.UNIT_TESTS == true }
            }
            steps {
                parallel(
                        "Windows": {
                            script {
                                def runner = new Tox(this)
                                runner.env = "pytest"
                                runner.windows = true
                                runner.stash = "Source"
                                runner.label = "Windows"
                                runner.post = {
                                    junit 'reports/junit-*.xml'
                                }
                                runner.run()
                            }
                        },
                        "Linux": {
                            script {
                                def runner = new Tox(this)
                                runner.env = "pytest"
                                runner.windows = false
                                runner.stash = "Source"
                                runner.label = "!Windows"
                                runner.post = {
                                    junit 'reports/junit-*.xml'
                                }
                                runner.run()
                            }
                        }
                )
            }
        }
        stage("Additional tests") {
            when {
                expression { params.ADDITIONAL_TESTS == true }
            }

            steps {
                parallel(
                        "Documentation": {
                            script {
                                def runner = new Tox(this)
                                runner.env = "docs"
                                runner.windows = false
                                runner.stash = "Source"
                                runner.label = "!Windows"
                                runner.post = {
                                    dir('.tox/dist/html/') {
                                        stash includes: '**', name: "HTML Documentation", useDefaultExcludes: false
                                    }
                                }
                                runner.run()

                            }
                        },
                        "MyPy": {
                            script {
                                def runner = new Tox(this)
                                runner.env = "mypy"
                                runner.windows = false
                                runner.stash = "Source"
                                runner.label = "!Windows"
                                runner.post = {
                                    junit 'mypy.xml'
                                }
                                runner.run()

                            }
                        }
                )
            }

        }
        stage("Packaging") {
            when {
                expression { params.PACKAGE == true }
            }
            steps {
                parallel(
                        "Windows Wheel": {
                            node(label: "Windows") {
                                deleteDir()
                                unstash "Source"
                                bat "${env.PYTHON3} setup.py bdist_wheel --universal"
                                archiveArtifacts artifacts: "dist/**", fingerprint: true
                            }
                        },
                        "Windows CX_Freeze MSI": {
                            node(label: "Windows") {
                                deleteDir()
                                unstash "Source"
                                bat """ ${env.PYTHON3} -m venv .env
                          call .env/Scripts/activate.bat
                          pip install -r requirements.txt
                          python cx_setup.py bdist_msi --add-to-path=true
                          """

                                dir("dist") {
                                    stash includes: "*.msi", name: "msi"
                                }

                            }
                            node(label: "Windows") {
                                deleteDir()
                                git url: 'https://github.com/UIUCLibrary/ValidateMSI.git'
                                unstash "msi"

                                bat """
                          ${env.PYTHON3} -m venv .env
                          call .env/Scripts/activate.bat
                          pip install --upgrade pip
                          pip install setuptools --upgrade
                          pip install -r requirements.txt
                          python setup.py install
    
                          echo Validating msi file(s)
                          FOR /f "delims=" %%A IN ('dir /b /s *.msi') DO (
                            python validate_msi.py ^"%%A^" frozen.yml
                            if not %errorlevel%==0 (
                              echo errorlevel=%errorlevel%
                              exit /b %errorlevel%
                              )
                            )
                          """
                                archiveArtifacts artifacts: "*.msi", fingerprint: true
                            }
                        },
                        "Source Release": {
                            createSourceRelease(env.PYTHON3, "Source")
                        }
                )
            }
        }
        stage("Deploying to Devpi") {
            agent {
                node {
                    label 'Windows'
                }
            }
            when {
                expression { params.DEPLOY_DEVPI == true }
            }
            steps {
                echo "I'm logging into Devpi"
                withCredentials([usernamePassword(credentialsId: 'DS_devpi', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    bat "whoami"
                    bat "devpi login %USERNAME% --password=%PASSWORD%"
                }

            }
        }
        stage("master branch stuff") {
            agent any
            when {
                branch 'master'
            }
            steps {
                echo "I'm running under the master branch"
            }
        }
        stage("Dev branch stuff") {
            agent any
            when {
                branch 'dev'
            }
            steps {
                echo "I'm running the ${env.BRANCH_NAME}"
            }
        }

        stage("Deploy - Staging") {
            agent any
            when {
                expression { params.DEPLOY_SCCM == true && params.PACKAGE == true }
            }
            steps {
                deployStash("msi", "${env.SCCM_STAGING_FOLDER}/${params.PROJECT_NAME}/")
                input("Deploy to production?")
            }
        }

        stage("Deploy - SCCM upload") {
            agent any
            when {
                expression { params.DEPLOY_SCCM == true && params.PACKAGE == true }
            }
            steps {
                deployStash("msi", "${env.SCCM_UPLOAD_FOLDER}")
            }
            post {
                success {
                    script {
                        unstash "Source"
                        def deployment_request = requestDeploy this, "deployment.yml"
                        echo deployment_request
                        writeFile file: "deployment_request.txt", text: deployment_request
                        archiveArtifacts artifacts: "deployment_request.txt"
                    }
                }
            }
        }
        stage("Update online documentation") {
            agent any
            when {
                expression { params.UPDATE_DOCS == true }
            }

            steps {
                updateOnlineDocs url_subdomain: params.URL_SUBFOLDER, stash_name: "HTML Documentation"
            }
        }
    }
}
