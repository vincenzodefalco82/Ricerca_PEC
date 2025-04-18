import os
import csv
from flask import Flask, render_template, request
import requests
import pandas as pd
import urllib.parse
from dotenv import load_dotenv

load_dotenv()  # carica le variabili da .env

API_BASE_URL = os.getenv('API_BASE_URL')
API_KEY      = os.getenv('API_KEY')

app = Flask(__name__)

# ROUTE per la pagina iniziale con i due form
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# ROUTE per il singolo lookup
@app.route('/get_pec', methods=['POST'])
def get_pec():
    vat = request.form.get('vat').strip()
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    url = f"{API_BASE_URL}/IT-pec/{vat}"
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        data = resp.json().get('data')
        pec = data[0].get('pec') if data else ''
        return render_template('result.html', vat=vat, pec=pec)
    else:
        err = resp.json().get('message', 'Errore sconosciuto')
        return render_template('result.html', vat=vat, error=err)

# ROUTE per il caricamento massivo con debug
@app.route('/bulk_upload', methods=['POST'])
def bulk_upload():
    # Legge il file Excel caricato
    file = request.files['file']
    df = pd.read_excel(file)
    if df.shape[1] < 1:
        return "Il file deve avere almeno una colonna con le P.IVA", 400

    # Prepara le P.IVA e Ragione Sociale
    vats = (
        df.iloc[:, 0]
          .astype(str)
          .str.strip()
          .str.replace(r'\.0$','', regex=True)
          .str.zfill(11)
    )
    if df.shape[1] > 1:
        ragioni = df.iloc[:, 1].astype(str).str.strip().fillna('')
    else:
        ragioni = pd.Series([''] * len(df), index=df.index)

    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }

    # Prepara il log su file CSV
    log_path = os.path.join(os.getcwd(), 'results.csv')
    file_exists = os.path.exists(log_path)
    f = open(log_path, 'a', newline='', encoding='utf-8')
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(['vat', 'ragione', 'pec'])

    results = []
    for vat, ragione in zip(vats, ragioni):
        url = f"{API_BASE_URL}/IT-pec/{vat}"
        resp = requests.get(url, headers=headers)
        # DEBUG: stampa lo status e il body
        print(f"[DEBUG] VAT={vat} → status={resp.status_code}, text={resp.text}")
        if resp.status_code == 200:
            data = resp.json().get('data')
            pec = data[0].get('pec') if data else ''
        else:
            pec = ''
        writer.writerow([vat, ragione, pec])
        results.append({'vat': vat, 'ragione': ragione, 'pec': pec})

    f.close()

    # Prepara CSV scaricabile in pagina
    df_out = pd.DataFrame(results, columns=['vat','ragione','pec'])
    csv_str = df_out.to_csv(index=False)
    csv_uri = "data:text/csv;charset=utf-8," + urllib.parse.quote(csv_str)

    return render_template('result_bulk.html',
                           results=results,
                           csv_uri=csv_uri)

# MAIN GUARD per avviare il server
if __name__ == '__main__':
    app.run(debug=True)
