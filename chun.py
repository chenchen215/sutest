import streamlit as st
import pandas as pd
import numpy as np

# 页面配置
st.set_page_config(page_title="南宁美食探索", layout="wide")

# ---------------------- 数据准备（修复列名） ----------------------
restaurants = pd.DataFrame({
    "店铺名称": ["豆香尝不忘", "老友粉王", "南宁酸嘢铺", "中山路烧烤", "卷筒粉世家", "柠檬鸭饭店"],
    "评分": [4.2, 4.5, 4.0, 4.3, 4.1, 4.4],
    "人均价格": [15, 20, 12, 30, 18, 25],
    "地址": ["青秀区民族大道", "兴宁区朝阳路", "西乡塘区大学路", "青秀区中山路", "江南区星光大道", "良庆区五象大道"],
    "latitude": [22.8170, 22.8265, 22.8456, 22.8108, 22.7830, 22.7668],  # 改为英文列名
    "longitude": [108.3665, 108.3415, 108.2900, 108.3428, 108.3488, 108.3485]  # 改为英文列名
})

# 2. 餐厅评分数据（bar_chart用）
rating_data = restaurants[["店铺名称", "评分"]].set_index("店铺名称")

# 3. 用餐高峰时段数据（area_chart用）
time_slots = pd.date_range("10:00", "22:00", freq="H").strftime("%H:00")
peak_data = pd.DataFrame({
    "时段": time_slots,
    "堂食客流": [5, 8, 15, 20, 30, 45, 50, 48, 35, 25, 20, 10, 5],
    "外卖订单": [3, 6, 12, 18, 25, 38, 42, 35, 28, 20, 15, 8, 3]
}).set_index("时段")

# 4. 5家餐厅12个月价格走势（line_chart用）
months = [f"{m}月" for m in range(1, 13)]
price_trend = pd.DataFrame({
    "月份": months,
    "豆香尝不忘": [14, 14, 15, 15, 15, 16, 16, 15, 15, 15, 15, 15],
    "老友粉王": [18, 18, 19, 20, 20, 21, 21, 20, 20, 20, 20, 20],
    "南宁酸嘢铺": [10, 10, 12, 12, 12, 13, 13, 12, 12, 12, 12, 12],
    "中山路烧烤": [28, 28, 29, 30, 30, 32, 32, 30, 30, 30, 30, 30],
    "卷筒粉世家": [16, 16, 18, 18, 18, 19, 19, 18, 18, 18, 18, 18]
}).set_index("月份")

# ---------------------- 页面布局 ----------------------
st.title("南宁美食探索")
st.markdown("探索南宁本地特色美食，包含店铺评分、价格、客流等信息")

# 分栏布局
col1, col2 = st.columns([2, 3])

# ---------------------- 页面布局 ----------------------
st.title("南宁美食探索")
st.markdown("探索南宁本地特色美食，包含店铺评分、价格、客流等信息")

col1, col2 = st.columns([2, 3])

with col1:
    st.subheader("南宁美食地图")
    st.map(restaurants, zoom=11)  # 现在列名匹配，可正常加载地图

    st.subheader("餐厅评分")
    rating_data = restaurants[["店铺名称", "评分"]].set_index("店铺名称")
    st.bar_chart(rating_data, height=200)


with col2:
    # 3. 5家餐厅12个月价格走势折线图
    st.subheader("餐厅12个月价格走势")
    st.line_chart(price_trend, height=200)

    # 4. 用餐高峰时段面积图
    st.subheader("用餐高峰时段")
    st.area_chart(peak_data, height=200)

    # 5. 餐厅详情
    st.subheader("餐厅详情")
    selected_rest = st.selectbox("选择餐厅查看详情", restaurants["店铺名称"])
    rest_detail = restaurants[restaurants["店铺名称"] == selected_rest].iloc[0]
    
    with st.expander(f"{rest_detail['店铺名称']} 详情"):
        st.write(f"**评分**: {rest_detail['评分']}/5.0")
        st.write(f"**人均价格**: {rest_detail['人均价格']}元")
        st.write(f"**地址**: {rest_detail['地址']}")
        # 按店铺匹配特色菜品，更贴合实际
        dish_map = {
            "豆香尝不忘": "老友粉、豆浆油条",
            "老友粉王": "经典老友粉、牛杂老友粉",
            "南宁酸嘢铺": "芒果酸嘢、李子酸嘢、木瓜酸嘢",
            "中山路烧烤": "烤肥牛、烤掌中宝、烤生蚝",
            "卷筒粉世家": "肉末卷筒粉、香菇卷筒粉",
            "柠檬鸭饭店": "正宗柠檬鸭、鸭血汤"
        }
        st.write(f"**推荐菜品**: {dish_map[rest_detail['店铺名称']]}")

# 追加：当前拥挤程度进度条
st.subheader("当前拥挤程度（模拟）")
for idx, row in restaurants.iterrows():
    col_left, col_right = st.columns([1, 5])
    with col_left:
        st.write(f"{row['店铺名称']}:")
    with col_right:
        crowd_level = np.random.uniform(0.2, 0.8)
        st.progress(crowd_level)
        st.caption(f"拥挤度: {crowd_level:.1%}")
