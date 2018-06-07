from flask import Flask, jsonify
from flask_cors import CORS
from companyupdater import CompanyUpdater

# Initialize the Flask app.
application = Flask(__name__)

# Only allow requests from React app.
CORS(application, resources={r"/*": {"origins": "*"}})

# Update interval is 5 minutes.
# 5 minutes to seconds is 5 * 60 = 300.
companyUpdater = CompanyUpdater(interval=300)

# Sanity check.
@application.route('/')
def index():
    return 'We are live.'

# Add error handling and 404.
@application.route('/companies', methods=['GET'])
def companies():
    companies = companyUpdater.companies
    return jsonify({'data': companies})

# Add error handling and 404.
@application.route('/symbol/<string:symbol>', methods=['GET'])
def symbol(symbol):
    try:
        company = next(company for company in companyUpdater.companies if company['symbol'] == symbol)
        return jsonify({'data': company})
    except:
        return 'No Symbol: ' + symbol, 404

if __name__ == '__main__':
    application.run(threaded=True)
