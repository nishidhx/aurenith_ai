
# to migrate the db

export FLASK_APP = main.py

flask db init

flask db migrate -m "message"

flasl db upgrade