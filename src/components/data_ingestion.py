import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

# Define a data class to store the file paths for the data ingestion process
@dataclass
class DataIngestionConfig:
    # Paths where train, test, and raw data files will be stored
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

# Class responsible for data ingestion
class DataIngestion:
    def __init__(self):
        # Initialize DataIngestionConfig to set up file paths
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        # Log the start of the data ingestion process
        logging.info("Entered the data ingestion method or component")
        try:
            # Read data from a CSV file into a pandas DataFrame
            df = pd.read_csv('notebook\data\stud.csv')  # Can read it from any data sources i.e API's or data basses.
            logging.info('Read the dataset as dataframe')

            # In simpler terms, this part of the code is getting the directory 'artifacts' from the full path 'artifacts/train.csv' then making 'artifacts' directory.
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save the raw data to the specified path
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Log that the train-test split process is starting
            logging.info("Train test split initiated")

            # Split the data into training and testing sets (80% train, 20% test)
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save the training set to the specified path
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            # Save the testing set to the specified path
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            # Log the completion of the data ingestion process
            logging.info("Ingestion of the data is completed")

            # Return the paths of the train and test data
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            # If any exception occurs, raise a custom exception with the original exception and system info
            raise CustomException(e, sys)

# Main block to execute the data ingestion, transformation, and model training
if __name__ == "__main__":
    # Create an instance of DataIngestion class
    obj = DataIngestion()

    # Initiate data ingestion process and obtain paths for train and test data
    train_data, test_data = obj.initiate_data_ingestion()

    # Create an instance of DataTransformation class
    data_transformation = DataTransformation()

    # Transform the data and obtain arrays for train and test data
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
