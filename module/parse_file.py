from module.model import Patient, Structure
import re

def parse(s: str) -> str:
    return s.split(": ")[-1]

def fparse(s: str) -> float:
    return float(parse(s))

def split_name(s: str) -> list:
    match = re.match(r"^([A-Za-z_]*)((?:[1-9]|1[0-9]|\_ART|\_GT))$", s)
    if match:
        return match.group(1), match.group(2)
    else:
        return s, None
    

def parse_file(filename):
    patient = Patient()

    this_structure = None

    with open(filename, "r") as file_in:
        for line in file_in.readlines():        
            if "Patient Name" in line:
                patient.name = parse(line).replace(",","").replace("\n", "")

            if "Total dose [Gy]" in line:
                patient.total_dose = fparse(line)
            
            if "Structure:" in line:
                this_structure = Structure()
                structure_split_name = split_name(parse(line).replace("\n", ""))
                this_structure.name = structure_split_name[0]
                this_structure.delin_style = structure_split_name[1]

            if "Volume [cm" in line:
                this_structure.volume_cc = fparse(line)
            
            if "Min Dose" in line:
                this_structure.min_dose_gy = fparse(line) * patient.total_dose / 100
            
            if "Max Dose" in line:
                this_structure.max_dose_gy = fparse(line) * patient.total_dose / 100

            if "Mean Dose" in line:
                this_structure.mean_dose_gy = fparse(line) * patient.total_dose / 100

            if "Median Dose" in line:
                this_structure.median_dose_gy = fparse(line) * patient.total_dose / 100

            if "RTOG CI" in line:
                patient.structures.append(this_structure)

    return patient