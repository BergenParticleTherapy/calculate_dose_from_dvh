import glob
import pandas as pd
from module.parse_file import parse_file

files = glob.glob("data/*.txt")
out_dict = {"Patient name": list(), "Justering": list()}

for file in files: 
    justering = "justering" in file.lower()
    patient = parse_file(file)

    for structure in patient.structures:
        d = structure.get_dict()
        out_dict["Patient name"].append(patient.name)
        out_dict["Justering"].append(justering)

        for k,v in structure.get_dict().items():
            if not k in out_dict:
                out_dict[k] = list()
            
            out_dict[k].append(v)          

df = pd.DataFrame(out_dict)
df.to_excel("results/dose_data.xlsx", index=False)