# -*- coding: utf-8 -*-

from mod.common.mod import Mod
import mod.server.extraServerApi as serverApi
import mod.client.extraClientApi as clientApi

@Mod.Binding(name = "scripts_armor", version = "1.0.0")

class dfsteve_armor(object):

    def __init__(self):
        print "初始化引擎"
        
    @Mod.InitServer()
    def register_server(self):
        serverApi.RegisterSystem("scripts_armor", "armorServer", "scripts_armor.modServer.armorServer")
        print "注册服务端"
        
    @Mod.InitClient()
    def register_client(self):
        clientApi.RegisterSystem("scripts_armor", "armorClient", "scripts_armor.modClient.armorClient")
        print "注册客户端"
        
    @Mod.DestroyServer()
    def destroy_server(self):
        print "销毁服务端"
        
    @Mod.DestroyClient()
    def destroy_client(self):
        print "销毁客户端"