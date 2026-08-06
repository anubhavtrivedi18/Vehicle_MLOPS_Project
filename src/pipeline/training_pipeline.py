import sys
from src.exception import MyException
from src.logger import logging

from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


from src.entity.config_entity import (DataIngestionConfig,DatavalidationConfig,
                                      DataTransformationConfig,
                                      ModelTrainerConfigure)

from src.entity.artifact_entity import (DataIngestionArtifact,
                                        DataValidationArtifact,
                                        DataTransformationArtifact,
                                        ModelTrainerArtifact
                                        )

class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidation()
        self.data_transformation = DataTransformation()
        self.model_trainer_config = ModelTrainerConfigure()


    def start_data_ingestion(self) -> DataIngestionArtifact:
        """
        This method of Trainpipeline class is responsible for sstarting sta ingestion components
        """

        try:
            logging.info("Entered the start_data_ingestion method of TrainPipeline class")
            logging.info("Getting the data from mongodb")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info("Exited the start_data_ingestion method of TrainPipeline class")
            return data_ingestion_artifact

        except Exception as e:
            raise MyException(e,sys) from e

    def start_validation(self,data_ingestion_artifact: DataIngestionArtifact) -> DataValidationArtifact:
        """
        This method of TrainPipeline class is reponsible for starting data validation components
        """

        logging.info("Entered the start_data_validation method of TrainPipeline class")

        try:
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,
                                             data_validation_config=self.data_validation_config)

            data_validation_artifact = data_validation.intiate_data_validation()
            logging.info("Performed the data validation operation")
            logging.info("Exited the start_data_validation method of TrainPipeline class")


            return data_validation_artifact
        except Exception as e:
            raise MyException(e, sys) from e

    def start_data_transformation(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_artifact: DataValidation) -> DataTransformationArtifact:
        """
        This method of TrainPipeline class is reponsible for starting data transformation component
        """        
        try:
            data_transformation = DataTransformation(data_ingestion_artifact=data_ingestion_artifact,
                                                     data_transformation_config=self.data_transformation,
                                                     data_validation_artifact=data-data_validation_artifact)
            data_transformation_artifact = data_transformation.initiate_data_trnasformation()
            return data_transformation_artifact

        except Exception as e:
            raise MyException(e, sys)




    

































    def run_pipeline(self,)-> None:
        """
        This method of trainingPipeline class is responsible for running complete pipeline
        """

        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact = data_ingestion_artifact)
            data_transformation_artifact = self.start_data_transformation(
                data_ingestion_artifact = data_ingestion_artifact, data_validation_artifact = data_validation_artifact)

            model_trainer_artifact = self.start_model_trainer(data_transformation_artifact = data_transformation_artifact)




            return None
        except Exception as e:
            raise MyException(e,sys)

            