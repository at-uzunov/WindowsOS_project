from tkinter import *


class Drives:
    def __init__(self, parent):
        self.parent = parent
        self.fldrs = []
        self.fldrs_create = []
        self.drvrs = []
        self.switch = 0
        self.create_folders()
        self.foldrs_lbl()
        self.create_drivers()

    def create_folders(self):
        img_path = 'ThisPC/middle_frame/middle_frame_icons'
        self.imges = {f'{img_path}/3dobj.png': '3D Objects',
                      f'{img_path}/desktop.png': 'Desktop',
                      f'{img_path}/documents.png': 'Documents',
                      f'{img_path}/downloads.png': 'Downloads',
                      f'{img_path}/music.png': 'Music',
                      f'{img_path}/pictures.png': 'Pictures',
                      f'{img_path}/videos.png': 'Videos'}

        current_x = 0
        label_width = 160  # Adjust this to your label width
        current_row = 1
        column_index = 0

        for content in self.imges:
            img = PhotoImage(file=f'{content}')
            label = Label(self.parent, image=img, text=self.imges[content], compound='left',
                          width=label_width, anchor='w', bg='white')
            label.image = img
            label.bind('<Enter>', lambda e, label=label:self.on_enter(e, label))
            label.bind('<Leave>', lambda e, label=label:self.on_leave(e, label))

            print(current_x)
            if current_x + label_width + 40 > int(self.parent.winfo_width() * 800):
                current_x = 0
                current_row += 1
                column_index = 0
                label.grid(row=current_row, column=column_index, padx=(5, 0), pady=(5, 0))
                column_index += 1
            else:
                current_x += label_width
                label.grid(row=current_row, column=column_index, padx=(5, 0), pady=(5, 0))
                column_index += 1

            self.fldrs.append(label)

    def foldrs_lbl(self):
        img = PhotoImage(file='ThisPC/left_frame/left_frame_icons/quick_access/down.png')
        img = img.subsample(x=2, y=2)
        label = Label(self.parent, image=img, compound='left',
                      text=f'  Folders ({len(self.imges)}) {"-" * 107}',
                      font=('Segoe Ui', 12), anchor='w', bg='white')
        label.grid(row=0, column=0, columnspan=10, padx=(10, 0), pady=(10, 0), sticky='w')
        label.image = img

        label.bind('<Enter>', lambda e, label=label: self.on_enter(e, label))
        label.bind('<Leave>', lambda e, label=label: self.on_leave(e, label))

        label.bind('<Button-1>', lambda event, hierarchy=1, arr=self.fldrs: self.remove_content(hierarchy,arr))

    def create_drivers(self):
        imges = {'ThisPC/left_frame/left_frame_icons/thispc/c.png': 'Local Disk (C:)',
                 'ThisPC/left_frame/left_frame_icons/quick_access/newvolume.png': 'New Volume (D:)'}
        for index, content in enumerate(imges):
            # print(imges[i])
            img = PhotoImage(file=content)
            lbl = Label(self.parent, image=img, text=imges[content], compound='left', width=160, height=45,
                        font=('Segoe Ui', 10), anchor='w', bg='white')
            lbl.grid(row=6, column=index, pady=(10, 0), padx=(5, 0))
            lbl.image = img
            lbl.bind('<Enter>', lambda e, label=lbl:self.on_enter(e, label))
            lbl.bind('<Leave>', lambda e, label=lbl:self.on_leave(e, label))
            self.drvrs.append(lbl)

        down_img = PhotoImage(file='ThisPC/left_frame/left_frame_icons/quick_access/down.png')
        down_img = down_img.subsample(x=2, y=2)
        title_lbl = Label(self.parent, image=down_img,
                          text=f'  Devices and drives: ({len(self.drvrs)}) {"-" * 95}',
                          font=('Segoe Ui', 12), anchor='w', compound='left',bg='white')
        title_lbl.grid(row=5, column=0, columnspan=10, sticky='w', pady=(10, 0), padx=(10, 0))
        title_lbl.image = down_img
        title_lbl.bind('<Enter>', lambda e, label=title_lbl: self.on_enter(e, label))
        title_lbl.bind('<Leave>', lambda e, label=title_lbl: self.on_leave(e, label))
        title_lbl.bind('<Button-1>', lambda e, hierarchy=2, arr=self.drvrs: self.remove_content(hierarchy, arr))

    def on_enter(self, e, *argv):
        for i in argv:
            i.configure(background='lightblue1')

    def on_leave(self, e, *argv):
        for i in argv:
            i.configure(background='white')

    def remove_content(self, hierarchy, arr):
        self.switch += 1
        match self.switch:
            case 1:
                for i in arr:
                    i.grid_forget()
                print(f'Pressed {self.switch}')
            case 2:
                current_x = 0
                current_row = 1
                label_width = 160
                column_index = 0
                for i in arr:
                    if current_x + label_width + 40 > self.parent.winfo_width():
                        current_x = 0
                        current_row += 1
                        column_index = 0
                        if hierarchy == 1:
                            i.grid(row=current_row, column=column_index, padx=(5, 0), pady=(5, 0))
                            column_index += 1
                        elif hierarchy == 2:
                            i.grid(row=current_row + 5, column=column_index, padx=(5, 0), pady=(5, 0))
                            column_index += 1

                    else:
                        current_x += label_width
                        if hierarchy == 1:
                            i.grid(row=current_row, column=column_index, padx=(5, 0), pady=(5, 0))
                            column_index += 1
                        elif hierarchy == 2:
                            i.grid(row=current_row+5, column=column_index, padx=(5, 0), pady=(5, 0))
                            column_index += 1
                self.switch = 0
