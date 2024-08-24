if self.middle_frame == 0:
    for i in self.category_storage:
        try:
            i.destroy()
        except:
            print('cat destroy')
    self.category_storage[0] = SystemSettings(self)
elif self.middle_frame == 1:
    for i in self.category_storage:
        try:
            i.destroy()
        except:
            print('cat destroy')
    self.category_storage[1] = BluetoothSettings(self)
elif self.middle_frame == 2:
    for i in self.category_storage:
        try:
            i.destroy()
        except:
            print('cat destroy')
    self.category_storage[2] = NetworkSettings(self)
elif self.middle_frame == 3:
    for i in self.category_storage:
        try:
            i.destroy()
        except:
            print('cat destroy')
    self.category_storage[3] = PersonalizationSettings(self)
elif self.middle_frame == 4:
    for i in self.category_storage:
        try:
            i.destroy()
        except:
            print('cat destroy')
    self.category_storage[4] = AppsSettings(self)
elif self.middle_frame == 5:
    for i in self.category_storage:
        try:
            i.destroy()
        except:
            print('cat destroy')
    self.category_storage[5] = AccountsSettings(self)
else:

    for i in self.category_storage:
        try:
            i.destroy()
        except:
            print('cat destroy')
    print(self.category_storage)