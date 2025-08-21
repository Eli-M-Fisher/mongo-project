# mongo-project


The system has four main functions:

* **Retrieval** - This class will receive the current connection address to the database instance, extract the existing data in the database and hold it in a format of your choice (dataframe recommended).
* **Processing** - This class will use the information that came from the retrieval object (dataframe recommended).
  Several processing and calculation operations must be performed on the texts.
  If necessary, new data fields must be created with information about the texts (feature extraction, engineering and augmentation)
  Each operation will create a new data field for the given text.
  The required operations:
* *Finding the rarest word in each text*
* *Finding the sentiment of the text* - positive, negative or neutral (a code snippet will be provided for this operation
* *Finding names of weapons* according to a blacklist (given a word file).
  This class will also save the data in a format of your choice (dataframe is recommended)
* **Management** - This class will manage the retrieval and processing operations, it will take care of transferring the information between the various objects, and will also take care of the method that accesses the information to the user.
* **Processed information access service** The entire system must be wrapped in a fastapi server. This service exposes an endpoint for a GET request to receive a Jason with the texts and new data fields that have been generated.


```
hostile-tweets-ex/
├── app/
│   ├── main.py          # FastAPI entrypoint
│   ├── fetcher.py       # Mongo fetch logic
│   ├── processor.py     # Text Processing logic
│   └── manager.py       # Manages fetcher+processor
│
├── data/
│   └── weapons.txt      # list of weapons (blacklist)
│
├── infra/               # OpenShift/K8s manifests (yaml files)
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── route.yaml
│   ├── secrets.yaml
│   └── configmap.yaml
│
├── scripts/
│   └── commands.bat     #
│
├── Dockerfile
├── requirements.txt
└── README.md

```

#### Structure explanation:
app/ - all Python code.

data/ - auxiliary files (weapons, etc.).

infra/ - everything related to cloud deployment / infrastructure (OpenShift / Kubernetes YAMLs), depending on your deployment process.

scripts/ - scripts (commands to run/clean up, etc.).

Dockerfile, requirements.txt, README.md - at the top of the project.
