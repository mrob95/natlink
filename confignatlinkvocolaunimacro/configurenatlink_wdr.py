# -*- coding: UTF-8 -*-

#-----------------------------------------------------------------------------
# Python source generated by wxDesigner from file: configurenatlink.wdr
# Do not modify this file, all changes will be lost!
#-----------------------------------------------------------------------------

# Include wxPython modules
import wx
import wx.grid
import wx.animate

# Window functions

ID_TEXTCTRLstatus = 10000
ID_TEXT = 10001
ID_BUTTONHelp1 = 10002
ID_BUTTONNatlinkEnable = 10003
ID_CHECKBOXNatlinkDebug = 10004
ID_BUTTONHelp2 = 10005
ID_CHECKBOXDebugCallbackOutput = 10006
ID_CHECKBOXDebugLoad = 10007
ID_BUTTONVocolaEnable = 10008
ID_TEXTvocolauserdir = 10009
ID_TEXTCTRLvocolauserdir = 10010
ID_CHECKBOXVocolaTakesLanguages = 10011
ID_CHECKBOXVocolaTakesUnimacroActions = 10012
ID_BUTTONHelp3 = 10013
ID_BUTTONNatlinkUserDirectory = 10014
ID_TEXTnatlinkuserdir = 10015
ID_TEXTCTRLuserDirectory = 10016
ID_BUTTONUnimacroInifilesDirectory = 10017
ID_TEXTCTRLunimacroinifilesDirectory = 10018
ID_BUTTONUnimacroEditor = 10019
ID_TEXTCTRLunimacroeditor = 10020
ID_BUTTONVocolaCompatibiliy = 10021
ID_IncludeUnimacroInPythonPath = 10022
ID_BUTTONHelp4 = 10023
ID_BUTTONregister = 10024
ID_BUTTONunregister = 10025
ID_BUTTONUndo = 5100
ID_BUTTONClose = 10026
ID_BUTTONHelp5 = 10027

