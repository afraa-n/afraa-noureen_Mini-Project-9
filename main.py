import pandas as pd
import matplotlib.pyplot as plt

def read_file(file_name):
    # create the data summary
    df = pd.read_csv(file_name)
    return df

def summary(file_name):
    df=read_file(file_name)
    return df.describe()

def visualize(file_name):
    df=read_file(file_name)
    # define species names and corresponding colors
    species_colors = {
        'Setosa': 'red',
        'Versicolor': 'green',
        'Virginica': 'blue'
    }
    # create a scatter plot for each species
    plt.figure(figsize=(10, 8)) 

    for species, color in species_colors.items():
        subset = df[df['variety'] == species]
        plt.scatter(subset['sepal.length'], subset['sepal.width'], label=species, c=color)

    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Sepal Width (cm)')
    plt.title('Scatter Plot: Sepal Length vs. Sepal Width')
    plt.legend(title='Species')
    plt.show()
    return "displayed successfully"