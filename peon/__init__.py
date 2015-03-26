#coding=utf-8
import argparse
from peon_construct import construct
from peon_server import server
from peon_watcher import watch
from peon_packing import packing
from peon_backup import backup


__version_info__ = ('0', '0', '4')
__version__ = '.'.join(__version_info__)

def command_options():
    # Dev server
    parser = argparse.ArgumentParser(
                    description='Options of run Peon dev server.')
    
    parser.add_argument('-s', '--server', 
                        dest='server',
                        action='store_const',
                        const=True,
                        help='Start Peon dev server.')
    
    parser.add_argument('-p', '--port', 
                        dest='server_port',
                        action='store',
                        type=int,
                        help='Setup Peon dev server port.')

    parser.add_argument('--harp', 
                        dest='harp_server',
                        action='store_const',
                        const=True,
                        help='Start Peon with harp server.')
    
    # Watcher
    parser.add_argument('-w', '--watcher', 
                        dest='watcher',
                        action='store_const',
                        const=True,
                        help='Run Peon watcher for coffee less and jade.')
    
    # Construct
    parser.add_argument('-c', '--construct', 
                        dest='construct',
                        action='store_const',
                        const=True,
                        help='Run Peon construct to build files.')

    parser.add_argument('--init', 
                        dest='construct_action',
                        action='store_const',
                        const='init',
                        help='Run Peon init tasks.')

    parser.add_argument('--release', 
                        dest='construct_action',
                        action='store_const',
                        const='release',
                        help='Run Peon build tasks.')
    
    # Packing
    parser.add_argument('-z', '--zip', 
                        dest='packing',
                        action='store_const',
                        const=True,
                        help='Run Peon packing zip file.')
    
    # Backup
    parser.add_argument('-backup', '--backup', 
                        dest='backup',
                        action='store_const',
                        const=True,
                        help='Run Peon backup files and datas.')
    
    opts, unknown = parser.parse_known_args()

    return opts


def run():
    opts = command_options()
    if opts.watcher:
        watch()
    elif opts.construct:
        construct(opts)
    elif opts.packing:
        packing()
    elif opts.backup:
        backup()
    else:
        server(opts)


if __name__ == '__main__':
    run()