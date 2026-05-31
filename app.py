from flask import Flask, request, render_template
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, template_folder='../templates')

# Get the Spoonacular API key from the environment variables
SPOONACULAR_API_KEY = os.getenv('SPOONACULAR_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    recipes = []
    if request.method == 'POST':
        query = request.form.get('query')
        response = requests.get(
            'https://api.spoonacular.com/recipes/complexSearch',
            params={'query': query, 'apiKey': SPOONACULAR_API_KEY}
        )
        if response.status_code == 200:
            data = response.json()
            recipes = data.get('results', [])
            print(recipes)
    return render_template('index.html', recipes=recipes)

@app.route('/recipe/templates<int:recipe_id>')
def recipe_detail(recipe_id):
    response = requests.get(
        f'https://api.spoonacular.com/recipes/{recipe_id}/information',
        params={'apiKey': SPOONACULAR_API_KEY}
    )
    if response.status_code == 200:
        recipe = response.json()
    else:
        recipe = None
    return render_template('recipe_detail.html', recipe=recipe)

if __name__ == '__main__':
    app.run(debug=True)
