import streamlit as st

# 设置页面配置
st.set_page_config(page_title="相册网站", page_icon="🖼️")

# 图片数据列表（包含图片URL和描述）
image_ua = [
    {
        'url': 'https://ss0.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=4001167109,3893799730&fm=253&gp=0.jpg',
        'text': '鱼'
    },
    {
        'url': 'https://img95.699pic.com/photo/50506/1953.jpg_wh860.jpg',
        'text': '鸟'
    },
    {
        'url': 'https://www.baltana.com/files/wallpapers-2/Cute-Cat-Images-07756.jpg',
        'text': '猫'
    }
]

# 初始化session_state中的索引（记录当前显示的图片）
if 'ind' not in st.session_state:
    st.session_state['ind'] = 0

# 显示当前图片
st.image(
    image_ua[st.session_state['ind']]['url'],
    caption=image_ua[st.session_state['ind']]['text']
)

# 定义“下一张”的切换函数
def nextImg():
    st.session_state['ind'] = (st.session_state['ind'] + 1) % len(image_ua)

# 定义“上一张”的切换函数
def prevImg():
    st.session_state['ind'] = (st.session_state['ind'] - 1) % len(image_ua)

# 创建分栏（放置“上一张”“下一张”按钮）
c1, c2 = st.columns(2)

# 放置“上一张”按钮
with c1:
    st.button("上一张", use_container_width=True, on_click=prevImg)

# 放置“下一张”按钮
with c2:
    st.button("下一张", use_container_width=True, on_click=nextImg)
