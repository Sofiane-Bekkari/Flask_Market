from distutils.log import debug
from market import app

#CHECK IF THE RUN.PY FILE HAS EXECUTED DIRECTLY AND NOT IMPORTED
if __name__ == '__main__':
    app.run(debug=True)