import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 데이터 불러오기
url = "https://raw.githubusercontent.com/jiyoung-2/250621test/main/seoul_parmacy.csv"
df = pd.read_csv(url, encoding="cp949")

# 열 이름 공백 제거
df.columns = df.columns.str.strip()

# 필요한 열만 선택하고 결측치 제거
columns_needed = ['주소', '약국명', '대표전화', '경도', '위도']
df = df[columns_needed].dropna(subset=['위도', '경도'])

# GUI 제목
st.title("서울시 약국 위치 및 정보")

# Folium 지도 생성 (서울시 중심 좌표)
m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

# 약국별 마커 추가
for _, row in df.iterrows():
    lat = row['위도']
    lon = row['경도']
    name = row['약국명']
    phone = row['대표전화']
    address = row['주소']
    
    popup_text = f"""
    <b>{name}</b><br>
     {phone}<br>
    {address}
    """
    
    folium.Marker(
        location=[lat, lon],
        popup=folium.Popup(popup_text, max_width=250),
        icon=folium.Icon(color="blue", icon="plus-sign")
    ).add_to(m)

# Folium 지도 표시
st.subheader("서울시 약국 지도")
st_folium(m, width=1000, height=700)

# 상세정보 테이블 출력
st.subheader("📋 약국 상세 정보")
st.dataframe(df.reset_index(drop=True))
