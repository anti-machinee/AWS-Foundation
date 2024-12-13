import pandas as pd

from br_initialize import *


def list_models():
    response = bedrock.list_foundation_models()
    model_summaries = response['modelSummaries']
    df_models = pd.DataFrame(model_summaries)
    print(df_models.describe())
    print(df_models)
    print(df_models["modelId"])


if __name__ == '__main__':
    list_models()
