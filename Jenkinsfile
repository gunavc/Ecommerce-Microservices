node {

     stage("Git Clone"){
 
        git branch: 'main', credentialsId: 'GITHUB_LOGIN_CREDENTIALS', url: 'https://github.com/gunavc/Ecommerce-Microservices.git'
    }


    stage("Docker build"){
        sh 'docker build -t gunavc/userapp-python:latest -f User/Dockerfile .'
        // sh 'docker tag jhooq-docker-demo subhasmita17/jhooq-docker-demo:jhooq-docker-demo'
    }

    

    stage("Push Image to Docker Hub"){
        withCredentials([string(credentialsId: 'DOCKER_HUB_PASSWORD', variable: 'PASSWORD')]) {
        sh 'docker login -u gunavc -p $PASSWORD'
    }
        sh 'docker push  gunavc/userapp-python:latest'
    }

    // stage("SSH Into k8s Server") {
    //     def remote = [:]
    //     remote.name = 'K8S master'
    //     remote.host = '100.0.0.2'
    //     remote.user = 'vagrant'
    //     remote.password = 'vagrant'
    //     remote.allowAnyHosts = true

    //     stage('Put k8s-spring-boot-deployment.yml onto k8smaster') {
    //         sshPut remote: remote, from: 'k8s-spring-boot-deployment.yml', into: '.'
    //     }

    //     stage('Deploy spring boot') {
    //       sshCommand remote: remote, command: "kubectl apply -f k8s-spring-boot-deployment.yml"
    //     }
    // }

}