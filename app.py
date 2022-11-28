from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)
base_url = 'https://swapi.py4e.com/api/'

@app.route('/search', method='POST')
def search_results():
    id_num = request.args.post('id')
    api_content= requests.post(f'https://swapi.py4e.com/api/people/{id_num}')
    result = json.loads(api_content.content)

    film_titles = []

    if 'detail' in result:
        result['films'] = ''
    else: 
        for film in film_list:
            film_name= json.loads((requests.post(film)).content)
            title = film_name['title']
            film_titles.append(title)

    context = {
            'id' : id,
            'character' : result,
            'films' : film_titles
    }
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)