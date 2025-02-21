import streamlit as st

# Define sushi plate prices
plate_prices = {
    "Red": 40, "Blue": 50, "Green": 60, "Yellow": 70,
    "Brown": 80, "Pink": 90, "Light Brown": 100, "White": 120,
    "Dark Red": 140, "Dark Blue": 160, "Black": 180
}

# Initialize session state to store plate counts
if "plate_count" not in st.session_state:
    st.session_state.plate_count = {plate: 0 for plate in plate_prices}
    st.session_state.ordered_plates = []

# Function to add a plate
def add_plate(plate):
    st.session_state.plate_count[plate] += 1
    st.session_state.ordered_plates.append(plate)

# Function to remove the last added plate
def remove_plate():
    if st.session_state.ordered_plates:
        last_plate = st.session_state.ordered_plates.pop()
        st.session_state.plate_count[last_plate] -= 1

# App title
st.title("🍣 Conveyor Belt Sushi Calculator")

# Display buttons for each plate color
cols = st.columns(4)  # Arrange buttons in 4 columns
for idx, (plate, price) in enumerate(plate_prices.items()):
    with cols[idx % 4]:
        if st.button(f"{plate} ({price} THB)", key=plate):
            add_plate(plate)

# Remove plate button
st.button("🗑️ Remove Last Plate", on_click=remove_plate)

# Calculate total price
total_price = sum(plate_prices[plate] for plate in st.session_state.ordered_plates)
service_charge = total_price * 0.10
final_price = total_price + service_charge

# Display results
st.subheader("📝 Order Summary")
for plate, count in st.session_state.plate_count.items():
    if count > 0:
        st.write(f"**{plate}**: {count} plate(s)")

st.subheader("💰 Total Price")
st.write(f"Subtotal: **{total_price} THB**")
st.write(f"Service Charge (10%): **{service_charge:.2f} THB**")
st.write(f"Final Price: **{final_price:.2f} THB**")
