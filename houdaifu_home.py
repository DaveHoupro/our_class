import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区'])

def page1():
    #文字
    st.write("这是子家老师的兴趣推荐页")
    #图片
    st.image("sss.jpg")
    #音频
    st.audio("懒得取名.mp3")
    #视频
    st.video("aaa.mp4")

def page2():
    st.write(":sunglasses:图片换色小程序:rose:")
    file_uploaded = st.file_uploader("图片上传",type=["png","jpg","jpeg"])
    if file_uploaded:
        tab1,tab2,tab3= st.tabs(["原图","改色1","旋转90度"])
        img = Image.open(file_uploaded)
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,2,1,0))
        with tab3:
            st.image(img.rotate(90))

def img_change(img,rc,gc,bc):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img
# def img_rotate(img):
#     img.rotate(90)
#     return img
def page3():
    
    with open("words_space.txt","r",encoding="utf-8") as f:
        words_list = f.read().split("\n")

    for i in range(len(words_list)):
        words_list[i] = words_list[i].split("#")

    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]


    with open("check_out_times.txt","r",encoding="utf-8") as f:
        times_list = f.read().split("\n")

    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")

    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])



    
    word = st.text_input("请输入您想查询的单词：")
    if word in words_dict:
        st.write(words_dict[word])
        
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1

        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)


        
        st.write("单词的查询次数为：",times_dict[n])
        

        if word == "python":
            st.code('''
                    # 恭喜你出发彩蛋
                    print("Hello,python")''')
        if word == "houdaifu":
            st.snow()
            st.image("yiyi.jpg")
        

def page4():
    with open("leave_messages.txt","r",encoding="utf-8") as f:
        messages_list = f.read().split("\n")

    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split("#")
        
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
                
    name = st.selectbox('我是……', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)


if page == '我的兴趣推荐':
    page1()
elif page == '我的图片处理工具':
    page2()
elif page == '我的智能词典':
    page3()
elif page == '我的留言区':
    page4()