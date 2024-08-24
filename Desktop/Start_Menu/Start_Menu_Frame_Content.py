from tkinter import *
from Desktop.Settings_categories.SettingsMainWindow import SettingsWindows


class Start_Menu_Frame_Content01:
    def __init__(self, parent, root):
        self.parent = parent
        self.root = root
        self.pined_icons = {'Desktop/Images/edge.png': 'Edge', 'Desktop/Images/settings.png': 'Settings',
                            'Desktop/Images/Calendar.png': 'Calendar',
                            'Desktop/Images/File_Explorer.png': 'File Explorer'}
        self.recommended_icons = {'Desktop/Images/documents.png': '  Documents',
                                  'Desktop/Images/gmail.png': '  Gmail',
                                  'Desktop/Images/youtube.png': '  Youtube',
                                  'Desktop/Images/google_presentation.png': '  Presentations',
                                  'Desktop/Images/google_sheets.png': '  Tables',
                                  'Desktop/Images/google_drive.png': '  Google Disk'}
        self.pinned_buttons = []
        self.recommended_buttons = []
        self.search_bar()
        self.labels()
        self.pinned_icons()

    def search_bar(self):

        frame = Frame(self.parent, background='#F4F6F9')
        frame.grid(row=0, column=1, columnspan=14, sticky='w')

        search_icon = PhotoImage(file='Desktop/Images/search_icon.png')
        search_icon = search_icon.subsample(x=9, y=9)
        place_search_icon = Label(frame, image=search_icon, background='#F4F6F9')
        place_search_icon.image = search_icon
        place_search_icon.grid(row=0, column=0)

        search_bar = Entry(frame, width=60)
        search_bar.grid(row=0, column=1)

    def labels(self):
        label = Label(self.parent, text='Pinned', bg='#F4F6F9', font=('Segoe Ui', 10, 'bold'))
        label.grid(row=1, column=1, columnspan=3, sticky='w')
        recommended = Label(self.parent, text='Recommended', bg='#F4F6F9', font=('Segoe Ui', 10, 'bold'))
        recommended.grid(row=6, column=1, columnspan=3, sticky='w')

    def pinned_icons(self):

        for index, text in enumerate(self.pined_icons):
            icons = PhotoImage(file=f'{text}')
            icons = icons.subsample(x=8, y=8)
            label = Label(self.parent, text=self.pined_icons[text], image=icons, compound='top', width=64, height=64,
                          bg='#F4F6F9', font=('Segoe Ui', 9), padx=8)
            label.grid(row=2, column=index + 1, sticky='w')
            label.bind('<Enter>', lambda e, label=label: self.on_enter(e, label))
            label.bind('<Leave>', lambda e, label=label: self.on_leave(e, label))
            label.image = icons
            self.pinned_buttons.append(label)

        for index, content in enumerate(self.recommended_icons):
            icons = PhotoImage(file=f'{content}')
            icons = icons.subsample(x=9, y=9)
            label = Label(self.parent, image=icons, text=self.recommended_icons[content], compound='left', width=80,
                          height=50, bg='#F4F6F9', font=('Segoe Ui', 9), anchor='w')
            label.bind('<Enter>', lambda e, label=label: self.on_enter(e, label))
            label.bind('<Leave>', lambda e, label=label: self.on_leave(e, label))
            if index < 3:
                label.grid(row=index + 7, column=1, columnspan=4, sticky='ew')
            else:
                label.grid(row=index + 4, column=4, columnspan=4, sticky='ew')
            label.image = icons
            self.recommended_buttons.append(label)

        self.pinned_buttons[1].bind('<Button-1>', self.run_settings_menu)

    def on_enter(self, e, label):
        label.configure(bg='#E3E3E3')

    def on_leave(self, e, label):
        label.configure(bg='#F4F6F9')

    def run_settings_menu(self, e):
        a = SettingsWindows(self.parent.parent.root)
        self.parent.destroy()
        a.run()
