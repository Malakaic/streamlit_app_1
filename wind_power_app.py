import streamlit as st

# Title and Introduction
st.title("Basic Streamlit App")
st.write("This app calculates the power output of a wind turbine based on user inputs.")

# User Inputs
st.header("Input Parameters")
location = st.text_input("Enter the location:")
capacity = st.number_input("Enter turbine capacity (kW):", min_value=0.0, value=0.0)
wind_speed = st.number_input("Enter average wind speed (m/s):", min_value=0.0, value=0.0)

# Calculate Power Output
def calculate_power(capacity, wind_speed):
    # Example: Power calculation using a basic wind power formula
    air_density = 1.225  # Air density in kg/m³ at sea level
    swept_area = 100  # Example swept area in m² (can be user input or default value)
    power_coefficient = 0.4  # Efficiency coefficient (Betz's limit ~59%, use 40% for simplicity)
    # Power formula: P = 0.5 * air_density * swept_area * wind_speed^3 * power_coefficient
    power_output = 0.5 * air_density * swept_area * (wind_speed ** 3) * power_coefficient
    # Limit by capacity
    return min(power_output / 1000, capacity)  # Convert to kW and cap at turbine capacity

if st.button("Calculate"):
    if capacity > 0 and wind_speed > 0:
        result = calculate_power(capacity, wind_speed)
        st.success(f"Location: {location}")
        st.write(f"Wind Turbine Power Output: {result:.2f} kW")
    else:
        st.error("Please enter valid inputs for capacity and wind speed.")

# Download Results
if st.button("Download Results"):
    # Prepare data for download
    result = calculate_power(capacity, wind_speed)
    result_data = f"Location: {location}, Capacity: {capacity} kW, Wind Speed: {wind_speed} m/s, Power Output: {result:.2f} kW"
    st.download_button(
        label="Download Results",
        data=result_data,
        file_name="wind_power_results.txt",
        mime="text/plain"
    )
