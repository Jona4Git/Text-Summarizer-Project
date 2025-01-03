from dataclasses import dataclass
from pathlib import Path

# Entity for data ingestion
@dataclass(frozen=True)
class DataIngestionConfig: 
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

# Entity for data validation
@dataclass(frozen= True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list
