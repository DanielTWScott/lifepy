# Game of Life

This project primarily concern's simulation of Conway's Game of Life using Python. 

In particular, I investigate differences in processing when using Python, the numpy package, and Cython. This demonstrated that processing speeds using either the numpy package or Cython are approximately five times as fast as when using standard Python.

Please see my "to do" list for information on planned next steps of this project.

## Example Animation of a Gosper Glider Gun 
The below animation shows a Gosper Glider Gun created within the Game of Life. (Please see [Gosper Glider Gun] (https://www.conwaylife.com/wiki/Gosper_glider_gun) for further information on this structure)

![](gosper.gif)

## Getting Started

### Prerequisites
- Python 3
- ImageMagick (if the user wishes to use the 'matplotlib' package to make a gif similar to that seen above)

### Installing
- The simplest way for the user to install this would be to clone this repository
- It should be noted that this project has only been tested on my machine, using Python 3.7 via Anaconda

## Running the code
The user should follow the below steps:
- View and run the notebook (of the files saved in this repository) with JupyterLab (in particular the file life.py, which contains the primary code underlying this project)
- If desirer, use the `--make-gif` flag to save the output of to a .gif file for display

View the notebook with Jupyter Lab.

## Acknowledgments
- I would like to acknowledge John Horton Conway, inventor of the Game of Life
