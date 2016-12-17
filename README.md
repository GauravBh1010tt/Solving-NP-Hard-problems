# Solving-NP-Hard-problems
Large scale approximate solutions to - TSP, VRP, Knapsack, Graph Coloring

# Travelling Salesman Problem(TSP)
The solution uses Opt2 heuristic and Simulate Annealing as meta-heuristics.
Data set containing a graph of 50-80000 cities is provided in the data folder.
To use the TSP module run the following command
```sh
$ python tsp_solver.py tsp_sample_data
```

# Vehicle Routing Problem(VRP) 
using K-Means clustering and Simulated Annealing. 
```sh
$ python vrp_solver.py vrp_sample_data
```

# Graph Coloring Problem 
solved as Constraint Satisfaction Problem using Arc-2 consistency and search space reduction heuristics. 
```sh
$ python graph_col.py gc_sample_data
```
# Knapsack Problem 
Solved using dynamic programming and Branch and Bound with linear relaxation, tested on knapsack with 2000 items.
```sh
$ python Knapsack_solver.py ks_sample_data
```


