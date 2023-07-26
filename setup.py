from setuptools import setup,find_packages

def get_requirements():
    requirement_list = []
    file_path = 'requirements.txt'
    with open(file_path) as file:
        requirement_list = file.readlines()
        requirement_list = [require.replace('\n', '') for require in requirement_list]

        if '- e.' in requirement_list:
            requirement_list.remove('- e.')
    return requirement_list
        


setup(
    name='x-ray-disease-detection',
    version='1.0.0',
    author='Rajan Devkota',
    author_email='r.devkota.98@gmail.com',
    package= find_packages(),
    install_require = get_requirements())
