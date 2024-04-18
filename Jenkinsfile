node {

     stage("Git Clone"){
 
        git branch: 'main', credentialsId: 'GITHUB_LOGIN_CREDENTIALS', url: 'https://github.com/gunavc/Ecommerce-Microservices.git'
    }


    stage("Docker build"){
        sh 'docker build -t gunavc/userapp-python:latest -f User/Dockerfile .'
    }

    

    stage("Push Image to Docker Hub"){
        withCredentials([string(credentialsId: 'DOCKER_HUB_PASSWORD', variable: 'PASSWORD')]) {
        sh 'docker login -u gunavc -p $PASSWORD'
    }
        sh 'docker push  gunavc/userapp-python:latest'
    }

    stage("Deploy to Kubernetes"){
        sh 'kubectl delete -f User/userapp.yaml'
        sh 'kubectl delete -f User/userapp-svc.yaml'
        sh 'kubectl delete -f User/productapp.yaml'
        sh 'kubectl delete -f User/productapp-svc.yaml'
        sh 'kubectl delete -f User/orderapp.yaml'
        sh 'kubectl delete -f User/orderapp-svc.yaml'
        sh 'kubectl create -f User/userapp.yaml'
        sh 'kubectl create -f User/userapp-svc.yaml'
        sh 'kubectl create -f User/productapp.yaml'
        sh 'kubectl create -f User/productapp-svc.yaml'
        sh 'kubectl create -f User/orderapp.yaml'
        sh 'kubectl create -f User/orderapp-svc.yaml'
        // sh 'kubectl rollout restart deployment/userapp'
    }

}