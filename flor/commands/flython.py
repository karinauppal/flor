import os
import shutil
import importlib
from uuid import uuid4

from flor.versioner.versioner import Versioner
from flor.complete_capture.walker import Walker
from flor.logs_manipulator.open_log import OpenLog


def exec_flython(args):
    # Get path and check
    full_path = os.path.abspath(args.path)
    assert os.path.splitext(os.path.basename(full_path))[1] == '.py'

    # Commit to repo before code transformation
    versioner = Versioner(full_path)
    versioner.save_commit_event("flor commit")

    # Transform code
    walker = Walker(os.path.dirname(full_path))
    walker.compile_tree(lib_code=False) # Transformed code in walker.targetpath

    # Overwrite current directory
    current_dir = os.getcwd()
    os.chdir(os.path.dirname(os.path.dirname(full_path)))
    shutil.rmtree(os.path.dirname(full_path))
    shutil.copytree(walker.targetpath, os.path.dirname(full_path))
    os.chdir(current_dir)

    # Model OpenLog Behavior
    ol = OpenLog(args.name, args.depth_limit)

    # Run code
    try:
        spec = importlib.util.spec_from_file_location("_{}".format(uuid4().hex), full_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        del module
    except:
        print("Cleaning up...")

    # Model OpenLog Behavior TODO Add some fault tolerance
    ol.exit()

    # Restore original
    versioner.reset_hard()

#
# import os
# import shutil
# import importlib
# from uuid import uuid4
#
# from flor.versioner.versioner import Versioner
# from flor.complete_capture.walker import Walker
# from flor.logs_manipulator.open_log import OpenLog
#
# def get_path(args):
#     full_path = os.path.abspath(args.path)
#     assert os.path.splitext(os.path.basename(full_path))[1] == '.py'
#     return full_path
#
# def transform(path, walker):
#     walker.compile_tree(lib_code=False) # Transformed code in walker.targetpath
#
# def overwrite(path, walker):
#     current_dir = os.getcwd()
#     os.chdir(os.path.dirname(os.path.dirname(path)))
#     shutil.rmtree(os.path.dirname(path))
#     shutil.copytree(walker.targetpath, os.path.dirname(path))
#     os.chdir(current_dir)
#
# def exec_flython(args):
#     # Get path and check
#     full_path = get_path(args)
#
#     # Commit to repo before code transformation
#     versioner = Versioner(full_path)
#     versioner.save_commit_event("flor commit")
#
#     walker = Walker(os.path.dirname(full_path))
#
#     # Transform code
#     transform(full_path, walker)
#
#     # Overwrite current directory
#     overwrite(full_path, walker)
#
#     # Model OpenLog Behavior
#     ol = OpenLog(args.name, args.depth_limit)
#
#     # Run code
#     try:
#         spec = importlib.util.spec_from_file_location("_{}".format(uuid4().hex), full_path)
#         module = importlib.util.module_from_spec(spec)
#         spec.loader.exec_module(module)
#         del module
#     except:
#         print("Cleaning up...")
#
#     # Model OpenLog Behavior TODO Add some fault tolerance
#     ol.exit()
#
#     # Restore original
#     versioner.reset_hard()
