import streamlit as st
import pandas as pd
import random

# CSVを読み込む
df = pd.read_csv("lipid_quiz_100.csv")

st.set_page_config(page_title="脂質クイズ100", layout="centered")
st.title("🧠 脂質領域クイズアプリ（100問）")

# ランダムに1問を選ぶ
question = df.sample(1).iloc[0]

st.markdown(f"### Q: {question['question']}")

# 選択肢を分解して表示
choices = question['options'].split(";")
user_answer = st.radio("選択肢を選んでください", choices)

# 答え合わせボタン
if st.button("答え合わせ"):
    if user_answer == question["answer"]:
        st.success("✅ 正解です！")
    else:
        st.error(f"❌ 不正解。正解は **{question['answer']}** です。")
    st.info(f"📝 解説: {question['explanation']}")
