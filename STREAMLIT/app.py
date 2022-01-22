import streamlit as st
import pickle
import numpy as np
import base64


model = pickle.load(open('RF_price_predicting_model.pkl','rb'))

def main():
  

    
    string = "Offical Release"
    st.set_page_config(page_title=string, page_icon="chart_with_upwards_trend")
    st.header("What's your chance of to get to forgein colleges ")
    st.markdown("##### Are you planning to go aborad !?\n##### So let's try evaluating the chance of you getting admit.. 🤖 ")
    st.image(
            "https://cdn.pixabay.com/photo/2017/09/08/00/37/friend-2727305_960_720.jpg",
            width=400, # Manually Adjust the width of the image as per requirement
        
        )
    st.sidebar.metric(label="Made By", value="Aditya Bhatt")
    st.sidebar.header("Linkdein")
    st.sidebar.subheader("https://www.linkedin.com/in/aditya-bhatt-92915a1b2/")
    st.sidebar.header("GitHub") 
    st.sidebar.subheader("https://github.com/aditya699")
    st.sidebar.header("Youtube")
    st.sidebar.subheader("https://www.youtube.com/channel/UCGKE__9Wmi0udQD5904NvCA")
    years = st.number_input('What is your GRE SCORE?',0, 340, step=1, key ='year')
    t_score= st.number_input('What is your TOEFL SCORE?',0, 120, step=1, key ='toefl score')
    rating= st.number_input('What is your UNIVERSITY RATING(1-5)?',0, 5, step=1, key ='university rating')
    rating1= st.number_input('What is your SOP RATING(1-5)?',0, 5, step=1, key ='sop rating')
    rating2= st.number_input('What is your LOR RATING(1-5)?',0, 5, step=1, key ='lor rating')
    rating3= st.number_input('What is your CGPA (1-10)?',0, 10, step=1, key ='cgpa rating')
    research=st.radio("Have you done and RESEARCH PREVIOUSLY ?", (0, 1) ,key='research')

    st.write('')
    st.write('')


    if st.button("Estmate your chance to get into universities", key='predict'):
        try:
            Model = model  #get_model()
            prediction = Model.predict([[years,t_score,rating,rating1,rating2,rating3,research]])
            output =np.round(prediction[0],2)
            if output<0:
                st.warning("You will be not get any colleges !!")
            else:
                st.success("You can get into forgein universities with a chance of {} % 🙌".format(output*100))
        except:
            st.warning("Opps!! Something went wrong\nTry again")



if __name__ == '__main__':
    main()
