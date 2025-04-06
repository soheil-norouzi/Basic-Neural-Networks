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
   git clone https://github.com/soheil-norouzi/Hebb-Network-Pattern-Recognizer.git
