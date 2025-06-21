import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="서울시 약국 지도", layout="wide")

st.title("💊 서울시 약국 위치 및 운영 시간 안내")

# CSV 파일 로드
df = pd.read_csv("https://raw.githubusercontent.com/jiyoung-2/250621test/main/seoul_parmacy.csv", encoding="utf-8")

# 지도 중심 좌표 설정 (서울 중심)
seoul_center = [37.5665, 126.9780]
m = folium.Map(location=seoul_center, zoom_start=11)

# 자치구 선택 기능 제거 → 전체 데이터 사용
filtered_df = df.copy()

# 지도에 약국 추가
for _, row in filtered_df.iterrows():
    name = row['약국명']
    lat = row['위도']
    lon = row['경도']

    # 요일별 운영시간 정보 수집
    days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    hours = "<br>".join([f"{day}: {row.get(day, '정보 없음')}" for day in days])

    popup_text = f"<b>{name}</b><br>{row['주소']}<br><br>{hours}"
    folium.Marker(
        location=[lat, lon],
        popup=folium.Popup(popup_text, max_width=300),
        icon=folium.Icon(color="blue", icon="plus-sign")
    ).add_to(m)

# Streamlit에 Folium 지도 표시
st_folium(m, width=1000, height=700)
