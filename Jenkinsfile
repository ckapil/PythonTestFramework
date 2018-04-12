node ('master'){
	checkout scm
	stage ('Build container'){
		sh 'docker build -t kcdockerhub/automation:PythonImage .'
	}
	stage ('Build in container'){
		def CONTAINER_ID = sh(
			script: "docker run -d --network=host kcdockerhub/automation:PythonImage"
			returnStdout: true
		).trim()
		echo "Container id: $(CONTAINER_ID)"			
	}
}