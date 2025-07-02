# app.py
from flask import Flask, render_template, request, send_file
from data_fetcher import get_stock_data_yf,get_all_sectors,get_stock_by_sector,  get_stock_details #get_stock_by_sector,
from utils import export_to_excel

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/sector', methods=['GET', 'POST'])
# def sector():
#     if request.method == 'POST':
#         sector = request.form['sector']
#         stocks = get_stock_by_sector(sector)
#         return render_template('sector.html', stocks=stocks, sector=sector)
#     return render_template('sector.html')

# @app.route('/sector', methods=['GET', 'POST'])
# def sector():
#     from data_fetcher import get_all_sectors
#     sectors = ["All"] + get_all_sectors()

#     if request.method == 'POST':
#         selected_sector = request.form['sector']
#         stocks = get_stock_data_yf(selected_sector)
#         # stocks = get_stock_by_sector(selected_sector)
#         return render_template('sector.html', stocks=stocks, sectors=sectors, selected=selected_sector)
    
#     # Default: show all
#     # stocks = get_stock_by_sector("All")
#     stocks = get_stock_data_yf("All")

#     return render_template('sector.html', stocks=stocks, sectors=sectors, selected="All")

@app.route("/sector", methods=["GET", "POST"])
def sector_view():
    sectors = get_all_sectors()
    selected = "all"
    stocks = []

    if request.method == "POST":
        selected = request.form.get("sector", "all")
        stocks = get_stock_by_sector(selected)
    else:
        stocks = get_stock_by_sector("all")

    return render_template("sector.html", sectors=sectors, selected=selected, stocks=stocks)



@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        symbol = request.form['symbol']
        data = get_stock_details(symbol)
        return render_template('search.html', data=data)
    return render_template('search.html')

@app.route('/export', methods=['POST'])
def export():
    data = request.json.get('data')
    filename = export_to_excel(data)
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
