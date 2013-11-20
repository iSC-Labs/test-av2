import os
import sys
import logging

def execute(vm, args):
    """ server side """
    from AVMaster import vm_manager

    logging.debug("    CS Execute REVERT")
    assert vm, "null vm"

    # TODO: check
    vm_manager.execute(vm, "revert_last_snapshot")
    return True, "Reverted VM"


