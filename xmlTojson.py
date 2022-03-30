import json
import xmltodict

with open('xml.xml') as xml_file:
    parsed_data = xmltodict.parse(xml_file.read())

    xml_file.close()

    json_conversion = json.dumps(parsed_data)

    with open('output.json', 'w') as json_file:
        json_file.write(json_conversion)

        json_file.close()