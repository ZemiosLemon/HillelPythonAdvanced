def return_requirements():
    with open('requirements.txt') as file:
        result = file.read()
        return result
