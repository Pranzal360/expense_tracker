# imports
from kivy.lang import Builder
from kivy.utils import rgba
from kivymd.uix.boxlayout import MDBoxLayout,BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from datetime import datetime

from datetime import datetime
from kivymd.uix.list import ThreeLineAvatarIconListItem
import sqlite3
from sqlite3.dbapi2 import Cursor
from kivy.core.window import Window
import sqlite3

##### D A T A B A S E ##########################################################################################
from database  import Database

db = Database()

##### D A T A B A S E ##########################################################################################

################################# HELPER $#################################################################
helper ="""

<Content1>:
    orientation:'vertical'
    spacing: "5dp"
    size_hint: .9, None
    height: "200dp"
    MDTextField:
        id:itemName1
        hint_text:"Item Name 1"
        
       
    MDTextField:
        id:cost1
        hint_text:"Cost 1"
    MDRaisedButton:
        text:'Cancel'
        pos_hint:{'center_x':.5,'center_y':.5}
        on_press:app.close1()

    MDRaisedButton:
        text:'Save'
        pos_hint:{'center_x':.5,'center_y':.3}
        on_press:(app.add_data_to_list1(itemName1,cost1),app.close1())
<Content2>:
    orientation:'vertical'
    spacing: "5dp"
    size_hint: .9, None
    height: "200dp"
    MDTextField:
        id:itemName2
        hint_text:"Item Name 2 "     
    MDTextField:
        id:cost2
        hint_text:"Cost 2"
    MDRaisedButton:
        text:'Cancel'
        pos_hint:{'center_x':.5,'center_y':.5}
        on_press:app.close2()
    MDRaisedButton:
        text:'Save'
        pos_hint:{'center_x':.5,'center_y':.3}
        on_press:(app.add_data_to_list2(itemName2,cost2),app.close2())

<Content3>:
    orientation:'vertical'
    spacing: "5dp"
    size_hint: .9, None
    height: "200dp"
    MDTextField:
        id:itemName3
        hint_text:"Item Name 3 "
       
    MDTextField:
        id:cost3
        hint_text:"Cost 3"
    MDRaisedButton:
        text:'Cancel'
        pos_hint:{'center_x':.5,'center_y':.5}
        on_press:app.close3()

    MDRaisedButton:
        text:'Save'
        pos_hint:{'center_x':.5,'center_y':.3}
        on_press:(app.add_data_to_list3(itemName3,cost3),app.close3())
<ListItemWithCheckbox1>:
    id: the_list_item1
    markup: True

    IconRightWidget:
        icon: 'trash-can-outline'
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        on_release:
            root.delete_item1(the_list_item1)
    IconLeftWidget:
        icon:'format-list-bulleted'
<ListItemWithCheckbox2>:
    id: the_list_item2
    markup: True

    IconRightWidget:
        icon: 'trash-can-outline'
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        on_release:
            root.delete_item2(the_list_item2)
    IconLeftWidget:
        icon:'format-list-bulleted'
<ListItemWithCheckbox3>:
    id: the_list_item3
    markup: True

    IconRightWidget:
        icon: 'trash-can-outline'
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1
        on_release:
            root.delete_item3(the_list_item3)
    IconLeftWidget:
        icon:'format-list-bulleted'

MDBoxLayout:
    orientation:'vertical'

    MDToolbar:
        title:'ADD YOUR EXPENSES'
        anchor_title: "center"
        mode:'free-end'
        md_bg_color: rgba(1,1,1,1)
        specific_text_color:app.theme_cls.accent_color
    MDTabs:
        id:tabs
        icon:'plus'
        background_color: rgba(1,1,1,1)
        text_color_normal: 1,1,1,1
        text_color_active : 1,1,.5,1


        Tab:
            title:'Page 1'
            ScrollView:
                MDList:
                    id:list1
            MDFloatingActionButton:
                icon: "plus"
                md_bg_color: app.theme_cls.accent_color
                pos_hint:{'center_x':.9,'center_y':.17}
                on_press:app.show_task_dialog1()
        Tab:
            title:'Page 2'
            text_color:1,1,1,1
            ScrollView:
                MDList:
                    id:list2
            MDFloatingActionButton:
                icon: "plus"
                md_bg_color: app.theme_cls.accent_color
                pos_hint:{'center_x':.9,'center_y':.17}
                on_press:app.show_task_dialog2()
        Tab:
            title:'Page 3'
            ScrollView:
                MDList:
                    id:list3
            MDFloatingActionButton:
                icon: "plus"
                md_bg_color: app.theme_cls.accent_color
                pos_hint:{'center_x':.9,'center_y':.17}
                on_press:app.show_task_dialog3()

"""
################################# HELPER $#################################################################

