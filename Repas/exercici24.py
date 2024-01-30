import json

def llegir_json_i_mostrar():
    with open("llibres.json", "r") as json_file:
        dades_json = json.load(json_file)

    json_string = json.dumps(dades_json, indent=2)

    print(json_string)

llegir_json_i_mostrar()
