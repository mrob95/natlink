# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: configurenatlink.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
# import wx.animate

# Window functions

ID_TEXTCTRLstatus = 10000
ID_BUTTONNatlinkEnable = 10001
ID_CHECKBOXDebugCallbackOutput = 10002
ID_CHECKBOXDebugLoad = 10003
ID_BUTTONHelp1 = 10004
ID_BUTTONVocolaEnable = 10005
ID_TEXTvocolauserdir = 10006
ID_TEXTCTRLvocolauserdirectory = 10007
ID_TEXT = 10008
ID_CHECKBOXVocolaTakesLanguages = 10009
ID_CHECKBOXVocolaTakesUnimacroActions = 10010
ID_BUTTONHelp2 = 10011
ID_BUTTONUnimacroEnable = 10012
ID_TEXTunimacrouserdir = 10013
ID_TEXTCTRLunimacrouserdirectory = 10014
ID_BUTTONUnimacroEditor = 10015
ID_TEXTCTRLunimacroeditor = 10016
ID_BUTTONVocolaCompatibiliy = 10017
ID_BUTTONHelp3 = 10018
ID_BUTTONUserEnable = 10019
ID_TEXTnatlinkuserdirectory = 10020
ID_TEXTCTRLnatlinkuserdirectory = 10021
ID_BUTTONHelp4 = 10022
ID_BUTTONregister = 10023
ID_BUTTONunregister = 10024
ID_BUTTONUndo = 5100
ID_BUTTONClose = 10025
ID_BUTTONHelp5 = 10026

