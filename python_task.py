import sys
import time

from util.task_status import TaskStatus
from util.task_args import get_task_id, get_db_url, get_task_name, get_cmd_arg

try:
    # Connect to SCDF's database.    
    status = TaskStatus(get_task_id(), get_db_url())

    # Set task's status to RUNNING.
    status.running()

    # Do something.
    print('Start task do biscoito:{}, id:{}'.format(get_task_name(), get_task_id()))

    print('Wait for 10 seconds ... :) ')
    sys.stdout.flush()
    time.sleep(10)

    if get_cmd_arg('error.message') is not None:
        raise Exception(get_cmd_arg('error.message'))

    print('message: ' + str(get_cmd_arg('message')))
    print(str(get_cmd_arg('password')))
    print("Goodbye!")

    # Set task's status to COMPLETED.
    status.completed()

except Exception as exp:
    # Set task's status to FAILED.
    status.failed(1, 'Task failed: {}'.format(exp))