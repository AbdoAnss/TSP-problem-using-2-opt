import csv
import streamlit as st
import numpy as np
from graphviz import Digraph

def two_opt(distances):
    """
    Implements the 2-opt algorithm for the traveling salesman problem.

    Args:
      distances: The distance matrix between nodes.

    Returns:
      A list of indices representing the optimized tour.
    """

    # Initialize the tour as the list of node indices
    n = len(distances)
    tour = list(range(n))

    # Calculate the initial tour length
    tour_length = np.sum([distances[tour[i]][tour[(i+1)%n]] for i in range(n)])

    # Iteratively try to improve the tour
    improved = True
    while improved:
        improved = False
        for i in range(n - 2):
            for j in range(i + 2, n):
                # Calculate the new tour length if nodes i and j are swapped
                new_tour = tour[:]
                new_tour[i:j] = new_tour[i:j][::-1]
                new_tour_length = (tour_length - distances[tour[i]][tour[i-1]] - distances[tour[j]][tour[(j+1)%n]]
                                   + distances[tour[i]][tour[(j-1)%n]] + distances[tour[j]][tour[i-1]])

                # If the new tour length is shorter, update the tour and tour length
                if new_tour_length < tour_length:
                    tour = new_tour
                    tour_length = new_tour_length
                    improved = True
                else:
                    improved = False

    return tour

st.title("2-Opt Algorithm")
st.write("The 2-opt algorithm is a simple and effective algorithm for solving the traveling salesman problem. It works by iteratively swapping pairs of nodes in the tour to improve its length.")
st.write("This app allows you to upload a CSV file containing the distance matrix between nodes, and it will output the optimized tour and its length.")

st.sidebar.title("TSP Problem Solver")
st.sidebar.write("This app uses the 2-opt algorithm to solve the traveling salesman problem. Upload a CSV file containing the distance matrix between nodes, and it will output the optimized tour and its length.")
st.sidebar.write("Made by: @AbdoAnss")


st.write("Upload a CSV file containing the distance matrix")

# File uploader

file_uploader = st.file_uploader("Choose a file", type="csv")

if file_uploader:
    distances = []
    # Read the contents of the uploaded file
    contents = file_uploader.read().decode('utf-8-sig').splitlines()
    # Parse the contents using the csv.reader function
    reader = csv.reader(contents)
    for ligne in reader:
        distances.append(list(map(float, ligne)))

    tournee_optimisee = two_opt(distances)

    longueur_optimisee = sum(distances[tournee_optimisee[k]][tournee_optimisee[(k + 1) % len(tournee_optimisee)]] for k in range(len(tournee_optimisee)))

    st.write("Longueur de la tournée optimisée:", longueur_optimisee)
    st.write("Tournée optimisée:", tournee_optimisee)

    # Create a graph of the optimized tour using Graphviz

    dot = Digraph(comment='Optimized Tour')
    for i in range(len(tournee_optimisee)):
        j = (i + 1) % len(tournee_optimisee)
        dot.edge(str(tournee_optimisee[i]), str(tournee_optimisee[j]), label=str(distances[tournee_optimisee[i]][tournee_optimisee[j]]))
    st.graphviz_chart(dot)
