import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Type in a to-do")
add_button = sg.Button("Add")

window = sg.Window("To-Do List", layout=[[label], [input_box, add_button]])
window.read()
window.close()