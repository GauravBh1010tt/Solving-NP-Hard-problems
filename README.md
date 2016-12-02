# Solving-NP-Hard-problems
Large scale approximate solutions to - TSP, VRP, Knapsack, N-Queens, Graph Coloring

# Travelling Salesman Problem(TSP)
The solution uses Opt2 heuristic and Simulate Annealing as meta-heuristics.
Data set containing a graph of 50-80000 cities is provided in the data folder.
To use the TSP module run the following command
```python
obj = TSP(data)
obj.run()
```

# Vehicle Routing Problem(VRP) 
using K-Means clustering and Simulated Annealing. 
```python
obj = VRP(data)
obj.run()
```

# Graph Coloring Problem 
solved as Constraint Satisfaction Problem using Arc-2 consistency and search space reduction heuristics. 
```python
obj = GCP(data)
obj.run()
```

# Knapsack Problem 
Solved using dynamic programming and Branch and Bound with linear relaxation, tested on knapsack with 2000 items.
```python
obj = KSP(data)
obj.run()
```

# N-Queens 
MinMax conflict i.e. randomized hill climbing approach, tested on a board of 10,000 * 10,000.
```python
obj = NQ(data)
obj.run()
```

