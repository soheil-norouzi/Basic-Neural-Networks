# Hebb Network Pattern Recognizer

This project implements a simple **Hebbian Neural Network** to recognize 'X' and 'O' patterns drawn on a 5x5 grid using a graphical user interface (GUI) built with Tkinter. The Hebbian learning rule is used to train the network based on pattern correlations.

## Features
- Draw patterns on a 5x5 grid by clicking cells to toggle between white (-1) and black (1).
- Train the network to recognize an 'X' or 'O' pattern.
- Predict whether a new pattern is closer to the trained 'X' or 'O'.
- Clear the grid to start over.

## How It Works
- **Hebbian Learning**: The network builds a weight matrix using the outer product of trained patterns ('X' and 'O'). Diagonal elements are zeroed to avoid self-connections.
- **Prediction**: The network multiplies the weight matrix by the input pattern and compares the result to the stored 'X' and 'O' patterns, choosing the best match.

## Requirements
- Python 3.x
- Libraries: `numpy`, `tkinter` (usually included with Python)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/soheil-norouzi/Basic-Neural-Networks-Pattern-Recognizer.git


# Binary Perceptron Pattern Recognizer

This project implements a **Binary Perceptron** to classify 'X' and 'O' patterns drawn on a 5x5 grid using a Tkinter-based GUI. Unlike the Hebbian approach, the Perceptron learns incrementally by adjusting weights based on prediction errors.

## Features
- Draw patterns on a 5x5 grid by clicking to toggle cells (white = -1, black = 1).
- Train the Perceptron to recognize 'X' or 'O' incrementally.
- Predict whether a new pattern is 'X' or 'O'.
- Clear the grid to start fresh.

## How It Works
- **Perceptron Learning**: Uses a single weight vector and bias, updated when predictions are wrong. 'X' is mapped to 1, 'O' to -1.
- **Prediction**: Computes a weighted sum of the input pattern plus bias, returning 'X' if positive, 'O' if negative.

## Requirements
- Python 3.x
- Libraries: `numpy`, `tkinter`

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/soheil-norouzi/Basic-Neural-Networks-Pattern-Recognizer.git


# Multi-Category Perceptron Pattern Recognizer

This project implements a **Multi-Category Perceptron** to classify multiple patterns ('X', 'O', and 'T') drawn on a 5x5 grid using a Tkinter GUI. It extends the binary Perceptron to handle more than two categories using a one-layer, multi-class approach.

## Features
- Draw patterns on a 5x5 grid (white = -1, black = 1).
- Train the network to recognize 'X', 'O', or 'T' patterns.
- Predict the category of a new pattern from the trained set.
- Clear the grid to reset.

## How It Works
- **Multi-Category Learning**: Uses a weight matrix (one row per category) and bias vector. Weights adjust to favor the correct category and penalize the wrong one.
- **Prediction**: Computes scores for all categories (e.g., 'X', 'O', 'I') and picks the one with the highest score.

## Requirements
- Python 3.x
- Libraries: `numpy`, `tkinter`

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/soheil-norouzi/Basic-Neural-Networks-Pattern-Recognizer.git
