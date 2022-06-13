---
title: From Networks to Optimal Higher-Order Models of Complex Systems
permalink: /
---

Graph-based data science and machine learning techniques such as graph mining, (social) network analysis, link prediction, node classification or community detection are an important foundation for data science applications in computer science, computational social science, and the life sciences. They help to detect patterns in large data sets that capture dyadic relations between pairs of genes, species, humans, or documents and they have improved our understanding of complex networks.

While the potential of analyzing graph representations of relational data is undisputed, we increasingly have access to data on networks that contain more than just dyadic relations. Consider, e.g., data on user click streams in the Web, time-stamped social networks, gene regulatory pathways, or time-stamped financial transactions. These are examples for time-resolved or sequential data that not only tell us who is related to whom but also when and in which order relations occur. Recent works have exposed that the timing and ordering of relations in such data can introduce higher-order, non-dyadic dependencies that are not captured by state-of-the-art graph representations. This oversimplification questions the validity of graph mining techniques in time series data and poses a threat for interdisciplinary applications of network analytics.

To address this challenge, researchers have developed advanced graph modelling and representation techniques based on higher-order models, which enable us to model non-Markovian characteristics in time series data on networks. Introducing this exciting research field, this tutorial gives an overview of higher-order network modelling techniques for time series data. Key takeaways for attendees will be (i) hands-on experience with higher-order network analytics, model selection, and data visualization, and (ii) a demonstration of the benefits of higher-order network analytics in real time series data on complex socio-technical systems.

# Tutor

[Prof. Dr. Ingo Scholtes](https://www.informatik.uni-wuerzburg.de/ml4nets/)  
Chair of Machine Learning for Complex Networks  
Center for Artificial Intelligence and Data Science (CAIDAS)  
Julius-Maximilians-Universität Würzburg  
Germany  

# Prerequisites

Participants should bring a laptop with a python 3.x environment. See [setup instructions](/mathplus2022-tutorial/setup). Prior exposure to python is beneficial.

# Schedule

**Welcome Note and Tutorial Overview**

**Lecture: From Networks to Optimal Higher-Order Models of Complex Systems** (approx. 90 min)
- Networks and Higher-Order Models  
- Causal paths in temporal networks  
- Higher-order models for causal topologies  
- Model Selection in Time Series Data 

**Coffee Break**

**Live Coding** (approx. 90 min)

Unit | Topic | Code
----|----|----
1 | Data Science with `python`, `jupyter`, and `VS Code` (self-study) | [.py](https://github.com/IngoScholtes/mathplus2022-tutorial/blob/master/code/1_vscode_jupyter.py)
2 | Analysis and Visualisation of Path Data in [`pathpy`](http://www.pathpy.net) (10 min) | [.ipynb](https://github.com/IngoScholtes/mathplus2022-tutorial/blob/master/code/2_pathpy.ipynb) 
3 | Fitting and Visualising Higher-order Network Models (10 min) |  [.ipynb](https://github.com/IngoScholtes/mathplus2022-tutorial/blob/master/code/3_higher_order.ipynb)
/ | **Coffee Break** | /
4 | Time-stamped Network Analysis in [`pathpy`](http://www.pathpy.net) (20 min) | [.ipynb](https://github.com/IngoScholtes/mathplus2022-tutorial/blob/master/code/4_temporal_networks.ipynb)
5 | Multi-order Model Selection (30 min) | [.ipynb](https://github.com/IngoScholtes/mathplus2022-tutorial/blob/master/code/5_multi_order.ipynb) 
6 | Optimal Higher-order Analytics for Temporal Data (20 min) | [.ipynb](https://github.com/IngoScholtes/mathplus2022-tutorial/blob/master/code/6_optimal_analysis.ipynb) 
7 | Exploration: Multi-order Analysis of [Time-stamped Social Networks](https://github.com/IngoScholtes/mathplus2022-tutorial/tree/master/data) (self-study) | [.ipynb](https://github.com/IngoScholtes/mathplus2022-tutorial/blob/master/code/7_exploration.ipynb)

# Data sets

A description of data sets that will be provided to participants, and which will be analyzed in the tutorial is available [here](https://github.com/IngoScholtes/mathplus2022-tutorial/tree/master/data).

# Setting up the environment

Hands-on sessions will be completed in `python`. A detailed description on how to set up the environment can be found in the [setup instructions](/mathplus2022-tutorial/setup).
