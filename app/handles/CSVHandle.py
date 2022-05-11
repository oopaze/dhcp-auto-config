from typing import Dict, List


def dictToCSV(values: Dict[str, any]):
    string_dict = ""

    for _, value in values.items():
        string_dict += f"{value},"

    return string_dict[0:-1] + "\n"


def listToCSV(values: List[any]):
    csv = ""

    for item in values:
        if isinstance(item, dict):
            csv += dictToCSV(item)
        else:
            csv += f"{item}\n"

    return csv
