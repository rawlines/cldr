# type: ignore

import json
import zoneinfo
import xml.etree.ElementTree as ET

file = "./common/bcp47/timezone_es.xml"

tree = ET.parse(file)
root = tree.find(".//key")
iter = root.iter("type")

timezones = zoneinfo.available_timezones()

arr = []

for elem in iter:
    name = elem.attrib.get("name")
    descr = elem.attrib.get("description")
    alias = elem.attrib.get("alias")
    iana = elem.attrib.get("iana")
    
    splt = alias.split(" ")
    if len(splt) > 1 and iana is None:
        iana = splt[0]
    elif iana is None:
        iana = alias
        
    if iana not in timezones:
        print(f"pene: {name} {descr} {alias} {iana}")
        
    arr.append({
        "name": name,
        "description": descr,
        "alias": alias,
        "iana": iana
    })
    
with open("./generated/timezones_iana_map_es.json", "w") as f:
    json.dump(arr, f, indent=4)
