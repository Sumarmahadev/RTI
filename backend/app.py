from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from ai import generate_rti_content
from pdfgen import create_pdf

app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rti.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class RTIRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(200))
    issue = db.Column(db.Text)
with app.app_context():
    db.create_all()

# POST API
@app.route('/generate-rti', methods=['POST'])
def generate_rti():
    data = request.json

    name = data.get('name')
    address = data.get('address')
    issue = data.get('issue')

    if not name or not address or not issue:
        return jsonify({"error": "All fields are required"}), 400

    new_request = RTIRequest(name=name, address=address, issue=issue)
    db.session.add(new_request)
    db.session.commit()

  
    summary, letter = generate_rti_content(name, address, issue)
    pdf_file = create_pdf(letter)

    return send_file(pdf_file, as_attachment=True)


@app.route('/requests', methods=['GET'])
def get_requests():
    data = RTIRequest.query.all()
    return jsonify([
        {
            "id": r.id,
            "name": r.name,
            "address": r.address,
            "issue": r.issue
        }
        for r in data
    ])

if __name__ == '__main__':
    app.run(debug=True)