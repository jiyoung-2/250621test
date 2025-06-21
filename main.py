import streamlit as st

st.set_page_config(page_title="MBTI 직업 추천기 🎯", page_icon="💼", layout="wide")

# 🎨 사용자 정의 CSS
st.markdown("""
    <style>
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #ff4b4b;
        text-align: center;
        margin-bottom: 30px;
    }
    .recommendation {
        font-size: 24px;
        padding: 20px;
        background-color: #f9f9f9;
        border-radius: 15px;
        margin-top: 20px;
        box-shadow: 2px 2px 10px #ccc;
    }
    .emoji-box {
        font-size: 50px;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 🎉 타이틀
st.markdown('<div class="title">🌈 나의 MBTI로 알아보는 꿈의 직업 💭</div>', unsafe_allow_html=True)

# 🎭 이모지 배너
st.markdown('<div class="emoji-box">🧠💡✨💼👩‍🚀👨‍🔬🎨🎤🛠️📚🎮🧑‍⚖️</div>', unsafe_allow_html=True)

# 📌 MBTI 선택
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

selected_mbti = st.selectbox("🧬 당신의 MBTI는 무엇인가요?", mbti_types)

# 💼 직업 추천 딕셔너리
job_recommendations = {
    "ISTJ": "🧮 회계사, 🏛️ 공무원, 🧑‍💼 관리자",
    "ISFJ": "🩺 간호사, 🧑‍🏫 교사, 👩‍🍳 제빵사",
    "INFJ": "🎨 예술가, 🧠 심리학자, ✍️ 작가",
    "INTJ": "👨‍💻 개발자, 🧑‍🔬 과학자, 🧮 전략기획자",
    "ISTP": "🛠️ 엔지니어, 🚗 정비사, 🚓 경찰관",
    "ISFP": "🎭 배우, 🎨 디자이너, 🧑‍🍳 셰프",
    "INFP": "✍️ 작가, 🎨 일러스트레이터, 🎭 예술가",
    "INTP": "🧠 연구원, 👨‍💻 프로그래머, 🤖 인공지능 개발자",
    "ESTP": "🎤 방송인, 🏋️‍♂️ 운동선수, 🧑‍🚒 소방관",
    "ESFP": "🎶 가수, 🧑‍🎤 연예인, 🎤 MC",
    "ENFP": "🌍 NGO 활동가, 🎭 창작가, 🎨 콘텐츠 크리에이터",
    "ENTP": "📣 마케팅 전문가, 🧠 기획자, 🎤 강연가",
    "ESTJ": "🏛️ 관리자, 📊 경영인, 🧑‍✈️ 군인",
    "ESFJ": "🧑‍🏫 교사, 💁‍♀️ 상담사, 🏥 의료 코디네이터",
    "ENFJ": "🎤 리더십 코치, 🌍 외교관, 🧑‍🏫 교육자",
    "ENTJ": "👔 CEO, 📈 사업가, 🧠 전략가"
}

# 🚀 결과 출력
if selected_mbti:
    st.markdown(f"""
        <div class="recommendation">
        <strong>{selected_mbti}</strong> 유형에게 추천하는 직업은...<br><br>
        <span style="font-size: 28px;">{job_recommendations[selected_mbti]}</span>
        </div>
    """, unsafe_allow_html=True)

# 🥳 푸터 이모지
st.markdown('<div class="emoji-box">🌟 꿈을 향해 나아가요! 🚀✨</div>', unsafe_allow_html=True)
