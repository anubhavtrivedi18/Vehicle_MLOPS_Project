from src.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    data_ingestion = DataIngestion()

    data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

    print(data_ingestion_artifact)