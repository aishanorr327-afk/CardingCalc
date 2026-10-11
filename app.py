
import streamlit as st

st.set_page_config(page_title="CardingCalc", page_icon="🧵")

st.title("🧵 CardingCalc")
st.subheader("Carding Calculations for Textile Engineering")

st.write("Calculate cylinder surface speed, feed lap linear density, draft and theoretical production.")

st.header("1. Cylinder Surface Speed")

diameter = st.number_input("Cylinder diameter (m)", min_value=0.01, value=1.0)
rpm = st.number_input("Cylinder speed (RPM)", min_value=0.0, value=300.0)

speed = 3.14159 * diameter * rpm

st.write(f"Cylinder surface speed = {speed:.2f} m/min")

st.header("2. Feed Lap Linear Density")

weight = st.number_input("Lap weight (g)", min_value=0.0, value=500.0)
length = st.number_input("Lap length (m)", min_value=0.01, value=10.0)

linear_density = weight / length

st.write(f"Linear density = {linear_density:.2f} g/m")

st.header("3. Draft Calculation")

input_density = st.number_input("Input linear density (g/m)", min_value=0.01, value=5.0)
output_density = st.number_input("Output linear density (g/m)", min_value=0.01, value=0.2)

draft = input_density / output_density

st.write(f"Draft = {draft:.2f}")

st.info("Educational calculations only. Check your course formulas and units before using results.")


