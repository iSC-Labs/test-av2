import os
import sys
import logging

def execute(vm, args):
    """ server side """
    from AVMaster import vm_manager

    logging.debug("    CS Execute")
    assert vm, "null vm"
    assert len(args) == 3 and isinstance(args, list), "PULL expects a list of 3 elements"

    #TODO pull files from vm
    src_files, src_dir, dst_dir = args
    assert isinstance(src_files, list), "PULL expects a list of src files"

    memo = []
    for src_file in src_files:
        print src_file
        try:
            d, f = src_file.split("\\")
        except ValueError:
            d = ""
            f = src_file

        src = "%s\\%s\\%s" % (src_dir, d, f)

        if d == "":
            dst = "%s/%s" % (dst_dir, f)
        else:
            dst = "%s/%s/%s" % (dst_dir, d, f)

        rdir = "%s/%s" % (dst_dir, d)
        if not rdir in memo:
            if not os.path.exists(rdir):
                logging.debug("mkdir %s " % (rdir))
                os.mkdir(rdir)
                memo.append(rdir)

        logging.debug("%s copy %s -> %s" % (vm, src, dst))
        vm_manager.execute(vm, "copyFileFromGuest", src, dst)

    return True, "Files copied from VM"
