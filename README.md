# ML_project101

SVM web API...

## Docker

### Development

- Use GitBash to run these commands below 

```
cd docker
docker build -t hoanglt705/mlproject01:0.1 .
docker run -d -p 5000:5000 hoanglt705/mlproject01:0.1
cd ..
curl -X POST localhost:5000/predict -H "Content-Type: application/json" -d @X_test.json
```

### Usage

- Download the docker image from Docker Hub

```
docker pull hoanglt705/mlproject01:0.1
docker run -d -p 5000:5000 hoanglt705/mlproject01:0.1
curl -X POST localhost:5000/predict  -H "Content-Type: application/json" -d @X_test.json
```
