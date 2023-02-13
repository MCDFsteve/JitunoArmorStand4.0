# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi

ClientSystem = clientApi.GetClientSystemCls()
class armorClient(ClientSystem):

    def __init__(self, namespace, systemName):
        super(armorClient, self).__init__(namespace, systemName)
        
