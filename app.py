from streamlit_option_menu import option_menu
from tokenize import Imagnumber
import streamlit as st
from PIL import Image
from bokeh.models.widgets import Div
import streamlit as st
import plotly.graph_objects as go

img=Image.open("a.gif")
st.set_page_config(page_title="DEEP SEO",page_icon=img,layout="centered")

# st.set_page_config(
#     page_title="Quick reference", # => Quick reference - Streamlit
#     page_icon="🐍",
#     layout="centered", # wide
#     initial_sidebar_state="auto") # collapsed

EXAMPLE_NO = 3

def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Our service", "Contact"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Our service", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Our service", "About us"],  # required
            icons=["house", "search", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected

selected = streamlit_menu(example=EXAMPLE_NO)

if selected == "Our service":

    st.title("What is SEO 🦾 ")

    """
    Search engine optimization (SEO) is the process of improving the quality and quantity of website traffic to a website or a web page from search engines.
    SEO targets unpaid traffic (known as "natural" or "organic" results) rather than direct traffic or paid traffic.
    Unpaid traffic may originate from different kinds of searches, including image search, video search, academic search,news search, and industry-specific vertical search engines.
    As an Internet marketing strategy, SEO considers how search engines work, the computer-programmed algorithms that dictate search engine behavior, what people search for, the actual search terms or keywords typed into search engines, and which search engines are preferred by their targeted audience.
    SEO is performed because a website will receive more visitors from a search engine when websites rank higher on the search engine results page (SERP).
    These visitors can then potentially be converted into customers.
    Immediately see which product listings need improvement.
    Get recommendations for changing your product title, bullet points, description and Seller Central backend search terms.
    """

    st.title("What is the issue 🧐 ")

    """
    An amazon seller wants to evaluate the quality of the landing pages of their products.
    Very cost to rely on experts or use their intuition.
    """
    st.title("Brainstorming 🧠")

    """
    If seller knows in advance whether their product will sell well or not allows sellers to revise their plans before the launch.
    """

    st.title("Our goal 🥅")

    """
    Developing a deep learning model that uses current data from similar products to evaluate the quality for a new product landing page in Amazon.
    Low cost solution to improve the chances of selling based on search results in relation to the rest of the competitors so they can appear in the results when a client looks for a product.
    """

    st.title("Solution overview 🤲")

    """
    Seller provides the information they have for a landing page
    The data goes through the model that classifies the product
    Seller gets an evaluation on the “searchability” of the product compared with similar products
    """


if selected == "About us":

    st.title("")

    original_title = '<p style="font-family:serif; color:Black; font-size: 25px;"> 🌼 Cristobal Cepeda</p>'
    st.markdown(original_title, unsafe_allow_html=True)

    def linkedin_url(name,a):
        if st.button(f"{name}'s LinkedIn"):
            js = "window.open(a)"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

    def github_url(name, b):
        if st.button(f"{name}'s GitHub"):
            js = "window.open(b)"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)

    linkedin_url("Cris","https://www.linkedin.com/in/crist%C3%B3bal-cepeda-lagos/?locale=en_US")

    github_url("Cris","https://github.com/Cris-CL/deep_seo")

    st.write("")


    original_title = '<p style="font-family:serif; color:Black; font-size: 25px;"> 🌼 Elizabeth Kok</p>'
    st.markdown(original_title, unsafe_allow_html=True)

    linkedin_url("Elizabeth","www.linkedin.com/in/elizabeth-kok-9407331b6")

    github_url("Elizabeth","https://github.com/Elizabeth-kok")

    st.write("")

    original_title = '<p style="font-family:serif; color:Black; font-size: 25px;"> 🌼 Kim Nayoung</p>'
    st.markdown(original_title, unsafe_allow_html=True)

    linkedin_url("Nayoung","www.linkedin.com/in/nayoung-kim-0589a8240")

    github_url("Nayoung","https://github.com/na0young124")

