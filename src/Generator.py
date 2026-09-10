import numpy as np
import pandas as pd
import os
import scipy.io
import argparse

np.set_printoptions(suppress=True, precision=4)

home_path = os.environ.get("HOME")

# 1. Initialize the argument parser
parser = argparse.ArgumentParser(description="A script that accepts a filename as an argument and processes the CSV file.")

# 2. Add an argument (positional or optional)
parser.add_argument("--import_dir", type=str, default=f"{home_path}/Dev/AI-Doktora/Dataset/NASA/", help="Dir of csv data files")

parser.add_argument("--export_dir", type=str, default=f"{home_path}/Dev/AI-Doktora/export/", help="Dir of exported csv files")

parser.add_argument("--metafile", type=str, default=f"metadata.csv", help="Name of the metadata file")

parser.add_argument('--genzip', action=argparse.BooleanOptionalAction, default=False, help="Generate a zip file to keep csv files")

# 3. Parse the command-line arguments
args = parser.parse_args()

# Define the path to CSV file
# (Can be a local file path or a direct web URL)
import_dir = args.import_dir
gen_zip = args.genzip

print("Zip Gen: ", gen_zip)

export_dir = args.export_dir
metafile = f"{export_dir}/{args.metafile}"


print (f"Checking {import_dir}")

# Helper functions
def load_filelist():
    
    FILELIST = []
    for dirname, _, filenames in os.walk(import_dir):
        for filename in filenames:

            #filepath = filename
            FILELIST.append(os.path.join(dirname, filename))
    return FILELIST
            
            
def filter_matfiles_list(filelist):
    filelist = [filepath for filepath in filelist if filepath.endswith('.mat')]
    #filelist = [filepath for filepath in filelist if "BatteryAgingARC_25_26_27_28_P1" not in filepath] # removing duplicates
    return filelist


def loadmat(filepath):
    return scipy.io.loadmat(filepath, simplify_cells=True)

FILELIST = filter_matfiles_list(load_filelist())

for item in FILELIST:
    print(item)

def process_data_dict(data_dict):
    """ Creates two dictionaries:
    - ndict: new dictionary with the test data to build a corresponding dataframe
    - metadata_dict: anything that doesn't fit in ndict ('Capacity' is just a float)
    """
    
    ndict = {}
    metadata_dict = {}
    for k, v in data_dict.items():
        if k not in ['Capacity', 'Re', 'Rct']:
            ndict[k]=v
        elif k == 'Capacity':
            metadata_dict[k]=v
        elif k == 'Re':
            metadata_dict[k]=v
        elif k == 'Rct':
            metadata_dict[k]=v
        else:
            print("c'est la merde")
    
    return ndict, metadata_dict


def fill_metadata_row(metadata, test_type, test_start_time, test_temperature, battery_name, test_id, uid, filename, capacity, re, rct):
    tmp = pd.DataFrame(data=[test_type, test_start_time, test_temperature, battery_name, test_id, uid, filename, capacity, re, rct])
    tmp = tmp.transpose()
    tmp.columns = metadata.columns
    metadata = pd.concat((metadata, tmp), axis=0)
    return metadata


def extract_more_metadata(metadata_dict):
    
    if 'Capacity' in metadata_dict.keys():
        capacity = metadata_dict['Capacity']
    else:
        capacity = np.nan
        
    if 'Re' in metadata_dict.keys():
        re = metadata_dict['Re']
    else:
        re = np.nan
        
    if 'Rct' in metadata_dict.keys():
        rct = metadata_dict['Rct']
    else:
        rct = np.nan
    
    return capacity, re, rct

metadata = pd.DataFrame(data=None, columns=['type', 'start_time', 'ambient_temperature', 'battery_id', 'test_id', 'uid', 'filename', 'Capacity', 'Re', 'Rct'])
battery_list = [item.split('/')[-1].split('.')[0] for item in FILELIST]

uid = 0
# counter = 0
for battery_name, mat_filepath in zip(battery_list, FILELIST):
    # counter +=1
    
    mat_data = scipy.io.loadmat(mat_filepath, simplify_cells=True)
    print(mat_filepath[-10:],"-->", battery_name)
    test_list = mat_data[battery_name]['cycle']
    
    for test_id in range(len(test_list)):
        
        uid += 1
        filename = str(uid).zfill(5)+'.csv'
        filepath = export_dir + filename

        # Extract the specific test data and save it as CSV! 
        ndict, metadata_dict = process_data_dict(test_list[test_id]['data'])
        test_df = pd.DataFrame.from_dict(ndict, orient='index')
        test_df = test_df.transpose()

        test_df.to_csv(filepath, index=False)
                
        # Add test information to the metadata
        test_type = test_list[test_id]['type']
        test_start_time = test_list[test_id]['time']
        test_temperature = test_list[test_id]['ambient_temperature']
        
        capacity, re, rct = extract_more_metadata(metadata_dict)
        metadata = fill_metadata_row(metadata, test_type, test_start_time, test_temperature, battery_name, test_id, uid, filename, capacity, re, rct)
        #print("CHECK TIME: ", test_start_time)
        
    # if counter > 2:
    #    break


metadata.to_csv(metafile, index=False)

metadata.info()

if (gen_zip):
    import shutil
    shutil.make_archive(base_name='data',format='zip', root_dir=export_dir, base_dir=".")