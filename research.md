# Research

## Monte Carlo

## General MCTS Info

- https://towardsdatascience.com/monte-carlo-tree-search-158a917a8baa
- https://jeffbradberry.com/posts/2015/09/intro-to-monte-carlo-tree-search/
- figures out best move (from set of moves) by Selecting, Expand, Simulating, Updates nodes in search tree
- Selection:
  - select node on tree that has highest probability of winning
  - Repeat recursively until leaf node; that path is most likely a winning state
- Expansion: 
  - Expand the leaf node we just visited; creating x children
- Simulation:
  - Simulate the game for each child node, assigning rewards to each child based on their performance
- Update:
  - Perform back propagation up the tree, updating nodes accordingly on the way up

## Perfect Information MCTS for Perfect Information Games

- https://pdfs.semanticscholar.org/011e/2c79575721764c127e210c9d8105a6305e70.pdf

### Imperfect Information MCTS for Imperfect Information Games

- https://skatgame.net/mburo/ps/recmc13.pdf
- 

### Solving Imperfect Information Games Using the Monte Carlo Heuristic

- https://pdfs.semanticscholar.org/cc52/4499c2e8c2fb829f0f371a1452d764cdd452.pdf



