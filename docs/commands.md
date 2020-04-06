# Useful Commands

## Bash
#### Add excluded files/folders in .gitignore using terminal
`echo "__pycache__" >> .gitignore`

#### Activate venv using UNIX hints
```
source virtualenv/Scripts/activate
```

#### Deactivate venv using UNIX hints
`deactivate`

#### Run Python (lifehack)
`py`

## Django

#### Running the Django dev server
`python manage.py runserver`

#### Running the functional tests
`python functional_tests.py`

#### Running the unit tests
`python manage.py test`

## Git

####  Add all changes to tracked files and uses the commit message
`git commit -am "Basic view now returns minimal HTML"`

#### Show last commits info
`git log --oneline`
