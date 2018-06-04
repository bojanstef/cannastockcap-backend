from flask import Flask, jsonify
from flask_cors import CORS
from companyupdater import CompanyUpdater

# Initialize the Flask app.
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Update interval is 5 minutes.
# 5 minutes to seconds is 5 * 60 = 300.
companyUpdater = CompanyUpdater(interval=300)

# Sanity check.
@app.route('/')
def index():
    return 'We are live.'

# 2. Add metadata; 'last-updated', 'total-companies', and 'error'.
@app.route('/listings', methods=['GET'])
def listings():
    return jsonify({'data': companyUpdater.companies})

# TODO: - Focus on /listings first. 
# 3. Add metadata; 'last-updated', and 'error'.
# @app.route('/ticker/<int:company_id>')
# def ticker(company_id):
#     company = companyUpdater.companies[company_id-1]
#     return jsonify({'data': company})
