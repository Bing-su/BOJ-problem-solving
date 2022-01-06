from pathlib import Path
import streamlit as st

root = Path(".")

path_num_map = {p: p.name.removesuffix(".py") for p in root.glob("problem/**/*.py")}
options = sorted(path_num_map.keys())

with st.sidebar:
    st.image("sundae.png")
    selected = st.selectbox(
        "Select Problem", options, format_func=lambda s: path_num_map[s]
    )
    st.markdown("[Github](https://github.com/Bing-su)")

with selected.open(encoding="utf-8") as file:
    code = file.read()

first_line = code.splitlines()[0]
if first_line.startswith("#"):
    st.markdown(first_line)

num = path_num_map[selected]
st.markdown(f"[Link](https://www.acmicpc.net/problem/{num})")
st.code(code)
