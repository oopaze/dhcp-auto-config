from typing import Dict, List


def dict_to_csv(values: Dict[str, any]):
    string_dict = ""

    for _, value in values.items():
        string_dict += f"{value},"

    return string_dict[0:-1] + "\n"


def list_to_csv(values: List[any]):
    csv = ""

    for item in values:
        if isinstance(item, dict):
            csv += dict_to_csv(item)
        else:
            csv += f"{item}\n"

    return csv
