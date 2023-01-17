# This script will go over python files in specific paths and generate shell wrappers for all none private functions

from os import getenv, environ, listdir, system

environ[
    "WRAP_FUNCTION_PATH"] = "/Users/kcw/Github/pythonToShellWrapper/functions:/Users/kcw/Github/pythonToShellWrapper/functions2"
environ["WRAP_LOADER_PATH"] = "/Users/kcw/Github/pythonToShellWrapper/loaders"
environ["WRAP_OUTPUT_PATH"] = "/Users/kcw/Github/pythonToShellWrapper/wrappers"

environ['PYTHON_TO_SHELL_PATH'] = getenv('PYTHON_TO_SHELL_PATH', "") + '/Users/kcw/GitHub/pythonToShellWrapper/'
# environ['PATH'] = getenv('PATH') + ':/usr/local/bin'
input_path = getenv("WRAP_FUNCTION_PATH")  # Path to input files
loader_path = getenv("WRAP_LOADER_PATH")  # Path to loaders that will be used to load the input files
output_path = getenv("WRAP_OUTPUT_PATH")  # Path to output shell files to add to path
clean_output_before_gen = getenv("WRAP_CLEAN_OUTPUT_BEFORE_GEN",
                                 "true")  # Clean output path before generating new files
# flat_list = [item for sublist in l for item in sublist]
flat_file_list = [f"{path}/{file}" for path in input_path.split(":") for file in listdir(path)]
flat_loader_list = [f"{path}/{file}" for path in loader_path.split(":") for file in listdir(path)]
print(flat_file_list)
print(flat_loader_list)

# map the loaders to the files
loader_map = {
    file: loader for file in flat_file_list
    for loader in flat_loader_list if file.split("/")[-1].endswith(loader.split("/")[-1].removesuffix(".sh"))}

# run the loaders on the files
for file, loader in loader_map.items():
    print(f"Running {loader} on {file}")
    system(f"{loader} {file} {output_path}")
