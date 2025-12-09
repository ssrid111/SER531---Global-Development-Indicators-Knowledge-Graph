# SER531 - Global Development Indicators Knowledge Graph

A complete working knowledge graph system with RDF generation, SPARQL querying, and web interface.

## 📁 Project Structure

```
project/
│── data/
│     └── cities.csv              # Sample CSV data
│── rdf/
│     └── generate_rdf.py         # Python script to convert CSV to RDF
│     └── output.ttl              # Generated RDF/Turtle file
│     └── SPARQL_QUERIES.md       # Example SPARQL queries
│── frontend/
│     └── index.html              # Web UI for SPARQL queries
│── backend/
│     └── app.py                  # Python backend (Flask)
│── requirements.txt              # Python dependencies
│── SETUP.md                      # Detailed setup instructions
```

## ✨ Features

- ✅ **Data Cleaning + RDF Generation** - Convert CSV/JSON to RDF triples
- ✅ **Fuseki Integration** - Load and query RDF data via Apache Jena Fuseki
- ✅ **SPARQL Query Execution** - Execute queries through REST API
- ✅ **Backend API** -  Python (Flask) 
- ✅ **Frontend UI** - Interactive web interface for running queries

## 🚀 Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Generate RDF:**
   ```bash
   cd rdf
   python generate_rdf.py
   ```

3. **Start Fuseki:**
   ```bash
   ./fuseki-server --update --mem /dataset
   ```
   Then upload `rdf/output.ttl` at `http://localhost:3030`

4. **Start backend** (choose one):
   - Python: `cd backend && python app.py`

5. **Open frontend:** Open `frontend/index.html` in your browser

See `SETUP.md` for detailed instructions.

## 📝 Note

This implementation provides everything **except the ontology**. You can plug in your own ontology later and everything will work seamlessly.