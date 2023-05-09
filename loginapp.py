import streamlit as st
def main():

# 登录状态管理
is_logged_in = st.checkbox("登录")

# 改变状态的按钮
if st.button("切换登录状态"):
    is_logged_in = not is_logged_in

# 根据登录状态显示不同的内容
if is_logged_in:
    st.write("您已登录")
else:
    st.write("您未登录")


if __name__ == '__main__':
    main()

