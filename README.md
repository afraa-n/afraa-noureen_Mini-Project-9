# IDS_706-Data_Engineering_Systems
## Mini-Project 9: Cloud-Hosted Notebook Data Manipulation

### PURPOSE

This project is for a data engineering course (Mini-Project 9). The purpose of this project is to setup and effectively utilize a cloud-based Jupyter Notebook environment, with a specific emphasis on harnessing the capabilities of Google Colab. This project also executes diverse data manipulation tasks on a provided sample dataset.

Dataset: [Iris Dataset](https://gist.github.com/netj/8836201)

***

### PROCESS

To achieve the objectives of this project, the following steps are taken:

1. **Setup and Configuration**
   a. Access Google Colab via a web browser with Google accounts.  
   b. Create a new Jupyter Notebook in Google Colab.  
   c. Configure the runtime settings for optimal performance.  

2. **Data Manipulation Tasks**
   a. Load the dataset into the Jupyter Notebook.  
   b. Explore the dataset's structure, data types, and basic statistics.  
   d. Perform data manipulation tasks such as filtering, sorting, and grouping the data.  
   e. Create visualizations using Matplotlib to convey insights from the data.  
   f. Conduct basic data analysis, including calculating summary statistics.  
   
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

***

### Workflows

On running the above commands, it runs successfully:

![1](https://github.com/afraa-n/afraa-noureen_Mini-Project-9/assets/143756865/0cea640f-1af7-4b30-9b99-38c5432f6324)
![2](https://github.com/afraa-n/afraa-noureen_Mini-Project-9/assets/143756865/9022f67d-22a5-485a-b881-d8a40ba4d5a5)

***

### Results

The documentation demonstrating the tasks performed can be found in _Documentation.md_.

#### Data Visualization
Created a scatter plot to visualize the relationship between Sepal Length and Sepal Width for different species.
![image](https://github.com/afraa-n/afraa-noureen_Mini-Project-9/assets/143756865/3277a351-f838-4b86-a3a0-195963ae24fe)

#### Data Manipulation
1. Filtered rows where sepal length is greater than 5.5
![image](https://github.com/afraa-n/afraa-noureen_Mini-Project-9/assets/143756865/00fa416f-8a6b-478c-a2bf-e0d84bd0fd0a)

2. Sorted the data by petal length in ascending order
![image](https://github.com/afraa-n/afraa-noureen_Mini-Project-9/assets/143756865/9601a1d7-7743-4624-9688-7873f8b1a12d)

3. Calculated the mean sepal length and sepal width by species
![image](https://github.com/afraa-n/afraa-noureen_Mini-Project-9/assets/143756865/4dadbbf1-2607-4f1f-9e6c-467da49ea815)
