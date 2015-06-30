# pylacuna
Python api for [Lacuna Expanse](http://www.lacunaexpanse.com/)

## Summary

I'm trying to accomplish three things here.

1. Produce generic python libraries for interacting with the Lacuna Expanse game, to allow developers to create their own scripts easily.
2. Use those libraries to create useful scripts that help a player perform routine actions.
3. Use those scripts with some AI to create an automated bot to play the game.


## Installation

_(Eventually we will want to host this on PyPy so we can just pip install it)_

To install (tested on Ubuntu 12.04, requires pip):
```bash
// Clone
git clone "https://github.com/miketwo/pylacuna"
cd pylacuna
// Create a virtual environment (optional but recommended -- keeps your comp clean)
virtualenv .venv
. .venv/bin/activate
// Install
pip install .
```

You should now be able to import in your own python script:
```python
import pylacuna
```

## Usage
TBD

## Development & Test
To develop and run tests (tested on Ubuntu 12.04):
```
// Clone
git clone "https://github.com/miketwo/pylacuna"
cd pylacuna
// Create a virtual environment (optional but recommended -- keeps your comp clean)
virtualenv .venv
. .venv/bin/activate
// Install in dev mode
pip install -e .
// Run tests
pylacuna_run_tests.sh
// Run main script
pylacuna
```

## ToDo
- so many things, will update here soon...



## Architecture
I'm trying to have code at multiple abstraction levels:

- CORE drivers are the raw interface to the JSONRPC. I'm trying to keep them
  dumb, simple, and stateless, though that last one might be hard because I
  also want to be smart about caching. Most are dervied from the `dict` object.

- MIDDLEWARE libraries will have more types of calculations, mission-level
  logic and hueristics. For example, maybe a method that ranks the nearest planets according
  to their resource content. Or something that intelligently upgrades the food production on a planet.

- HIGH-LEVEL libraries will include the AI. I'm leaning toward starting with
  A*, depending on how easy it is to simulate future states. It'll depend a lot on
  how the middleware layer turns out.

### Layout
Uses a "standard" Python project layout
```
Project/
|-- bin/
|   |-- scripts
|
|-- project/
|   |-- tests/
|   |   |-- __init__.py
|   |   |-- test_library1.py
|   |   |-- test_library2.py
|   |
|   |-- __init__.py
|   |-- library1.py
|   |-- library2.py
|
|-- var/
|   |-- generated files
|
|-- docs/
|   |-- All documentation
|
|-- setup.py
|-- README.md
```

### Ideas about AI

A simple approach might be to try to attempt the following
 - **ENUMERATE** all the actions available to the player right now.
 - **EVALUATE** all actions according to a heuristic
 - **SUGGEST** best action

Eventually this might lead to being able to go 2 "moves" ahead, by looping it. Maybe...

#### Enumerate all actions
Not sure how to do this. I guess we can check for upgrading every building, building every new building, demolishing every building, building every ship, sending every ship, doing every mission, buying every trade, ... The list of actions is huge. We will need to restrict it at first to be manageable.

### [License](license.md)




