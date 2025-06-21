import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
pd.read_csv("https://github.com/jiyoung-2/250621test/blob/main/seoul_parmacy.csv", encoding="cp949")


st.set_page_config(page_title="Global Market Cap Top 10", layout="wide")

st.title("🌍 글로벌 시가총액 Top 10 기업 📈")

# 미리 선정한 글로벌 시가총액 상위 10개 기업의 티커 (2024 기준)
tickers = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Saudi Aramco": "2222.SR",  # 사우디 증시
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Nvidia": "NVDA",
    "Meta": "META",
    "Berkshire Hathaway": "BRK-B",
    "TSMC": "TSM",
    "Eli Lilly": "LLY"
}

market_caps = {}
currency = {}

# 데이터 수집
for name, ticker in tickers.items():
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        market_cap = info.get("marketCap", None)
        cur = info.get("financialCurrency", "USD")
        if market_cap:
            market_caps[name] = market_cap
            currency[name] = cur
    except Exception as e:
        st.warning(f"{name} 데이터 로딩 실패: {e}")

# 정렬
sorted_data = sorted(market_caps.items(), key=lambda x: x[1], reverse=True)

# 시각화용 데이터
names = [item[0] for item in sorted_data]
caps = [item[1] / 1e12 for item in sorted_data]  # 단위: 조(Trillion USD)

fig = go.Figure(data=[
    go.Bar(
        x=names,
        y=caps,
        text=[f"${cap:.2f}T" for cap in caps],
        textposition='auto',
        marker_color='indianred'
    )
])

fig.update_layout(
    title="🌐 글로벌 시가총액 Top 10 기업 (단위: Trillion USD)",
    xaxis_title="기업명",
    yaxis_title="시가총액 (Trillion USD)",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)
