import streamlit as st
import sqlite3
import pandas as pd

st.title("Food Wastage Management System")
conn = sqlite3.connect("food_waste.db")

# ── FILTERS ──
st.subheader("🔍 Filter Food Donations")
col1, col2, col3 = st.columns(3)
city = col1.selectbox("City", ["All"] + pd.read_sql("SELECT DISTINCT Location FROM food_listings", conn)["Location"].tolist())
provider = col2.selectbox("Provider", ["All"] + pd.read_sql("SELECT DISTINCT Name FROM food_providers", conn)["Name"].tolist())
food_type = col3.selectbox("Food Type", ["All"] + pd.read_sql("SELECT DISTINCT Food_Type FROM food_listings", conn)["Food_Type"].tolist())

q = "SELECT f.*, p.Name AS Provider FROM food_listings f JOIN food_providers p ON f.Provider_ID = p.Provider_ID WHERE 1=1"
params = []
if city != "All": q += " AND f.Location=?"; params.append(city)
if provider != "All": q += " AND p.Name=?"; params.append(provider)
if food_type != "All": q += " AND f.Food_Type=?"; params.append(food_type)
st.dataframe(pd.read_sql(q, conn, params=params))

# ── CONTACTS ──
st.subheader("📞 Contacts")
tab1, tab2 = st.tabs(["Providers", "Receivers"])
tab1.dataframe(pd.read_sql("SELECT * FROM food_providers", conn))
tab2.dataframe(pd.read_sql("SELECT * FROM food_receivers", conn))

# ── CRUD ──
st.subheader("⚙️ Manage Food Listings")
op = st.selectbox("Operation", ["Add", "Update", "Delete"])

if op == "Add":
    name = st.text_input("Food Name")
    qty = st.number_input("Quantity", min_value=1)
    exp = st.date_input("Expiry Date")
    pid = st.number_input("Provider ID", min_value=1)
    ptype = st.text_input("Provider Type")
    loc = st.text_input("Location")
    ftype = st.text_input("Food Type")
    mtype = st.text_input("Meal Type")
    if st.button("Add"):
        if not all([name, loc, ftype, mtype]):
            st.error("Fill in all fields.")
        else:
            conn.execute("INSERT INTO food_listings (Food_Name,Quantity,Expiry_Date,Provider_ID,Provider_Type,Location,Food_Type,Meal_Type) VALUES (?,?,?,?,?,?,?,?)",
                         (name, qty, str(exp), pid, ptype, loc, ftype, mtype))
            conn.commit(); st.success("Added!")

elif op == "Update":
    fid = st.number_input("Food ID", min_value=1)
    qty = st.number_input("New Quantity", min_value=1)
    if st.button("Update"):
        cur = conn.execute("UPDATE food_listings SET Quantity=? WHERE Food_ID=?", (qty, fid))
        conn.commit()
        st.success("Updated!") if cur.rowcount else st.warning("ID not found.")

elif op == "Delete":
    fid = st.number_input("Food ID", min_value=1)
    if st.checkbox("Confirm delete") and st.button("Delete"):
        cur = conn.execute("DELETE FROM food_listings WHERE Food_ID=?", (fid,))
        conn.commit()
        st.success("Deleted!") if cur.rowcount else st.warning("ID not found.")


st.subheader("SQL Query Results")

query = st.selectbox(
    "Choose a question",
    (
        "Q1: Total Food Available",
        "Q2: Providers per City",
        "Q3: Receivers per City",
        "Q4: Provider-wise Total Food Donated",
        "Q5: Average Food Provided by Each Provider",
        "Q6: City with Highest Food Listings",
        "Q7: Most Common Food Type",
        "Q8: Claims per Food Item",
        "Q9: Provider with Most Claims",
        "Q10: Average Food Claimed per Receiver",
        "Q11: Most Claimed Meal Type",
        "Q12: City with Highest Claims",
        "Q13: Food Type Claimed the Most",
        "Q14: Receiver Type vs Food Type Preference",
        "Q15: Provider-wise Average Donation"
    )
)

if query == "Q1: Total Food Available":
    q1_df = pd.read_sql("""
        SELECT SUM(Quantity) AS total_food_available
        FROM food_listings
    """, conn)
    st.dataframe(q1_df)

if query == "Q2: Providers per City":
    q2_df = pd.read_sql("""
        SELECT City, COUNT(*) AS provider_count
        FROM food_providers
        GROUP BY City
    """, conn)
    st.dataframe(q2_df)

if query == "Q3: Receivers per City":
    df = pd.read_sql("""
        SELECT City, COUNT(*) AS receiver_count
        FROM food_receivers
        GROUP BY City
    """, conn)
    st.dataframe(df)

if query == "Q4: Provider-wise Total Food Donated":
    df = pd.read_sql("""
        SELECT p.Name, SUM(f.Quantity) AS total_food
        FROM food_listings f
        JOIN food_providers p
        ON f.Provider_ID = p.Provider_ID
        GROUP BY p.Name
    """, conn)
    st.dataframe(df)

if query == "Q5: Average Food Provided by Each Provider":
    df = pd.read_sql("""
        SELECT p.Name, AVG(f.Quantity) AS avg_food
        FROM food_listings f
        JOIN food_providers p
        ON f.Provider_ID = p.Provider_ID
        GROUP BY p.Name
    """, conn)
    st.dataframe(df)

