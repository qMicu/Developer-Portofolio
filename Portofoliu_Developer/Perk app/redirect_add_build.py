import PySimpleGUI as sg
import sqlite3
import random
import subprocess


local_db = './SQLite_Python.db'
connection = sqlite3.connect(local_db)
db_cursor = connection.cursor()

dbd_theme = {'BACKGROUND': '#aea092',
                'TEXT': '#654933',
                'INPUT': '#874b26',
                'TEXT_INPUT': '#afa193',
                'SCROLL': '#837d77',
                'BUTTON': ('#afa193', '#874b26'),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}

sg.theme_add_new('DBD', dbd_theme)
sg.theme('DBD')





perk_list=["Ace in the Hole","Adrenaline","Aftercare","Alert","Any Means Necessary","Appraisal","Autodidact","Balanced Landing","Better than New","Bite the Bullet","Blast Mine","Blood Pact","Boil Over","Boon: Circle of Healing","Boon: Dark Theory","Boon: Exponential","Boon: Shadow Step","Bond","Borrowed Time","Botany Knowledge","Breakdown","Breakout","Buckle Up","Build to Last","Corrective Action","Counterforce","Clairvoyance","Dance With Me","Dark Sense","Dead hard","Deception","Decisive Strike","Déjà Vu","Deliverance","Desperate Measures","Detective's Hunch","Distortion","Diversion","Empathic Connection","Empathy","Fast Track","Flashbang","Flip-Flop","Fogwise","For the People","Guardian","Head On","Hope","Hyperfocus","Inner Focus","Inner healing","Iron Will","Kindred","Kinship","Leader","Left Behind","Lightweight","Lithe","Low Profile","Lucky Break","Mettle of Man","No Mither","No One Left Behind","Object of Obsession","Off the Record","Open Handed","Overcome","Overzealous","Parental Guidance","Pharmacy","Plunderer's Instinct","Poised","Potential Energy","Power Struggle","Premonition","Prove Thyself","Quick Gambit","Quick & Quiet","Reactive Healing","Reassurance","Red Herring","Renewal","Repressed Alliance","Residual Manifest","Resilience","Resurgence","Rookie Spirit","Saboteur","Self-Aware","Self-Care","Self-Preservation","Situational Awarness","Slippery Meat","Small Game","Smash Hit","Sole Survivor","Solidarity","Soul Guard","Spine Chill","Sprint Burst","Stake Out","Streetwise","Tehnician","Tenacity","This Is Not Happening","Unbreakable","Up the Ante","Urban Evasion","Vigil","Visionary","Wake Up","We'll Make It","We're Gonna Live Forever","Windows of Opportunity","Wiretap"]
layout_add = [[sg.Push(),sg.Text('What is the name of the build?'),sg.Push()],
        [sg.Push(),sg.Text("Build Name"),sg.Input(key='build_name'), sg.Push()],
        [sg.Combo(perk_list,size=(42,1),enable_events=True, key='combo_perk_1',readonly=True,default_value="Select a perk"),sg.Combo(perk_list,size=(42,1),enable_events=True, key='combo_perk_2',readonly=True,default_value="Select a perk"),sg.Combo(perk_list,size=(42,1),enable_events=True, key='combo_perk_3',readonly=True,default_value="Select a perk"),sg.Combo(perk_list,size=(42,1),enable_events=True, key='combo_perk_4',readonly=True,default_value="Select a perk")],
        [sg.Push(),sg.Submit("Create Build"),sg.Cancel("Cancel"),sg.Push()],]


headings = ["Build Name","First Perk","Second Perk","Third Perk","Fourth Perk"]
sql_datashow_name = """SELECT NAME,PERK_1,PERK_2,PERK_3,PERK_4 FROM Perk_builds"""
i = 0
db_cursor.execute(sql_datashow_name)
test = db_cursor.fetchall()
data = [test[0]]
for index in test:
    try:
        i += 1
        data.append(test[i])
    except IndexError:
        break


