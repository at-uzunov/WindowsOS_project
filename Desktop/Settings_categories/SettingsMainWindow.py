from tkinter import *

from Desktop.Settings_categories.Settings_System import SystemSettings
from Desktop.Settings_categories.Settings_Left_Frame import LeftFrame
from Desktop.Settings_categories.Settings_Bluetooth import BluetoothSettings
from Desktop.Settings_categories.Settings_Network import NetworkSettings
from Desktop.Settings_categories.Settings_Personalization import PersonalizationSettings
from Desktop.Settings_categories.Settings_Apps import AppsSettings
from Desktop.Settings_categories.Settings_Accounts import AccountsSettings
from Desktop.Settings_categories.Settings_Time import TimeSettings
from Desktop.Settings_categories.Settings_Accessibility import AccessibilitySettings
from Desktop.Settings_categories.Settings_Privacy import PrivacySettings
from Desktop.Settings_categories.Settings_WinUpdate import WinUpdateSettings
from Desktop.Settings_categories.Settings_Hello import LinedInSettings


class SettingsWindows(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.middle_frame = None
        self.category_storage = {
            0: SystemSettings,
            1: BluetoothSettings,
            2: NetworkSettings,
            3: PersonalizationSettings,
            4: AppsSettings,
            5: AccountsSettings,
            6: TimeSettings,
            7: AccessibilitySettings,
            8: PrivacySettings,
            9: WinUpdateSettings,
            10: LinedInSettings
        }
        self.cat_store = [None] * 11
        self.configure(background='#F3F3F3')
        for i in range(25):
            self.columnconfigure(i, minsize=64)
            self.rowconfigure(i, minsize=64)

    def window_placement(self):
        root_x, root_y = self.parent.winfo_x(), self.parent.winfo_y()
        settings_x = int(root_x * 2.1)
        settings_y = int(root_y * 3)
        screen_width, screen_height = int(self.parent.winfo_width() * 0.8), int(self.parent.winfo_height() * 0.8)
        self.geometry(f"{screen_width}x{screen_height}+{settings_x}+{settings_y}")
        self.wm_transient(self.parent)

    def button_try(self):
        button = Button(self, text='test')
        button.grid(row=1, column=18)

    def left_frame_hold(self):
        left_frame = LeftFrame(self)

    def system_settings(self):
        for i in self.cat_store:
            try:
                i.destroy()
            except:
                continue
        selected_category = self.category_storage.get(self.middle_frame)

        if selected_category is not None:
            self.cat_store[self.middle_frame] = selected_category(self)

    def run(self):
        self.window_placement()
        self.left_frame_hold()
        self.system_settings()
        self.button_try()
        self.mainloop()
