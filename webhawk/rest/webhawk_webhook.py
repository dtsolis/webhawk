from rest.api_errors import InvalidUsage
from rest.webhook_base import WebHookBase

__author__ = "Dimi Balaouras"
__copyright__ = "Copyright 2016, Stek.io"
__license__ = "Apache License 2.0, see LICENSE for more details."


class WebHawkWebHook(WebHookBase):
    """
    RESTful Resource for the Github Webhook
    """
    resource_name = "webhawk"

    def create_task(self, input):
        """
        Creates a new build task using the input (usually a POST Payload)
        """

        # Get the task manager
        task_manager = self._context.get("task_manager")

        # Process the input
        try:
            repository_name = input['repository']
            branch_name = input['branch']
            vcs = input['scm']
        except KeyError:
            raise InvalidUsage("Invalid payload: %s" % str(input))

        # Construct the new task
        new_task = task_manager.create_new_task(repository_name=repository_name, branch_name=branch_name, vcs=vcs)

        return new_task
