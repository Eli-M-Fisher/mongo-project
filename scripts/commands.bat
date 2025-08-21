REM i build docker image (local) with unique version tag
set VERSION=v5
docker buildx build --platform linux/amd64 -t hostile-tweets-ex:%VERSION% .

REM now i can run locally for testing
docker run -it --rm -p 8000:8000 ^
  -e MONGO_URI="mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/" ^
  hostile-tweets-ex:%VERSION%

REM tag image for docker hub
docker tag hostile-tweets-ex:%VERSION% elif2/hostile-tweets-ex:%VERSION%

REM than i push to Docker Hub
docker push elif2/hostile-tweets-ex:%VERSION%

REM i did needed from time to time to clean previous deployment in openshift
oc delete all --selector app=hostile-tweets-ex

REM then apply secrets and configmap
oc apply -f infra/secrets.yaml
oc apply -f infra/configmap.yaml

REM deploy the app yaml (deployment, service, route)
oc apply -f infra/deployment.yaml
oc apply -f infra/service.yaml
oc apply -f infra/route.yaml

REM 8. if deeded to udate deployment to use the new image
oc set image deployment/hostile-tweets-ex-deployment hostile-tweets-ex=your_dockerhub_user/hostile-tweets-ex:%VERSION%

REM that i got route URL
oc get route hostile-tweets-ex-route -o jsonpath="{.spec.host}"
echo.