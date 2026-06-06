import streamlit as st
import math
import statistics as stats

st.set_page_config(
    page_title="Scientific Calculator",
    page_icon="🧮",
    layout="wide"
)

# ---------- CSS ----------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg,#ff7b00,#ffb347);
}
.title {
    text-align:center;
    font-size:50px;
    font-weight:bold;
    color:white;
    padding:20px;
    border-radius:20px;
    background:linear-gradient(90deg,#000000,#333333);
}
.result {
    background:white;
    padding:20px;
    border-radius:15px;
    font-size:30px;
    text-align:center;
    font-weight:bold;
    box-shadow:0px 4px 10px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🧮 Ultimate Scientific Calculator</div>', unsafe_allow_html=True)

tab1, tab2 = st.tabs(["🔬 Scientific Calculator", "📊 Statistics"])

# ---------------- SCIENTIFIC ----------------
with tab1:

    st.subheader("Scientific Operations")

    col1, col2 = st.columns(2)

    with col1:
        num1 = st.number_input("First Number", value=0.0)

    with col2:
        num2 = st.number_input("Second Number", value=0.0)

    operation = st.selectbox(
        "Choose Operation",
        [
            "Add",
            "Subtract",
            "Multiply",
            "Divide",
            "Power",
            "Square Root (1st Number)",
            "Sin",
            "Cos",
            "Tan",
            "Log10",
            "Natural Log"
        ]
    )

    if st.button("Calculate 🚀"):

        try:

            if operation == "Add":
                result = num1 + num2

            elif operation == "Subtract":
                result = num1 - num2

            elif operation == "Multiply":
                result = num1 * num2

            elif operation == "Divide":
                result = "Cannot divide by zero" if num2 == 0 else num1 / num2

            elif operation == "Power":
                result = num1 ** num2

            elif operation == "Square Root (1st Number)":
                result = math.sqrt(num1)

            elif operation == "Sin":
                result = math.sin(math.radians(num1))

            elif operation == "Cos":
                result = math.cos(math.radians(num1))

            elif operation == "Tan":
                result = math.tan(math.radians(num1))

            elif operation == "Log10":
                result = math.log10(num1)

            elif operation == "Natural Log":
                result = math.log(num1)

            st.markdown(
                f'<div class="result">Result: {result}</div>',
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"Error: {e}")

# ---------------- STATISTICS ----------------
with tab2:

    st.subheader("Statistics Calculator")

    data = st.text_input(
        "Enter numbers separated by commas",
        "10,20,30,40,50"
    )

    if st.button("Analyze Data 📈"):

        try:

            numbers = [float(x.strip()) for x in data.split(",")]

            mean_value = stats.mean(numbers)
            median_value = stats.median(numbers)

            try:
                mode_value = stats.mode(numbers)
            except:
                mode_value = "No unique mode"

            range_value = max(numbers) - min(numbers)

            variance_value = stats.variance(numbers) if len(numbers) > 1 else 0
            stdev_value = stats.stdev(numbers) if len(numbers) > 1 else 0

            st.success("Analysis Complete!")

            c1, c2, c3 = st.columns(3)

            c1.metric("Mean", round(mean_value, 4))
            c2.metric("Median", round(median_value, 4))
            c3.metric("Mode", mode_value)

            c4, c5, c6 = st.columns(3)

            c4.metric("Range", round(range_value, 4))
            c5.metric("Variance", round(variance_value, 4))
            c6.metric("Std Dev", round(stdev_value, 4))

        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.markdown(
    "<center><h3>🔥 Orange & Black Scientific Calculator 🔥</h3></center>",
    unsafe_allow_html=True
)
