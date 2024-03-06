# Traveling Salesman Problem Solver

This application solves the Traveling Salesman Problem (TSP) using the 2-Opt Algorithm. The TSP is a classic algorithmic problem in the field of computer science and operations research which focuses on optimization. In this problem, a salesman is given a list of cities, and must determine the shortest possible route that allows them to visit each city once and return to their original location.

## Features

* Upload a CSV file containing the distance matrix between cities
* Solve the TSP using the 2-Opt Algorithm
* Display the optimized tour length and tour
* Visualize the cities and distances between them using a graph

## Getting Started

### Prerequisites

* Python 3.x
* Streamlit
* graphviz

### Installation

1. Clone this repository to your local machine
```bash
git clone https://github.com/your-username/tsp-solver.git
```
2. Install the required packages
```
pip install streamlit graphviz
```
3. Run the application
```
streamlit run main.py
```
4. Upload a CSV file containing the distance matrix between cities
5. Observe the optimized tour length, tour, and graph visualization

## Example CSV File

Here is an example CSV file that can be used to test the application:
```css
0,10,20,30,40
10,0,5,15,25
20,5,0,10,30
30,15,10,0,25
40,25,30,20,0
```
This file represents the distances between 5 cities. The first line and first column represent the names of the cities (in this example, we have simply used numeric indices for the cities). The other lines and columns represent the distances between the cities. For example, the distance between city 0 and city 1 is 10, the distance between city 1 and city 2 is 5, etc.

## Built With

* [Streamlit](https://streamlit.io/) - The web application framework used
* [graphviz](https://graphviz.org/) - The graph visualization library used

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Acknowledgments

* [Streamlit](https://streamlit.io/) - For providing an easy-to-use framework for building data applications
* [graphviz](https://graphviz.org/) - For providing a powerful library for graph visualization
