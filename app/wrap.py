#!/usr/bin/env python3
# This file was generated by WRAP
import os
import shutil
import subprocess
import sys
from enum import Enum
from os import getenv, environ, listdir, system
from os.path import splitext, isdir
from pathlib import Path
from shutil import which
from time import sleep


class shell(Enum):
    false = "False"
    zsh = "zsh"
    bash = "bash"
    fish = "fish"

    def __str__(self):
        return self.value


class wrap:

    @staticmethod
    def install(wrap_folder: str = "~/.wrap", install_to_shell: shell = shell.zsh.value, install_examples: bool = True):
        """
        Installs a default configuration for wrap using the base processors
        and some sensible defaults (wrap can be used without this)
        also imports examples
        :param install_to_shell: the shell to install to
        """
        # create wrap folder
        wrap_folder_path = Path(wrap_folder).expanduser().resolve()
        wrap_folder_path.mkdir(parents=True, exist_ok=True)
        # Path(f"{wrap_folder_path}/input").mkdir(parents=True, exist_ok=True)
        Path(f"{wrap_folder_path}/output").mkdir(parents=True, exist_ok=True)

        # Install examples
        if install_examples:
            shutil.copytree(__file__.replace(__file__.split("/")[-1], "examples"), f"{wrap_folder_path}/input",
                            dirs_exist_ok=True,
                            ignore=shutil.ignore_patterns("*.pyc", "__pycache__"))

        if install_to_shell == shell.zsh:
            zshrc_path = Path("~/.zshrc").expanduser().resolve()
            wrap_script = f'\n# wrap\nexport PATH="{wrap_folder_path}/output:$PATH"' \
                          f'\nwrap gen # uses defaults, run wrap gen --help for more info\n'
            with open(zshrc_path, "r+") as f:
                if wrap_script not in f.read():
                    f.write(wrap_script)

    @staticmethod
    def gen(
            input_path: str = str(Path("~/.wrap/input").expanduser().resolve()),
            output_path: str = str(Path("~/.wrap/output").expanduser().resolve()),
            processor_path: str = __file__.replace("wrap.py", "generic_typer_processor.py"),
            clean_output_path: bool = True,
            debug_mode: bool = False,
    ):
        """
        The main function of wrap, this will process all files in the input path using the processors in the
        processor path and output the results to the output path
        """
        try:
            flat_file_list = [Path(f"{path}/{file}") for path in input_path.split(":") for file in listdir(path)]
            flat_loader_list = [Path(path) for path in processor_path.split(":") if not isdir(path)]
            flat_loader_list += [Path(f"{path}/{file}") for path in processor_path.split(":") for file in
                                 (listdir(path) if isdir(path) else [])]
            print(flat_file_list) if debug_mode else None
            print(flat_loader_list) if debug_mode else None
        except FileNotFoundError:
            raise FileNotFoundError("Input path or processor path not found")

        # map the loaders to the files based on the file name
        # file format is <name>.<source_format>_<target_format>.<extension>
        for loader in flat_loader_list:
            # parse get resut as utf-8 string

            print(subprocess.check_output([f"{loader}", "get-input-formats"]).decode(sys.stdout.encoding).strip())

        try:
            loader_map = {
                file: loader for file in flat_file_list
                for loader in flat_loader_list if
                loader.name != "__pycache__" and file.name.split(".")[-1] == subprocess.check_output(
                    [f"{loader}", "get-input-formats"]).decode(sys.stdout.encoding).strip()
                # file extension matches loader source format
            }
        except:
            raise Exception(
                "Invalid file or loader name, please make sure to use the format <name>.<source_format>_<target_format>.<extension>")
        print(loader_map) if debug_mode else None
        # clean output path
        if clean_output_path:
            print("Cleaning old files") if debug_mode else None
            system(f"rm {output_path}/* 2> /dev/null || true")
            # sleep(1)

        # run the loaders on the files
        print(f"Map of files to processors: {loader_map}")
        for file, loader in loader_map.items():
            print(f"Running {loader} on {file}") if debug_mode else None
            system(f"chmod +x {loader} || true")
            # print(f"{loader} gen {file} {output_path} {'--debug_mode' if debug_mode else ''}")
            system(f"{loader} gen {file} {output_path} {'--debug_mode' if debug_mode else ''}")