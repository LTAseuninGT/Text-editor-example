import wx
import webbrowser

def load(event):
    file = open(filenameload.GetValue())
    contents.SetValue(file.read())
    file.close()
def save(event):
    file = open(filenamesave.GetValue(), "w")
    file.write(contents.GetValue())
    file.close()
def site(event):
    webbrowser.open("http://www.ryqol.comuf.com")

app = wx.App()
win = wx.Frame(None, title="Ligature Myriad", size=(603, 592))

bkg = wx.Panel(win)

saveButton = wx.Button(bkg, label="Save")
saveButton.Bind(wx.EVT_BUTTON, save)

loadButton = wx.Button(bkg, label="Open")
loadButton.Bind(wx.EVT_BUTTON, load)

siteButton = wx.Button(bkg, label="View Site")
siteButton.Bind(wx.EVT_BUTTON, site)

filenamesave = wx.TextCtrl(bkg)
filenameload = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(filenamesave, proportion = 1, flag=wx.EXPAND)
hbox.Add(saveButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(filenameload, proportion =1, flag=wx.EXPAND)
hbox.Add(loadButton, proportion=0, flag=wx.LEFT, border=5)
hbox.Add(siteButton, proportion=0, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border=5)

bkg.SetSizer(vbox)
win.Show()

app.MainLoop()
