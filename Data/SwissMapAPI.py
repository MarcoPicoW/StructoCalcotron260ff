import requests
import json

# Deine LV03 Koordinaten
x = 682290.24
y = 242882.82

# Radius in Metern um den Punkt
radius = 5

# Bounding Box berechnen
xmin = x - radius
ymin = y - radius
xmax = x + radius
ymax = y + radius

# API-Parameter zusammenbauen
params = {
    "geometryType": "esriGeometryEnvelope",
    "geometry": f"{xmin},{ymin},{xmax},{ymax}",
    "sr": 21781,
    "tolerance": 0,
    "mapExtent": "0,0,0,0",
    "imageDisplay": "0,0,0",
    "layers": "all:ch.swisstopo.amtliches-strassenverzeichnis,ch.swisstopo.swisstlm3d-strassen,ch.astra.nationalstrassenachsen,ch.astra.hauptstrassennetz,ch.bav.schienennetz,ch.astra.veloland,ch.astra.mountainbikeland,ch.astra.wanderland,ch.astra.skatingland,ch.astra.winterwanderwege,ch.bfe.elektrische-anlagen_ueber_36,ch.bafu.wasser-leitungen,ch.bafu.wasser-gebietsauslaesse,ch.bafu.wasser-vorfluter,ch.bafu.schutzgebiete-paerke_nationaler_bedeutung,ch.bafu.schutzgebiete-ramsar,ch.bafu.bundesinventare-bln,ch.bafu.waldreservate,ch.bafu.grundwasserkoerper,ch.bafu.bundesinventare-auen,ch.bafu.bundesinventare-flachmoore,ch.bafu.schutzgebiete-smaragd,ch.bafu.gefahren-baugrundklassen,ch.bafu.sturm-boeenspitzen_30",
    "returnGeometry": "false"
}

url = "https://api3.geo.admin.ch/rest/services/api/MapServer/identify"

# Anfrage senden
r = requests.get(url, params=params)
data = r.json()


## Ergebnisse anzeigen
print(json.dumps(data, indent=2, ensure_ascii=False))
