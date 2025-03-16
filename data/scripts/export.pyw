import os
import json
import logging
import shutil

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def export_game_files(game_path):
    dest_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "game_files")
    
    if not os.path.exists(dest_dir):
        logging.error(f"The destination directory '{dest_dir}' does not exist.")
        return
    
    pak_subpath = os.path.join("HeroesOfValor", "Content", "Paks", "HeroesOfValor-WindowsNoEditor.pak")
    source_pak_path = os.path.join(dest_dir, pak_subpath)
    
    logging.info(f"Checking for 'HeroesOfValor-WindowsNoEditor.pak' at: {source_pak_path}")
    
    if not os.path.exists(source_pak_path):
        missing_files = [f"'{pak_subpath}'"]
        logging.error(f"Missing files: {', '.join(missing_files)}")
        return

    try:
        destination_pak_path = os.path.join(game_path, pak_subpath)
        
        shutil.copy2(source_pak_path, destination_pak_path)
        logging.info(f"Copied: {source_pak_path} to {destination_pak_path}")
        
        logging.info("Game files have been successfully exported back to the original game path.")
    
    except Exception as e:
        logging.error(f"Failed to export files: {e}")

def main():
    config_file_path = "data\\config\\path_to_game_files.json"
    
    if not os.path.exists(config_file_path):
        logging.error(f"The configuration file '{config_file_path}' does not exist.")
        return

    try:
        with open(config_file_path, 'r') as config_file:
            config_data = json.load(config_file)
            game_path = config_data.get("game_path", "").strip()
        
        if not game_path or not os.path.exists(game_path):
            logging.error(f"The specified game path '{game_path}' does not exist.")
            return

        export_game_files(game_path)
    
    except FileNotFoundError:
        logging.error(f"File not found: {config_file_path}")
    except PermissionError:
        logging.error(f"Permission denied for reading the file: {config_file_path}")
    except json.JSONDecodeError as e:
        logging.error(f"Failed to decode JSON from '{config_file_path}': {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