if selected == "Home":
    '''
    # DEEP SEO
    '''
    st.markdown('''
    Fill in the details for your product.
    ''')

    title = st.text_input('Title')
    # st.write('Title', title)

    description = st.text_input('Description')
    # st.write('Description ', description)

    feature = st.text_input('Feature')
    # st.write('Features ', features)

    image_input1 = st.text_input('Image Link 1')
    if st.button('Show image 1'):
        # print is visible in the server output, not in the page
        if image_input1=="":
            st.write("Please input your image URL")
        else:
            try:
                st.image(image_input1, caption='Your Amazon Product Picture', use_column_width=False,width=200)
            except:
                st.write("Please input a correct image URL")

    image_input2 = st.text_input('Image Link 2')
    if st.button('Show image 2'):
        # print is visible in the server output, not in the page
        if image_input2=="":
            st.write("Please input your image URL")
        else:
            try:
                st.image(image_input2, caption='Your Amazon Product Picture', use_column_width=False,width=200)
            except:
                st.write("Please input a correct image URL")

    image_input3 = st.text_input('Image Link 3')
    if st.button('Show image 3'):
        # print is visible in the server output, not in the page
        if image_input3=="":
            st.write("Please input your image URL")
        else:
            try:
                st.image(image_input3, caption='Your Amazon Product Picture', use_column_width=False,width=200)
            except:
                st.write("Please input a correct image URL")

    data={'title': title,
        'description': description,
        'feature': feature,
        'imageone': image_input1,
        'imagetwo': image_input2,
        'imagethree': image_input3}

    url = 'https://deepseofourth-5ost5gg5jq-ew.a.run.app/seo_eval'
    urll="?title=" + data.get("title") + " &description=" + data.get("description") + "&feature=" + data.get("feature") + "&imageone=" + data.get("imageone") + "&imagetwo="+ data.get("imagetwo")+"&imagethree="+ data.get("imagethree")
    new_url=url + urll
# /seo_eval?title=fake title for a fake product &description=this description is awesome&feature=I have no features&imageone=https://cdn-image02.casetify.com/usr/4787/34787/~v3/22690451x2_iphone13_16003249.png.1000x1000-w.m80.jpg&imagetwo=https://m.media-amazon.com/images/I/81MLO3k15iL._AC_SL1500_.jpg&imagethree=https://m.media-amazon.com/images/I/71HiwDwAcoL._AC_SL1500_.jpg

    # import requests
    # x= requests.get(new_url)
    # print (x.json()["Classification"])

    # value_rank = 11 - 1 - int(x.json()["Classification"])
    def image_graphic(val_rank):

        def color_rank(rank):
            if rank > 0 and rank < 6:
                return 'red'
            elif rank > 5 and rank <8:
                return 'orange'
            return 'green'

        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = val_rank,
            gauge = {'axis': {'range': [1, 10]},
                        'bar': {'color':color_rank(val_rank)},
                        'threshold': {'line': {'color': "black", 'width': 5},
                                    'thickness': 1,
                                    'value': val_rank}},
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Listing rating"}))

        fig.update_layout( autosize=False, width=300, height=300, margin=dict(l=40, r=40, b=40, t=40))

        return st.plotly_chart(fig)

    def imageranking(a):
        if a=='rankone':
            st.write("10/10!! Perfect image!")
        elif a=='ranktwo':
            st.write("9/10! Good image!")
        elif a=='rankthree':
            st.write("8/10! This image is really good!")
        elif a=='rankfour':
            st.write("7/10! This image is good enough.")
        elif a=='rankfive':
            st.write("6/10! This image is fine ~")
        elif a=='ranksix':
            st.write("5/10 Average image.")
        elif a=='rankseven':
            st.write("4/10 This image is alright. Try again!")
        elif a=='rankeight':
            st.write("3/10 🥲 Try looking for better quality image")
        elif a=='ranknine':
            st.write("2/10 🥲 You might want to try other image.")
        else:
            st.write("1/10 🙈 This is not a good image. Please check if you input the correct image URL.")


    '''
    ↘️ Click "Submit" to get your product ranking
    '''
    if st.button('Submit'):
        # print is visible in the server output, not in the page
        import requests
        x= requests.get(new_url)
        a=x.json()["Classification"]
        b=x.json()["Rank Image 1"]
        c=x.json()["Rank Image 2"]
        d=x.json()["Rank Image 3"]
        st.write("## Your text result is :")
        if a=="1":
            st.write("10/10! You have all the perfect words for your product!")
        elif a=="2":
            st.write("9/10! Awesome!!")
        elif a=="3":
            st.write("8/10! Amazing!!")
        elif a=="4":
            st.write("7/10! Good enough!")
        elif a=="5":
            st.write("6/10! Great!")
        elif a=="6":
            st.write("5/10 Not bad!")
        elif a=="7":
            st.write("4/10 You can do better than this!")
        elif a=="8":
            st.write("3/10 🥲 Try harder!!")
        elif a=="9":
            st.write("2/10 🥲 Try harder!!!!")
        else:
            st.write("1/10 You got the lowest score 🙈 Try again!")

        st.write("## Image 1's result :")
        imageranking(b)
        st.write("## Image 2's result :")
        imageranking(c)
        st.write("## Image 3's result :")
        imageranking(d)


        def overall_rating(a_1,b_1,c_1,d_1):
            img_rating = {'rankone':10,
                        'ranktwo':9,
                        'rankthree':8,
                        'rankfour':7,
                        'rankfive':6,
                        'ranksix':5,
                        'rankseven':4,
                        'rankeight':3,
                        'ranknine':2,
                        'rankten':1}
            im_sum = img_rating.get(b_1) + img_rating.get(c_1) + img_rating.get(d_1)
            img_avg = 0.3*(im_sum) / 3
            txt_rat = 0.7*(11-int(a_1))
            overall = img_avg + txt_rat
            return overall

        overall = overall_rating(a,b,c,d)



        st.write(f"## Your product's info overall rating is {overall}")

        image_graphic(overall)






        # st.write(x.json()["Classification"])
        # st.write(x.json()["Rank Image 1"])
        # st.write(x.json()["Rank Image 2"])
        # st.write(x.json()["Rank Image 3"])

