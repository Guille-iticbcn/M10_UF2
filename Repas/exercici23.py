import json

def generar_i_guardar_json():
    llibres = []
    for i in range(1, 5):
        llibre = {
            "book": {
                "title": f"Book_Title_{i}",
                "cover": f"Book_Cover_{i}.jpg",
                "year": 2000 + i,
                "pages": 300 + i * 50
            }
        }
        llibres.append(llibre)

    dades_json = {"books": llibres}

    json_string = json.dumps(dades_json, indent=2)
    print(json_string)

    with open("llibres.json", "w") as json_file:
        json.dump(dades_json, json_file, indent=2)

generar_i_guardar_json()
