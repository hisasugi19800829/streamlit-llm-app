import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

def query_expert(user_input: str, expert: str) -> str:
    # 専門家ごとのシステムプロンプト
    if expert == "ファッションスタイリスト":
        system_prompt = "あなたは優秀なファッションスタイリストです。"
    elif expert == "栄養士":
        system_prompt = "あなたは経験豊富な栄養士です。"
    elif expert == "旅行プランナー":
        system_prompt = "あなたはプロの旅行プランナーです。"
    else:
        system_prompt = "あなたは優秀な専門家です。"

    # ChatOpenAI の呼び出し
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.0)

    # メッセージを組み立てて API 呼び出し
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input),
    ]
    ai_message = llm(messages)  # ここで AIMessage が返る
    return ai_message.content

def main():
    st.title("👩‍⚕️👗👨‍💼 専門家チャットアプリ")

    # 専門家の選択肢
    experts = ["ファッションスタイリスト", "栄養士", "旅行プランナー", "その他"]
    expert = st.selectbox("専門家を選択してください", experts)

    # 質問入力
    user_input = st.text_area("質問を入力", height=150)

    # 送信ボタン
    if st.button("送信"):
        if not user_input.strip():
            st.warning("質問を入力してください。")
        else:
            with st.spinner("専門家が考え中…"):
                try:
                    answer = query_expert(user_input, expert)
                    st.markdown("**回答:**")
                    st.write(answer)
                except Exception as e:
                    st.error(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()

# --- Streamlit UI ---
st.title("専門家チャットアプリ")

expert = st.radio(
    "専門家を選択してください：",
    ("ファッションスタイリスト", "栄養士", "旅行プランナー")
)

user_input = st.text_area("質問を入力してください：", height=150)

if st.button("送信"):
    if not user_input.strip():
        st.warning("質問を入力してください。")
    else:
        with st.spinner("回答生成中..."):
            answer = query_expert(user_input, expert)
        st.subheader("回答")
        st.write(answer)