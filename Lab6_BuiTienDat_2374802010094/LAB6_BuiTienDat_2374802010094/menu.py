from flask import Flask, render_template, abort

app = Flask(__name__)

# Sample menu data
menu_data = {
    "drinks": [
        {"name": "Coffee", "price": 2},
        {"name": "Tea", "price": 1.5},
        {"name": "Juice", "price": 2.5}
    ],
    "food": [
        {"name": "Burger", "price": 5},
        {"name": "Pizza", "price": 8},
        {"name": "Salad", "price": 4}
    ]
}

@app.route('/menu/<category>')
def show_menu(category):
    items = menu_data.get(category)
    if items:
        return render_template('menu.html', category=category.capitalize(), items=items)
    else:
        abort(404, description="Category not found")

if __name__ == '__main__':
    app.run(debug=True)
