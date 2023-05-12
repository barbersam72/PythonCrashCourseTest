import os

def rename_files():
    directory = 'data'  # Specify the directory containing the files
    files = os.listdir(directory)
    
    for filename in files:
        if filename.startswith('HL_') and filename.endswith('.txt'):
            day = filename[3:6]
            ordinal = get_ordinal(day.lower())
            new_filename = filename.replace(day, ordinal)
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f'Renamed file: {filename} -> {new_filename}')

def get_ordinal(day):
    weekdays = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    ordinals = ['01', '02', '03', '04', '05', '06', '07']
    
    if day in weekdays:
        return ordinals[weekdays.index(day)]
    else:
        return day

rename_files()