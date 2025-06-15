import streamlit as st
import pandas as pd
import random

# CSVの読み込み（最初に一度だけ）
@st.cache_data
def load_data():
    return pd.read_csv("lipid_quiz_100.csv")

df = load_data()

st.set_page_config(page_title="脂質クイズ100", layout="centered")
st.title("🧠 脂質領域クイズアプリ（100問）")

# セッション内で問題を保持（最初の1問）
if "question_idx" not in st.session_state:
    st.session_state.question_idx = random.randint(0, len(df) - 1)
    st.session_state.answered = False

# 現在の問題データ
row = df.iloc[st.session_state.question_idx]
choices = row["options"].split(";")

# 問題の表示
st.markdown(f"### Q{row['id']}: {row['question']}")
user_answer = st.radio("選択肢を選んでください", choices, key="answer")

# 答え合わせボタン
if st.button("✅ 答え合わせ"):
    st.session_state.answered = True
    if user_answer == row["answer"]:
        st.success("正解です！🎉")
    else:
        st.error(f"不正解です。正解は「{row['answer']}」です。")
    st.info(f"📝 解説: {row['explanation']}")

# 次の問題へ
if st.session_state.answered:
    if st.button("➡️ 次の問題へ"):
        st.session_state.question_idx = random.randint(0, len(df) - 1)
        st.session_state.answered = False
        st.rerun()

