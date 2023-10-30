from main import read_file, summary, visualize
import matplotlib.pyplot as plt

"Testing main.py"

def test_read_file():
    df=read_file('iris.csv')
    assert len(df)==150

def test_describe():
    df=read_file('iris.csv')
    desc_stats = summary(df)
    assert desc_stats['sepal.length'].mean()==5.843333

def test_visualize():
    df=read_file('iris.csv')
    test_plot = visualize(df)
    assert test_plot == "displayed successfully"


if __name__ == "__main__":
    test_read_file()
    test_describe()
    test_visualize()