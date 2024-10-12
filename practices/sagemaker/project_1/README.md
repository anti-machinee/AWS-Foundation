# Introduction
- This project follows [1] which is an AWS document
- This project is about creating an experiment using SageMaker Autopilot
- For concept learning purpose, the coding is not be completed
- My works in in Steps section

# Requirements
- See [1]

# AWS guide
- Specify experiment name, location of input data, target column, and output location
- Specify the type of problem
- Choose modeling strategy
- Select list of algorithms
- Compare results
- Download explainability and performance report

# AWS offerings
- CreateAutoMLJobV2 API
- CreateAutoMLJob 

## Steps
### Datasets
- Support tabulars (CSV or Parquet) with samples datasets
- Support images (PNG or JPG )and PDF files
### Problem type
- Regression
- Binary classification
- Multiclass classification
### Training modes
- Ensambling
- Hyperparameter optimization
### Algorithms supported
- Ensemble algorithms
- HPO algorithms
### Metrics and validation
- Metrics
- Cross-validation
### Deploy models
- Using Autopilot UI
- Using SageMaker APIs
### Share models
- Share model details and model performance with other users
### Generate Notebooks
- For EDA
- Propose best models

# References
- [1] https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development-create-experiment.html