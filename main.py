from pathlib import Path
import streamlit as st


@st.cache
def get_options() -> tuple[dict[Path, str], list[Path]]:
    root = Path(".")
    path_to_name = {p: p.name.removesuffix(".py") for p in root.glob("problem/**/*.py")}
    options = sorted(path_to_name.keys(), key=lambda k: int(path_to_name[k].split()[0]))
    return path_to_name, options


path_to_name, options = get_options()

with st.sidebar:
    st.image("sundae.png")
    selected: Path = st.selectbox(
        "Select Problem", options, format_func=lambda s: path_to_name[s]
    )
    st.markdown("[Github](https://github.com/Bing-su)")

with selected.open(encoding="utf-8") as file:
    code = file.read()

num, name = path_to_name[selected].split(maxsplit=1)
st.title(f"{num} {name}")
st.markdown(f"[Link](https://www.acmicpc.net/problem/{num})")
st.code(code)