def MainWindow( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item2 = wx.StaticBox( parent, -1, "Status" )
    item2.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.NORMAL ) )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item4 = wx.TextCtrl( parent, ID_TEXTCTRLstatus, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
    item4.SetBackgroundColour( wx.LIGHT_GREY )
    item3.Add( item4, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item6 = wx.Button( parent, ID_BUTTONHelp1, "Help-&1", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item3.AddGrowableCol( 0 )

    item1.Add( item3, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item0.Add( item1, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item8 = wx.StaticBox( parent, -1, "Natlink" )
    item8.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.NORMAL ) )
    item7 = wx.StaticBoxSizer( item8, wx.VERTICAL )
    
    item9 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item10 = wx.Button( parent, ID_BUTTONNatlinkEnable, "Enable/Disable", wx.DefaultPosition, wx.DefaultSize, 0 )
    item9.Add( item10, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item11 = wx.CheckBox( parent, ID_CHECKBOXNatlinkDebug, "Send Debug output to DNS logfile", wx.DefaultPosition, wx.DefaultSize, 0 )
    item9.Add( item11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 10 )

    item12 = wx.Button( parent, ID_BUTTONHelp2, "Help-&2", wx.DefaultPosition, wx.DefaultSize, 0 )
    item9.Add( item12, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item13 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item9.Add( item13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item14 = wx.BoxSizer( wx.HORIZONTAL )
    
    item15 = wx.CheckBox( parent, ID_CHECKBOXDebugCallbackOutput, "Debug Callback", wx.DefaultPosition, wx.DefaultSize, 0 )
    item14.Add( item15, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item16 = wx.CheckBox( parent, ID_CHECKBOXDebugLoad, "Debug load output", wx.DefaultPosition, wx.DefaultSize, 0 )
    item14.Add( item16, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item9.Add( item14, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item9.AddGrowableCol( 1 )

    item7.Add( item9, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item0.Add( item7, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item18 = wx.StaticBox( parent, -1, "Vocola" )
    item18.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.NORMAL ) )
    item17 = wx.StaticBoxSizer( item18, wx.VERTICAL )
    
    item19 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item20 = wx.Button( parent, ID_BUTTONVocolaEnable, "Enable/Disable", wx.DefaultPosition, wx.DefaultSize, 0 )
    item19.Add( item20, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item21 = wx.StaticText( parent, ID_TEXTvocolauserdir, "Vocola User Directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item19.Add( item21, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item22 = wx.TextCtrl( parent, ID_TEXTCTRLvocolauserdir, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
    item22.SetBackgroundColour( wx.LIGHT_GREY )
    item19.Add( item22, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item23 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item19.Add( item23, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item24 = wx.CheckBox( parent, ID_CHECKBOXVocolaTakesLanguages, "Vocola Multi languages", wx.DefaultPosition, wx.DefaultSize, 0 )
    item19.Add( item24, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item25 = wx.BoxSizer( wx.HORIZONTAL )
    
    item26 = wx.CheckBox( parent, ID_CHECKBOXVocolaTakesUnimacroActions, "Vocola takes Unimacro Actions", wx.DefaultPosition, [280,-1], 0 )
    item25.Add( item26, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item27 = wx.Button( parent, ID_BUTTONHelp3, "Help-&3", wx.DefaultPosition, wx.DefaultSize, 0 )
    item25.Add( item27, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item19.Add( item25, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item19.AddGrowableCol( 2 )

    item17.Add( item19, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item0.Add( item17, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item29 = wx.StaticBox( parent, -1, "Unimacro" )
    item29.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.NORMAL ) )
    item28 = wx.StaticBoxSizer( item29, wx.VERTICAL )
    
    item30 = wx.FlexGridSizer( 0, 3, 0, 0 )
    
    item31 = wx.Button( parent, ID_BUTTONNatlinkUserDirectory, "Enable/Disable", wx.DefaultPosition, wx.DefaultSize, 0 )
    item30.Add( item31, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item32 = wx.StaticText( parent, ID_TEXTnatlinkuserdir, "NatLink User Directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
    item30.Add( item32, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item33 = wx.TextCtrl( parent, ID_TEXTCTRLuserDirectory, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
    item33.SetBackgroundColour( wx.LIGHT_GREY )
    item30.Add( item33, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item34 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item30.Add( item34, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item35 = wx.Button( parent, ID_BUTTONUnimacroInifilesDirectory, "Unimacro User Directory", wx.DefaultPosition, wx.DefaultSize, 0 )
    item30.Add( item35, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item36 = wx.TextCtrl( parent, ID_TEXTCTRLunimacroinifilesDirectory, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
    item36.SetBackgroundColour( wx.LIGHT_GREY )
    item30.Add( item36, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item37 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item30.Add( item37, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item38 = wx.Button( parent, ID_BUTTONUnimacroEditor, "Unimacro Editor", wx.DefaultPosition, wx.DefaultSize, 0 )
    item30.Add( item38, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item39 = wx.TextCtrl( parent, ID_TEXTCTRLunimacroeditor, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
    item39.SetBackgroundColour( wx.LIGHT_GREY )
    item30.Add( item39, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item40 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item30.Add( item40, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item41 = wx.Button( parent, ID_BUTTONVocolaCompatibiliy, "Vocola compatibility", wx.DefaultPosition, wx.DefaultSize, 0 )
    item30.Add( item41, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item42 = wx.BoxSizer( wx.HORIZONTAL )
    
    item43 = wx.CheckBox( parent, ID_IncludeUnimacroInPythonPath, "Include Unimacro directory in PythonPath", wx.DefaultPosition, wx.DefaultSize, 0 )
    item42.Add( item43, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item44 = wx.Button( parent, ID_BUTTONHelp4, "Help-&4", wx.DefaultPosition, wx.DefaultSize, 0 )
    item42.Add( item44, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item30.Add( item42, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item30.AddGrowableCol( 2 )

    item28.Add( item30, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item0.Add( item28, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    item46 = wx.StaticBox( parent, -1, "Repair" )
    item46.SetFont( wx.Font( 10, wx.SWISS, wx.NORMAL, wx.NORMAL ) )
    item45 = wx.StaticBoxSizer( item46, wx.VERTICAL )
    
    item47 = wx.FlexGridSizer( 0, 6, 0, 0 )
    
    item48 = wx.Button( parent, ID_BUTTONregister, "(re)Register NatLink", wx.DefaultPosition, wx.DefaultSize, 0 )
    item47.Add( item48, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item49 = wx.Button( parent, ID_BUTTONunregister, "unRegister NatLink", wx.DefaultPosition, wx.DefaultSize, 0 )
    item47.Add( item49, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item50 = wx.StaticText( parent, ID_TEXT, "", wx.DefaultPosition, wx.DefaultSize, 0 )
    item47.Add( item50, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item51 = wx.Button( parent, ID_BUTTONUndo, "Undo", wx.DefaultPosition, wx.DefaultSize, 0 )
    item47.Add( item51, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item52 = wx.Button( parent, ID_BUTTONClose, "Close", wx.DefaultPosition, wx.DefaultSize, 0 )
    item47.Add( item52, 0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item53 = wx.Button( parent, ID_BUTTONHelp5, "Help-5", wx.DefaultPosition, wx.DefaultSize, 0 )
    item47.Add( item53, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item47.AddGrowableCol( 2 )

    item45.Add( item47, 0, wx.FIXED_MINSIZE|wx.ALIGN_CENTER|wx.ALL|wx.SHAPED, 0 )

    item0.Add( item45, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 0 )

    if set_sizer == True:
        parent.SetSizer( item0 )
        if call_fit == True:
            item0.SetSizeHints( parent )
    
    return item0

ID_TEXTDNSversion = 10028
ID_TEXTCTRLDNSVersion = 10029
ID_TEXTCTRLWindowsVersion = 10030
ID_TEXTCTRLpythonversion = 10031
ID_TEXTdnsinstallpath = 10032
ID_TEXTCTRLDNSinstallpath = 10033
ID_BUTTONchangednsinstallpath = 10034
ID_BUTTONClearDNSInstallPath = 10035
ID_TEXTdnsinifilepath = 10036
ID_TEXTCTRLdnsinifilepath = 10037
ID_BUTTONchangednsinifilepath = 10038
ID_BUTTONClearDNSInifilePath = 10039
ID_TEXTNatlinkCorePath = 10040
ID_TEXTCTRLnatlinkcorepath = 10041
ID_BUTTONLogInfo = 10042
ID_BUTTONHelpInfo = 10043

def InfoWindow( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item2 = wx.StaticBox( parent, -1, "Info" )
    item1 = wx.StaticBoxSizer( item2, wx.VERTICAL )
    
    item3 = wx.FlexGridSizer( 0, 4, 0, 0 )
    
    item4 = wx.StaticText( parent, ID_TEXTDNSversion, "DNS version", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item5 = wx.BoxSizer( wx.HORIZONTAL )
    
    item6 = wx.TextCtrl( parent, ID_TEXTCTRLDNSVersion, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
    item6.SetBackgroundColour( wx.LIGHT_GREY )
    item5.Add( item6, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item7 = wx.StaticText( parent, ID_TEXT, "Windows version", wx.DefaultPosition, wx.DefaultSize, 0 )
    item5.Add( item7, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item8 = wx.TextCtrl( parent, ID_TEXTCTRLWindowsVersion, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
    item8.SetBackgroundColour( wx.LIGHT_GREY )
    item5.Add( item8, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3.Add( item5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item9 = wx.StaticText( parent, ID_TEXT, "Python version", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item9, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item10 = wx.TextCtrl( parent, ID_TEXTCTRLpythonversion, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
    item10.SetBackgroundColour( wx.LIGHT_GREY )
    item3.Add( item10, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item11 = wx.StaticText( parent, ID_TEXTdnsinstallpath, "DNS install path", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item11, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item12 = wx.TextCtrl( parent, ID_TEXTCTRLDNSinstallpath, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
    item12.SetBackgroundColour( wx.LIGHT_GREY )
    item3.Add( item12, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item13 = wx.Button( parent, ID_BUTTONchangednsinstallpath, "Change-&d", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item13, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item14 = wx.Button( parent, ID_BUTTONClearDNSInstallPath, "Clear-&D", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item14, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item15 = wx.StaticText( parent, ID_TEXTdnsinifilepath, "DNS ini file path", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item15, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item16 = wx.TextCtrl( parent, ID_TEXTCTRLdnsinifilepath, "", wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
    item16.SetBackgroundColour( wx.LIGHT_GREY )
    item3.Add( item16, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item17 = wx.Button( parent, ID_BUTTONchangednsinifilepath, "Change-&c", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item17, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item18 = wx.Button( parent, ID_BUTTONClearDNSInifilePath, "Clear-&C", wx.DefaultPosition, wx.DefaultSize, 0 )
    item3.Add( item18, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

    item19 = wx.StaticText( parent, ID_TEXTNatlinkCorePath, "NatlinkCore path", wx.DefaultPosition, wx.DefaultSize, 0 )
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

ID_CHECKBOXRefreshUnimacroVch = 10044
ID_CHECKBOXMakeUnimacroIncludeLines = 10045
ID_CHECKBOXRemoveUnimacroIncludeLines = 10046
ID_BUTTONOK = 10047
ID_BUTTONCancel = 10048

def DialogVocolaCombatibility( parent, call_fit = True, set_sizer = True ):
    item0 = wx.BoxSizer( wx.VERTICAL )
    
    item1 = wx.StaticText( parent, ID_TEXT, 
        "Vocola can profit from Unimacro features. \n"
        "\n"
        "The features can be used if either \n"
        "  -- Unimacro is switched on, or\n"
        "  -- the checkbox \"Include Unimacro in PythonPath\" (in the configure tab) is checked.\n"
        "\n"
        "The include file \"Unimacro.vch\" can help as a wrapper around\n"
        "the Unimacro Shorthand Commands functions.\n"
        "\n"
        "Please check the options you want to be processed and press/call OK",
        wx.DefaultPosition, wx.DefaultSize, 0 )
    item1.SetBackgroundColour( wx.WHITE )
    item0.Add( item1, 0, wx.ALIGN_CENTER|wx.ALL, 15 )

    item2 = wx.CheckBox( parent, ID_CHECKBOXRefreshUnimacroVch, "Copy the include file \"Unimacro.vch\" into your Vocola User Files directory", wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item3 = wx.CheckBox( parent, ID_CHECKBOXMakeUnimacroIncludeLines, "Insert  a \"include Unimacro.vch;\" line in all your Vocola Command Files", wx.DefaultPosition, wx.DefaultSize, 0 )
    item0.Add( item3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

    item4 = wx.CheckBox( parent, ID_CHECKBOXRemoveUnimacroIncludeLines, "Remove the \"include Unimacro.vch;\" lines from your Vocola Command Files", wx.DefaultPosition, wx.DefaultSize, 0 )
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

# Menubar functions

ID_MENUClose = 10049
ID_MENUFile = 10050
ID_MENUhelp = 10051

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
