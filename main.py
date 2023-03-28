import json
import os


json_list = []


for filename in sorted(os.listdir('json-folder'), key=lambda x: int(x.split('.')[0])):
    if filename.endswith('.json'):

        with open(os.path.join('json-folder', filename), 'r') as f:
            json_obj = json.load(f)

           
            output_dict = {
                'name': json_obj['name'],
                'description': json_obj['description'],
                'dna': json_obj['dna'],
                'image': json_obj['image'],
                'attributes': json_obj['attributes']
            }

            json_list.append(output_dict)


with open('output.json', 'w') as f:
    json.dump(json_list, f, indent=2)