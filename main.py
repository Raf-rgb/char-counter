import streamlit as st

if "total_chars" not in st.session_state:
    st.session_state["total_chars"] = 0

if "total_words" not in st.session_state:
    st.session_state["total_words"] = 0

if "total_letters" not in st.session_state:
    st.session_state["total_letters"] = 0

if "text" not in st.session_state:
    st.session_state["text"] = None

special_caracters = [
    " ", ",", ".", 
    ":", ";", "(", 
    ")", "-", "/", 
    '"', "$", "%", 
    "#", "'", "!", 
    "¡", "¿", "?",
    "|", "°", "&",
]

def quit_special_chars(text:str, except_space:bool=False) -> str:
    chars_to_replace = special_caracters.copy()
    text_result      = text

    if except_space:
        chars_to_replace.remove(" ")
        print(special_caracters)
        
    for c in chars_to_replace:
        text_result = text_result.replace(c, "")

    print(text_result)

    return text_result

def main():
    st.header("Text counter")

    st.divider()

    col_total_chars, col_total_letters, col_total_words = st.columns(3)
    
    col_total_chars.metric("Total chars", st.session_state.total_chars)
    col_total_words.metric("Total words", st.session_state.total_words)
    col_total_letters.metric("Total letters", st.session_state.total_letters)

    st.divider()

    st.session_state.text = st.text_area("Text", st.session_state.text, height=500)
    

    if st.button("Count!", type="primary") and st.session_state.text is not None:
        text = st.session_state.text
        st.session_state.total_chars = len(list(text))
        st.session_state.total_words = len(quit_special_chars(text, True).strip().split(" ")) if text != "" else 0
        st.session_state.total_letters = len(quit_special_chars(text))

        st.rerun()

if __name__ == "__main__":
    main()