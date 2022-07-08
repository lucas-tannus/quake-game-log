# Quake Log Game

## Introduction
The porpouse of this repo is solving Quake Game Log.

### Built With
This project has been created using a simple stack based on:
 - Python 3.9.11

## Getting Started
In this section we're going to describe the setup needed on your local machine in order to run the script.

### Prerequisites

1. Install [Python 3.9.11](https://www.python.org/downloads/release/python-3911/) according to your operating system.

### Installing

1. Clone the repo
  ```sh
  git@github.com:lucas-tannus/quake-game-log.git
  ```
2. Start a virtual environment according to your IDE and operating system. 
3. Activate the virtual environment.
4. Go to the root directory.
  ```sh
  cd quake-game-log
  ```
5. To run the script.
  ```sh
  make run file={file_name}
  ```
The **file_name** should be a file that it's inside the `quake-game-log/data` folder, e.g. log_1.txt
  
#### Result
By running the `make run` a new file called `result.txt` is going to be created inside `quake-game-log/data` folder having the solution.

> :warning: **In case of happen any error**: All will be logged inside `quake-game-log/data/logs`

### Testing
In order to run the unit tests and generate coverage report.
  ```sh
  make tests
  ```