# url = 'https://deepseofirst-5ost5gg5jq-ew.a.run.app/seo_eval'
# urll="?title=" + data.get("title") + "&description=" + data.get("description") + "&feature=" + data.get("feature") + "&imageone=" + data.get("imageone") + "&imagetwo="+ data.get("imagetwo")+"&imagethree="+ data.get("imagethree")

# """
# data={'title': "fake title for a fake product",
#     'description': "this description is awesome",
#     'feature': "I have no features",
#     'imageone': "https://cdn-image02.casetify.com/usr/4787/34787/~v3/22690451x2_iphone13_16003249.png.1000x1000-w.m80.jpg",
#     'imagetwo': "https://m.media-amazon.com/images/I/81MLO3k15iL._AC_SL1500_.jpg",
#     'imagethree': "https://m.media-amazon.com/images/I/71HiwDwAcoL._AC_SL1500_.jpg"}

# url = 'https://deepseosecond-5ost5gg5jq-ew.a.run.app/seo_eval'
# secondurl="https://deepseosecond-5ost5gg5jq-ew.a.run.app/seo_eval"
# urll="?title=fake title for a fake product &description=this description is awesome&feature=I have no features&imageone=https://cdn-image02.casetify.com/usr/4787/34787/~v3/22690451x2_iphone13_16003249.png.1000x1000-w.m80.jpg&imagetwo=https://m.media-amazon.com/images/I/81MLO3k15iL._AC_SL1500_.jpg&imagethree=https://m.media-amazon.com/images/I/71HiwDwAcoL._AC_SL1500_.jpg"

# urlll="?title=" + data.get("title") + " &description=" + data.get("description") + "&feature=" + data.get("feature") + "&imageone=" + data.get("imageone") + "&imagetwo="+ data.get("imagetwo")+"&imagethree="+ data.get("imagethree")


# fullurl= url+urll
# print(fullurl)

# dict_fullurl= secondurl+urlll
# print(dict_fullurl)

# import requests
# x= requests.get(dict_fullurl)

# print("---------------------------------")
# print (x)

# print("---------------------------------")
# print (x.json())

# print("---------------------------------")
# print (x.json()["Classification"])


# # st.write('Best Selling product ever! :D')
# # st.write(x.json()["Classification"])
# # st.write(x.json()["Rank Image 1"])
# # st.write(x.json()["Rank Image 2"])
# # st.write(x.json()["Rank Image 3"])

# # <Response [200]>
# # ---------------------------------
# # {'Classification': '10', 'Rank Image 1': 'rankten', 'Rank Image 2': 'rankfive', 'Rank Image 3': 'rankseven'}

# """
