import streamlit as st

st.write("Hello World: Getting Bore, Hello Brother!!")
st.title("Display Title use st.title()")
st.write("To write text use st.write()")
st.header("I am header to write header use st.header()")
st.subheader("I am subheader to write subheader use st.subheader()")
st.text("Hey I am simple text to write simple text use st.text")
# to create hyperlink
st.markdown("[Streamlit](https://streamlit.io/)")
st.markdown("[Streamlit Cheatsheet](https://cheat-sheet.streamlit.io/)")
st.info("Information")
st.success("SUCCESS!")
st.warning("This is a warning")
st.error("This is an error!!")

from PIL import Image
img=Image.open("smj.jpg")
st.image(img, width=300, caption="Satyamev Jayate")

video_file = open("vid.mp4","rb")
video_bytes = video_file.read()
st.video(video_bytes)

st.video("https://www.youtube.com/watch?v=2v8urSwf8TI")

audio_file = open("song.mp3","rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")

st.button("Play")
st.header("Button Widgets")

if st.button("Play1"):
    st.text("HELLO WORLD")
    
if st.button("Play2"):
    st.text("Enjoy Music")    
    st.video("https://www.youtube.com/watch?v=HRiCRmPYAl8")
    
if st.checkbox("Checkbox"):
    st.text("Checkbox Selected")
    
 