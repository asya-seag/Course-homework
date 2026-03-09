from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    recipes = [
        {'id': 1, 'title': 'Spaghetti Carbonara', 'description': 'A classic Italian pasta dish.'},
        {'id': 2, 'title': 'Chicken Curry', 'description': 'A spicy and flavorful dish.'},
        {'id': 3, 'title': 'Chocolate Cake', 'description': 'A rich and moist dessert.'}
    ]
    return render_template('index.html', recipes=recipes)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)


