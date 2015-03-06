# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  6 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1000,800 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer1 = wx.FlexGridSizer( 1, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 200,500 ), wx.TAB_TRAVERSAL )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.scrambutton = wx.Button( self.m_panel1, wx.ID_ANY, u"SCRAM", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.scrambutton, 0, wx.ALL, 5 )
		
		self.pausebutton = wx.ToggleButton( self.m_panel1, wx.ID_ANY, u"Pause", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.pausebutton, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"REACTOR CONTROL", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer1.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self.m_staticline15 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline15, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.pwrSetPt = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer1.Add( self.pwrSetPt, 0, wx.ALL, 5 )
		
		self.m_staticText1 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Power SetPoint [MW]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.pwrbox = wx.CheckBox( self.m_panel1, wx.ID_ANY, u"Power Ctrl", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer1.Add( self.pwrbox, 0, wx.ALL, 5 )
		
		self.coolantBox = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer1.Add( self.coolantBox, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Coolant Flow Rate [kg/s]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		bSizer1.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rodSetPt = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PROCESS_ENTER )
		bSizer1.Add( self.rodSetPt, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Rod Setpoint", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.rodSlide = wx.Slider( self.m_panel1, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size( 100,250 ), wx.SL_VERTICAL )
		bSizer1.Add( self.rodSlide, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		self.m_panel1.SetSizer( bSizer1 )
		self.m_panel1.Layout()
		fgSizer1.Add( self.m_panel1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( 150,-1 ), wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText8 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Plot Zoom", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.plotZoom = wx.Slider( self.m_panel4, wx.ID_ANY, 20, 0, 100, wx.DefaultPosition, wx.Size( 150,-1 ), wx.SL_HORIZONTAL )
		bSizer2.Add( self.plotZoom, 0, wx.ALL, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.powOut = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.powOut, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Power Output [MW]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		bSizer2.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.m_staticline8 = wx.StaticLine( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline8, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.fueltOut = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.fueltOut.SetMaxLength( 0 ) 
		bSizer2.Add( self.fueltOut, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Fuel Temp [K]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		bSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.cooltOut = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cooltOut.SetMaxLength( 0 ) 
		bSizer2.Add( self.cooltOut, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Coolant Temp [K]", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_staticline14 = wx.StaticLine( self.m_panel4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer2.Add( self.m_staticline14, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.rodPosOut = wx.TextCtrl( self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.rodPosOut.SetMaxLength( 0 ) 
		bSizer2.Add( self.rodPosOut, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Rod % Withdrawn", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.rodGauge = wx.Gauge( self.m_panel4, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size( 50,250 ), wx.GA_SMOOTH|wx.GA_VERTICAL )
		self.rodGauge.SetValue( 0 ) 
		bSizer2.Add( self.rodGauge, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		self.m_panel4.SetSizer( bSizer2 )
		self.m_panel4.Layout()
		fgSizer1.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 600,800 ), wx.TAB_TRAVERSAL )
		fgSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"exit", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.m_menuItem1 )
		
		self.m_menubar1.Append( self.m_menu1, u"File" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		# Connect Events
		self.scrambutton.Bind( wx.EVT_BUTTON, self.SCRAM )
		self.pausebutton.Bind( wx.EVT_TOGGLEBUTTON, self.pauseSim )
		self.pwrSetPt.Bind( wx.EVT_TEXT_ENTER, self.setReactorPwr )
		self.pwrbox.Bind( wx.EVT_CHECKBOX, self.pwrCtrlON )
		self.coolantBox.Bind( wx.EVT_TEXT_ENTER, self.coolantSet )
		self.rodSetPt.Bind( wx.EVT_TEXT_ENTER, self.setRodPos )
		self.rodSlide.Bind( wx.EVT_SCROLL, self.rodSlideSet )
		self.plotZoom.Bind( wx.EVT_SCROLL, self.setPlotZoom )
		self.Bind( wx.EVT_MENU, self.exitSim, id = self.m_menuItem1.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def SCRAM( self, event ):
		event.Skip()
	
	def pauseSim( self, event ):
		event.Skip()
	
	def setReactorPwr( self, event ):
		event.Skip()
	
	def pwrCtrlON( self, event ):
		event.Skip()
	
	def coolantSet( self, event ):
		event.Skip()
	
	def setRodPos( self, event ):
		event.Skip()
	
	def rodSlideSet( self, event ):
		event.Skip()
	
	def setPlotZoom( self, event ):
		event.Skip()
	
	def exitSim( self, event ):
		event.Skip()
	

