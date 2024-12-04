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
- Pipeline Role Permissions
    - Require
        - IAM pipeline execution role passed to Pipelines 
        - The role of SM instance creating pipeline must have iam:PassRole
        - Create and Describe permissions for each job types
        - S3 permission
            - Resource based policies
            - Identity based policies
- Pipeline Step Permissions
    - Require
        - IAM role in account that provides access for the needed resource
        - This role is passed to the SM service principal by the pipline
    - Separate permissions for each step
- Customize access management for Pipelines jobs
    - Customize IAM policies to give permisisons to users
    - Follow conventions of defining policies names
- Service Control Policies with Pipelines
    - Centralize controls 
#### Set up cross-account support
- Grant controlled access to pipelines
- Allow other accounts to view  pipelines, trigger executions and monitor runs
- Set up cross-account pipeline sharing
    - TODO
- Get responses to your resource share invitation
    - TODO
- Permission policies for Pipelines resources
    - TODO
- Extended pipeline execution permissions
    - TODO
- Access shared pipeline entities through direct API calls
    - TODO
#### Pipeline parameters
- Use parameters as inputs to pipeline steps
- Must match the parameter type
#### Pipelines steps
- Step properties
    - Add dependencies between steps in the pipeline
- Step parallelism
    - Run independent steps in parallel
    - Care about executing many steps
- Data dependency between steps
    - Pass properties of one step as input to another step
- Custom dependency between steps
    - Customize how to access data from previous steps
- Custom images in a step
    - Can not create images in Studio Classic
    - Provide image URI in the estimator definition
#### Add steps

### Pipelines actions

## K8S Ocherstration

## Notebook Jobs