alt_data = data[1:]
layout_builds = [[sg.Table(alt_data, headings=headings, key='-TABLE-')],
                 [sg.Push(),sg.Push(),sg.Push(),sg.Push(),sg.Push(),sg.Text("YOU NEED TO REFRESH TO SEE NEW CHANGES!" ,text_color="#874b26",),sg.Push(),sg.Push(),sg.Push(),sg.Push(),],
                 [sg.Submit("Delete Build",size=(10,1)),sg.Push(),sg.Submit("Get Random Build",size=(14,1)),sg.Submit("Refresh",size=(10,1)),sg.Push()]]

tabgrp=[[sg.TabGroup([[sg.Tab("Your Builds",layout_builds),sg.Tab("New Build",layout_add)]])]]

window = sg.Window('Perk Randomizer',icon="./Freddy.ico",size = (1280,720),resizable=False, layout = tabgrp, auto_size_buttons=False,default_button_element_size=(30,1),use_default_focus=False, finalize=True)

def new_del_win():
    del_lay = [[sg.Push(),sg.Text("The name of the build you want to delete is:"),sg.Push()],
               [sg.Push(),sg.InputText(key = "-DEL-"),sg.Push()],
               [sg.Push(),sg.Submit("Submit"),sg.Cancel(),sg.Push()]]
    
    del_win = sg.Window("Delete Build",layout=del_lay,icon="./Freddy.ico")
    event_del,values_del = del_win.read()
    del_win.close()
    del_input = values_del["-DEL-"]
    sql_delete =  """DELETE FROM Perk_builds WHERE NAME=?"""
    if del_input == "DO":
        pass
    else:
        db_cursor.execute(sql_delete,(del_input,))
        connection.commit() 
    if event_del == "Submit":
        if del_input == "DO":
            sg.Popup("Acces Interzis",icon="./Freddy.ico")
        else:
            sg.Popup("Build "+ str(del_input) + " has been deleted!",icon="./Freddy.ico")
 


while True:
    event,values = window.read()
    if event == "Get Random Build":
        try:
            x = random.choices(alt_data)
            if sg.Window("Random Build", [[sg.Push(),sg.Text("Your build is:"),sg.Push()],
                                        [sg.Table(x,headings=headings)], 
                                        [sg.Yes("Ok")]]).read(close=True)[0] == "Ok":
                pass
        except IndexError:
            sg.Popup("You need to add a build first",custom_text = "Ok",title = "Error", button_color="red",icon="./Freddy.ico" )


    if event == "Refresh":
        sp = subprocess.Popen("./redirect_add_build.exe", stdin=subprocess.PIPE)  
        window.close()

    if event == "Delete Build":
        new_del_win()

    if event == "Create Build":
        a = list(values)
        combo_1 = values['combo_perk_1']
        combo_2 = values['combo_perk_2']
        combo_3 = values['combo_perk_3']
        combo_4 = values['combo_perk_4']
        build_names = values['build_name']
        perks = (build_names,combo_1,combo_2,combo_3,combo_4)


        if combo_1 == '' or combo_2 == '' or combo_3 == '' or combo_4 == '' or build_names == '' or combo_1 == 'Select a perk' or combo_2 == 'Select a perk' or combo_3 == 'Select a perk' or combo_4 == 'Select a perk':
            sg.Popup("All fields need to be completed (Perks + Name)!",custom_text="Ok",button_color="red",line_width=(500),title="Error",modal=True,icon="./Freddy.ico")
        elif combo_1 == combo_2 or combo_1 == combo_3 or combo_1 == combo_4 or combo_2 == combo_3 or combo_2 == combo_4 or combo_3 == combo_4:
            sg.Popup("You can't add the same perk twice",custom_text="Ok",button_color="red",line_width=(500),title="Error",modal=True,icon="./Freddy.ico")
        else:
            try:
                sql_select = """INSERT INTO Perk_builds(NAME,PERK_1,PERK_2,PERK_3,PERK_4) VALUES(?,?,?,?,?)"""
                db_cursor.execute(sql_select,perks)
                connection.commit()

                sg.Popup("Your build has been registered!",custom_text="Ok",title="Succes",modal=True,icon="./Freddy.ico")

            except sqlite3.IntegrityError:
                sg.Popup("You have another build with this name.",custom_text="Ok",button_color="red",line_width=(500),title="Error",modal=True,icon="./Freddy.ico")


    if event == sg.WIN_CLOSED or event == "Cancel":
        connection.close()
        break
window.close()