def MainWindow( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item2 = wx.StaticBox( parent, -1, "Status" )
    item2.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.NORMAL ) )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = wx.FlexGridSizer( 0, 1, 0, 0 )
    
    item4 = wx.TextCtrl( parent, ID_TEXTCTRLstatus, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
    item4.SetBackgroundColour( wx.LIGHT_GREY )
    item3.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL, 5 )

    item3.AddGrowableCol( 0 )

    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item6 = wx.StaticBox( parent, -1, "Natlink" )
    item6.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.NORMAL ) )
    item5 = wx.StaticBoxSizer( item6, wx.VERTICAL )
    
    item7 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item8 = wx.Button( parent, ID_BUTTONNatlinkEnable, "Enable/Disable", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item9 = wx.BoxSizer( wx.HORIZONTAL )
    
    item10 = wx.CheckBox( parent, ID_CHECKBOXDebugCallbackOutput, "Debug Callback", wx.DefaultPosition, wx.DefaultSize, 0 )
    item9.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item11 = wx.CheckBox( parent, ID_CHECKBOXDebugLoad, "Debug load output", wx.DefaultPosition, wx.DefaultSize, 0 )
    item9.Add( item11, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item7.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item12 = wx.Button( parent, ID_BUTTONHelp1, "Help-&1", wx.DefaultPosition, wx.DefaultSize, 0 )
    item7.Add( item12, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item7.AddGrowableCol( 1 )

    item5.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item0.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item14 = wx.StaticBox( parent, -1, "Vocola" )
    item14.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.NORMAL ) )
    item13 = wx.StaticBoxSizer( item14, wx.VERTICAL )
    
    item15 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item16 = wx.Button( parent, ID_BUTTONVocolaEnable, "Enable/Disable", wx.DefaultPosition, wx.DefaultSize, 0 )
    item15.Add( item16, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item17 = wx.StaticText( parent, ID_TEXTvocolauserdir, "Vocola User Directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item15.Add( item17, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item18 = wx.TextCtrl( parent, ID_TEXTCTRLvocolauserdirectory, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
    item18.SetBackgroundColour( wx.LIGHT_GREY )
    item15.Add( item18, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item19 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item15.Add( item19, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item20 = wx.CheckBox( parent, ID_CHECKBOXVocolaTakesLanguages, "Vocola multi languages", wx.DefaultPosition, wx.DefaultSize, 0 )
    item15.Add( item20, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item21 = wx.BoxSizer( wx.HORIZONTAL )
    
    item22 = wx.CheckBox( parent, ID_CHECKBOXVocolaTakesUnimacroActions, "Vocola takes Unimacro Actions", wx.DefaultPosition, [280,-1], 0 )
    item21.Add( item22, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item23 = wx.Button( parent, ID_BUTTONHelp2, "Help-&2", wx.DefaultPosition, wx.DefaultSize, 0 )
    item21.Add( item23, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item15.Add( item21, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item15.AddGrowableCol( 2 )

    item13.Add( item15, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item0.Add( item13, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item25 = wx.StaticBox( parent, -1, "Unimacro" )
    item25.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.NORMAL ) )
    item24 = wx.StaticBoxSizer( item25, wx.VERTICAL )
    
    item26 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item27 = wx.Button( parent, ID_BUTTONUnimacroEnable, "Enable/Disable", wx.DefaultPosition, wx.DefaultSize, 0 )
    item26.Add( item27, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item28 = wx.StaticText( parent, ID_TEXTunimacrouserdir, "Unimacro User Directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item26.Add( item28, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item29 = wx.TextCtrl( parent, ID_TEXTCTRLunimacrouserdirectory, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
    item29.SetBackgroundColour( wx.LIGHT_GREY )
    item26.Add( item29, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item30 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item26.Add( item30, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item31 = wx.Button( parent, ID_BUTTONUnimacroEditor, "Unimacro Editor", wx.DefaultPosition, wx.DefaultSize, 0 )
    item26.Add( item31, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item32 = wx.TextCtrl( parent, ID_TEXTCTRLunimacroeditor, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
    item32.SetBackgroundColour( wx.LIGHT_GREY )
    item26.Add( item32, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item33 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item26.Add( item33, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item34 = wx.Button( parent, ID_BUTTONVocolaCompatibiliy, "Vocola compatibility", wx.DefaultPosition, wx.DefaultSize, 0 )
    item26.Add( item34, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item35 = wx.BoxSizer( wx.HORIZONTAL )
    
    item36 = wx.Button( parent, ID_BUTTONHelp3, "Help-&3", wx.DefaultPosition, wx.DefaultSize, 0 )
    item35.Add( item36, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item26.Add( item35, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item26.AddGrowableCol( 2 )

    item24.Add( item26, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item0.Add( item24, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item38 = wx.StaticBox( parent, -1, "UserDirectory" )
    item37 = wx.StaticBoxSizer( item38, wx.VERTICAL )
    
    item39 = wx.FlexGridSizer( 0, 4, 0, 0 )
    
    item40 = wx.Button( parent, ID_BUTTONUserEnable, "Enable/Disable", wx.DefaultPosition, wx.DefaultSize, 0 )
    item39.Add( item40, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item41 = wx.StaticText( parent, ID_TEXTnatlinkuserdirectory, "Natlink User Directory:", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT )
    item39.Add( item41, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item42 = wx.TextCtrl( parent, ID_TEXTCTRLnatlinkuserdirectory, "", wx.DefaultPosition, [80,-1], wx.TE_READONLY )
    item42.SetBackgroundColour( wx.LIGHT_GREY )
    item39.Add( item42, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item43 = wx.Button( parent, ID_BUTTONHelp4, "Help-&4", wx.DefaultPosition, wx.DefaultSize, 0 )
    item39.Add( item43, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item39.AddGrowableCol( 2 )

    item37.Add( item39, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item0.Add( item37, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item45 = wx.StaticBox( parent, -1, "Repair" )
    item45.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.NORMAL ) )
    item44 = wx.StaticBoxSizer( item45, wx.VERTICAL )
    
    item46 = wx.FlexGridSizer( 0, 6, 0, 0 )
    
    item47 = wx.Button( parent, ID_BUTTONregister, "(re)Register NatLink", wx.DefaultPosition, wx.DefaultSize, 0 )
    item46.Add( item47, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item48 = wx.Button( parent, ID_BUTTONunregister, "unRegister NatLink", wx.DefaultPosition, wx.DefaultSize, 0 )
    item46.Add( item48, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item49 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item46.Add( item49, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item50 = wx.Button( parent, ID_BUTTONUndo, "Undo", wx.DefaultPosition, wx.DefaultSize, 0 )
    item46.Add( item50, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item51 = wx.Button( parent, ID_BUTTONClose, "Close", wx.DefaultPosition, wx.DefaultSize, 0 )
    item46.Add( item51, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item52 = wx.Button( parent, ID_BUTTONHelp5, "Help-5", wx.DefaultPosition, wx.DefaultSize, 0 )
    item46.Add( item52, 0, wx.ALIGN_CENTER, 5 )

    item46.AddGrowableCol( 2 )

    item44.Add( item46, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( item44, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_TEXTDNSversion = 10027
ID_TEXTCTRLDNSVersion = 10028
ID_TEXTCTRLWindowsVersion = 10029
ID_TEXTCTRLpythonversion = 10030
ID_TEXTdnsinstallpath = 10031
ID_TEXTCTRLDNSinstallpath = 10032
ID_BUTTONchangednsinstallpath = 10033
ID_BUTTONClearDNSInstallPath = 10034
ID_TEXTdnsinifilepath = 10035
ID_TEXTCTRLdnsinifilepath = 10036
ID_BUTTONchangednsinifilepath = 10037
ID_BUTTONClearDNSInifilePath = 10038
ID_TEXTNatlinkCorePath = 10039
ID_TEXTCTRLnatlinkcorepath = 10040
ID_BUTTONLogInfo = 10041
ID_BUTTONHelpInfo = 10042

def InfoWindow( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item2 = wx.StaticBox( parent, -1, "Info" )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = wx.FlexGridSizer( 0, 4, 0, 0 )
    
    item4 = wx.StaticText( parent, ID_TEXTDNSversion, "DNS version:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = wx.BoxSizer( wx.HORIZONTAL )
    
    item6 = wx.TextCtrl( parent, ID_TEXTCTRLDNSVersion, "", wx.DefaultPosition, [50,-1], wx.TE_READONLY )
    item6.SetBackgroundColour( wx.LIGHT_GREY )
    item5.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP|wx.BOTTOM, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, "Windows version:", wx.DefaultPosition, [180,-1], wx.ALIGN_RIGHT )
    item5.Add( item7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item8 = wx.TextCtrl( parent, ID_TEXTCTRLWindowsVersion, "", wx.DefaultPosition, [50,-1], wx.TE_READONLY )
    item8.SetBackgroundColour( wx.LIGHT_GREY )
    item5.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.TOP|wx.BOTTOM, 5 )

    item3.Add( item5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item9 = wx.StaticText( parent, ID_TEXT, "Python version:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item10 = wx.TextCtrl( parent, ID_TEXTCTRLpythonversion, "", wx.DefaultPosition, [50,-1], wx.TE_READONLY )
    item10.SetBackgroundColour( wx.LIGHT_GREY )
    item3.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 10 )

    item11 = wx.StaticText( parent, ID_TEXTdnsinstallpath, "DNS install path:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item12 = wx.TextCtrl( parent, ID_TEXTCTRLDNSinstallpath, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
    item12.SetBackgroundColour( wx.LIGHT_GREY )
    item3.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item13 = wx.Button( parent, ID_BUTTONchangednsinstallpath, "Change-&d", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item14 = wx.Button( parent, ID_BUTTONClearDNSInstallPath, "Clear-&D", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item14, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item15 = wx.StaticText( parent, ID_TEXTdnsinifilepath, "DNS ini file path:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item15, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item16 = wx.TextCtrl( parent, ID_TEXTCTRLdnsinifilepath, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
    item16.SetBackgroundColour( wx.LIGHT_GREY )
    item3.Add( item16, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item17 = wx.Button( parent, ID_BUTTONchangednsinifilepath, "Change-&c", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item17, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item18 = wx.Button( parent, ID_BUTTONClearDNSInifilePath, "Clear-&C", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item18, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item19 = wx.StaticText( parent, ID_TEXTNatlinkCorePath, "NatlinkCore path:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item19, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item20 = wx.TextCtrl( parent, ID_TEXTCTRLnatlinkcorepath, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
    item20.SetBackgroundColour( wx.LIGHT_GREY )
    item3.Add( item20, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item21 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item21, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item22 = wx.Button( parent, ID_BUTTONLogInfo, "Log info-&i", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item22, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item23 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item23, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item24 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item24, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item25 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item25, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item26 = wx.Button( parent, ID_BUTTONHelpInfo, "Help-&Info", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item26, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item3.AddGrowableCol( 1 )

    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_CHECKBOXMakeUnimacroIncludeLines = 10043
ID_CHECKBOXRemoveUnimacroIncludeLines = 10044
ID_CHECKBOXRefreshUnimacroVch = 10045
ID_BUTTONOK = 10046
ID_BUTTONCancel = 10047

def DialogVocolaCombatibility( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item1 = wx.StaticText( parent, ID_TEXT, 
        "Vocola can profit from Unimacro features.\n"
        "\n"
        "If you wish to do so, switch on the checkbox \"Vocola takes Unimacro Actions\" in the configure panel.\n"
        "\n"
        "It is then useful to include the file \"Unimacro.vch\" as a wrapper around the Unimacro Shorthand Commands functions.\n"
        "\n"
        "With the options below, you can insert or remove an \"include\" line in all your Vocola Command Files, \n"
        "and ensure the include file is copied into the correct directory. \n"
        "This last action is sometimes needed after an update of the NatLink/Vocola/Unimacro system.\n"
        "\n"
        "Please check the options you want to be processed and press/call OK",
        wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetBackgroundColour( wx.WHITE )
    item0.Add( item1, 0, wx.ALIGN_CENTER|wx.ALL, 15 )

    item2 = wx.CheckBox( parent, ID_CHECKBOXMakeUnimacroIncludeLines, "Insert  a \"include Unimacro.vch;\" line in all your Vocola Command Files", wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3 = wx.CheckBox( parent, ID_CHECKBOXRemoveUnimacroIncludeLines, "Remove the \"include Unimacro.vch;\" lines from your Vocola Command Files", wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item4 = wx.CheckBox( parent, ID_CHECKBOXRefreshUnimacroVch, "Copy the include file \"Unimacro.vch\" into your Vocola User Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = wx.BoxSizer( wx.HORIZONTAL )
    
    item6 = wx.Button( parent, ID_BUTTONOK, "OK", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item7 = wx.Button( parent, ID_BUTTONCancel, "Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item0.Add( item5, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_TEXTahkexedir = 10048
ID_TEXTCTRLAhkExeDir = 10049
ID_BUTTONsetahkexedir = 10050
ID_BUTTONclearahkexedir = 10051
ID_TEXTahkuserdir = 10052
ID_TEXTCTRLahkuserdir = 10053
ID_BUTTONsetahkuserdir = 10054
ID_BUTTONclearahkuserdir = 10055
ID_BUTTONahkhelp = 10056
ID_BUTTONcloseadvanced = 10057
ID_BUTTONhelprepair = 10058

def ExtraWindow( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item2 = wx.StaticBox( parent, -1, "AutoHotkey" )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = wx.FlexGridSizer( 0, 4, 0, 0 )
    
    item4 = wx.StaticText( parent, ID_TEXTahkexedir, "Ahk Exe Directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = wx.TextCtrl( parent, ID_TEXTCTRLAhkExeDir, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
    item5.SetBackgroundColour( wx.LIGHT_GREY )
    item3.Add( item5, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item6 = wx.Button( parent, ID_BUTTONsetahkexedir, "Set", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item7 = wx.Button( parent, ID_BUTTONclearahkexedir, "Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item8 = wx.StaticText( parent, ID_TEXTahkuserdir, "Ahk User Directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item8, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item9 = wx.TextCtrl( parent, ID_TEXTCTRLahkuserdir, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
    item9.SetBackgroundColour( wx.LIGHT_GREY )
    item3.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item10 = wx.Button( parent, ID_BUTTONsetahkuserdir, "Set", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item10, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item11 = wx.Button( parent, ID_BUTTONclearahkuserdir, "Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item11, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item12 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item12, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item13 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item14 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item14, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item15 = wx.Button( parent, ID_BUTTONahkhelp, "Help", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item15, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item3.AddGrowableCol( 1 )

    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item17 = wx.StaticBox( parent, -1, "Repair" )
    item17.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.NORMAL ) )
    item16 = wx.StaticBoxSizer( item17, wx.VERTICAL )
    
    item18 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item19 = wx.BoxSizer( wx.HORIZONTAL )
    
    item20 = wx.Button( parent, ID_BUTTONregister, "(re)Register NatLink", wx.DefaultPosition, wx.DefaultSize, 0 )
    item19.Add( item20, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item21 = wx.Button( parent, ID_BUTTONunregister, "unRegister NatLink", wx.DefaultPosition, wx.DefaultSize, 0 )
    item19.Add( item21, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

    item18.Add( item19, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item22 = wx.BoxSizer( wx.HORIZONTAL )
    
    item23 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, [20,20], 0 )
    item22.Add( item23, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item18.Add( item22, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item24 = wx.BoxSizer( wx.HORIZONTAL )
    
    item25 = wx.Button( parent, ID_BUTTONcloseadvanced, "Close", wx.DefaultPosition, wx.DefaultSize, 0 )
    item24.Add( item25, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

    item26 = wx.Button( parent, ID_BUTTONhelprepair, "Help", wx.DefaultPosition, wx.DefaultSize, 0 )
    item24.Add( item26, 0, wx.ALIGN_CENTER, 5 )

    item18.Add( item24, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item18.AddGrowableCol( 1 )

    item16.Add( item18, 0, wx.FIXED_MINSIZE|wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.SHAPED, 0 )

    item1.Add( item16, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

# Menubar functions

ID_MENUClose = 10059
ID_MENUFile = 10060
ID_MENUhelp = 10061

def MyMenuBarFunc():
    item0 = wx.MenuBar()
    
    item1 = wx.Menu()
    item1.Append( ID_MENUClose, "Close\tc", "" )
    item0.Append( item1, "File" )
    
    item2 = wx.Menu()
    item2.Append( ID_MENUhelp, "Help", "" )
    item0.Append( item2, "Help" )
    
    return item0

# Toolbar functions

# Bitmap functions


# End of generated file
