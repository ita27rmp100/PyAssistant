import webbrowser
import os


applications = {
    'google chrome': 'chrome.exe',
    'my editor': "Visual Studio Code.lnk",
}


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

        print("Our Services".center(70))

        for index, service in enumerate(Menu.SERVICES, start=1):
            print(f"[{index}] {service}")

        return None


class Orders:
    """
        Consisting All the commands that can done by the script;

        :ARGS:
            None;

    """
    def open_app(app_name: str):
        """
            :ARGS:
                app_name:str => the app you want to open;

            :RETURNS:
                return None;

            :INFO:
                open a specific app on your machine;
        """
        os.startfile(applications[app_name])

    def open_website(name: str):
        """
            :ARGS:
                name: str => the website you want to open;

            :RETURNS:
                return None;

            :INFO:
                open any website using your machine default browser;
        """
        webbrowser.open(name)

    def search_about_something(txt: str):
        """
            :ARGS:
                txt: str => the text you want to search about it;

            :RETURNS:
                return None;

            :INFO:
                search about any thing using google;
        """
        webbrowser.open(f'https://www.google.com/search?q={txt}')

    def search_in_youtube(txt: str):
        """
            :ARGS:
                txt: str => the text you want to search about it;

            :RETURNS:
                return None;

            :INFO:
                search about any thing in youtube;

        """
        webbrowser.open(f'https://www.youtube.com/results?search_query={txt}')
