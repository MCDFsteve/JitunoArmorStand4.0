# -*- coding: utf-8 -*-

from mod.common.minecraftEnum import ItemPosType
import mod.server.extraServerApi as serverApi
import logging
import random

ServerSystem = serverApi.GetServerSystemCls()


class armorServer(ServerSystem):

    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        self.armor = 0
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
                            'ItemUseOnAfterServerEvent', self, self.OnItemUseOnAfterServer)

    def OnItemUseOnAfterServer(self, data):
        entityId = data['entityId']
        itemDict = data['itemDict']     
        self.armor += 1 

        comp = serverApi.GetEngineCompFactory().CreateItem(entityId)
        itemDict = comp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED, 0)  

        if itemDict['newItemName'] == 'dfsteve:armor_item1' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item2' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item3' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item4' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item5' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item6' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)   

        elif itemDict['newItemName'] == 'dfsteve:armor_item7' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item8' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item9' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item10' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item11' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)   

        elif itemDict['newItemName'] == 'dfsteve:armor_item12' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item13' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item14' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item15' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item16' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)   

        elif itemDict['newItemName'] == 'dfsteve:armor_item17' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item18' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item19' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item20' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item21' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 

        elif itemDict['newItemName'] == 'dfsteve:armor_item22' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item23' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item24' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item25' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item26' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)   

        elif itemDict['newItemName'] == 'dfsteve:armor_item27' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item28' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item29' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item30' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item31' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)   

        elif itemDict['newItemName'] == 'dfsteve:armor_item32' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item33' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item34' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item35' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item36' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)   

        elif itemDict['newItemName'] == 'dfsteve:armor_item_1' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_2' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_3' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_4' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_5' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 

        elif itemDict['newItemName'] == 'dfsteve:armor_item_6' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_7' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_8' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_9' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_10' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)   

        elif itemDict['newItemName'] == 'dfsteve:armor_item_11' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_12' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_13' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_14' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_15' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)   

        elif itemDict['newItemName'] == 'dfsteve:armor_item_16' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_17' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_18' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_19' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_20' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 

        elif itemDict['newItemName'] == 'dfsteve:armor_item_21' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_22' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_23' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_24' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_25' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)   

        elif itemDict['newItemName'] == 'dfsteve:armor_item_26' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_27' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_28' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_29' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_30' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)   

        elif itemDict['newItemName'] == 'dfsteve:armor_item_31' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_32' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_33' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_34' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_35' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_36' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:armor_item_37' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)


        elif itemDict['newItemName'] == 'dfsteve:citydlc_303' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 

        elif itemDict['newItemName'] == 'dfsteve:citydlc_tnt' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:citydlc_dream' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 

        elif itemDict['newItemName'] == 'dfsteve:pqf_aidi' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:pqf_diyu303' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:pqf_mochen' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)   

        elif itemDict['newItemName'] == 'dfsteve:pqf_moyingwang' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:pqf_moyingzhanshen' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:pqf_shiti303' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:pqf_tezhonghim' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:pqf_xiaoheizihim' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)   

        elif itemDict['newItemName'] == 'dfsteve:pqf_heimaoshaonv' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:pqf_himnv' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:pqf_huasheng' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:pqf_jiran' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:pqf_kongcha' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:pqf_lingjiang' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:pqf_lingxue' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)


        elif itemDict['newItemName'] == 'dfsteve:pqf_qiuyuehusan' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 

        elif itemDict['newItemName'] == 'dfsteve:pqf_shixuemei' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:pqf_yueli' and self.armor == 1:

            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 

        elif itemDict['newItemName'] == 'dfsteve:vtuber_a' and self.armor == 1:
            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 
        elif itemDict['newItemName'] == 'dfsteve:vtuber_b' and self.armor == 1:
            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 
        elif itemDict['newItemName'] == 'dfsteve:vtuber_c' and self.armor == 1:
            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 
        elif itemDict['newItemName'] == 'dfsteve:vtuber_d' and self.armor == 1:
            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 
        elif itemDict['newItemName'] == 'dfsteve:vtuber_e' and self.armor == 1:
            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 
        elif itemDict['newItemName'] == 'dfsteve:vtuber_f' and self.armor == 1:
            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 
        elif itemDict['newItemName'] == 'dfsteve:vtuber_g' and self.armor == 1:
            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 
        elif itemDict['newItemName'] == 'dfsteve:vtuber_h' and self.armor == 1:
            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 
        elif itemDict['newItemName'] == 'dfsteve:vtuber_i' and self.armor == 1:
            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)
        
        elif itemDict['newItemName'] == 'dfsteve:skygod_bloodfire' and self.armor == 1:
            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 
        elif itemDict['newItemName'] == 'dfsteve:skygod_kangyu' and self.armor == 1:
            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 
        elif itemDict['newItemName'] == 'dfsteve:skygod_kodoragon' and self.armor == 1:
            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 
        elif itemDict['newItemName'] == 'dfsteve:skygod_ranxia' and self.armor == 1:
            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 
        elif itemDict['newItemName'] == 'dfsteve:skygod_yekong' and self.armor == 1:
            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 
        elif itemDict['newItemName'] == 'dfsteve:skygod_yonghao' and self.armor == 1:
            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 
        elif itemDict['newItemName'] == 'dfsteve:skygod_zhudan' and self.armor == 1:
            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

        elif itemDict['newItemName'] == 'dfsteve:skygod_zombie' and self.armor == 1:
            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data) 
        elif itemDict['newItemName'] == 'dfsteve:skygod_apple' and self.armor == 1:
            compAddTimer = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
            compAddTimer.AddTimer(0.2, self.armor2, data)

    def armor2(self,data):
        x = data['x']
        y = data['y']
        z = data['z'] 
        self.armor = 0
        pos = (x,y,z)

        compCreateCommand = serverApi.GetEngineCompFactory().CreateCommand(serverApi.GetLevelId())
        compCreateCommand.SetCommand('/playsound mob.villager.hit @p ' + str(pos[0]) + ' ' + str(pos[1]) + ' ' + str(pos[2]) + ' 16 1 0',data["entityId"])

        compCreateCommand = serverApi.GetEngineCompFactory().CreateCommand(serverApi.GetLevelId())
        compCreateCommand.SetCommand("/say @p 不对！不是这么用的！皮肤包要对着史蒂夫/艾利克斯盔甲架使用！",data["entityId"])

        compCreateCommand = serverApi.GetEngineCompFactory().CreateCommand(serverApi.GetLevelId())
        compCreateCommand.SetCommand("/give @p dfsteve:armor_talk",data["entityId"])      
         