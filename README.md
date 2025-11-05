# my-first-repo

Learning and practicing version control! 2

# setup

clone the repo to download it from github. perhaps onto the desktop.

navigate to the repo using the command line. 

'''sh
cd ~/Desktop/my-first-repo
'''

create a virtual environment: 
'''sh
conda create -n my-first-env-fall-2025 python=3.11
'''

activate virtual environment: 
'''sh
conda activate -n my-first-env-fall-2025 python=3.11
'''

install package dependences: 
'''sh
pip install -r requirements.txt
'''

# usage 

Example script: 

'''sh
python app/my_script.py
'''

Game of rock, paper, scissors:

'''sh
python app/rps.py
'''

# alternative modular style 
python -m app.rps
```

# testing

Run tests:

```sh
pytest
```