import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 데이터 불러오기
url = "https://raw.githubusercontent.com/jiyoung-2/250621test/main/seoul_parmacy.csv"
df = pd.read_csv(url, encoding="cp949")

# 열 이름 공백 제거
df.columns = df.columns.str.strip()

# 필요한 열만 선택
columns_needed = ['주소', '약국명', '대표전화', '경도', '위도']
df = df[columns_needed]

# GUI 제목
st.title("서울시 약국 위치 및 정보")

# 지도 표시 (경도/위도 → lon/lat 이름으로 변경 필요)
# map_df = df.rename(columns={"위도": "lat", "경도": "lon"}).dropna(subset=["lat", "lon"])
# st.map(map_df)
for _, row in filtered_df.iterrows():
    name = row['약국명']
    lat = row['위도']
    lon = row['경도']

# 상세정보 확인용 테이블
st.subheader("약국 상세 정보")
st.dataframe(df.reset_index(drop=True))
folium.Marker(
    location=[lat, lon],
    popup=folium.Popup(popup_text, max_width=300),
    icon=folium.Icon(color="blue", icon="plus-sign")
    ).add_to(m)

# Streamlit에 Folium 지도 표시
st_folium(m, width=1000, height=700)
