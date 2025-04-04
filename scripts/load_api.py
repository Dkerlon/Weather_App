import requests
from datetime import datetime,timedelta
import json

local_home = {"City":"Niterói","Lat":-22.8808,"Lon":-43.1043}

def fetch_api(lat=local_home['Lat'],log=local_home['Lon']):
    api = f"https://my.meteoblue.com/packages/basic-1h_basic-day?lat={lat}&lon={log}&apikey="
    api_key = "XkOTfVldKi0vnstx"
    request = requests.get(f"{api}{api_key}")

    return request.json()

#Chamadas das API's
_current = fetch_api()
_current_api_location = None

def fetch_api_location(location):
    global _current,_current_api_location
    endpoint = f"https://nominatim.openstreetmap.org/search?q={location}&format=json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"  # Define um User-Agent
    }
    response = requests.get(endpoint, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            _current = fetch_api(data[0]["lat"],data[0]["lon"])
            _current_api_location = data
        except requests.exceptions.JSONDecodeError:
            print("Erro: A resposta da API não está em formato JSON!")
            print("Conteúdo recebido:", response.text)
    else:
        print(f"Erro: Código de status {response.status_code}")
            
def load_api_data():
    return {
    "Temperatura":int(_current["data_day"]["temperature_mean"][today[3]]),
    "Temperatura_max":int(_current["data_day"]["temperature_max"][today[3]]),
    "Temperatura_min":int(_current["data_day"]["temperature_min"][today[3]]),
    "Sensação_termica":int(_current["data_day"]["felttemperature_mean"][today[3]]),
    "Umidade":_current["data_day"]["relativehumidity_mean"][today[3]],
    "Horas":_current["data_1h"]["time"],
    "Umidade_horas":_current['data_1h']['relativehumidity'],
    "Temperatura_horas":_current['data_1h']['temperature'],
    "Pressao": _current['data_day']['sealevelpressure_mean'][today[3]],
    "Pressao_Amanha": _current['data_day']['sealevelpressure_mean'][today[3]+1],
    "Vento_Amanha":_current['data_day']['windspeed_mean'][today[3]+1],
    "Uv_Amanha": _current['data_day']['uvindex'][today[3]+1],
    "Nome": _current_api_location[0]['name'] if _current_api_location else "Niterói",
    "Lat":float(_current_api_location[0]['lat']) if _current_api_location else -22.8808,
    "Lon":float(_current_api_location[0]['lon']) if _current_api_location else -43.1043
}
days_week_PT = {
    "Monday":"Seg",
    "Tuesday":"Ter",
    "Wednesday":"Qua",
    "Thursday":"Qui",
    "Friday":"Sex",
    "Saturday":"Sáb",
    "Sunday":"Dom",
}
days_week = {
    (datetime.today() + timedelta(days=0)).strftime("%Y-m-%d"): [days_week_PT[datetime.now().strftime("%A")],0,24,0],
    (datetime.today() + timedelta(days=1)).strftime("%Y-m-%d"): [days_week_PT[(datetime.today() + timedelta(days=1)).strftime("%A")],25,49,1],
    (datetime.today() + timedelta(days=2)).strftime("%Y-m-%d"): [days_week_PT[(datetime.today() + timedelta(days=2)).strftime("%A")],50,73,2],
    (datetime.today() + timedelta(days=3)).strftime("%Y-m-%d"): [days_week_PT[(datetime.today() + timedelta(days=3)).strftime("%A")],74,97,3],
    (datetime.today() + timedelta(days=4)).strftime("%Y-m-%d"): [days_week_PT[(datetime.today() + timedelta(days=4)).strftime("%A")],98,121,4],
    (datetime.today() + timedelta(days=5)).strftime("%Y-m-%d"): [days_week_PT[(datetime.today() + timedelta(days=5)).strftime("%A")],122,145,5],
    (datetime.today() + timedelta(days=6)).strftime("%Y-m-%d"): [days_week_PT[(datetime.today() + timedelta(days=6)).strftime("%A")],145,169,6],
}
today = days_week[datetime.now().strftime("%Y-m-%d")]
