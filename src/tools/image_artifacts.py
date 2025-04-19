import google.genai.types as types
from google.adk.agents.callback_context import CallbackContext

def load_local_image_artifact(image_path: str, context: CallbackContext):
    try:
        # Read the image file
        with open(image_path, 'rb') as f:
            image_bytes = f.read()

        image_artifact = types.Part.from_bytes(
            data=image_bytes,
            mime_type="image/jpeg",  # Assumes JPEG, adjust if needed
        )
        filename = 'bird.jpg'

        version = context.save_artifact(
            filename=filename,
            artifact=image_artifact,
        )
        print(f"Successfully saved artifact '{filename}' as version {version}.")
    except Exception as e:
        raise Exception(f"Error loading image artifact: {str(e)}")


load_local_image_artifact('src/tools/bird.jpg', None)
