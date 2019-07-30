# ML_project101

SVM web API...

## Docker

### Development

- Use GitBash to run these commands below 

```
cd docker
docker build -t flask-tutorial:latest .
docker run -d -p 5000:5000 flask-tutorial
cd ..
curl -X POST localhost:5000/predict -H "Content-Type: application/json" -d @X_test.json
```

Console

```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 32047  100  2023  100 30024  21521   311k --:--:-- --:--:-- --:--:--  332k{
  "prediction": "['Failed', 'Failed', 'Failed', 'Failed', 'Failed', 'Failed', 'F                                                                                                                ailed', 'Failed', 'Failed', 'Failed', 'Failed', 'Passed', 'Passed', 'Failed', 'P                                                                                                                assed', 'Passed', 'Passed', 'Passed', 'Passed', 'Failed', 'Passed', 'Passed', 'F                                                                                                                ailed', 'Failed', 'Failed', 'Failed', 'Failed', 'Failed', 'Failed', 'Passed', 'F                                                                                                                ailed', 'Failed', 'Failed', 'Failed', 'Failed', 'Passed', 'Passed', 'Failed', 'F                                                                                                                ailed', 'Failed', 'Passed', 'Failed', 'Passed', 'Passed', 'Failed', 'Failed', 'F                                                                                                                ailed', 'Failed', 'Failed', 'Passed', 'Passed', 'Failed', 'Passed', 'Passed', 'P                                                                                                                assed', 'Failed', 'Passed', 'Passed', 'Failed', 'Passed', 'Failed', 'Failed', 'F                                                                                                                ailed', 'Failed', 'Failed', 'Passed', 'Passed', 'Passed', 'Failed', 'Failed', 'P                                                                                                                assed', 'Failed', 'Passed', 'Failed', 'Failed', 'Failed', 'Passed', 'Failed', 'F                                                                                                                ailed', 'Failed', 'Passed', 'Failed', 'Failed', 'Passed', 'Passed', 'Failed', 'F                                                                                                                ailed', 'Failed', 'Failed', 'Failed', 'Failed', 'Passed', 'Passed', 'Failed', 'P                                                                                                                assed', 'Failed', 'Failed', 'Failed', 'Failed', 'Failed', 'Failed', 'Passed', 'F                                                                                                                ailed', 'Failed', 'Failed', 'Failed', 'Failed', 'Passed', 'Failed', 'Failed', 'F                                                                                                                ailed', 'Passed', 'Failed', 'Failed', 'Passed', 'Passed', 'Passed', 'Failed', 'P                                                                                                                assed', 'Failed', 'Passed', 'Failed', 'Failed', 'Passed', 'Failed', 'Failed', 'F                                                                                                                ailed', 'Failed', 'Passed', 'Passed', 'Failed', 'Failed', 'Failed', 'Passed', 'F                                                                                                                ailed', 'Failed', 'Failed', 'Passed', 'Failed', 'Failed', 'Failed', 'Passed', 'P                                                                                                                assed', 'Passed', 'Failed', 'Passed', 'Failed', 'Passed', 'Failed', 'Failed', 'F                                                                                                                ailed', 'Passed', 'Failed', 'Passed', 'Passed', 'Passed', 'Failed', 'Failed', 'F                                                                                                                ailed', 'Failed', 'Failed', 'Passed', 'Failed', 'Failed', 'Failed', 'Passed', 'F                                                                                                                ailed', 'Failed', 'Failed', 'Failed', 'Failed', 'Failed', 'Failed', 'Failed', 'F                                                                                                                ailed', 'Failed', 'Failed', 'Passed', 'Failed', 'Failed', 'Passed', 'Failed', 'P                                                                                                                assed', 'Failed', 'Failed', 'Passed', 'Passed', 'Failed', 'Failed', 'Passed', 'F                                                                                                                ailed', 'Passed', 'Failed', 'Passed', 'Failed', 'Failed', 'Failed', 'Failed', 'P                                                                                                                assed', 'Passed']"
}

```
