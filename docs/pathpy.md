---
title: Hands-on Tutorial on Higher-Order Network Analysis
permalink: /pathpy
---

# Higher-order Network Analysis with pathpy

This tutorial gives an introduction to the python Open Source data analytics package `pathpy`.

`pathpy` uses higher-order network models to analyze and visualize time-series data on complex networks. Examples include time-stamped social networks, temporal proximity data, traces on flow processes in networks, passenger itineraries in transportation networks, user click streams in the Web, citation networks, or biological pathway data. Building on the higher- and multi-order statistical modelling framework introduced in [[1]](http://www.nature.com/ncomms/2014/140924/ncomms6024/full/ncomms6024.html) and [[2]](http://dl.acm.org/citation.cfm?id=3098145), `pathpy` offers machine learning techniques to select optimal, higher-order network models for your data. It then uses these models to detect, model, and visualize higher-order dependencies and patterns discarded by standard network models.

The following video gives a high-level explanation of the ideas behind `pathpy`:

[![Watch promotional video](https://img.youtube.com/vi/CxJkVrD2ZlM/0.jpg)](https://www.youtube.com/watch?v=CxJkVrD2ZlM)

The methodological foundations of `pathpy` are described in the following published works:

1. L Petrovic, I Scholtes: [Learning the Markov order of paths in a network](https://arxiv.org/abs/2007.02861), In Proceedings of WWW '22: The Web Conference 2022, Lyon, France, April 2022
2. V Perri, I Scholtes: [HOTVis: Higher-Order Time-Aware Visualisation of Dynamic Graphs](https://arxiv.org/abs/1908.05976), Proceedings of the 28th International Symposium on Graph Drawing and Network Visualization (GD 2020), Vancouver, BC, Canada, September 15-18, 2020
3. T LaRock, V Nanumyan, I Scholtes, G Casiraghi, T Eliassi-Rad and F Schweitzer: [HYPA: Efficient Detection of Path Anomalies in Time Series Data on Networks](https://arxiv.org/abs/1905.10580), In Proceedings of SIAM International Conference on Data Mining (SDM 2020), May 7-9 2020
4. R Lambiotte, M Rosvall, I Scholtes: [From Networks to Optimal Higher-Order Models of Complex Systems](https://arxiv.org/abs/1806.05977), Nature Physics, Vol. 15, p. 313-320, March 25 2019
5. I Scholtes: [When is a network a network? Multi-Order Graphical Model Selection in Pathways and Temporal Networks](http://dl.acm.org/citation.cfm?id=3098145), In KDD'17 - Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Halifax, Nova Scotia, Canada, August 13-17, 2017
6. I Scholtes, N Wider, A Garas: [Higher-Order Aggregate Networks in the Analysis of Temporal Networks: Path structures and centralities](http://dx.doi.org/10.1140/epjb/e2016-60663-0), The European Physical Journal B, 89:61, March 2016
7. I Scholtes, N Wider, R Pfitzner, A Garas, CJ Tessone, F Schweitzer: [Causality-driven slow-down and speed-up of diffusion in non-Markovian temporal networks](http://www.nature.com/ncomms/2014/140924/ncomms6024/full/ncomms6024.html), Nature Communications, 5, September 2014
8. R Pfitzner, I Scholtes, A Garas, CJ Tessone, F Schweitzer: [Betweenness preference: Quantifying correlations in the topological dynamics of temporal networks](http://journals.aps.org/prl/abstract/10.1103/PhysRevLett.110.198701), Phys Rev Lett, 110(19), 198701, May 2013

This interactive tutorial introduces the theoretical foundations of `pathpy` and uses empirical and synthetic data to show how they can be practically applied in `python`. The latest release of `pathpy` is available via the [python package index](https://pypi.org/project/pathpy2/). In python 3.x, you can install it by typing:

```
pip install pathpy2
```

`pathpy` is fully integrated with `jupyter`, providing in-line, interactive and dynamic visualisations of graphs, temporal networks, as well as higher- and multi-order network models. This teaser highlights some of its features:

[![Watch promotional video](https://img.youtube.com/vi/QIPqFaR2Z5c/0.jpg)](https://www.youtube.com/watch?v=QIPqFaR2Z5c)

A description of the [recommended setup](https://ingoscholtes.github.io/mathplus2022-tutorial/setup) to complete this tutorial is available [online](https://ingoscholtes.github.io/mathplus2022-tutorial/setup). A brief introduction to interactive data science with `python`, `Visual Studio Code`, and `jupyter` is given in [unit 1](https://github.com/IngoScholtes/mathplus2022-tutorial/blob/master/code/1_vscode_jupyter.py).

`pathpy` is brought to you by the Chair of Machine Learning for Complex Networks at [University of Würzburg](https://www.informatik.uni-wuerzburg.de/ml4nets/).

Feel free to [get in touch](https://www.informatik.uni-wuerzburg.de/ml4nets/) if you want to host an interaction hands-on tutorial in your research group or institute.