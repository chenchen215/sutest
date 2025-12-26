import streamlit as st
import pandas as pd
import numpy as np

# ---------------------- 全局页面配置 ----------------------
st.set_page_config(
    page_title="多功能综合平台",
    page_icon="🖥️",
    layout="wide"
)

# ---------------------- 侧边栏按钮式导航（替换下拉选择框） ----------------------
st.sidebar.title("📚 功能导航")
# 初始化选中状态
if 'selected_menu' not in st.session_state:
    st.session_state.selected_menu = "首页"

# 侧边栏按钮（每个功能对应一个按钮）
menu_buttons = [
    ("首页", "🏠"),
    ("个人简历生成器", "📄"),
    ("动物图鉴", "🖼️"),
    ("南宁美食数据", "🍜"),
    ("数字档案", "📊"),
    ("音乐播放器", "🎵"),
    ("视频中心", "🎬")
]

for menu_name, icon in menu_buttons:
    # 按钮样式：选中项高亮
    if st.sidebar.button(
        f"{icon} {menu_name}",
        use_container_width=True,
        key=menu_name,
        type="primary" if st.session_state.selected_menu == menu_name else "secondary"
    ):
        st.session_state.selected_menu = menu_name
        st.rerun()  # 点击后刷新页面切换模块

# ---------------------- 各功能模块实现 ----------------------

# 1. 首页
if st.session_state.selected_menu == "首页":
    st.title("多功能综合平台")
    st.markdown("""
    <div style="padding:20px; background-color:#f5f5f5; border-radius:10px;">
        <h3>欢迎使用多功能综合平台</h3>
        <p>本平台整合了个人简历生成、动物图鉴、美食探索、数字档案、音乐播放、视频观看等功能</p>
        <p>请通过左侧侧边栏选择需要使用的功能模块</p>
    </div>
    """, unsafe_allow_html=True)

