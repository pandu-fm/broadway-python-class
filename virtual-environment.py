
"""
virtual-environment.py
This file is used to create a virtual environment 
for the pandas course.

supppose we are working on different projects 
and we want to keep the dependencies for each project separate.
We can create a virtual environment for each project 
and install the dependencies in that environment.

i.e. in project a we will use pandas version 1.0 
and in project b we will use pandas version 2.0.

in that case we will create a virtual environment for project a 
and virtual environment for project b and install the
 required version of pandas in each environment.

suppoe project env_name os project_a env and
project_b env_name is project_b env.

project a we will install pandas 1.0
in project b we will install pandas 2.0
"""

"""
you can run the command pip freeze to see 
the list of installed packages in the current environment.

to install the specific version of the package you can use the command
pip install package_name==version_number
"""

"""
command to create a virtual environment
python -m venv <any env_name that is meaningful>

to activate the virtual environment
on windows
env_name\Scripts\activate

to deactivate the virtual environment
deactivate
"""

"""
project 1 will be based on python 3.8 and project 2 will be based on python 3.10
so we will create two virtual environments for each project
command to create a virtual environment for project 1 using python 3.8
python -m venv project1_env --python=python3.8

command to create a virtual environment for project 2 using python 3.10
python -m venv project2_env --python=python3.10

on windows to install different python version you can use the command
py -3.8 -m venv project1_env
py -3.10 -m venv project2_env
"""