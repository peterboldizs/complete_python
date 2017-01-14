import logging

logging.basicConfig(
#    filename='ch11.log',
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s:%(message)s',
    datefmt='%Y-%m-%d %I:%M:%S %p'
)

mylist = [1,2,3]
logging.info('Starting to process `mylist` ...')

for pos in range(4):
    try:
        logging.debug('value at position {} is {}'.format(pos, mylist[pos]))
    except IndexError:
        logging.exception('faulty position : {}'.format(pos))

logging.info('done parsing `mylist`')
