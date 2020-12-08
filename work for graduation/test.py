import read_filepath_module

Path = r'I:\Data\Personal Data\graduation project\SACOL\original_data'
target_str = "MWR"
lists = []
lists = read_filepath_module.read_filepath(Path,target_str)
print(str(lists[0:1]))