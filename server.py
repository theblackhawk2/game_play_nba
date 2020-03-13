from flask import Flask
from flask import request
import random

app = Flask(__name__)

PARAMS_REQUIS  = ['GP','MIN','PTS','FGM','FGA','FG%','3P Made','3PA','3P%','FTM','FTA','FT%','OREB','DREB','REB','AST','STL','BLK','TOV'
]

class MockModel:
    """
    Cette classe est une  classe de test pour un classificateur
    qui a un échantillonage aléatoire entre 0 et 1
    """
    def __init__(self):
        print("Object Mock créé")
        

    def predict(self,X):
        return random.randint(0,1)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/nba_inputs', methods = ['POST','GET'])
def return_prediction():
    assert request.path == '/nba_inputs'
    assert request.method == 'POST'
    print(request.args)
    """
    args = {}
    for arg in PARAMS_REQUIS:
        args[arg] = request.args[arg]
    print(args)
    
    """
    A = MockModel()
    return A.predict("Test")

if __name__ == '__main__':
    app.run(debug=True)

    
    