# 2. 个人简历生成器
elif st.session_state.selected_menu == "个人简历生成器":
    st.title("个人简历生成器")
    st.markdown("使用Streamlit创建您的个性化简历")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("个人信息表单")
        name = st.text_input("姓名")
        position = st.text_input("职位")
        phone = st.text_input("电话")
        email = st.text_input("邮箱")
        birth_date = st.date_input("出生日期", value="2000-01-01")
        gender = st.radio("性别", ["男", "女", "其他"])
        intro = st.text_area("个人简介", value="这个人很神秘，没有留下任何介绍...")
        education = st.selectbox("学历", ["高中", "大专", "本科", "硕士", "博士"])
        language = st.text_input("语言能力")
        work_exp = st.number_input("工作经验（年）", min_value=0, step=1)
        salary = st.select_slider("期望薪资", options=["3000-5000元", "5000-8000元", "8000-10000元", "10000-20000元", "20000元以上"])
        contact_time = st.time_input("最佳联系时间", value="09:00")
    
    with col2:
        st.subheader("简历实时预览")
        st.markdown(f"""
        <div style="padding:15px; border:1px solid #eee; border-radius:8px; height:100%;">
            <h4 style="margin:0 0 10px 0;">{name if name else '姓名'}</h4>
            <p><strong>职位:</strong> {position if position else '未填写'}</p>
            <p><strong>电话:</strong> {phone if phone else '未填写'}</p>
            <p><strong>邮箱:</strong> {email if email else '未填写'}</p>
            <p><strong>出生日期:</strong> {birth_date}</p>
            <p><strong>性别:</strong> {gender}</p>
            <p><strong>学历:</strong> {education}</p>
            <p><strong>工作经验:</strong> {work_exp}年</p>
            <p><strong>期望薪资:</strong> {salary}</p>
            <p><strong>最佳联系时间:</strong> {contact_time.strftime('%H:%M')}</p>
            <p><strong>语言能力:</strong> {language if language else '未填写'}</p>
            <p><strong>个人简介:</strong> {intro}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.button("生成简历", use_container_width=True)

# 3. 动物图鉴
elif st.session_state.selected_menu == "动物图鉴":
    st.set_page_config(page_title="相册网站", page_icon="🖼️")
    image_ua = [
        {'url': 'https://ss0.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=4001167109,3893799730&fm=253&gp=0.jpg', 'text': '鱼'},
        {'url': 'https://img95.699pic.com/photo/50506/1953.jpg_wh860.jpg', 'text': '鸟'},
        {'url': 'https://www.baltana.com/files/wallpapers-2/Cute-Cat-Images-07756.jpg', 'text': '猫'}
    ]
    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0
    st.image(image_ua[st.session_state['ind']]['url'], caption=image_ua[st.session_state['ind']]['text'])
    
    def nextImg():
        st.session_state['ind'] = (st.session_state['ind'] + 1) % len(image_ua)
    def prevImg():
        st.session_state['ind'] = (st.session_state['ind'] - 1) % len(image_ua)
    
    c1, c2 = st.columns(2)
    with c1:
        st.button("上一张", use_container_width=True, on_click=prevImg)
    with c2:
        st.button("下一张", use_container_width=True, on_click=nextImg)

# 4. 南宁美食数据
elif st.session_state.selected_menu == "南宁美食数据":
    st.set_page_config(page_title="南宁美食探索", layout="wide")
    restaurants = pd.DataFrame({
        "店铺名称": ["豆香尝不忘", "老友粉王", "南宁酸嘢铺", "中山路烧烤", "卷筒粉世家", "柠檬鸭饭店"],
        "评分": [4.2, 4.5, 4.0, 4.3, 4.1, 4.4],
        "人均价格": [15, 20, 12, 30, 18, 25],
        "地址": ["青秀区民族大道", "兴宁区朝阳路", "西乡塘区大学路", "青秀区中山路", "江南区星光大道", "良庆区五象大道"],
        "latitude": [22.8170, 22.8265, 22.8456, 22.8108, 22.7830, 22.7668],
        "longitude": [108.3665, 108.3415, 108.2900, 108.3428, 108.3488, 108.3485]
    })
    time_slots = pd.date_range("10:00", "22:00", freq="H").strftime("%H:00")
    peak_data = pd.DataFrame({
        "时段": time_slots,
        "堂食客流": [5, 8, 15, 20, 30, 45, 50, 48, 35, 25, 20, 10, 5],
        "外卖订单": [3, 6, 12, 18, 25, 38, 42, 35, 28, 20, 15, 8, 3]
    }).set_index("时段")
    months = [f"{m}月" for m in range(1, 13)]
    price_trend = pd.DataFrame({
        "月份": months,
        "豆香尝不忘": [14, 14, 15, 15, 15, 16, 16, 15, 15, 15, 15, 15],
        "老友粉王": [18, 18, 19, 20, 20, 21, 21, 20, 20, 20, 20, 20],
        "南宁酸嘢铺": [10, 10, 12, 12, 12, 13, 13, 12, 12, 12, 12, 12],
        "中山路烧烤": [28, 28, 29, 30, 30, 32, 32, 30, 30, 30, 30, 30],
        "卷筒粉世家": [16, 16, 18, 18, 18, 19, 19, 18, 18, 18, 18, 18]
    }).set_index("月份")
    
    st.title("南宁美食探索")
    st.markdown("探索南宁本地特色美食，包含店铺评分、价格、客流等信息")
    col1, col2 = st.columns([2, 3])
    with col1:
        st.subheader("南宁美食地图")
        st.map(restaurants, zoom=11)
        st.subheader("餐厅评分")
        st.bar_chart(restaurants[["店铺名称", "评分"]].set_index("店铺名称"), height=200)
    with col2:
        st.subheader("餐厅12个月价格走势")
        st.line_chart(price_trend, height=200)
        st.subheader("用餐高峰时段")
        st.area_chart(peak_data, height=200)
        st.subheader("餐厅详情")
        selected_rest = st.selectbox("选择餐厅查看详情", restaurants["店铺名称"])
        rest_detail = restaurants[restaurants["店铺名称"] == selected_rest].iloc[0]
        with st.expander(f"{rest_detail['店铺名称']} 详情"):
            st.write(f"**评分**: {rest_detail['评分']}/5.0")
            st.write(f"**人均价格**: {rest_detail['人均价格']}元")
            st.write(f"**地址**: {rest_detail['地址']}")
            dish_map = {
                "豆香尝不忘": "老友粉、豆浆油条",
                "老友粉王": "经典老友粉、牛杂老友粉",
                "南宁酸嘢铺": "芒果酸嘢、李子酸嘢、木瓜酸嘢",
                "中山路烧烤": "烤肥牛、烤掌中宝、烤生蚝",
                "卷筒粉世家": "肉末卷筒粉、香菇卷筒粉",
                "柠檬鸭饭店": "正宗柠檬鸭、鸭血汤"
            }
            st.write(f"**推荐菜品**: {dish_map[rest_detail['店铺名称']]}")
    
    st.subheader("当前拥挤程度（模拟）")
    for idx, row in restaurants.iterrows():
        col_left, col_right = st.columns([1, 5])
        with col_left:
            st.write(f"{row['店铺名称']}:")
        with col_right:
            crowd_level = np.random.uniform(0.2, 0.8)
            st.progress(crowd_level)
            st.caption(f"拥挤度: {crowd_level:.1%}")

# 5. 数字档案
elif st.session_state.selected_menu == "数字档案":
    st.title("🕶学生起飞小组-数字档案")
    st.header("🔑基础信息")
    st.text("学生ID：NEO-2025-029")
    st.markdown("注册时间: <span style='color:green;'>2025-11-11 15：08：30</span> | 精神状态: ✅ 正常", unsafe_allow_html=True)
    st.markdown("当前教室: <span style='color:green;'>实训楼301</span> | 安全等级: <span style='color:green;'>绝密</span>", unsafe_allow_html=True)
    st.header("📊技能矩阵")
    c1, c2, c3 = st.columns(3)
    c1.metric(label="c语言", value="95%", delta="2%", help='近期训练提升')
    c2.metric(label="Pyhon", value="87%", delta="-1%")
    c3.metric(label="Java", value="68%", delta="-10%", help='用则进废则退')
    st.subheader("Streamlit课程进度")
    st.write('Streamlit课程进度')
    st.progress(10)
    st.header("📝任务日志")
    data = {
        '日期': ['2025-11-12', '2025-11-13', '2025-11-14'],
        '任务': ['学生数字档案', '课程管理系统', '数据图表展示'],
        '状态': ['✅完成', '🕛进行中', '❌未完成'],
        '难度': ['★☆☆☆☆', '★★☆☆☆', '★★★☆☆'],
    }
    df = pd.DataFrame(data, index=[0, 1, 2])
    st.table(df)
    st.header("🔐 最新代码成果")
    python_code = '''def matrix_breach():
    while True:
        if detect_vulnerability():
            exploit()
            return "ACCESS GRANTED"
        else:
            stralth_evade()
'''
    st.code(python_code)
    st.markdown('***')
    st.markdown("<span style='color:green;'>>> SYSTEM MESSAGE:</span>下一个任务目标已解锁...", unsafe_allow_html=True)
    st.markdown("<span style='color:green;'>>> TARGET:</span>课程管理系统", unsafe_allow_html=True)
    st.markdown("<span style='color:green;'>>> COUNTDOWN:</span>2025-12-18 07:22:45", unsafe_allow_html=True)
    st.write("系统状态: 在线 连接状态: 已加密")

# 6. 音乐播放器
elif st.session_state.selected_menu == "音乐播放器":
    st.set_page_config(page_title='音乐播放器')
    st.title('简易音乐播放器')
    st.text('使用Streamlit制作的简单音乐播放器，支持切歌和基本播放控制')
    images = [
        'https://p1.music.126.net/qKSYMuy9ruRRdVRO8MsONA==/109951172418592653.jpg',
        'https://p2.music.126.net/_unjrno3g2ojZ4I6m4MAnQ==/109951172383235131.jpg',
        'https://p1.music.126.net/Sycq-TSBOy57___ChEEdyA==/109951172406249431.jpg'
    ]
    audio_files = [
        'https://music.163.com/song/media/outer/url?id=3327856998.mp3',
        'https://music.163.com/song/media/outer/url?id=3324846858.mp3',
        'https://music.163.com/song/media/outer/url?id=3312521577.mp3'
    ]
    song_names = ["春予你", "潇洒", "过客"]
    artists = ["李嘉格", "TizzyT / GALI / 马思唯", "范晓萱 / 100%乐团"]
    song_time = ["4:01", "3:33", "4:58"]
    if 'current_index' not in st.session_state:
        st.session_state.current_index = 0
    current_index = st.session_state.current_index
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(images[current_index], width=250)
    with col2:
        st.title(song_names[current_index])
        st.text(f"歌手: {artists[current_index]}")
        st.text(f"时长: {song_time[current_index]}")
        col3, col4 = st.columns([2, 2])
        with col3:
            if st.button('上一首', disabled=current_index == 0):
                st.session_state.current_index -= 1
                st.rerun()
        with col4:
            if st.button('下一首', disabled=current_index == len(images) - 1):
                st.session_state.current_index += 1
                st.rerun()
    st.audio(audio_files[current_index])
    st.divider()

# 7. 视频中心
elif st.session_state.selected_menu == "视频中心":
    st.set_page_config(page_title="视频中心")
    video_arr = [
        {'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/37/17/34206321737/34206321737-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1766568058&trid=08ec7ba97506424181cd8c17013d3e8O&os=estghw&uipk=5&nbs=1&oi=143446004&platform=html5&mid=0&gen=playurlv3&og=hw&upsig=af01a291c7f4bd29d343c064c2fa9b51&uparams=e,deadline,trid,os,uipk,nbs,oi,platform,mid,gen,og&bvc=vod&nettype=1&bw=660455&agrr=1&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3', 'title': '熊出没之环球大冒险-第1集'},
        {'url': 'https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/10/17/33905051710/33905051710-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&og=ali&nbs=1&os=mcdn&platform=html5&trid=0000ec5d267acb7f471697eac2304d21b04O&mid=0&oi=1939826609&deadline=1766568296&uipk=5&gen=playurlv3&upsig=41cd220ba114f4acbda927b146da225c&uparams=e,og,nbs,os,platform,trid,mid,oi,deadline,uipk,gen&mcdnid=50045237&bvc=vod&nettype=1&bw=655191&buvid=&build=7330300&dl=0&f=O_0_0&agrr=1&orderid=0,3', 'title': '熊出没之环球大冒险-第2集'},
        {'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/07/35/33940373507/33940373507-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&deadline=1766568176&oi=143443039&trid=a6dbb5f5be8c4e4283bb80755d341f5O&gen=playurlv3&nbs=1&uipk=5&platform=html5&os=estghw&og=hw&upsig=0c66ee62fea42e369a7c7250b149496c&uparams=e,mid,deadline,oi,trid,gen,nbs,uipk,platform,os,og&bvc=vod&nettype=1&bw=629513&agrr=1&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3', 'title': '熊出没之环球大冒险-第3集'},
        {'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/13/69/32469746913/32469746913-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=7bbdf65c12f74f1eae08bf318f5da72O&oi=143443039&mid=0&platform=html5&os=estgcos&deadline=1766568409&nbs=1&uipk=5&gen=playurlv3&og=cos&upsig=a705e6d35cc56a9c80fa40011c4876f9&uparams=e,trid,oi,mid,platform,os,deadline,nbs,uipk,gen,og&bvc=vod&nettype=1&bw=697172&f=O_0_0&agrr=1&buvid=&build=7330300&dl=0&orderid=0,3', 'title': '熊出没之环球大冒险-第4集'},
        {'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/18/58/33965345818/33965345818-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1766568445&uipk=5&platform=html5&trid=2fe5f228591b45fe912f6f56ba0b862O&og=cos&mid=0&oi=143446004&nbs=1&gen=playurlv3&os=estgcos&upsig=f4e2e2bf5fba8f8d9d93e353000306a2&uparams=e,deadline,uipk,platform,trid,og,mid,oi,nbs,gen,os&bvc=vod&nettype=1&bw=621876&agrr=1&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3', 'title': '熊出没之环球大冒险-第5集'}
    ]
    if 'ind' not in st.session_state:
        st.session_state.ind = 0
    st.title(video_arr[st.session_state.ind]['title'])
    st.video(video_arr[st.session_state.ind]['url'])
    
    def playVideo(index):
        st.session_state.ind = index
    n_cols = 3
    for i in range(0, len(video_arr), n_cols):
        cols = st.columns(n_cols)
        for j in range(n_cols):
            idx = i + j
            if idx < len(video_arr):
                with cols[j]:
                    st.button(f"第{idx + 1}集", key=f"btn_{idx}", on_click=playVideo, args=(idx,), use_container_width=True)
