import streamlit as st
def task():
    
    taskbox = st.selectbox("功能", ("上传", "下载", "记录"))
    if taskbox == '上传':
        st.subheader("上传你需要检测的图片")

    elif taskbox == '下载':
        st.subheader("下载")
    elif taskbox == '记录':
        st.subheader("记录")

    return taskbox


def main():
    # st.title("欢迎使用垃圾分类系统，请登录")
    menu = ("主页", "登录", "注册")
    choice = st.sidebar.selectbox("菜单", menu)

    if choice == "主页":
        st.subheader("主页")  # 功能介绍

    elif choice == "登录":
        st.subheader("登录")

        username = st.sidebar.text_input("账号")  # 输入
        password = st.sidebar.text_input("密码", type='password')
        if st.sidebar.button("登录"):
            if password == '12345':
                st.success("作为 {} 登录".format(username))
                task()

            else:
                st.warning("账号或密码错误！")

    elif choice == "注册":
        st.subheader("注册新的账号")
        new_user = st.text_input("账号")
        new_password = st.text_input("密码", type='password')
        if st.button("注册"):
            st.success("你已经成功注册了新的账号")
            st.info("请到登录菜单进行登录")


if __name__ == '__main__':
    main()

