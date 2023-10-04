import arcpy
import json

aprx_path = "C:\\Users\\klaud\\OneDrive\\Dokumenty\\probny.mxd"
mapx_path = "C:\\Users\\klaud\\OneDrive\\Dokumenty\\probny_map.mapx"
map_def = None
aprx = arcpy.mp.ArcGISProject(aprx_path)
for map in aprx.listMaps():
    print("Map: " + map.name)
    map_def = map.getDefinition()  # <-- Get the CIM definition

with open(mapx_path.format(map.name), 'w') as map_file:
    json_mapx_data = json.load(map_file)  # <-- Needed serialize and load mapx as JSON
    json_mapx_data.write(json.dumps(map_def))
