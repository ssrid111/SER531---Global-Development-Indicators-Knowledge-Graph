# SER531 - Global Development Indicators Knowledge Graph

A complete working knowledge graph system with RDF generation, SPARQL querying, and web interface.

## Project Structure

```
project/
│── backend/
│     └── app.py                  # Python backend (Flask)
│── data/
│     └── Final Data.csv          # CSV data
│── rdf/
│     └── generate_sdg_rdf.py     # Python script to convert CSV to RDF
│── frontend/
│     └── index.html              # Web UI for SPARQL queries
│── requirements.txt              # Python dependencies
```

## Features

- **Data Cleaning + RDF Generation** - Convert CSV/JSON to RDF triples
- **Fuseki Integration** - Load and query RDF data via Apache Jena Fuseki
- **SPARQL Query Execution** - Execute queries through REST API
- **Backend API** -  Python (Flask) 
- **Frontend UI** - Interactive web interface for running queries

## Quick Start
1. **Install dependencies:**
    - Windows
   ```bash 
   pip install -r requirements.txt
   ````
    - MacOS
   ```bash 
   pip3 install -r requirements.txt
   ````

2. **Start Fuseki:**
   Install [Fuseki](https://jena.apache.org/documentation/fuseki2/#download-fuseki)
   Run Fuseki server
   ```bash
   ./fuseki-server
   ```
   Then upload `rdf/output.ttl` at `http://localhost:3030`
   
### Note: ttl HAS to be name rdf/output.ttl

3. **Start backend** (choose one):
   - Windows
   ```bash 
   cd backend
   python app.py
   ````
    - MacOS
   ```bash 
   cd backend
   python3 app.py
   ````

4. **Open frontend:** Open `frontend/index.html` in your browser

## Note

This implementation provides everything **except the ontology**. You can plug in your own ontology later and everything will work seamlessly.

## Changes made to the overall design after Deliverable 2 submission

- We introduced observation pattern to the ontology to handle multi-literal values
- Changed the application development phase of the implementation plan