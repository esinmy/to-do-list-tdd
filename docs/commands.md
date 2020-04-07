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

#### Running all tests
`python manage.py test`

#### Running the functional tests
`python manage.py test functional_tests`

#### Running the unit tests
`python manage.py test lists`

## Git

####  Add all changes to tracked files and uses the commit message
`git commit -am "Basic view now returns minimal HTML"`

#### Show last commits info
`git log --oneline`

#### Move the file
`git mv tests.py tests/tests.py`
