import os
import json


def process_jsonl_files(input_folder, output_folder, languages_of_interest):
    # Create dictionaries to store data for each language and set
    language_data = {lang: {'train': [], 'test': [], 'dev': []} for lang in languages_of_interest}

    # Create a dictionary to store translations from English to other languages for the train set
    translations = {'en_to_xx': {'id': [], 'utt': []}}

    # Loop through JSONL files in the folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".jsonl"):
            with open(os.path.join(input_folder, filename), 'r', encoding='utf-8') as file:
                for line in file:
                    data = json.loads(line)
                    language = data.get('locale')
                    set_type = data.get('partition')

                    # Filter for languages of interest and set types
                    if language in languages_of_interest:
                        if set_type in ['train', 'test', 'dev']:
                            language_data[language][set_type].append(data)

                            # Extract translations from English to other languages for the train set
                            if language == 'en-US' and set_type == 'train':
                                translations['en_to_xx']['id'].append(data['id'])
                                translations['en_to_xx']['utt'].append(data['utt'])

    # Create a large JSON file for translations from English to other languages for the train set
    large_json_filename = os.path.join(output_folder, 'en_to_xx_large.json')
    with open(large_json_filename, 'w', encoding='utf-8') as large_json_file:
        json.dump(translations, large_json_file, ensure_ascii=False, indent=2)
    print(f'Large JSON file {large_json_filename} created.')


base_directory = os.path.dirname(os.path.abspath(__file__))  # Use __file__ to get the script's location
jsonl_input_folder = os.path.join(base_directory, '..', 'data')
json_output_folder = os.path.join(base_directory, '..', 'outputs')

lang_of_interest = ['en-US', 'sw-KE', 'de-DE']
process_jsonl_files(jsonl_input_folder, json_output_folder, lang_of_interest)
