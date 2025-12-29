import streamlit as st
import pickle
import pandas as pd

# ------------- 左侧侧边栏导航 -------------
st.sidebar.title("导航")
# 侧边栏单选框（实现“简介”“预测医疗费用”切换）
nav_option = st.sidebar.radio(
    "",  # 单选框标题留空，更贴合截图样式
    ["简介", "预测医疗费用"],
    index=0  # 默认选中“简介”
)


# ------------- 简介页面内容 -------------
if nav_option == "简介":
    st.header("欢迎使用")
    st.subheader("医疗费用预测应用")
    st.write("这个应用利用机器学习模型来预测医疗费用，为保险公司的保险定价提供参考。")
    
    st.subheader("背景介绍")
    st.markdown("""
    - 开发目标: 帮助保险公司合理定价保险产品，控制风险
    - 模型算法: 利用随机森林回归算法训练医疗费用预测模型
    """)
    
    st.subheader("使用指南")
    st.markdown("""
    - 输入准确完整的被保险人信息，可以得到更准确的费用预测
    - 预测结果可以作为保险定价的重要参考，但需谨慎决策
    - 有任何问题欢迎联系我们的技术支持
    """)
    st.write("技术支持：📧 support@example.com")


# ------------- 预测医疗费用页面内容 -------------
elif nav_option == "预测医疗费用":
    st.header("使用说明")
    st.write("这个应用利用机器学习模型来预测医疗费用，为保险公司的保险定价提供参考。")
    st.markdown("""
    - 输入信息: 在下面输入被保险人的个人信息、疾病信息等
    - 费用预测: 应用会预测被保险人的未来医疗费用支出
    """)

    # 表单部分
    with st.form('user_inputs'):
        age = st.number_input('年龄', min_value=0)
        sex = st.radio('性别', ['男性', '女性'])
        bmi = st.number_input('BMI', min_value=0.0)
        children = st.number_input("子女数量：", step=1, min_value=0)
        smoke = st.radio("是否吸烟", ("是", "否"))
        region = st.selectbox('区域', ('东南部', '西南部', '东北部', '西北部'))
        submitted = st.form_submit_button('预测费用')

    if submitted:
        # 数据预处理（独热编码对应）
        sex_female = 1 if sex == '女性' else 0
        sex_male = 1 if sex == '男性' else 0
        smoke_yes = 1 if smoke == '是' else 0
        smoke_no = 1 if smoke == '否' else 0
        
        region_northeast = 1 if region == '东北部' else 0
        region_southeast = 1 if region == '东南部' else 0
        region_northwest = 1 if region == '西北部' else 0
        region_southwest = 1 if region == '西南部' else 0

        # 构造特征数据
        format_data = [
            age, bmi, children, sex_female, sex_male,
            smoke_no, smoke_yes,
            region_northeast, region_southeast, region_northwest, region_southwest
        ]

        # 加载模型并预测（添加异常处理，避免应用崩溃）
        try:
            with open('rfr_model.pkl', 'rb') as f:
                rfr_model = pickle.load(f)
            
            # 构造DataFrame并预测
            format_data_df = pd.DataFrame([format_data], columns=rfr_model.feature_names_in_)
            predict_result = rfr_model.predict(format_data_df)[0]
            
            # 显示预测结果
            st.success(f'根据您输入的数据，预测该客户的医疗费用是：{round(predict_result, 2)}')
        
        except FileNotFoundError:
            # 处理模型文件不存在的情况
            st.error("错误：未找到rfr_model.pkl模型文件，请确认文件已放在当前目录下！")
        except pickle.UnpicklingError:
            # 处理模型文件损坏的情况
            st.error("错误：rfr_model.pkl模型文件损坏或格式不正确，无法加载！")
        except Exception as e:
            # 处理其他未知异常
            st.error(f"未知错误：{str(e)}")
