import streamlit as st

st.set_page_config(page_title="MBTI 직업 추천기 🎯", page_icon="💼", layout="wide")

# 사용자 정의 CSS
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
    .reason {
        font-size: 20px;
        background-color: #fff8e1;
        padding: 15px;
        border-left: 8px solid #ffb74d;
        margin-top: 20px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 타이틀
st.markdown('<div class="title">🌈 나의 MBTI로 알아보는 꿈의 직업 💭</div>', unsafe_allow_html=True)

# 이모지 배너
st.markdown('<div class="emoji-box">🧠💡✨💼👩‍🚀👨‍🔬🎨🎤🛠️📚🎮🧑‍⚖️</div>', unsafe_allow_html=True)

# MBTI 선택
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]
selected_mbti = st.selectbox("🧬 당신의 MBTI는 무엇인가요?", mbti_types)

# MBTI 특성 및 추천 직업 + 이유
mbti_info = {
    "ISTJ": {
        "traits": "🧱 신중하고 책임감 있으며 현실적이고 체계적인 성격",
        "jobs": "🧮 회계사, 🏛️ 공무원, 🧑‍💼 관리자",
        "reason": "정확성과 규칙을 중요시하는 ISTJ는 안정적이고 구조화된 환경에서 최고의 성과를 냅니다."
    },
    "ISFJ": {
        "traits": "🌷 친절하고 조용하며 헌신적인 성격",
        "jobs": "🩺 간호사, 🧑‍🏫 교사, 👩‍🍳 제빵사",
        "reason": "도움을 주는 일을 좋아하며 세심한 배려가 필요한 직업에 잘 어울립니다."
    },
    "INFJ": {
        "traits": "🔮 통찰력 있고 창의적이며 조용한 이상주의자",
        "jobs": "🎨 예술가, 🧠 심리학자, ✍️ 작가",
        "reason": "깊은 감성과 통찰력을 바탕으로 사람의 내면을 이해하는 일을 잘합니다."
    },
    "INTJ": {
        "traits": "🧠 전략적이고 독립적이며 분석적인 성격",
        "jobs": "👨‍💻 개발자, 🧑‍🔬 과학자, 🧮 전략기획자",
        "reason": "미래를 설계하고 복잡한 문제를 해결하는 데 강점을 보입니다."
    },
    "ISTP": {
        "traits": "🔧 유연하고 논리적이며 실용적인 해결사",
        "jobs": "🛠️ 엔지니어, 🚗 정비사, 🚓 경찰관",
        "reason": "손으로 직접 해결하고 즉각적인 반응이 필요한 직업에서 강점을 보입니다."
    },
    "ISFP": {
        "traits": "🎨 조용하고 예술적이며 감성적인 성격",
        "jobs": "🎭 배우, 🎨 디자이너, 🧑‍🍳 셰프",
        "reason": "감각이 뛰어나고 창의적이어서 예술 분야에 잘 어울립니다."
    },
    "INFP": {
        "traits": "🌈 이상주의적이고 상상력이 풍부한 성격",
        "jobs": "✍️ 작가, 🎨 일러스트레이터, 🎭 예술가",
        "reason": "내면 세계가 깊고 자신만의 신념을 표현하는 직업에 적합합니다."
    },
    "INTP": {
        "traits": "🧪 논리적이고 분석적이며 지적인 탐구자",
        "jobs": "🧠 연구원, 👨‍💻 프로그래머, 🤖 인공지능 개발자",
        "reason": "복잡한 시스템을 이해하고 개발하는 데 뛰어난 능력을 보입니다."
    },
    "ESTP": {
        "traits": "🎯 에너지 넘치고 즉흥적이며 현실적인 성격",
        "jobs": "🎤 방송인, 🏋️‍♂️ 운동선수, 🧑‍🚒 소방관",
        "reason": "위기 상황에서 빠르게 반응하고 행동하는 직업에 적합합니다."
    },
    "ESFP": {
        "traits": "🎉 사교적이고 유쾌하며 감각적인 성격",
        "jobs": "🎶 가수, 🧑‍🎤 연예인, 🎤 MC",
        "reason": "사람들과 함께할 때 에너지가 높아지며 무대 위에서 빛을 발합니다."
    },
    "ENFP": {
        "traits": "🚀 열정적이고 창의적이며 자유로운 성격",
        "jobs": "🌍 NGO 활동가, 🎭 창작가, 🎨 콘텐츠 크리에이터",
        "reason": "자유로운 사고방식과 새로운 아이디어로 사람들에게 영향력을 미칠 수 있습니다."
    },
    "ENTP": {
        "traits": "⚡ 재치 있고 논쟁을 즐기며 도전적인 성격",
        "jobs": "📣 마케팅 전문가, 🧠 기획자, 🎤 강연가",
        "reason": "아이디어와 말로 사람을 움직이는 능력에서 탁월합니다."
    },
    "ESTJ": {
        "traits": "🏗️ 실용적이고 조직적인 지도자형 성격",
        "jobs": "🏛️ 관리자, 📊 경영인, 🧑‍✈️ 군인",
        "reason": "구조적이고 명확한 체계를 선호하여 리더 역할에 강합니다."
    },
    "ESFJ": {
        "traits": "🤝 협동적이고 따뜻하며 책임감 있는 성격",
        "jobs": "🧑‍🏫 교사, 💁‍♀️ 상담사, 🏥 의료 코디네이터",
        "reason": "사람을 돌보고 도와주는 직업에서 탁월한 만족감을 느낍니다."
    },
    "ENFJ": {
        "traits": "🌟 리더십 있고 감정이입이 뛰어난 성격",
        "jobs": "🎤 리더십 코치, 🌍 외교관, 🧑‍🏫 교육자",
        "reason": "사람을 이끌고 변화시키는 데 강한 열정을 가지고 있습니다."
    },
    "ENTJ": {
        "traits": "📈 야망 있고 효율적인 전략가형 성격",
        "jobs": "👔 CEO, 📈 사업가, 🧠 전략가",
        "reason": "계획 수립과 리더십에서 타의 추종을 불허합니다."
    },
}

# 출력
if selected_mbti:
    info = mbti_info[selected_mbti]

    st.markdown(f"""
        <div class="recommendation">
            <strong>{selected_mbti}</strong> 유형의 성격은?<br><br>
            <span>{info['traits']}</span><br><br>
            ✨ 추천 직업: <span style="font-size: 28px;">{info['jobs']}</span>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="reason">
            🔍 <strong>왜 이런 직업이 어울릴까요?</strong><br><br>
            {info['reason']}
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="emoji-box">🌟 너의 가능성을 펼쳐봐! 🚀</div>', unsafe_allow_html=True)
