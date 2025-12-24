import streamlit as st

# 设置页面标题
st.set_page_config(page_title="视频中心")

# 视频列表
video_arr = [
    {
        'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/37/17/34206321737/34206321737-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1766568058&trid=08ec7ba97506424181cd8c17013d3e8O&os=estghw&uipk=5&nbs=1&oi=143446004&platform=html5&mid=0&gen=playurlv3&og=hw&upsig=af01a291c7f4bd29d343c064c2fa9b51&uparams=e,deadline,trid,os,uipk,nbs,oi,platform,mid,gen,og&bvc=vod&nettype=1&bw=660455&agrr=1&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3',
        'title': '熊出没之环球大冒险-第1集'
    },
    {
        'url': 'https://upos-sz-mirrorhw.bilivideo.com/upgcxcode/10/17/33905051710/33905051710-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&og=ali&nbs=1&os=mcdn&platform=html5&trid=0000ec5d267acb7f471697eac2304d21b04O&mid=0&oi=1939826609&deadline=1766568296&uipk=5&gen=playurlv3&upsig=41cd220ba114f4acbda927b146da225c&uparams=e,og,nbs,os,platform,trid,mid,oi,deadline,uipk,gen&mcdnid=50045237&bvc=vod&nettype=1&bw=655191&buvid=&build=7330300&dl=0&f=O_0_0&agrr=1&orderid=0,3',
        'title': '熊出没之环球大冒险-第2集'
    },
    {
        'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/07/35/33940373507/33940373507-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&deadline=1766568176&oi=143443039&trid=a6dbb5f5be8c4e4283bb80755d341f5O&gen=playurlv3&nbs=1&uipk=5&platform=html5&os=estghw&og=hw&upsig=0c66ee62fea42e369a7c7250b149496c&uparams=e,mid,deadline,oi,trid,gen,nbs,uipk,platform,os,og&bvc=vod&nettype=1&bw=629513&agrr=1&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3',
        'title': '熊出没之环球大冒险-第3集'
    },
    {
        'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/13/69/32469746913/32469746913-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&trid=7bbdf65c12f74f1eae08bf318f5da72O&oi=143443039&mid=0&platform=html5&os=estgcos&deadline=1766568409&nbs=1&uipk=5&gen=playurlv3&og=cos&upsig=a705e6d35cc56a9c80fa40011c4876f9&uparams=e,trid,oi,mid,platform,os,deadline,nbs,uipk,gen,og&bvc=vod&nettype=1&bw=697172&f=O_0_0&agrr=1&buvid=&build=7330300&dl=0&orderid=0,3',
        'title': '熊出没之环球大冒险-第4集'
    },
    {
        'url': 'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/18/58/33965345818/33965345818-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1766568445&uipk=5&platform=html5&trid=2fe5f228591b45fe912f6f56ba0b862O&og=cos&mid=0&oi=143446004&nbs=1&gen=playurlv3&os=estgcos&upsig=f4e2e2bf5fba8f8d9d93e353000306a2&uparams=e,deadline,uipk,platform,trid,og,mid,oi,nbs,gen,os&bvc=vod&nettype=1&bw=621876&agrr=1&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3',
        'title': '熊出没之环球大冒险-第5集'
    }
]

# 初始化当前剧集索引
if 'ind' not in st.session_state:
    st.session_state.ind = 0

# 显示当前剧集标题
st.title(video_arr[st.session_state.ind]['title'])

# 播放当前视频
st.video(video_arr[st.session_state.ind]['url'])

# 定义切换函数
def playVideo(index):
    st.session_state.ind = index

# === 一行三集布局 ===
n_cols = 3
for i in range(0, len(video_arr), n_cols):
    cols = st.columns(n_cols)
    for j in range(n_cols):
        idx = i + j
        if idx < len(video_arr):
            with cols[j]:
                st.button(
                    f"第{idx + 1}集",
                    key=f"btn_{idx}",
                    on_click=playVideo,
                    args=(idx,),
                    use_container_width=True
                )
