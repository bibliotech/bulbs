# -*- coding: utf-8 -*-
#
# Copyright 2012 James Thornton (http://jamesthornton.com)
# BSD License (see LICENSE for details)
#
"""
An interface for executing Gremlin scripts on the client.

"""
from .utils import initialize_elements, get_one_result


class Gremlin(object):
    """
    An interface for executing Gremlin scripts on the client.
    
    :param client: The Client object for the database.
    :type client: Client

    """

    def __init__(self, client):
        self.client = client

    def command(self, script, params=None):
        """
        Returns the raw Result object from an arbitrary Gremlin command.

        :param script: Gremlin script to execute on the client.
        :type script: str
 
        :param params: Optional paramaters to bind to the Gremlin script. 
        :type params: dict or None

        :rtype: Result

        """
        resp = self.client.gremlin(script,params)
        return get_one_result(resp)

    def query(self, script, params=None):
        """
        Returns initialized Element objects from an arbitrary Gremlin query.

        :param script: Gremlin script to execute on the client.
        :type script: str
 
        :param params: Optional paramaters to bind to the Gremlin script. 
        :type params: dict or None

        :rtype: Generator of objects: Vertex, Edge, Node, or Relationship

        """
        resp = self.client.gremlin(script, params)
        return initialize_elements(self.client, resp)
 
    def execute(self, script, params=None):
        """
        Returns the raw Response object from an arbitrary Gremlin script.

        :param script: Gremlin script to execute on the client.
        :type script: str
 
        :param params: Optional paramaters to bind to the Gremlin script. 
        :type params: dict or None

        :rtype: Response

        .. note:: Use case: You are returning element IDs and the actual
                  elements are cached in Redis or Membase.

                  Or, you're returning primitives or Table data.

        """
        return self.client.gremlin(script, params)
 