############## CLASSES  ###############################################
class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''

class ListItemWithCheckbox1(ThreeLineAvatarIconListItem):
    '''Custom list item'''
    

    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        # state a pk which we shall use link the list items with the database primary keys
        self.pk = pk
    # DELETING ITEM FROM THE PAGE 1
    def delete_item1(self, the_list_item1):
        '''Delete the task'''
        self.parent.remove_widget(the_list_item1)
        db.deleteData1(the_list_item1.pk)# Here



class ListItemWithCheckbox2(ThreeLineAvatarIconListItem):
    '''Custom list item'''
    

    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        # state a pk which we shall use link the list items with the database primary keys
        self.pk = pk
    # DELETING ITEM FROM THE PAGE 2
    def delete_item2(self, the_list_item2):
        '''Delete the task'''
        self.parent.remove_widget(the_list_item2)
        db.deleteData2(the_list_item2.pk)

class ListItemWithCheckbox3(ThreeLineAvatarIconListItem):
    '''Custom list item'''
    

    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        # state a pk which we shall use link the list items with the database primary keys
        self.pk = pk
    # DELETING ITEM FROM THE PAGE 1
    def delete_item3(self, the_list_item3):
        '''Delete the task'''
        self.parent.remove_widget(the_list_item3)
        db.deleteData3(the_list_item3.pk)# Here
#SEPARATED CONTAINER FOR PAGE 1

