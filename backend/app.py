from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from SPARQLWrapper import SPARQLWrapper, JSON
import os

# Get the project root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
frontend_dir = os.path.join(project_root, 'frontend')

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route("/api/runQuery", methods=["POST"])
def run_query():
    try:
        # Get query from request
        if request.is_json:
            user_query = request.json.get("query")
        else:
            user_query = request.form.get("query")
        
        if not user_query:
            return jsonify({"error": "No query provided"}), 400
        
        # Execute SPARQL query
        # Note: Dataset name must be exactly "dataset" (lowercase)
        sparql = SPARQLWrapper("http://localhost:7200/repositories/SER531_Project_Final_GDIKG")
        sparql.setQuery(user_query)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def index():
    # Serve the frontend HTML file
    return send_from_directory(frontend_dir, 'index.html')

if __name__ == "__main__":
    print("Starting Flask server...")
    print(f"Frontend directory: {frontend_dir}")
    print("Open http://localhost:5000 in your browser")
    app.run(port=5000, debug=True)
