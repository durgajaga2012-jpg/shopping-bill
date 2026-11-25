import streamlit as st

st.set_page_config(page_title="Shopping Bill", page_icon="🧾")
st.markdown("<style>.stApp{background:linear-gradient(135deg,#0f2027,#2c5364)} h1,h3,label{color:white!important} .box{background:rgba(255,255,255,.12);padding:20px;border-radius:15px;color:white} .bill{background:#fff;color:#000;padding:20px;border-radius:15px;font-family:monospace}</style>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align:center'>🧾 SMART SHOPPING BILL</h1>", unsafe_allow_html=True)

# Global Variable
SHOP_NAME = "MARISHA MART"

# Dictionary - Items & Price
items = {"Milk": 50, "Rice (5kg)": 350, "Oil": 220, "Shampoo": 299, "Shoes": 1200, "Watch": 2500, "Laptop Bag": 999}

# Functions
def subtotal(d): return sum(d.values())
def discount(s): return s*0.10 if s>3000 else s*0.05 if s>1000 else 0
def gst(s): return s*0.18
def show_scope():
    tax = 18 # Local Variable - only inside function
    return f"Global: {SHOP_NAME} | Local tax inside function: {tax}%"

# Lambda + map() + filter()
increased = dict(zip(items.keys(), map(lambda p: round(p*1.10,2), items.values())))
costly = dict(filter(lambda x: x[1]>500, items.items()))

# UI
st.markdown(f"<div class='box'><b>🏪 {SHOP_NAME}</b> | {show_scope()}<br><br>Select Items:</div>", unsafe_allow_html=True)
selected = {k: v for k,v in items.items() if st.checkbox(f"{k} - ₹{v}", value=True)}
col1, col2 = st.columns(2)
with col1: show_inc = st.checkbox("Show 10% Increased Price (map+lambda)")
with col2: show_costly = st.checkbox("Show Items > ₹500 (filter+lambda)")

if st.button("🧾 GENERATE BILL"):
    s = subtotal(selected); d = discount(s); g = gst(s-d); final = s-d+g
    bill = f"====== {SHOP_NAME} ======\n"
    for k,v in selected.items(): bill += f"{k:<15} ₹{v}\n"
    bill += f"----------------------\nSubtotal : ₹{s:.2f}\nDiscount : -₹{d:.2f}\nGST (18%): +₹{g:.2f}\n----------------------\nTOTAL    : ₹{final:.2f}\nThank You! Visit Again ❤️"
    st.markdown(f"<div class='bill'><pre>{bill}</pre></div>", unsafe_allow_html=True)
    st.success(f"Global Variable Used: {SHOP_NAME} | Local Variable 'tax' cannot be used outside function")

if show_inc: st.write("**After 10% Increase (map + lambda):**", increased)
if show_costly: st.write("**Items > ₹500 (filter + lambda):**", costly)