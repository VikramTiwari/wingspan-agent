import os

import pandas as pd

from enum import Enum


class NestType(Enum):
    PLATFORM = "Platform"
    CAVITY = "Cavity"
    GROUND = "Ground"
    BOWL = "Bowl"
    WILD = "Wild"
    NONE = "None"

bird_not_found = {
    "common_name": "Bird not found",
    "scientific_name": "Bird not found",
    "nest_type": NestType.NONE.value,
    "wingspan": 0,
}

def load_wingspan_db() -> dict:
    """Loads the wingspan.csv file into a dictionary format matching mock_birds_db structure.

    Returns:
        dict: Dictionary with bird data where keys are normalized bird names
    """
    try:
        # Get the directory of the current file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(current_dir, "wingspan.csv")

        # Read CSV into DataFrame
        df = pd.read_csv(csv_path)

        # Convert DataFrame to dictionary format
        birds_dict = {}
        for _, row in df.iterrows():
            normalized_name = row['common_name'].lower().strip().replace(" ", "_")
            birds_dict[normalized_name] = {
                "common_name": row['common_name'],
                "scientific_name": row['scientific_name'],
                "nest_type": row['nest_type'],
                "wingspan": row['wingspan']
            }

        return birds_dict
    except Exception as e:
        print(f"Error loading wingspan database: {str(e)}")
        return {}

# Load the database when module is imported
mock_birds_db = load_wingspan_db()


def get_bird(bird_name: str) -> dict:
    """Retrieves facts about a specific bird from the database.

    Args:
        bird_name (str): The name of the bird

    Returns:
        dict: A dictionary containing the bird information. Keys are:
            common_name: string
            scientific_name: string
            nest_type: string
    """
    try:
        print(f"--- Tool: get_bird called for bird: {bird_name} ---") # Log tool execution
        bird_normalized = bird_name.lower().strip().replace(" ", "_") # Basic normalization
        print(f"Normalized bird name: {bird_normalized}") # Log normalized bird name

        bird = bird_not_found

        if bird_normalized in mock_birds_db:
            bird = mock_birds_db[bird_normalized]

        # print(f"Bird found: {bird}", type(bird)) # Log found bird information

        return bird
    except Exception as e:
        print(f"Error in get_bird function: {str(e)}")
        return bird_not_found
