# Istio Python + MySQL Example

## Steps

1. Enable Istio sidecar injection:
```
kubectl label ns default istio-injection=enabled --overwrite
```

2. Deploy MySQL:
```
kubectl apply -f mysql/mysql-pvc.yaml
kubectl apply -f mysql/mysql-deployment.yaml
kubectl apply -f mysql/mysql-service.yaml
```

3. Build and Push Docker image:
```
cd app
docker build -t cubensquare/python-mysql-app:latest .
docker push cubensquare/python-mysql-app:latest
```

4. Deploy Python App:
```
kubectl apply -f app/python-deployment.yaml
```

5. Deploy Istio resources:
```
kubectl apply -f istio/gateway.yaml
kubectl apply -f istio/virtualservice.yaml
kubectl apply -f istio/destinationrule.yaml
kubectl apply -f istio/peerauthentication.yaml
kubectl apply -f istio/authorizationpolicy.yaml
```

6. Access App:
```
kubectl get svc istio-ingressgateway -n istio-system
curl http://<EXTERNAL-IP>
```
