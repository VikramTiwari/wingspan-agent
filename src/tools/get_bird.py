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
    "nest_type": NestType.NONE.value
}

mock_birds_db = {
    "american_avocet": {
        "common_name": "American Avocet",
        "scientific_name": "Recurvirostra americana",
        "nest_type": NestType.GROUND.value
    },
    "galah": {
        "common_name": "Galah",
        "scientific_name": "Eolophus roseicapilla",
        "nest_type": NestType.CAVITY.value
    },
    "wild_turkey": {
        "common_name": "Wild Turkey",
        "scientific_name": "Meleagris gallopavo",
        "nest_type": NestType.GROUND.value
    },
}

def get_bird(bird_name: str) -> dict:
    """Retrieves facts about a specific bird from the database.

    Args:
        bird_name (str): The name of the bird (e.g., "American Avocet", "Galah", "Wild Turkey").

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
