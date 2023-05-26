import math

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/emi', methods=['POST'])
def loan_emi_count():
    data = request.get_json()
    loanAmount = float(data['loanAmount'])
    interestRate = float(data['interestRate'])
    loanDuration = float(data['loanDuration'])
    monthlyInterest = interestRate / 100 / 12
    emiCount = (loanAmount * monthlyInterest * math.pow(1 + monthlyInterest, loanDuration)) / (
            math.pow(1 + monthlyInterest, loanDuration) - 1)
    total_payable_amount = emiCount * loanDuration
    response = {
        'monthly_emi': emiCount,
        'total_payable_amount': total_payable_amount,
        'interest_Rate': interestRate
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
