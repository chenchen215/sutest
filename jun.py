import streamlit as st

# 页面配置
st.set_page_config(page_title="个人简历生成器", page_icon="🎨", layout="wide")

# 标题与描述
st.markdown("<h1 style='color: white; font-size: 2.5em;'>🎨 个人简历生成器</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #888; font-size: 0.9em;'>使用Streamlit创建您的个性化简历</p>", unsafe_allow_html=True)

# 分栏布局：左侧表单，右侧预览
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("## 个人信息表单")

    # 姓名
    name = st.text_input("姓名", placeholder="请输入您的姓名")

    # 职位
    position = st.text_input("职位", placeholder="如：软件工程师、产品经理等")

    # 电话
    phone = st.text_input("电话", placeholder="请输入手机号码")

    # 邮箱
    email = st.text_input("邮箱", placeholder="请输入邮箱地址")

    # 出生日期
    birth_date = st.date_input("出生日期", value=None)

    # 性别
    gender = st.radio("性别", ["男", "女", "其他"], index=0)

    # 学历
    education = st.selectbox("学历", ["高中", "大专", "本科", "硕士", "博士"])

    # 语言能力
    language = st.selectbox("语言能力", ["中文", "英语", "日语", "法语", "德语", "其他"], index=0)

    # 技能（多选）
    skills = st.multiselect("技能（可多选）", [
        "Python", "Java", "JavaScript", "HTML/CSS", "React", "Vue", 
        "SQL", "数据分析", "机器学习", "项目管理", "沟通表达"
    ])

    # 工作经验（滑块）
    work_experience = st.slider("工作经验（年）", min_value=0, max_value=30, value=0, step=1)

    # 期望薪资范围（双滑块）
    salary_min, salary_max = st.slider(
        "期望薪资范围（元）",
        min_value=5000,
        max_value=50000,
        value=(10000, 20000),
        step=1000
    )

    # 个人简介
    bio = st.text_area("个人简介", placeholder="请简要介绍您的专业背景、职业目标和个人特点...", height=150)

    # 最佳联系时间段
    contact_time = st.selectbox("每日最佳联系时间段", [
        "08:00 - 12:00", "14:00 - 18:00", "19:00 - 22:00", "全天均可"
    ])

    # 上传头像
    uploaded_file = st.file_uploader("上传个人照片", type=["jpg", "jpeg", "png"], accept_multiple_files=False)

with col2:
    st.markdown("## 简历实时预览")

    # 信息展示区域
    st.markdown("---")
    if name:
        st.markdown(f"<h3 style='color: black;'>{name}</h3>", unsafe_allow_html=True)
    else:
        st.markdown("<h3 style='color: black;'>姓名未填写</h3>", unsafe_allow_html=True)
    
    # ========== 头像预览 - 放在职位上方 ==========
    if uploaded_file is not None:
        st.image(uploaded_file, width=150)  # 仅保留 width 参数
    
    # 基本信息（分列显示）
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f"**职位:** {position or '未填写'}")
        st.markdown(f"**电话:** {phone or '未填写'}")
        st.markdown(f"**邮箱:** {email or '未填写'}")
        st.markdown(f"**出生日期:** {birth_date.strftime('%Y/%m/%d') if birth_date else '未填写'}")
    with col_b:
        st.markdown(f"**性别:** {gender}")
        st.markdown(f"**学历:** {education}")
        st.markdown(f"**工作经验:** {work_experience}年")
        st.markdown(f"**期望薪资:** {salary_min}-{salary_max}元")
        st.markdown(f"**最佳联系时间:** {contact_time}")

    # 语言能力
    st.markdown(f"**语言能力:** {language}")

    # 技能
    if skills:
        st.markdown("**技能:** " + ", ".join(skills))
    else:
        st.markdown("**技能:** 未填写")

    # 个人简介
    st.markdown("---")
    st.markdown("## 个人简介")
    if bio.strip():
        st.markdown(bio)
    else:
        st.markdown("这个人很神秘，没有留下任何介绍...")
