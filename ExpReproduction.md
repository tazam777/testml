# Experiment Reproduction with Restler Tool

## Introduction
This document outlines the steps taken to reproduce the experiment results with Restler. The objective of this reproduction was to check if the original poject of the entry paper works . The environment for this reproduction was local, and a simple login API was used as the target for testing using Restler.

## Experiment Details
- **Tool Used**: Restler
- **Objective**: Able to reproduce outputs from Entry paper
- **Environment**: Local
- **Date of Experiment**: [20-Feb-2024]

## Steps to Reproduce
1. **Setup Environment**:
   - Cloned the Restler repository from GitHub:
     ```
     git clone https://github.com/microsoft/restler-fuzzer.git
     ```
   - Ensured that the target API (simple login API) is running and accessible. The API project is available at [group-formation-ainetworks/testProj](https://github.com/mcs-cu-sp24/group-formation-ainetworks/tree/main/testProj).

2. **Run Restler**:

3. **Analyze Results**:
   - After Restler execution completed, examined the generated files. These may include logs, reports, and any other artifacts created by Restler during the fuzzing process.
   
4. **Review Server Errors**:
   - Examined the errors logged on the application server during the Restler testing. These errors are saved in the file [applicationServerErrorlogs.txt](https://github.com/mcs-cu-sp24/group-formation-ainetworks/blob/main/applicationServerErrorlogs.txt).

5. **Auxiliary Files**:
   - Downloaded the auxiliary files zip archive from [Auxiliary_files.zip](https://github.com/mcs-cu-sp24/group-formation-ainetworks/blob/main/Auxiliary_files.zip) for additional artifacts related to the experiment.

## Observations
- During the fuzzing process, Restler logged a bug with status code 500 when an empty JSON payload was passed to the server.
- Document any other errors, vulnerabilities, or unexpected behavior encountered during the reproduction process.

## References
- [Restler GitHub Repository](https://github.com/microsoft/restler-fuzzer.git)
- [Group Formation AI Networks GitHub Repository](https://github.com/mcs-cu-sp24/group-formation-ainetworks.git)
- [Link to Server Error Log (applicationServerErrorlogs.txt)](https://github.com/mcs-cu-sp24/group-formation-ainetworks/blob/main/applicationServerErrorlogs.txt)
