# streamlit_app.py

import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

# 글로벌 시가총액 기준 Top 10 기업 (2024년 기준, 티커는 Yahoo Finance 기준)
top10_tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",
    "NVIDIA": "NVDA",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Meta Platforms": "META",
    "Berkshire Hathaway": "BRK-B",
    "TSMC": "TSM",
    "Eli Lilly": "LLY"
}

st.set_page_config(page_title="글로벌 시가총액 Top10 주가 변화", layout="wide")
st.title("📈 글로벌 시가총액 Top 10 기업 주가 변화 (최근 1년)")
st.markdown("출처: [Yahoo Finance](https://finance.yahoo.com)")

# 날짜 범위 설정
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# 사용자 선택
selected_companies = st.multiselect("🔎 비교할 회사를 선택하세요", options=list(top10_tickers.keys()), default=list(top10_tickers.keys())[:5])

# 데이터 불러오기
@st.cache_data
def load_data(ticker):
    df = yf.download(ticker, start=start_date, end=end_date)
    return df["Adj Close"]

# 그래프 생성
fig = go.Figure()
for company in selected_companies:
    ticker = top10_tickers[company]
    try:
        data = load_data(ticker)
        fig.add_trace(go.Scatter(x=data.index, y=data.values, mode='lines', name=company))
    except Exception as e:
        st.warning(f"{company} 데이터 로드 실패: {e}")

# 그래프 꾸미기
fig.update_layout(
    title="최근 1년간 주가 변화 (Adjusted Close)",
    xaxis_title="날짜",
    yaxis_title="주가 ($)",
    template="plotly_dark",
    legend_title="기업",
    hovermode="x unified"
)

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)
