import functions
import PySimpleGUI as sg

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="enter to-do", key="todo", text_color="green")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True,
                      size=[45,10])
edit_button = sg.Button("Edit")


window = sg.Window("My To-Do App",
                   layout=[[label], [input_box,add_button],[list_box,edit_button]],
                   font=("Helvetica", 20))
# displays the window on the screen
while True:
    event, values = window.read()
    print(event,values)
    match event:
        case "Add":
            todos = functions.get_todos()
            print(values["todo"])
            todos.append(values["todo"] + "\n")
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":

            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            curr_todos = functions.get_todos()
            index_for_edit = curr_todos.index(todo_to_edit)
            curr_todos[index_for_edit] = new_todo + "\n"
            functions.write_todos(curr_todos)
            window["todos"].update(values=curr_todos)
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break
window.close()