class Content1(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
#SEPARATED CONTAINER FOR PAGE 2
        
class Content2(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
#SEPARATED CONTAINER FOR PAGE 3
class Content3(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class mainApp(MDApp):
    dialog1 = None
    dialog2 = None
    dialog3 = None

    def build(self):

        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "Indigo"
        self.theme_cls.theme_style = "Dark"
        # INITIALIZING THE BUILDER
        self.a = Builder.load_string(helper)
        return self.a
    # SEPARATED DIALOG BOX FOR PAGE 1
    def show_task_dialog1(self):
        if not self.dialog1:
            self.dialog1 = MDDialog(
                title="Create Task",
                type="custom",
                radius=[20, 7, 20, 7],
                content_cls=Content1(),
            )
        self.dialog1.open()
    # SEPARATED DIALOG BOX FOR PAGE 2
    def show_task_dialog2(self):
        if not self.dialog2:
            self.dialog2 = MDDialog(
                title="Create Task",
                type="custom",
                radius=[20, 7, 20, 7],
                content_cls=Content2(),
            )
        self.dialog2.open()

    # SEPARATE DIALOG BOX FOR THE PAGE 3
    def show_task_dialog3(self):
        if not self.dialog3:
            self.dialog3 = MDDialog(
                title="Create Task",
                type="custom",
                radius=[20, 7, 20, 7],
                content_cls=Content3(),
            )
        self.dialog3.open()

    def on_start(self):
        """GET DATA FROM DB AND CREATE TABLE IF DOESN'T EXISTS"""
        # CREATING TABLES AT THE FIRST PLACE
        db.create_table1()
        db.create_table2()
        db.create_table3()
        # FETCHING THE DATA FROM THE FUCNTION FETCHDATA1
        data1 = db.fetchData1()
        for thing1 in data1:
            # ADD THE VALUE TO THE PLACEHOLDER OF ID = LIST1
            self.root.ids.list1.add_widget(ListItemWithCheckbox1(pk = thing1[0] ,text=str(thing1[1]),
            secondary_text=str(thing1[2]),
            tertiary_text=str(thing1[3]),
            ))

        data2 = db.fetchData2()
        for thing2 in data2:
            # ADD THE VALUE TO THE PLACEHOLDER OF ID = LIST2
            self.root.ids.list2.add_widget(ListItemWithCheckbox2(pk = thing2[0] ,text=str(thing2[1]),secondary_text=str(thing2[2]),tertiary_text=str(thing2[3])))
        data3 = db.fetchData3()
        for thing3 in data3:
            # ADD THE VALUE TO THE PLACEHOLDER OF ID = LIST2
            self.root.ids.list3.add_widget(ListItemWithCheckbox3(pk = thing3[0] ,text=str(thing3[1]),secondary_text=str(thing3[2]),tertiary_text=str(thing3[3])))
    def add_data_to_list1(self,item,cost):
        '''send and retrive from DB'''
        dateTime = datetime.now()
        item = item.text
        cost = cost.text
        list1 = [
            (item,cost,dateTime)
        ]
        self.root.ids.list1.clear_widgets()
        # ADD THE LIST TO DATABASE NO 3
        ab= db.addIntoDB1(list1)
        things1 = db.fetchData1()
        for thing1 in things1:
            # ADD THE VALUE TO THE PLACEHOLDER OF ID = LIST1
            self.root.ids.list1.add_widget(ListItemWithCheckbox1(pk = thing1[0] ,text=str(thing1[1]),secondary_text=str(thing1[2]),tertiary_text=str(thing1[3])))

    # data added to the list of page 2
    def add_data_to_list2(self,item2,cost2):
        '''send and retrive from DB'''
        dateTime = datetime.now()
        item2 = item2.text
        cost2 = cost2.text
        list2 = [
            (item2,cost2,dateTime)
        ]
        self.root.ids.list2.clear_widgets()
        # ADD THE LIST TO DATABASE NO 3
        ab= db.addIntoDB2(list2)
        things2 = db.fetchData2()
        for thing2 in things2:
            # ADD THE VALUE TO THE PLACEHOLDER OF ID = LIST2
            self.root.ids.list2.add_widget(ListItemWithCheckbox2(pk = thing2[0] ,text=str(thing2[1]),secondary_text=str(thing2[2]),tertiary_text=str(thing2[3])))
    # data added to the list of page 3
    def add_data_to_list3(self,item3,cost3):
        '''send and retrive from DB'''
        dateTime = datetime.now()
        
        # CHANGING ALL THE VALUES TO THE STRING FORM OR GETTING INTO TEXT
        item3= item3.text
        cost3 = cost3.text
        # CREATING THE LIST SO THAT THE VALUE INPUT BECOMES EASY IN DATABASE
        list3 =[
            (item3,cost3,dateTime)
        ]
        #CLEAR THE PRELISTED WIDGETS OF PAGE 3
        self.root.ids.list3.clear_widgets()
        # ADD THE LIST TO DATABASE NO 3
        ab= db.addIntoDB3(list3)
        things3 = db.fetchData3()
        for thing3 in things3:
            # ADD THE VALUE TO THE PLACEHOLDER OF ID = LIST2
            self.root.ids.list3.add_widget(ListItemWithCheckbox3(pk = thing3[0] ,text=str(thing3[1]),secondary_text=str(thing3[2]),tertiary_text=str(thing3[3])))
            
    

    # CLOSE ALL DIALOGE BOXES    
    def close1(self,*args):
        self.dialog1.dismiss()
    def close2(self,*args):
        self.dialog2.dismiss()
    def close3(self,*args):
        self.dialog3.dismiss()
        
        

mainApp().run()
############## CLASSES  ###############################################