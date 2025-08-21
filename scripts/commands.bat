REM Build Docker image
docker build -t hostile-tweets-ex .

REM Run locally with Mongo connection
docker run -it --rm -p 8000:8000 -e MONGO_URI="mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/" hostile-tweets-ex

REM Tag for Docker Hub
docker tag hostile-tweets-ex your_dockerhub_user/hostile-tweets-ex:latest

REM Push to Docker Hub
docker push your_dockerhub_user/hostile-tweets-ex:latest

REM Clean previous project
oc delete all --selector app=hostile-tweets-ex

REM Apply secrets and configmap
oc apply -f infra/secrets.yaml
oc apply -f infra/configmap.yaml

REM Deploy app
oc apply -f infra/deployment.yaml
oc apply -f infra/service.yaml
oc apply -f infra/route.yaml

REM Get route URL
oc get route hostile-tweets-ex-route -o jsonpath='{.spec.host}'
