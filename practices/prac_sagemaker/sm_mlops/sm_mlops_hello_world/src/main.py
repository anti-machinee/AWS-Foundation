import sys
sys.path.append(".")
from utils.helper_load import load_config
from sm_pipeline.sm_pipeline import SMPipeline

def main():
    config = load_config("configs/config_sm_pipeline.yaml")
    sm_pipeline = SMPipeline(config).create_pipeline()


if __name__ == "__main__":
    main()
