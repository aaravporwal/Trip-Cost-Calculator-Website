from flask import Flask, render_template, request
app = Flask(__name__)

def calculate_trip_cost(distance, mileage, fuel_price):
    fuel_consumption = distance / mileage
    trip_cost = fuel_consumption * fuel_price
    return trip_cost

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    distance = float(request.form.get('distance'))
    mileage = float(request.form.get('mileage'))
    fuel_price = float(request.form.get('fuel_price'))

    total_cost = calculate_trip_cost(distance, mileage, fuel_price)

    return render_template('result.html', total_cost=total_cost)

if __name__ == '__main__':
    app.run(debug=True)
