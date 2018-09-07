import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from src import create_app

app = create_app('flask.cfg')

if __name__ == '__main__':
    app.run()
