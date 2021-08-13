#!/usr/bin/python

import logging

def findem(logger):
    print()
    for x in dir(logger):
      print('logger.'+x)

def showem(logger):
    print()
    print('            addFilter:', logger.addFilter)
    print('           addHandler:', logger.addHandler)
    print('         callHandlers:', logger.callHandlers)
    print('             critical:', logger.critical)
    print('                debug:', logger.debug)
    print('             disabled:', logger.disabled)
    print('                error:', logger.error)
    print('            exception:', logger.exception)
    print('                fatal:', logger.fatal)
    print('               filter:', logger.filter)
    print('              filters:', logger.filters)
    print('           findCaller:', logger.findCaller)
    print('             getChild:', logger.getChild)
    print('    getEffectiveLevel:', logger.getEffectiveLevel)
    print('               handle:', logger.handle)
    print('             handlers:', logger.handlers)
    print('          hasHandlers:', logger.hasHandlers)
    print('                 info:', logger.info)
    print('         isEnabledFor:', logger.isEnabledFor)
    print('                level:', logger.level)
    print('                  log:', logger.log)
    print('           makeRecord:', logger.makeRecord)
    print('              manager:', logger.manager)
    print('                 name:', logger.name)
    print('               parent:', logger.parent)
    print('            propagate:', logger.propagate)
    print('         removeFilter:', logger.removeFilter)
    print('        removeHandler:', logger.removeHandler)
    print('                 root:', logger.root)
    print('             setLevel:', logger.setLevel)
    print('                 warn:', logger.warn)
    print('              warning:', logger.warning)

fname = 'bogus.txt'
logging.basicConfig(filename=fname, level=logging.INFO, filemode='w', format='[%(asctime)s  %(name)s %(funcName)-27.27s %(levelname)5.5s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

mainlogger = logging.getLogger(__name__)
mainlogger.setLevel(logging.DEBUG)
mainlogger.info('abc')
mainlogger.debug('def')
findem(mainlogger)
showem(mainlogger)

otherlogger = logging.getLogger('other')
otherlogger.setLevel(logging.INFO)
otherlogger.info('abc')
otherlogger.debug('def')
findem(otherlogger)
showem(otherlogger)

