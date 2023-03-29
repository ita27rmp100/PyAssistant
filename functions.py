import webbrowser
import os

services = ['open an application', 'search about something',
            'search in youtube', 'open a website']

applications = {
    'google chrome': 'chrome.exe',
    'my editor': "Visual Studio Code.lnk",
}
print('our services :')
for j in services:
    print(j)


class Menu:
    """
        Menu to view all the available services;

        :ARGS:
            None;

    """

    SERVICES = ['open an application', 'search about something',
                'search in youtube', 'open a website']

    def draw(self):
        """
            :ARGS:
                None;

            :RETURNS:
                return None;

            :INFO:
                draw the menu on the terminal;
        """

        for index, service in enumerate(Menu.SERVICES, start=1):
            print(f"[{index}] {service}")


class Orders:
    """
        Consisting All the commands that can done by the script;

        :ARGS:
            None;

    """
    def OpenAnApp(app_name: str):
        os.startfile(applications[app_name])

    def OpenWebSite(name: str):
        webbrowser.open(name)

    def SearchAboutSomething(txt: str):
        webbrowser.open(f'https://www.google.com/search?q={txt}')

    def SearchInYoutube(txt: str):
        webbrowser.open(f'https://www.youtube.com/results?search_query={txt}')
