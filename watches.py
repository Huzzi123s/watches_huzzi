import streamlit as st
import os

# Get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Watches Data
watches = {
    "Rolex Submariner": {
        "image": os.path.join(current_dir, "watch1.jpeg"),
        "info": "A luxury diving watch with a timeless design.",
        "features": [
            "Water-resistant up to 300m", 
            "Automatic movement", 
            "Ceramic bezel", 
            "Stainless steel case"
        ]
    },
    "Omega Speedmaster": {
        "image": os.path.join(current_dir, "watch2.jpeg"),
        "info": "The first watch worn on the moon, known for its precision.",
        "features": [
            "Chronograph function", 
            "Manual winding", 
            "Hesalite crystal", 
            "Tachymeter scale"
        ]
    }
}

# App Title
st.title("Luxury Watches Showcase")

# Toggle Buttons for Watches  
toggle_rolex = st.toggle("Rolex Submariner")
toggle_omega = st.toggle("Omega Speedmaster")

# Function to Display Watch Details
def display_watch(watch_name):
    watch = watches[watch_name]
    # Check if image file exists
    if os.path.exists(watch["image"]):
        st.image(watch["image"], caption=watch_name, use_column_width=True)
    else:
        st.warning(f"Image file not found: {os.path.basename(watch['image'])}")

    st.write("**Description:**", watch["info"])
    st.write("**Features:**")
    st.write("\n".join([f"- {feature}" for feature in watch["features"]]))

# Display Rolex Submariner
if toggle_rolex:
    display_watch("Rolex Submariner")

# Display Omega Speedmaster
if toggle_omega:
    display_watch("Omega Speedmaster")
