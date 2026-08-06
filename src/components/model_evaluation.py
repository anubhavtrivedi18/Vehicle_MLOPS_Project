from src.entity.config_entity import ModelEvaluationConfig
from src.entity.artifact_entity import ModelTrainerArtifact, DataIngestionArtifact, ModelEvaluationArtifact
from sklearn.metrics import f1_score
from src.exception import MyException
from src.constant import TARGET_COLUMN
from src.logger import logging
from src.utils.main_utils import load_object
import sys
import pandas as pd
from typing import Optional
from src.entity.s3_estimators import Proj1Estimator
from dataclasses import dataclass


@dataclass
class EvaluatedmodelResponse:
    trained_model_f1_score: float
    best_model_f1_score: float
    is_model_accepted = bool
    difference: float

class ModelEvaluation:
    
