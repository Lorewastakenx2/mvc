
import os

FOLDER_NAME = 'tests'


if __name__ == '__main__':
    
    test_dir = os.path.join(os.path.dirname(__file__), FOLDER_NAME)

    for item in os.listdir(test_dir):
        
        if item.endswith('.py'):
            test_name = item.split('.')[0]

            print(f'\n#### RUNNING TEST {test_name} ####\n')

            success = False
            error = None

            try:
                exec(f'import {FOLDER_NAME}.{test_name}')
                success = True
            except Exception as err:
                error = err

            if success:
                print(f'\n#### SUCCESS ####\n')
            else:
                print(f'\n### TEST {test_name} FAILED ###')
                print(f'... due to exception={error}\n')