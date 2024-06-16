### Week 4 Homework

This week we learn about creating a prediction service, which can take many dimensions, __Batch__, __Stream__, ..

For the homework we deal with creating a local solution.

#### Q1
We simply modify the code in a previous notebook to fetch the standard deviation of the predicted duration of March  2023 data

#### Q2 - Q3
Covered in the starter.ipynb notebook

#### Q4 Pipenv 
Here, you have to 
`pip install pipenv`
`pipenv --python 3.x` (put the appropriate python version in)
`pipenv install <package>==<package.version`
to then install the neccessary packages like _os_, _sklearn_, etc

Once this is done, indeed your __Pipfile__ and __Pipfile.lock__ files appear.

#### Q5: Parametrize the script
Parametrize here means that we use/set system variable that can accept values that it can now run from the terminal.

See how this is done in the `script.py` script, particularly this is set for __taxi-type__, __year__ and __month__ like so:
```
taxi_type = sys.argv[1] #yellow
year = int(sys.argv[2]) #2024
month = int(sys.argv[3]) #3
```
after you have the script, run the following in the terminal:
`python starter.py yellow 2023 4` - a print statement would handle the mean predicted duration for April 2023.

You should have:
```
(MLOps_24) C:\Users\buasc\OneDrive\Desktop\MLOps_24\wk4\notebooks>python starter.py yellow 2023 4
reading the data from https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-04.parquet...
loading the model with RUN_ID=../models/model.bin...
applying the model...
Q5. Mean of predictions: 14.292
saving the result to ../output_files/yellow/2023-04.parquet...

```

#### Q6: Docker container
Here, we breathe a sign of relief, last question.
[ChatGPT]
A Docker container is a lightweight, standalone, and executable package of software that includes everything needed to run an application. It packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another.

In the same directory as you have been working all along;
We simply create a `Dockerfile`, launch our Docker Engine - locally and create a `requirements.txt` that has a list and versions of your packages. 

Update the Dockerfile like you would see in this repo.

Run:
To build your docker image, replace "<name>" to any name of your choice, here "my-model" is used.
` docker build -t <name> .`
`docker run my-model`
```
$ docker run my-model
reading the data from https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-05.parquet...
loading the model with RUN_ID=model.bin...
applying the model...
Q6. Mean of predictions: 0.192
saving the result to ../output_files/yellow/2023-05.parquet...
```
That's it!

Let me know if you have any challenges.

**NB** Difference between __starter.py__ and __script.py__ is the latter is built to have the pre-built model from the **FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim** docker image.