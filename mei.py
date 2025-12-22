import streamlit as st    # 导入Streamlit并用st代表它，用于快速构建Web应用
import pandas as pd     # 导入pandas并用pd代表它，用于数据处理和表格展示


st.title("🕶学生起飞小组-数字档案")  # 设置页面主标题，展示项目名称

st.header("🔑基础信息")  # 设置基础信息板块的二级标题

st.text("学生ID：NEO-2025-029")  # 展示学生唯一标识ID

# 使用markdown展示注册时间和精神状态，通过HTML标签设置文字颜色为绿色，unsafe_allow_html=True允许解析HTML
st.markdown("注册时间: <span style='color:green;'>2025-11-11 15：08：30</span> | 精神状态: ✅ 正常", unsafe_allow_html=True)
# 使用markdown展示当前教室和安全等级，绿色文字突出关键信息
st.markdown("当前教室: <span style='color:green;'>实训楼301</span> | 安全等级: <span style='color:green;'>绝密</span>", unsafe_allow_html=True)

st.header("📊技能矩阵")  # 设置技能矩阵板块的二级标题
c1, c2, c3 = st.columns(3)  # 将页面分为3列，用于并列展示技能指标
# 第一列展示C语言技能值，delta显示变化量，help参数提供鼠标悬停提示
c1.metric(label="c语言", value="95%", delta="2%",help='近期训练提升')
# 第二列展示Python技能值，delta为负数表示下降
c2.metric(label="Pyhon", value="87%", delta="-1%")
# 第三列展示Java技能值，delta大幅下降，help提示原因
c3.metric(label="Java", value="68%", delta="-10%",help='用则进废则退')

st.subheader("Streamlit课程进度")  # 设置课程进度子标题
st.write('Streamlit课程进度')  # 文本说明进度条含义
st.progress(10)  # 展示进度条，数值10表示完成10%


st.header("📝任务日志")  # 设置任务日志板块的二级标题
# 定义字典格式的任务数据，包含日期、任务、状态、难度字段
data = {
    '日期':['2025-11-12', '2025-11-13', '2025-11-14'],
    '任务':['学生数字档案', '课程管理系统', '数据图表展示'],
    '状态':['✅完成', '🕛进行中', '❌未完成'],
    '难度':['★☆☆☆☆','★★☆☆☆','★★★☆☆'],
}
# 定义数据框所用的索引，使用Series创建连续索引
index = pd.Series([0,1,2])
# 根据数据和索引创建pandas数据框，结构化展示任务信息
df = pd.DataFrame(data, index=index)
# 生成静态表格展示任务日志数据
st.table(df)


st.header("🔐 最新代码成果")  # 设置代码成果板块的二级标题
# 创建要显示的Python代码块的内容，模拟黑客风格的函数
python_code = '''def matrix_breach():
    while True:
        if detect_vulnerability():
            exploit()
            return "ACCESS GRANTED"
        else:
            stralth_evade()
'''
st.code(python_code)  # 以代码块格式展示Python代码，保留语法高亮
st.markdown('***')  # 插入分隔线，分隔不同内容板块


# 使用markdown展示系统消息，绿色文字模拟终端输出效果
st.markdown("<span style='color:green;'>>> SYSTEM MESSAGE:</span>下一个任务目标已解锁...", unsafe_allow_html=True)
# 展示任务目标信息，保持终端风格的视觉效果
st.markdown("<span style='color:green;'>>> TARGET:</span>课程管理系统", unsafe_allow_html=True)
# 展示任务倒计时时间，明确任务截止节点
st.markdown("<span style='color:green;'>>> COUNTDOWN:</span>2025-12-18 07:22:45", unsafe_allow_html=True)
# 展示系统状态信息，简洁说明当前系统连接情况
st.write("系统状态: 在线 连接状态: 已加密")

