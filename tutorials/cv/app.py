import streamlit as st
import ultralytics
import PIL.Image as Image

# Load the YOLOv8 model
if st.session_state.get('model') is None:
    st.session_state['model'] = ultralytics.YOLO('models/best.pt')

# Set the title of the app
st.title("Rock Paper Scissors Detector")

# Upload an image from webcam or file
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image
    image = Image.open(uploaded_file)
    
    # Display the image
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Run inference
    results = st.session_state['model'](image)

    # # Display results
    # st.write("Detection Results:")
    # st.write(results)

    # Display bounding boxes on the image
    try:
        annotated_image = results[0].plot()
        st.image(annotated_image, caption='Annotated Image', use_column_width=True)
    except Exception as e:
        st.write("Error in plotting results:", e)

# Add a footer
st.write("Made with ❤️ by Your Duke Hackathon Organizers")
