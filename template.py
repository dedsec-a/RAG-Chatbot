# Template file for Creating the Folder Structure
import os

def create_folder_structure(base_dir):
    # Folder structure
    folder_structure = [
        'backend',
        'backend/tests',
        'config',
        'data',
        'data/embeddings'
    ]
    
    # Files in each folder
    files = {
        'backend': [
            '__init__.py',
            'chatbot.py',
            'data_ingestion.py',
            'document_processing.py',
            'event_data.py',
            'query_processing.py',
            'utils.py'
        ],
        'config': [
            '__init__.py',
            'settings.py',
            'api_config.py'
        ],
        'data': [
            'event_schedule.json',
            'faq_data.json'
        ],
        'backend/tests': [
            'test_chatbot.py',
            'test_document_processing.py',
            'test_event_data.py'
        ],
    }
    
    # Create folders and files
    for folder in folder_structure:
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
        if folder in files:
            for file in files[folder]:
                file_path = os.path.join(folder_path, file)
                with open(file_path, 'w') as f:
                    # You can add basic template or comments to each file for now
                    f.write(f"# {file} - Auto-generated template file\n")

    print(f"Folder structure created at {base_dir}")

if __name__ == "__main__":
    # Set the base directory where the folders will be created
    base_dir = 'event-chatbot'
    create_folder_structure(base_dir)
