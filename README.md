# Game of Life

This project primarily concern's simulation of Conway's Game of Life using Python. 

In particular, I investigate differences in processing when using Python, the numpy package, and Cython. This demonstrated that processing speeds using either the numpy package or Cython are approximately five times as fast as when using standard Python.

Please see my "to do" list for information on planned next steps of this project.

![](gosper.gif)

## Getting Started

### Prerequisites
- Python 3
- ImageMagick (if the user wishes to use the 'matplotlib' package to make a gif similar to that seen above)

### Installing
- The simplest way for the user to install this would be to clone this repository
- It should be noted that this project has only been tested on my machine, using Python 3. [ ] via Anaconda

## Running the code

View interactive matplotlib

```sh
python life.py gosper
```

use the `--make-gif` flag to save to a .gif.

View the notebook with Jupyter Lab.

## Acknowledgments
- I would like to acknowledge John Horton Conway, inventor of the Game of Life