if query == "Q6: City with Highest Food Listings":
    df = pd.read_sql("""
        SELECT Location, COUNT(*) AS listing_count
        FROM food_listings
        GROUP BY Location
        ORDER BY listing_count DESC
        LIMIT 1
    """, conn)
    st.dataframe(df)

if query == "Q7: Most Common Food Type":
    df = pd.read_sql("""
        SELECT Food_Type, COUNT(*) AS count
        FROM food_listings
        GROUP BY Food_Type
        ORDER BY count DESC
    """, conn)
    st.dataframe(df)

if query == "Q8: Claims per Food Item":
    df = pd.read_sql("""
        SELECT f.Food_Name, COUNT(c.Claim_ID) AS total_claims
        FROM claims c
        JOIN food_listings f
        ON c.Food_ID = f.Food_ID
        GROUP BY f.Food_Name
    """, conn)
    st.dataframe(df)

if query == "Q9: Provider with Most Claims":
    df = pd.read_sql("""
        SELECT p.Name, COUNT(c.Claim_ID) AS claim_count
        FROM claims c
        JOIN food_listings f
        ON c.Food_ID = f.Food_ID
        JOIN food_providers p
        ON f.Provider_ID = p.Provider_ID
        GROUP BY p.Name
        ORDER BY claim_count DESC
        LIMIT 1
    """, conn)
    st.dataframe(df)

if query == "Q10: Average Food Claimed per Receiver":
    df = pd.read_sql("""
        SELECT r.Name, AVG(f.Quantity) AS avg_quantity
        FROM claims c
        JOIN food_listings f
        ON c.Food_ID = f.Food_ID
        JOIN food_receivers r
        ON c.Receiver_ID = r.Receiver_ID
        GROUP BY r.Name
    """, conn)
    st.dataframe(df)

if query == "Q11: Most Claimed Meal Type":
    df = pd.read_sql("""
        SELECT f.Meal_Type, COUNT(*) AS claim_count
        FROM claims c
        JOIN food_listings f
        ON c.Food_ID = f.Food_ID
        GROUP BY f.Meal_Type
        ORDER BY claim_count DESC
    """, conn)
    st.dataframe(df)

if query == "Q12: City with Highest Claims":
    df = pd.read_sql("""
        SELECT f.Location, COUNT(*) AS total_claims
        FROM claims c
        JOIN food_listings f
        ON c.Food_ID = f.Food_ID
        GROUP BY f.Location
        ORDER BY total_claims DESC
        LIMIT 1
    """, conn)
    st.dataframe(df)

if query == "Q13: Food Type Claimed the Most":
    df = pd.read_sql("""
        SELECT f.Food_Type, COUNT(*) AS total_claims
        FROM claims c
        JOIN food_listings f
        ON c.Food_ID = f.Food_ID
        GROUP BY f.Food_Type
        ORDER BY total_claims DESC
        LIMIT 1
    """, conn)
    st.dataframe(df)

if query == "Q14: Receiver Type vs Food Type Preference":
    df = pd.read_sql("""
        SELECT r.Type AS receiver_type,
               f.Food_Type,
               COUNT(*) AS claims_count
        FROM claims c
        JOIN food_listings f
        ON c.Food_ID = f.Food_ID
        JOIN food_receivers r
        ON c.Receiver_ID = r.Receiver_ID
        GROUP BY r.Type, f.Food_Type
        ORDER BY claims_count DESC
    """, conn)
    st.dataframe(df)

if query == "Q15: Provider-wise Average Donation":
    df = pd.read_sql("""
        SELECT p.Name, AVG(f.Quantity) AS avg_donation
        FROM food_listings f
        JOIN food_providers p
        ON f.Provider_ID = p.Provider_ID
        GROUP BY p.Name
    """, conn)
    st.dataframe(df)

# ── ANALYSIS ──
st.subheader("📈 Analysis")

st.markdown("**Top Providers**")
df = pd.read_sql("SELECT p.Name, SUM(f.Quantity) AS total FROM food_listings f JOIN food_providers p ON f.Provider_ID=p.Provider_ID GROUP BY p.Name ORDER BY total DESC LIMIT 5", conn)
st.dataframe(df); st.bar_chart(df.set_index("Name"))

st.markdown("**Highest Demand Locations**")
df = pd.read_sql("SELECT f.Location, COUNT(c.Claim_ID) AS claims FROM claims c JOIN food_listings f ON c.Food_ID=f.Food_ID GROUP BY f.Location ORDER BY claims DESC", conn)
st.dataframe(df); st.bar_chart(df.set_index("Location"))

st.markdown("**Food Wastage Trends**")
df = pd.read_sql("SELECT f.Food_Name, f.Quantity, COUNT(c.Claim_ID) AS claimed, (f.Quantity - COUNT(c.Claim_ID)) AS unclaimed FROM food_listings f LEFT JOIN claims c ON f.Food_ID=c.Food_ID GROUP BY f.Food_ID ORDER BY unclaimed DESC LIMIT 10", conn)
st.dataframe(df); st.bar_chart(df.set_index("Food_Name")["unclaimed"])

conn.close()