# bookingSystemAPI

##### run project

`poetry run python app/main.py`

> If you have an error when starting: ModuleNotFoundError: No module named ... - then you need to set the PYTHONPATH variable:
> `export PYTHONPATH=.`

<br>

##### generate migration:

`poetry run alembic revision --autogenerate -m "Desription"`

<br>

##### run migration:

`poetry run alembic upgrade heads`
