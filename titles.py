import glob
import json
jsons = glob.glob('./netflix-[0-9]*.json')

json_gen = (json.load(open(json_file)) for json_file in jsons)
grouped_titles = [ ["%s (%s)" % (x["title"],x["year"]) for x in json_data["data"]] for json_data in json_gen ]
titles = [ title for group in grouped_titles for title in group]

print(u"\n".join(titles))
