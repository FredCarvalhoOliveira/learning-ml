# My Machine Learning Adventure

This repo serves as a personal notebook for machine learning concepts.

As I learn I'll try to create quality notes, examples and visualizations to help others learn these concepts


# Contents
- [Introduction](#intro)
- [ML Strategy](#strat)
- [Distance Based Classifiers](#dbc)
- [Clustering Techniques](#cluster)
- [Supervised Learning](#super_learn)
- [Unsupervised Learning](#unsuper_learn)

- [Computer Vision](#cv)
- [Natural Language Processing](#nlp)
- [Tabular](#tab)
- [Time Series](#ts)




<a name="intro" />

## Introduction
- TODO

<a name="strat" />

# ML Strategy

## Orthogonalization
Orthogonalization is a system design property that ensures that modification of an instruction or an algorithm component does not create or propagate side effects to other system components.
Orthogonalization makes it easier to independently verify the algorithms, thus reducing the time required for testing and development.

In the development of machine learning system one common problem is dealing with the vast amount of tuneable parameters to achieve a desired result.

Orthogonalization in ML is the process of choosing and tuning parameters that represent a dimension of what we want to achieve, orthogonal parameters should be tuned first

## Chain of assumptions in ML <sub>(by Andrew Ng)</sub>

### 1. Fit training set well on cost function
- **If unsuccessful:**
  - Bigger Model 
  - Different optimizer 

### 2. Fit dev set well on cost function
- **If unsuccessful:**
  - Regularization 
  - Increase training set size

### 3. Fit test set well on cost function
- **If unsuccessful:**
  - Increase dev set size

### 4. Performs well on real world
- **If unsuccessful:**
  - Change test set, as it might not represent the real world scenario
  - Change cost function, as it might not be evaluation the right thing

## Setting up your goal

### Define a single number evaluation metric
By defining a single number evaluation metric you have a clear metric to represent how good a model is in relation to others.
This simplifies the process of evaluating the results from different experiments to choose which one produced the best model


### Satisficing and Optimizing metric


<a name="dbc" />

# Distance Based Classifiers
- TODO

<a name="cluster" />

# Clustering Techniques
- TODO

<a name="super_learn" />

# Supervised Learning
- TODO

<a name="unsuper_learn" />

# Unsupervised Learning
- TODO

<a name="cv" />

# Computer Vision
- TODO

<a name="nlp" />

# Natural Language Processing
- TODO


