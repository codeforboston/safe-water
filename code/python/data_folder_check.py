from pprint import pprint
import click 
import os
from collections import namedtuple

SDWIS_FOLDER = [
    'contaminant-codes.csv',
    'contaminant-group-codes.csv',
    'ENFORCEMENT_ACTION.csv',
    'GEOGRAPHIC_AREA.csv',
    'LCR_SAMPLE_RESULT.csv',
    'LCR_SAMPLE.csv',
    'SERVICE_AREA.csv',
    'TREATMENT.csv',
    'VIOLATION_ENF_ASSOC.csv',
    'VIOLATION.csv',
    'WATER_SYSTEM_FACILITY.csv',
    'WATER_SYSTEM.csv'
]

FILE_LIST = ['sdwis/' + fn for fn in SDWIS_FOLDER]

OPTIONAL_FILES = []

###################################################################################################

def compare_files_and_folders(
        files:list=[],
        root_dir:str='',
        optional_files:list=None,
        return_correct=False,
        return_optional=False
    ) -> dict:
    """Compares a root_dir to a list of files (specified by the ``files`` kwarg) and sees what
    files are either missing in the directory (missing files) or are in the directory but not
    listed (extra files).
    
    Note that both ``files`` and ``optional_files`` are a list of relative paths, not just the file
    names. So for example, if the list has "my_file.ext", it will check "$root_dir/my_file.ext".
    But if my_file.ext is actually located at "$root_dir/path/to/my_file.ext", it will be
    considered missing.
    
    Note that this code uses os.path.realpath() and .replace('\\','/') to use consistent
    comparisons of files, e.g. so that "path/to/my_file.ext" is considered equal to
    "path\\to\\my_file.ext".
    
    :param files: List of files to check against
    :param root_dir: The directory being looked at.
    :param optional_files: Files that are not considered extra files but also not required.
    :param return_correct: If true, returns the list of files that are both in the list and also in
                           the root_dir.
    :param return_optional: If true, returns the list of optional files that were found in the
                            root_dir.
    :returns: Dict of lists of files
    """
    required_files = [
        os.path.realpath(os.path.join(root_dir, fn)).replace('\\','/') for fn in files
    ]
    
    # create list of root_dir's contents
    dir_contents = []
    for _root, _dirs, _files in os.walk(root_dir):
        for fn in _files:
            dir_contents.append(
                os.path.realpath(os.path.join(_root, fn)).replace('\\','/')
            )
    
    # comparison of root_dir and files list
    trim_path = lambda s: s[len(os.path.realpath(root_dir).replace('\\','/')):]
    extra_files = [trim_path(fn) for fn in dir_contents if fn not in required_files]
    missing_files = [trim_path(fn) for fn in required_files if fn not in dir_contents]
    correct_files = [trim_path(fn) for fn in required_files if fn in dir_contents]
    
    # remove and record optional files
    optional_files_in_folder = []
    for fn in optional_files:
        if fn in extra_files:
            extra_files.remove(fn)
            optional_files_in_folder.append(fn)
        
    # return the results
    return_dict = {
        'Extra files' : extra_files,
        'Missing files' : missing_files
    }
    
    if return_correct:
        return_dict['Correct files'] = correct_files
    if return_optional:
        return_dict['Optional files'] = optional_files_in_folder
    
    return return_dict

py_file_loc = os.path.dirname(os.path.realpath(__file__))

@click.command()
@click.option('--data_dir',
              default=os.path.join(py_file_loc, '../../data'),
              help="Data directory path.")
@click.option('--files',
              default=FILE_LIST,
              help="File list to compare against what's in data_dir")
@click.option('--optional_files',
              default=OPTIONAL_FILES,
              help="Files that are not considered extra files but also not required.")
@click.option('--return_correct',
              default=False,
              help="Return list of files that match.")
@click.option('--return_optional',
              default=False,
              help="Return list of optional files that were found.")
def cli_run(data_dir, files, optional_files, return_correct, return_optional):
    lists = compare_files_and_folders(files=FILE_LIST,
                                      optional_files=OPTIONAL_FILES,
                                      root_dir=data_dir)
    print('Root dir (input):', data_dir)
    print('Root dir (real):', os.path.realpath(data_dir))
    pprint(lists)

if __name__ == '__main__':
    cli_run()