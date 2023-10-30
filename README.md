# IDS_706-Data_Engineering_Systems
## Mini-Project 9: Cloud-Hosted Notebook Data Manipulation

### PURPOSE

This project is for a data engineering course (Mini-Project 9). The purpose of this project is to setup and effectively utilize a cloud-based Jupyter Notebook environment, with a specific emphasis on harnessing the capabilities of Google Colab. This project also executes diverse data manipulation tasks on a provided sample dataset.

Dataset: 

***

### PROCESS

To achieve the objectives of this project, the following steps are taken:

1. **Setup and Configuration**
   a. Access Google Colab via a web browser with Google accounts.
   b. Create a new Jupyter Notebook in Google Colab.
   c. Configure the runtime settings for optimal performance.

2. **Data Manipulation Tasks**
   a. Load the dataset into the Jupyter Notebook using libraries like Scikit-learn.
   b. Explore the dataset's structure, data types, and basic statistics, utilizing visualization if needed.
   c. Clean the data by addressing missing values and outliers.
   d. Perform data manipulation tasks such as filtering, sorting, merging, or reshaping the data.
   e. Create visualizations using Matplotlib to convey insights from the data.
   f. Conduct basic data analysis, including calculating summary statistics and identifying correlations within the dataset.
   
***

### Commands to Run the Repo

To run the project, you can use the Makefile and follow these commands:
1. ```
   # To install the required the python packages
   make install
   ```
2. ```
   # To check code style
   make lint
   ```
3. ```
   # To run tests
   make test
   ```
4. ```
   # To format the code
   make format
   ```
5. ```
   # To extract data
   make extract
   ```
6. ```
   # To tranform data
   make transform_load
   ```
7. ```
   # To query data
   make query
   ```

