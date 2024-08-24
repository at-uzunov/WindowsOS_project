from Desktop.Start_Menu.Start_Menu_Frame import Start_Menu_Frame
from ThisPC.screen_setup import MainScreen
from CollectionManager.collection_manager import CManager_Ui

class ButtonActions:
    def __init__(self, parent):
        self.parent = parent
        self.settings_count = 0
        self.start_menu_frame = None

    def thispc_run(self,e):
        thispc_menu = MainScreen(self.parent.root)

    def collection_manager(self, e):
        c_manager = CManager_Ui(self.parent.root)
        c_manager.run()

    def place_frame(self):
        self.settings_count += 1
        if self.settings_count % 2 != 0:
            self.start_menu_frame = Start_Menu_Frame(self.parent)
        else:
            if self.start_menu_frame:
                self.start_menu_frame.destroy()
                self.settings_count = 0
