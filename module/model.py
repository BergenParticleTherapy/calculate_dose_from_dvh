
from typing import List

class Structure:
    name: str
    delin_style: str
    volume_cc: str
    min_dose_gy: float
    mean_dose_gy: float
    median_dose_gy: float
    max_dose_gy: float

    def get_dict(self):
        return {
            "Structure name": self.name,
            "Delineation type": self.delin_style,
            "Volume [cc]": self.volume_cc,
            "Min dose [Gy]": self.min_dose_gy,
            "Mean dose [Gy]": self.mean_dose_gy,
            "Median dose [Gy]": self.median_dose_gy,
            "Max dose [Gy]": self.max_dose_gy
        }


class Patient:
    name: str
    total_dose: float
    structures: List[Structure] = list()