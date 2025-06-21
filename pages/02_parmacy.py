import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium



st.set_page_config(page_title="서울시 약국 지도", layout="wide")

st.title("💊 서울시 자치구별 약국 위치 및 운영 시간 안내")

# CSV 파일 로드
df = pd.read_csv("https://raw.githubusercontent.com/your-username/your-repo/main/seoul_parmacy.csv")

#gpt가 알려준 해법 -> 근데 안됨ㅜㅜ
#url = "https://raw.githubusercontent.com/jiyoung-2/250621test/main/seoul_parmacy.csv"
#df = pd.read_csv(url, encoding="cp949")  # 또는 encoding="utf-8"로 테스트


# 필수 컬럼 예시 (컬럼명은 실제 파일에 맞게 조정)
# ['약국명', '주소', '자치구', '위도', '경도', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

# 지도 중심 좌표 설정 (서울 중심)
seoul_center = [37.5665, 126.9780]
m = folium.Map(location=seoul_center, zoom_start=11)

# 자치구 선택
gu_list = df['자치구'].unique().tolist()
selected_gu = st.multiselect("📍 자치구를 선택하세요", options=gu_list, default=gu_list)

# 필터링
filtered_df = df[df['자치구'].isin(selected_gu)]

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



