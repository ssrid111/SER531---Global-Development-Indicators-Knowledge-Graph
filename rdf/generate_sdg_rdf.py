import csv
import os
from rdflib import Graph, Namespace, URIRef, Literal, RDF, XSD

# Get the project root directory
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)

# Namespaces
SDG = Namespace("http://example.org/sdg/")
GDI = Namespace("http://example.org/gdi/")

g = Graph()
g.bind("sdg", SDG)
g.bind("gdi", GDI)

# Load CSV
csv_path = os.path.join(project_root, "data", "Final Data.csv")
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        # Create URI for indicator
        ind_code = row['IndCode'].strip()
        indicator_uri = URIRef(f"http://example.org/sdg/indicator/{ind_code}")
        
        # Indicator type
        g.add((indicator_uri, RDF.type, SDG.Indicator))
        
        # Basic properties
        g.add((indicator_uri, SDG.indicatorCode, Literal(ind_code)))
        g.add((indicator_uri, SDG.indicatorName, Literal(row['Indicator'])))
        g.add((indicator_uri, SDG.sdgNumber, Literal(int(row['SDG']), datatype=XSD.integer)))
        
        # Coverage flags
        if row.get('Global', '').lower() == 'yes':
            g.add((indicator_uri, SDG.hasGlobalCoverage, Literal(True, datatype=XSD.boolean)))
        if row.get('OECD', '').lower() == 'yes':
            g.add((indicator_uri, SDG.hasOECDCoverage, Literal(True, datatype=XSD.boolean)))
        if row.get('Spillover', '').lower() == 'yes':
            g.add((indicator_uri, SDG.hasSpillover, Literal(True, datatype=XSD.boolean)))
        
        # Trend flags
        if row.get('Trend_Global', '').lower() == 'yes':
            g.add((indicator_uri, SDG.hasGlobalTrend, Literal(True, datatype=XSD.boolean)))
        if row.get('Trend_OECD', '').lower() == 'yes':
            g.add((indicator_uri, SDG.hasOECDTrend, Literal(True, datatype=XSD.boolean)))
        
        # Years
        if row.get('Years used'):
            g.add((indicator_uri, SDG.yearsUsed, Literal(row['Years used'])))
        if row.get('Reference year'):
            try:
                ref_year = int(row['Reference year'])
                g.add((indicator_uri, SDG.referenceYear, Literal(ref_year, datatype=XSD.gYear)))
            except ValueError:
                g.add((indicator_uri, SDG.referenceYear, Literal(row['Reference year'])))
        
        # Thresholds (convert to numbers if possible)
        thresholds = ['Optimum (= 100)', 'Green threshold', 'Red threshold', 'Lower Bound (=0)']
        threshold_props = [SDG.optimum, SDG.greenThreshold, SDG.redThreshold, SDG.lowerBound]
        
        for threshold_col, prop in zip(thresholds, threshold_props):
            if row.get(threshold_col):
                try:
                    val = float(row[threshold_col])
                    g.add((indicator_uri, prop, Literal(val, datatype=XSD.double)))
                except ValueError:
                    g.add((indicator_uri, prop, Literal(row[threshold_col])))
        
        # Metadata
        if row.get('Justification for Optimum'):
            g.add((indicator_uri, SDG.optimumJustification, Literal(row['Justification for Optimum'])))
        if row.get('Source'):
            g.add((indicator_uri, SDG.source, Literal(row['Source'])))
        if row.get('Description'):
            g.add((indicator_uri, SDG.description, Literal(row['Description'])))
        if row.get('Dwldlink'):
            link = row['Dwldlink'].strip()
            # Only use URIRef if it's a valid URL, otherwise use Literal
            if link and (link.startswith('http://') or link.startswith('https://')):
                try:
                    g.add((indicator_uri, SDG.downloadLink, URIRef(link)))
                except:
                    g.add((indicator_uri, SDG.downloadLink, Literal(link)))
            elif link:
                g.add((indicator_uri, SDG.downloadLink, Literal(link)))
        if row.get('Imputation'):
            g.add((indicator_uri, SDG.imputation, Literal(row['Imputation'])))

# Save RDF file
output_path = os.path.join(script_dir, "sdg_output.ttl")
g.serialize(output_path, format="turtle")
print(f"RDF created -> {output_path}")
print(f"Total triples: {len(g)}")
print(f"Total indicators: {len(set(g.subjects(RDF.type, SDG.Indicator)))}")

