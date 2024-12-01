# AWS SageMaker - Implement MLOps

# Why MLOps?
- Support project management, CI/CD and quality assurance when transforming from individual to business
- Improve delivery time, reduce defects and make data science more efficient
## Challenges
- Project management
    - Transpancy communication between data scientists and engineers
- Communication and collaboration
    - Visibility across different stakeholders
- Everything is code
    - ML strategies impact the coding
    - Model lifecycle independent of the applications and systems
    - Wide range of techniques (IaC, CaC, PaC)
- CI/CD
    - Source data
        - act: version and trigger
    - ML model
        - act: verson
    - Automated test
        - act: validate ML models. time: development and production
    - Building
        - act: trigger correctly and not always when components change
    - Deployment
        - act: package ML models and expose to applications
- Monitoring and logging
    - Building 
        - act: monitor training metrics and model experiments
    - Deployment
        - act: monitor input data streams, serving metrics and ML models metrics
## Benefit
- Productivity
- Repetability
- Reliability
- Auditability
- Data and model quality

# Experiments

# Workflows

## ML Pipelines
- Benefits
    - Auto-scaling serverless infrastructure
        - act: do not need to manage the infrastructure
    - Intuitive user experience
        - act: provide multi interfaces
    - Integration with AWS
        - act: provide seamless integration
    - Reduce costs
        - act: pay jobs orchestrated by the Pipelines
    - Auditability and lineage tracking
        - act: track history of data
### Pipelines overview
- Interconnected steps in directed acyclic graph
- Example steps
    - Processing
    - Training
    - Condition
    - RegisterModel
    - CreateModel
    - Transform
#### Structure and Execution
- Pipeline Structure
    - Name, parameters and steps
    - Steps automatically determine their order of execution by their data dependencies on one another
- Pipeline Execution using Parallelism Configuration
#### Access Management
#### Set up cross-account support
### Pipelines actions

## K8S Ocherstration

## Notebook Jobs