import webbrowser , os

services = ['open an application','search about something','search in youtube','open a website']
applications = {
    'google chrome':'chrome.exe',
    'my editor':"Visual Studio Code.lnk",
}
print('our services :')
for j in services :
    print(j)

class Orders :
    def OpenAnApp(app_name):
        os.startfile(applications[app_name])
    def OpenWebSite(name):
        webbrowser.open(name)
    def SearchAboutSomething(txt) :
        webbrowser.open(f'https://www.google.com/search?q={txt}')
    def SearchInYoutube(txt):
        webbrowser.open(f'https://www.youtube.com/results?search_query={txt}')