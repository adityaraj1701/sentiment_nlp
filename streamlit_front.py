import streamlit as st
import pickle

st.image("https://growtraffic-bc85.kxcdn.com/blog/wp-content/uploads/2019/01/Amazon-5-Star-Review-Illustration.jpg")    
model = pickle.load(open("sample_data.pkl", "rb"))
def predict(sentence):
    prediction = model.predict([sentence])
    if prediction[0]==1:
        return "Positive"
    elif prediction[0]==0:
        return "Negative"
    #return prediction[0]

def main():
    # Title and description
    #set_bg_image("C:\\Users\\ankus\\OneDrive\\Desktop\\Screenshots\\Screenshot 2024-03-23 154721.png")
    st.title("Understand the emotions behind the Amazon reviews!!")
    # Text input field
    sentence = st.text_input("Enter your sentence:")

    # Button to trigger prediction
    if st.button("Predict"):
        if sentence:
            prediction = predict(sentence)  
            st.write(f"Predicted Sentiment: {prediction}")
        else:
            st.error("Please enter a sentence.")

if __name__ == "__main__":
    main()
