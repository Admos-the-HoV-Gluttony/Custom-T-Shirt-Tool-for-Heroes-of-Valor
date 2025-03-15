import os
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_game_files(game_path):
    exe_subpath = os.path.join("HeroesOfValor", "HeroesOfValor.exe")
    pak_subpath = os.path.join("HeroesOfValor", "Content", "Paks", "HeroesOfValor-WindowsNoEditor.pak")

    exe_path = os.path.join(game_path, exe_subpath)
    pak_path = os.path.join(game_path, pak_subpath)

    logging.info(f"Checking for 'HeroesOfValor.exe' at: {exe_path}")
    logging.info(f"Checking for 'HeroesOfValor-WindowsNoEditor.pak' at: {pak_path}")

    if os.path.exists(exe_path) and os.path.exists(pak_path):
        logging.info("Both 'HeroesOfValor.exe' and 'HeroesOfValor-WindowsNoEditor.pak' have been found.")
    else:
        missing_files = []
        if not os.path.exists(exe_path):
            missing_files.append(f"'{exe_subpath}'")
        if not os.path.exists(pak_path):
            missing_files.append(f"'{pak_subpath}'")
        
        logging.error(f"Missing files: {', '.join(missing_files)}")

def main():
    config_file_path = "data\\config\\settings.json"
    
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

        check_game_files(game_path)
    
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
