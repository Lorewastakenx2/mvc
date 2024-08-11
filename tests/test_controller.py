
from architecture.mvc.controller import Controller

import logging



if __name__ == '__main__':

    logging.basicConfig(
        level=logging.DEBUG, 
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    )


    App: Controller = Controller()

    level1 = Controller()
    level2 = Controller()

    App.register_controllable(controllable=level1)
    level1.register_controllable(controllable=level2)

    App.register_event('toplevel', lambda: None)
    level1.register_event('level1', lambda: None)

    level2.dispatch_event('level1')
    level2.dispatch_event('toplevel')

    level1.dispatch_event('toplevel')
    
    level1.dispatch_event('random event')
    

    print('... done')