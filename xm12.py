# 移除无用导入，精简代码
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os
import pickle
from sklearn.ensemble import RandomForestRegressor

# 设置页面配置
st.set_page_config(
    page_title="学生成绩分析与预测系统",
    page_icon="📊",
    layout="wide"
)

# 通用工具函数：获取文件路径并检查是否存在（解决CSV/模型文件找不到问题）
def get_file_path(file_name):
    """
    获取文件绝对路径，并检查文件是否存在
    :param file_name: 文件名（如student_data_adjusted_rounded.csv）
    :return: 文件绝对路径
    """
    try:
        # 获取当前脚本所在目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
    except:
        # 若无法获取脚本路径（如某些云端环境），使用当前工作目录
        current_dir = os.getcwd()
    file_path = os.path.join(current_dir, file_name)
    # 检查文件是否存在
    if not os.path.exists(file_path):
        st.error(f"错误：未找到文件 {file_name}，当前查找路径：{file_path}")
        st.error("请确保该文件已上传至项目根目录！")
        st.stop()  # 终止程序，避免后续报错
    return file_path

def introduce_page():
    # 右边主内容区域
    st.title("📒学生成绩分析与预测系统")
    st.markdown('***')

    col11, col12 = st.columns(2)
    with col11:
        # 项目概述
        st.header("🗒️项目概述")
        st.write("本项目是一个基于streamlit的学生成绩分析平台，通过数据可视化和机器学习技术，帮助教育工作者和学生深入了解学业表现，并预测期末考试成绩")

        # 主要特点
        st.subheader("✨主要特点")
        st.markdown("""
        - 📊**数据可视化**：直观展示学生成绩分布和趋势
        - 📚**智能预测**：基于历史数据预测学生未来成绩
        - 🧠**多维度分析**：从课程、时间、学生等多个维度进行分析
        - 💡**个性化建议**：根据分析结果提供个性化学习建议
        """)

    with col12:
        images_ua = [
            {'url':'images/1.png','text':'项目介绍'},
            {'url':'images/2.png','text':'专业数据分析'},
            {'url':'images/3.png','text':'专业数据分析'},
            {'url':'images/4.png','text':'专业数据分析'},
            {'url':'images/5.png','text':'专业数据分析'},
            {'url':'images/6.png','text':'成绩预测'},
        ]
        # 图片轮播展示区
        st.subheader("📷 项目截图展示")
        # 初始化 session_state 中的图片索引
        if "images_idx" not in st.session_state:
            st.session_state.images_idx = 0

        # 上一张/下一张按钮回调
        def next_images():
            st.session_state.images_idx = (st.session_state.images_idx + 1) % len(images_ua)

        def prev_images():
            st.session_state.images_idx = (st.session_state.images_idx - 1) % len(images_ua)

        # 当前图片信息
        current = images_ua[st.session_state.images_idx]
        images_path = current["url"]
        images_desc = current["text"]

        # 展示图片（兼容新版Streamlit，使用use_container_width=True更稳定）
        col_img, col_desc = st.columns([3, 1])
        with col_img:
            # 检查图片文件夹是否存在
            images_dir = os.path.dirname(images_path)
            if os.path.exists(images_dir) or not images_dir:
                st.image(images_path, use_container_width=True)
            else:
                # 图片文件夹不存在，给出提示
                st.warning(f"图片文件夹不存在：{images_dir}，请创建images文件夹并放入图片")
                st.info("当前图片描述：" + images_desc)
        with col_desc:
            st.markdown(f"**{images_desc}**")
            st.markdown(f"第 {st.session_state.images_idx + 1} / {len(images_ua)} 张")

        # 上下一张按钮
        col_prev, _, col_next = st.columns([1, 3, 1])
        with col_prev:
            st.button("◀ 上一张", on_click=prev_images)
        with col_next:
            st.button("下一张 ▶", on_click=next_images)

    st.markdown('***')

    # 项目目标
    st.header("项目目标")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 🎯 目标一")
        st.markdown("**分析影响因素**")
        st.markdown('''- 建立学生成绩数据库
- 实现数据的高效管理
- 支持多种数据导入格式  
            ''')

    with col2:
        st.markdown("### 📈 目标二")
        st.markdown("**可视化展示**")
        st.markdown('''- 开发成绩分析算法
- 实现多维度分析
- 生成可视化报告
            ''')

    with col3:
        st.markdown("### 🎓 目标三")
        st.markdown("**成绩预测**")
        st.markdown('''- 构建预测模型
- 提高预测准确性
- 提供个性化建议''')

    st.markdown('***')

    # 技术架构
    st.header("技术架构")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("**前端框架**")
        st.code("""Streamlit""")

    with col2:
        st.markdown("**数据处理**")
        st.code("""Pandas
Numpy""")

    with col3:
        st.markdown("**可视化**")
        st.code("""Plotly
Express & Graph Objects""")

    with col4:
        st.markdown("**机器学习**")
        st.code("""Scikit-learn""")

    # 页脚
    st.markdown("---")
    st.markdown("© 2025 学生成绩分析与预测系统 | 技术支持：Streamlit团队 | 参与人员：PLY，SFY")

