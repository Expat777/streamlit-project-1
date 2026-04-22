import streamlit as st
# st.title('hell world!!!')

# st.title('calculator')

# val_1 = st.number_input('Insert a number', key = 'val_1')
# val_2 = st.number_input('Insert a number',key = 'val_2')

# st.write(f'result{val_1 + val_2}')

 

name = st.text_input('what is you name?', placeholder=' put you name ...')
st.write(f'Hello {name}!')

if 'show_text' not in st.session_state:
    st.session_state.show_text = False

def show_handler():
    st.session_state.show_text = not st.session_state.show_text



st.button('**please click**', on_click= show_handler)


if st.session_state.show_text:
    st.write('hide message ')

