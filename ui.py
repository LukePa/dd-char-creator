import tkinter
import character

class Application(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        
        self.character = character.Character()
        self.create_score_allocate_widgets()
        
        


    def create_score_allocate_widgets(self):
        str_label = tkinter.Label(text='Str:')
        str_label.grid(row=1,column=1)
        dec_str_button = tkinter.Button(text='<-',
                                        command = self.character.dec_str)
        dec_str_button.grid(row = 1, column = 2)
        self.str_display_label = tkinter.Label(text=self.character.get_str())
        self.str_display_label.grid(row=1,column=3)
        inc_str_button = tkinter.Button(text='->',
                                        command = self.character.inc_str)
        inc_str_button.grid(row = 1, column = 4)


        dex_label = tkinter.Label(text='Dex:')
        dex_label.grid(row=2,column=1)
        dec_dex_button = tkinter.Button(text='<-',
                                        command = self.character.dec_dex)
        dec_dex_button.grid(row = 2, column = 2)
        self.dex_display_label = tkinter.Label(text=self.character.get_dex())
        self.dex_display_label.grid(row=2,column=3)
        inc_dex_button = tkinter.Button(text='->',
                                        command = self.character.inc_dex)
        inc_dex_button.grid(row = 2, column = 4)


        con_label = tkinter.Label(text='Con:')
        con_label.grid(row=3,column=1)
        dec_con_button = tkinter.Button(text='<-',
                                        command = self.character.dec_con)
        dec_con_button.grid(row = 3, column = 2)
        self.con_display_label = tkinter.Label(text=self.character.get_con())
        self.con_display_label.grid(row=3,column=3)
        inc_con_button = tkinter.Button(text='->',
                                        command = self.character.inc_con)
        inc_con_button.grid(row = 3, column = 4)


        int_label = tkinter.Label(text='Int:')
        int_label.grid(row=4,column=1)
        dec_int_button = tkinter.Button(text='<-',
                                        command = self.character.dec_int)
        dec_int_button.grid(row = 4, column = 2)
        self.int_display_label = tkinter.Label(text=self.character.get_int())
        self.int_display_label.grid(row=4,column=3)
        inc_int_button = tkinter.Button(text='->',
                                        command = self.character.inc_int)
        inc_int_button.grid(row = 4, column = 4)


        wis_label = tkinter.Label(text='Wis:')
        wis_label.grid(row=5,column=1)
        dec_wis_button = tkinter.Button(text='<-',
                                        command = self.character.dec_wis)
        dec_wis_button.grid(row = 5, column = 2)
        self.wis_display_label = tkinter.Label(text=self.character.get_wis())
        self.wis_display_label.grid(row=5,column=3)
        inc_wis_button = tkinter.Button(text='->',
                                        command = self.character.inc_wis)
        inc_wis_button.grid(row = 5, column = 4)


        cha_label = tkinter.Label(text='Cha:')
        cha_label.grid(row=6,column=1)
        dec_cha_button = tkinter.Button(text='<-',
                                        command = self.character.dec_cha)
        dec_cha_button.grid(row = 6, column = 2)
        self.cha_display_label = tkinter.Label(text=self.character.get_cha())
        self.cha_display_label.grid(row=6,column=3)
        inc_cha_button = tkinter.Button(text='->',
                                        command = self.character.inc_cha)
        inc_cha_button.grid(row = 6, column = 4)

        points_label = tkinter.Label(text='Points Remaining:')
        points_label.grid(row=1, column=5)
        self.points_remaining_label = tkinter.Label(text=self.character.points)
        self.points_remaining_label.grid(row=1, column=6)

    def update_point_allocate(self):
        
        
        
        
root = tkinter.Tk()
a = Application(master=root)
a.mainloop()