def data_analysis_page():
    # 获取CSV数据文件路径
    data_file = 'student_data_adjusted_rounded.csv'
    data_path = get_file_path(data_file)
    # 读取数据
    df = pd.read_csv(data_path)
    
    # 1. 各专业男女性别比例
    st.title("📊 专业数据分析")
    st.header("1. 各专业男女性别比例")

    # 创建两列布局：左侧图表，右侧数据表格
    col21, col22 = st.columns(2)
    with col21:
        # 按专业和性别分组计数
        gender_counts = df.groupby(['专业', '性别']).size().reset_index(name='人数')
        # 使用Plotly创建交互式柱状图
        fig = px.bar(
            gender_counts,
            x='专业',
            y='人数',
            color='性别',
            color_discrete_map={'男': '#1f77b4', '女': '#ff7f0e'},
            title='各专业男女性别比例',
            labels={'专业': '专业', '人数': '人数', '性别': '性别'},
            height=600
        )
        # 优化图表样式，兼容所有Plotly版本
        fig.update_layout(
            title_x=0.05,
            xaxis_tickangle=-45,
            xaxis_title_font=dict(size=14),
            yaxis_title_font=dict(size=14),
            font=dict(family="SimHei, Arial, sans-serif", size=12),
            margin=dict(l=50, r=50, t=80, b=80)
        )
        st.plotly_chart(fig, use_container_width=True)
        
    with col22:
        st.subheader("性别比例数据")
        # 重塑数据为透视表格式展示
        gender_pivot = df.groupby(['专业', '性别']).size().unstack(fill_value=0)
        st.dataframe(gender_pivot.T, use_container_width=True)

    # 2. 各专业学习指标对比
    st.header("2. 各专业学习指标对比")
    # 按专业分组计算平均值
    major_stats = df.groupby('专业').agg({
        '每周学习时长（小时）': 'mean',
        '期中考试分数': 'mean',
        '期末考试分数': 'mean'
    }).reset_index()
    # 重命名列名
    major_stats.columns = ['专业', '每周平均学时', '期中考试平均分', '期末考试平均分']

    col_21, col_22 = st.columns(2)
    with col_21:
        # 创建组合图表：柱状图（学习时间）+ 折线图（成绩）
        fig = go.Figure()

        # 添加平均学习时间柱状图
        fig.add_trace(go.Bar(
            x=major_stats['专业'],
            y=major_stats['每周平均学时'],
            name='平均学习时间',
            marker_color='#87CEFA',
            yaxis='y1'
        ))

        # 添加期中考试成绩折线图
        fig.add_trace(go.Scatter(
            x=major_stats['专业'],
            y=major_stats['期中考试平均分'],
            name='平均期中成绩',
            marker_color='#FFA500',
            mode='lines+markers',
            yaxis='y2'
        ))

        # 添加期末考试成绩折线图
        fig.add_trace(go.Scatter(
            x=major_stats['专业'],
            y=major_stats['期末考试平均分'],
            name='平均期末成绩',
            marker_color='#008000',
            mode='lines+markers',
            yaxis='y2'
        ))

        # 设置双Y轴，修复所有Plotly API兼容问题
        fig.update_layout(
            title='各专业平均学习时间与成绩对比',
            title_x=0.05,
            xaxis_tickangle=-45,
            xaxis_title='专业',
            yaxis=dict(
                title='平均学习时间（小时）',
                title_font=dict(color='#000000'),
                tickfont=dict(color='#000000'),
                side='left'
            ),
            yaxis2=dict(
                title='平均分数',
                title_font=dict(color='#000000'),
                tickfont=dict(color='#000000'),
                overlaying='y',
                side='right'
            ),
            legend=dict(
                x=0,
                y=1.15,
                orientation='h'  # 关键修复：将'horizontal'改为'h'，符合Plotly API规范
            ),
            height=600,
            font=dict(family="SimHei, Arial, sans-serif", size=12),
            margin=dict(l=50, r=50, t=80, b=80)
        )
        st.plotly_chart(fig, use_container_width=True)

    with col_22:
        st.subheader("详细数据")
        st.dataframe(major_stats, use_container_width=True)

    # 3. 各专业出勤率分析
    st.header("3. 各专业出勤率分析")
    # 按专业分组计算平均出勤率
    attendance_stats = df.groupby('专业')['上课出勤率'].mean().reset_index()
    # 转换为百分比格式（若原始数据是小数）
    if attendance_stats['上课出勤率'].max() <= 1:
        attendance_stats['上课出勤率'] = attendance_stats['上课出勤率'] * 100

    col_23, col_24 = st.columns(2)
    with col_23:
        # 使用Plotly创建渐变色柱状图
        fig = px.bar(
            attendance_stats,
            x='专业',
            y='上课出勤率',
            title='各专业出勤率对比',
            labels={'专业': '专业', '上课出勤率': '出勤率 (%)'},
            color='上课出勤率',
            color_continuous_scale=px.colors.sequential.Viridis,
            height=600
        )
        # 添加百分比标签，优化显示
        fig.update_traces(
            texttemplate='%{y:.1f}%',
            textposition='outside',
            textfont=dict(color='white', weight='bold', size=10)
        )
        # 优化样式
        fig.update_layout(
            title_x=0.05,
            xaxis_tickangle=-45,
            coloraxis_colorbar=dict(title='出勤率 (%)'),
            font=dict(family="SimHei, Arial, sans-serif", size=12),
            margin=dict(l=50, r=50, t=80, b=100)
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col_24:
        st.subheader("出勤率排名")
        # 排序出勤率数据
        attendance_sorted = attendance_stats.sort_values('上课出勤率', ascending=False).reset_index(drop=True)
        attendance_sorted = attendance_sorted[['专业', '上课出勤率']]
        st.dataframe(attendance_sorted, use_container_width=True)

    # 4. 大数据管理专业专项分析
    st.header("4. 大数据管理专业专项分析")
    # 筛选大数据管理专业
    big_data_major = df[df['专业'] == '大数据管理']
    
    # 处理空数据（避免无该专业数据时报错）
    if big_data_major.empty:
        st.warning("未找到大数据管理专业的相关数据！")
        return
    
    # 计算各项指标（若出勤率是小数则转换为百分比）
    attendance_col = '上课出勤率'
    if big_data_major[attendance_col].max() <= 1:
        avg_attendance = big_data_major[attendance_col].mean() * 100
    else:
        avg_attendance = big_data_major[attendance_col].mean()
    
    avg_final_score = big_data_major['期末考试分数'].mean()
    pass_rate = (big_data_major['期末考试分数'] >= 60).mean() * 100
    avg_study_time = big_data_major['每周学习时长（小时）'].mean()
    
    # 创建四列布局展示四个指标
    col_41, col_42, col_43, col_44 = st.columns(4)
    with col_41:
        st.markdown("**平均出勤率**")   
        st.markdown(f"## {avg_attendance:.1f}%")
    with col_42:
        st.markdown("**平均期末成绩**")   
        st.markdown(f"## {avg_final_score:.1f}分")
    with col_43:
        st.markdown("**及格率**")   
        st.markdown(f"## {pass_rate:.1f}%")
    with col_44:
        st.markdown("**平均学习时间**")   
        st.markdown(f"## {avg_study_time:.1f}小时")
     
    # 绘制成绩分布直方图（Plotly交互式版本）
    fig = px.histogram(
        big_data_major,
        x='期末考试分数',
        nbins=15,
        title='大数据管理专业期末考试成绩分布',
        labels={'期末考试分数': '期末考试分数', 'count': '人数'},
        color_discrete_sequence=['#4CAF50'],
        height=500
    )
    # 优化深色背景样式，兼容显示
    fig.update_layout(
        plot_bgcolor='#000000',
        paper_bgcolor='#000000',
        font=dict(color='#ffffff', family="SimHei, Arial, sans-serif"),
        xaxis_title_font=dict(color='#ffffff'),
        yaxis_title_font=dict(color='#ffffff'),
        xaxis_tickfont=dict(color='#ffffff'),
        yaxis_tickfont=dict(color='#ffffff'),
        title_font=dict(color='#ffffff', size=14),
        title_x=0.5,
        margin=dict(l=50, r=50, t=80, b=80)
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True)

def predict_page():
    st.markdown("## 🎲期末成绩预测")
    st.markdown("***")
    st.markdown("根据输入的学习数据，预测期末成绩")
    
    # 1. 读取CSV数据
    data_file = 'student_data_adjusted_rounded.csv'
    data_path = get_file_path(data_file)
    df = pd.read_csv(data_path)
    
    # 2. 数据预处理
    df_encoded = pd.get_dummies(df, columns=['性别', '专业'])
    # 定义特征和目标变量
    target_col = '期末考试分数'
    X = df_encoded.drop([target_col], axis=1) if target_col in df_encoded.columns else df_encoded
    
    # 3. 加载预训练模型
    model_file = 'student_data_adjusted_rounded.pkl'
    model_path = get_file_path(model_file)
    try:
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
    except Exception as e:
        st.error(f"加载模型失败！错误信息：{str(e)}")
        st.error("请确保模型文件是在当前scikit-learn版本下训练生成的！")
        st.stop()
    
    # 4. 用户输入表单
    st.markdown("### 请输入学生信息")
    with st.form("prediction_form"):
        col3_1, co3_2 = st.columns(2)
        with col3_1:
            student_id = st.text_input("学号")
            gender = st.selectbox("性别", options=['男', '女'])
            major = st.selectbox("专业", options=df['专业'].unique())
        with co3_2:
            weekly_study_time = st.slider('每周学习时长（小时）', 0.00, 40.00, value=10.00)
            attendance_rate = st.slider('上课出勤率', 0.0, 1.0, value=0.8)
            midterm_score = st.slider('期中考试分数', 0.00, 100.00, value=70.00)
            homework_completion = st.slider('作业完成率', 0.0, 1.0, value=0.8)
        
        submit_button = st.form_submit_button("开始预测")
    
    # 5. 预测逻辑
    if submit_button:
        # 输入验证
        if not student_id:
            st.error("请输入学号！")
            return
        try:
            student_id_int = int(student_id)
        except ValueError:
            st.error("学号必须为数字格式！")
            return
        
        # 构建用户输入特征
        user_input = {
            '学号': student_id_int,
            '每周学习时长（小时）': weekly_study_time,
            '上课出勤率': attendance_rate,
            '期中考试分数': midterm_score,
            '作业完成率': homework_completion
        }
        
        # 处理性别和专业的独热编码
        for col in X.columns:
            if col not in user_input:
                # 初始化未设置的特征为0
                user_input[col] = 0
                # 性别特征赋值
                if col.startswith('性别_'):
                    user_input[col] = 1 if col == f'性别_{gender}' else 0
                # 专业特征赋值
                if col.startswith('专业_'):
                    user_input[col] = 1 if col == f'专业_{major}' else 0
        
        # 转换为DataFrame（保证列顺序与训练数据一致）
        try:
            user_df = pd.DataFrame([user_input], columns=X.columns)
        except Exception as e:
            st.error(f"构建输入特征失败！错误信息：{str(e)}")
            st.info("请确认输入的信息与训练数据格式一致！")
            return
        
        # 进行预测
        try:
            prediction = model.predict(user_df)
            predicted_score = prediction[0]
            # 限制成绩范围在0-100之间，更合理
            predicted_score = max(0, min(100, predicted_score))
        except Exception as e:
            st.error(f"预测失败！错误信息：{str(e)}")
            st.info("请确认模型文件未损坏且与当前数据格式匹配！")
            return
        
        # 显示预测结果
        st.markdown("### 📊预测结果")
        st.markdown(f"**预测的期末成绩：** {predicted_score:.2f}")
        
        # 显示进度条（确保值在0-1之间）
        progress_value = min(max(predicted_score / 100, 0.0), 1.0)
        st.progress(progress_value)
        
        # 根据成绩显示提示
        if predicted_score >= 60:
            st.markdown("## 🎉 恭喜！预测您的期末考试将及格！")
            st.markdown("<div style='font-size: 100px; text-align: center;'>🎊</div>", unsafe_allow_html=True)
        else:
            st.markdown("## 💪 加油！再努力一下就能及格了！")
            st.markdown("<div style='font-size: 100px; text-align: center;'>📚</div>", unsafe_allow_html=True)

# 左边导航栏
nav = st.sidebar.radio("导航", ["项目介绍", "专业数据分析", "成绩预测"])

# 页面路由
if nav == "项目介绍":
    introduce_page()
elif nav == "专业数据分析":
    data_analysis_page()
elif nav == "成绩预测":
    predict_page()
