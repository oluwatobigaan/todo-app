import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todo = todo.capitalize()
    todos.append(todo)
    functions.write_todos(todos)

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)


st.text_input(label="add todo", label_visibility="hidden", placeholder="Add new todo....",
              on_change=add_todo, key="new_todo")

print("HI")

st.session_state