from __future__ import annotations

import json
import subprocess
import sys
from typing import Any, Dict

import streamlit as st

from src.inference import predict_query
from src.llm_refiner import refine_with_llm


st.set_page_config(page_title="Student Query Understanding", layout="centered")
st.title("Student Query Understanding")
st.caption("Classify intent, topic, and difficulty from a student query.")


def _train_models() -> None:
    subprocess.run(
        [sys.executable, "-m", "src.models"],
        check=True,
    )


def _render_json(obj: Dict[str, Any]) -> None:
    st.code(json.dumps(obj, indent=2), language="json")


with st.sidebar:
    st.subheader("Options")
    use_llm = st.checkbox("Refine with LLM", value=False)
    llm_model = st.text_input("LLM model", value="gpt-4o-mini", disabled=not use_llm)
    st.divider()
    st.write("If inference errors say models are missing, train once:")
    if st.button("Train / Re-train models", type="secondary"):
        with st.status("Training models… (first run may download embeddings model)", expanded=True):
            _train_models()
        st.success("Training complete. You can run inference now.")


query = st.text_area(
    "Student query",
    value="I don't understand backpropagation.",
    height=120,
)

run = st.button("Predict", type="primary", disabled=not query.strip())

if run:
    try:
        with st.status("Running ML inference…", expanded=False):
            ml_result = predict_query(query.strip())
        st.subheader("ML prediction")
        _render_json(ml_result)

        if use_llm:
            with st.status("Refining with LLM…", expanded=False):
                refined = refine_with_llm(query.strip(), ml_result, model=llm_model)
            st.subheader("LLM refinement")
            _render_json(refined)
    except Exception as e:  # Streamlit surface: show actionable error
        st.error(str(e))
