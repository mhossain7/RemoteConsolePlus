'''Created by Dmytro Konobrytskyi, 2012(C)'''
import wx
from Network.Server import Server
from UI.UIManager import UIManager
from FilterRouter.FilterRouter import FilterRouter
from MessageProtocol.JSONWithBinaryTail import ProtocolParser
from OutputRouter.OutputRouter import OutputRouter
from ConfigManager.ConfigManager import NetworkConfig

class RCPServer(object):
    '''
    Main class of RCP server. 
    It creates and controls all message processing pipeline components.
    '''

    def __init__(self):
        self._app = wx.App(redirect=False)  #default error output to console
        
        #Create all message processing pipeline components 
        self._uiManager = UIManager()
        self._outputRouter = OutputRouter(self._uiManager)
        self._filterRouter = FilterRouter(self._outputRouter)
        self._protocolParser = ProtocolParser(self._filterRouter)
        self._server = Server(self._protocolParser)

        #Run main message receiving timer
        timerOwner = wx.EvtHandler()
        self._mainTimer = wx.Timer(timerOwner, wx.ID_ANY)
        self._mainTimer.Start(NetworkConfig.ReceivingMessagesInterval)
        timerOwner.Bind(wx.EVT_TIMER, self.ProcessMessagess, self._mainTimer)
        
        self._app.MainLoop()

    def ProcessMessagess(self, event):
        self._server.ReceiveMessages()
        