import pandas as pd
from typing import List, Dict


def process_data(docs: List[Dict]) -> List[Dict]:
    """
    i load here document into a dataframe, and then apply processing, and return json.
    for now i just loads and returns as is.
    """
    if not docs:
        return []

    df = pd.DataFrame(docs)

    # for example transformtion (and replaced later):
    # df["full_name"] = df["first_name"] + " " + df["last_name"]

    return df.to_dict(orient="records")