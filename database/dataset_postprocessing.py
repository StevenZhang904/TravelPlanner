import json

keys_to_remove = ['Phone', 'Website']
with open('database/train_ref_info.jsonl') as f:
    data = [json.loads(line) for line in f]

for x in data:
    for key in x.keys():
        if 'Attractions' not in key:
            pass
        elif 'Attractions' in key:
            attractions = x[key]
            for attraction in attractions:
                attraction_keys = list(attraction.keys())
                for attraction_key in attraction_keys:
                    if attraction_key in keys_to_remove:
                        del attraction[attraction_key]
            x[key] = attractions
        else:
            raise ValueError('Attractions Key not found')

with open('database/train_ref_info_postprocessed.jsonl', 'w') as f:
    for x in data:
        f.write(json.dumps(x) + '\n')