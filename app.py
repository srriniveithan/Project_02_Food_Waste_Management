# # import streamlit as st
# # import sqlite3
# # import pandas as pd

# # st.title("Food Wastage Management System")

# # # Connect to SQLite database
# # conn = sqlite3.connect("food_waste.db")

# # st.subheader("SQL Query Results")

# # query = st.selectbox(
# #     "Choose a question",
# #     (
# #         "Q1: Total Food Available",
# #         "Q2: Providers per City",
# #         "Q3: Receivers per City",
# #         "Q4: Provider-wise Total Food Donated",
# #         "Q5: Average Food Provided by Each Provider",
# #         "Q6: City with Highest Food Listings",
# #         "Q7: Most Common Food Type",
# #         "Q8: Claims per Food Item",
# #         "Q9: Provider with Most Claims",
# #         "Q10: Average Food Claimed per Receiver",
# #         "Q11: Most Claimed Meal Type",
# #         "Q12: City with Highest Claims",
# #         "Q13: Food Type Claimed the Most",
# #         "Q14: Receiver Type vs Food Type Preference",
# #         "Q15: Provider-wise Average Donation"
# #     )
# # )

# # #Q1: Total Food Available
# # if query == "Q1: Total Food Available":
# #     q1_df = pd.read_sql("""
# #         SELECT SUM(Quantity) AS total_food_available
# #         FROM food_listings
# #     """, conn)
# #     st.dataframe(q1_df)

# # #Q2: Providers per City
# # if query == "Q2: Providers per City":
# #     q2_df = pd.read_sql("""
# #         SELECT City, COUNT(*) AS provider_count
# #         FROM food_providers
# #         GROUP BY City
# #     """, conn)
# #     st.dataframe(q2_df)

# # #Q3: Receivers per City
# # if query == "Q3: Receivers per City":
# #     df = pd.read_sql("""
# #         SELECT City, COUNT(*) AS receiver_count
# #         FROM food_receivers
# #         GROUP BY City
# #     """, conn)
# #     st.dataframe(df)

# # #Q4: Provider-wise Total Food Donated
# # if query == "Q4: Provider-wise Total Food Donated":
# #     df = pd.read_sql("""
# #         SELECT p.Name, SUM(f.Quantity) AS total_food
# #         FROM food_listings f
# #         JOIN food_providers p
# #         ON f.Provider_ID = p.Provider_ID
# #         GROUP BY p.Name
# #     """, conn)
# #     st.dataframe(df)


# # #Q5: Average Food Provided by Each Provider
# # if query == "Q5: Average Food Provided by Each Provider":
# #     df = pd.read_sql("""
# #         SELECT p.Name, AVG(f.Quantity) AS avg_food
# #         FROM food_listings f
# #         JOIN food_providers p
# #         ON f.Provider_ID = p.Provider_ID
# #         GROUP BY p.Name
# #     """, conn)
# #     st.dataframe(df)

# # #Q6: City with Highest Food Listings
# # if query == "Q6: City with Highest Food Listings":
# #     df = pd.read_sql("""
# #         SELECT Location, COUNT(*) AS listing_count
# #         FROM food_listings
# #         GROUP BY Location
# #         ORDER BY listing_count DESC
# #         LIMIT 1
# #     """, conn)
# #     st.dataframe(df)
       
        
# # #Q7: Most Common Food Type
# # if query == "Q7: Most Common Food Type":
# #     df = pd.read_sql("""
# #         SELECT Food_Type, COUNT(*) AS count
# #         FROM food_listings
# #         GROUP BY Food_Type
# #         ORDER BY count DESC
# #     """, conn)
# #     st.dataframe(df)

 
# # #Q8: Claims per Food Item
# # if query == "Q8: Claims per Food Item":
# #     df = pd.read_sql("""
# #         SELECT f.Food_Name, COUNT(c.Claim_ID) AS total_claims
# #         FROM claims c
# #         JOIN food_listings f
# #         ON c.Food_ID = f.Food_ID
# #         GROUP BY f.Food_Name
# #     """, conn)
# #     st.dataframe(df)

# # #Q9: Provider with Most Claims
# # if query == "Q9: Provider with Most Claims":
# #     df = pd.read_sql("""
# #         SELECT p.Name, COUNT(c.Claim_ID) AS claim_count
# #         FROM claims c
# #         JOIN food_listings f
# #         ON c.Food_ID = f.Food_ID
# #         JOIN food_providers p
# #         ON f.Provider_ID = p.Provider_ID
# #         GROUP BY p.Name
# #         ORDER BY claim_count DESC
# #         LIMIT 1
# #     """, conn)
# #     st.dataframe(df)

# # #Q10: Average Food Claimed per Receiver
# # if query == "Q10: Average Food Claimed per Receiver":
# #     df = pd.read_sql("""
# #         SELECT r.Name, AVG(f.Quantity) AS avg_quantity
# #         FROM claims c
# #         JOIN food_listings f
# #         ON c.Food_ID = f.Food_ID
# #         JOIN food_receivers r
# #         ON c.Receiver_ID = r.Receiver_ID
# #         GROUP BY r.Name
# #     """, conn)
# #     st.dataframe(df)

# # #Q11: Most Claimed Meal Type
# # if query == "Q11: Most Claimed Meal Type":
# #     df = pd.read_sql("""
# #         SELECT f.Meal_Type, COUNT(*) AS claim_count
# #         FROM claims c
# #         JOIN food_listings f
# #         ON c.Food_ID = f.Food_ID
# #         GROUP BY f.Meal_Type
# #         ORDER BY claim_count DESC
# #     """, conn)
# #     st.dataframe(df)

# # #Q12: City with Highest Claims
# # if query == "Q12: City with Highest Claims":
# #     df = pd.read_sql("""
# #         SELECT f.Location, COUNT(*) AS total_claims
# #         FROM claims c
# #         JOIN food_listings f
# #         ON c.Food_ID = f.Food_ID
# #         GROUP BY f.Location
# #         ORDER BY total_claims DESC
# #         LIMIT 1
# #     """, conn)
# #     st.dataframe(df)

# # #Q13: Food Type Claimed the Most
# # if query == "Q13: Food Type Claimed the Most":
# #     df = pd.read_sql("""
# #         SELECT f.Food_Type, COUNT(*) AS total_claims
# #         FROM claims c
# #         JOIN food_listings f
# #         ON c.Food_ID = f.Food_ID
# #         GROUP BY f.Food_Type
# #         ORDER BY total_claims DESC
# #         LIMIT 1
# #     """, conn)
# #     st.dataframe(df)

# # #Q14: Receiver Type vs Food Type Preference
# # if query == "Q14: Receiver Type vs Food Type Preference":
# #     df = pd.read_sql("""
# #         SELECT r.Type AS receiver_type,
# #                f.Food_Type,
# #                COUNT(*) AS claims_count
# #         FROM claims c
# #         JOIN food_listings f
# #         ON c.Food_ID = f.Food_ID
# #         JOIN food_receivers r
# #         ON c.Receiver_ID = r.Receiver_ID
# #         GROUP BY r.Type, f.Food_Type
# #         ORDER BY claims_count DESC
# #     """, conn)
# #     st.dataframe(df)



# # #Q15: Provider-wise Average Donation
# # if query == "Q15: Provider-wise Average Donation":
# #     df = pd.read_sql("""
# #         SELECT p.Name, AVG(f.Quantity) AS avg_donation
# #         FROM food_listings f
# #         JOIN food_providers p
# #         ON f.Provider_ID = p.Provider_ID
# #         GROUP BY p.Name
# #     """, conn)
# #     st.dataframe(df)

# # conn.close()


# import streamlit as st
# import sqlite3
# import pandas as pd

# st.set_page_config(page_title="Food Wastage Management System", layout="wide")

# st.title("Food Wastage Management System")

# # Connect to SQLite database
# conn = sqlite3.connect("food_waste.db")

# # Sidebar Navigation
# menu = st.sidebar.selectbox(
#     "Navigation",
#     ["SQL Analysis", "Filter Food Donations", "Manage Food (CRUD)", "Contact Directory"]
# )

# # ==========================================================
# # 1️⃣ SQL ANALYSIS SECTION (Your Original Queries Preserved)
# # ==========================================================

# if menu == "SQL Analysis":

#     st.subheader("SQL Query Results")

#     query = st.selectbox(
#         "Choose a question",
#         (
#             "Q1: Total Food Available",
#             "Q2: Providers per City",
#             "Q3: Receivers per City",
#             "Q4: Provider-wise Total Food Donated",
#             "Q5: Average Food Provided by Each Provider",
#             "Q6: City with Highest Food Listings",
#             "Q7: Most Common Food Type",
#             "Q8: Claims per Food Item",
#             "Q9: Provider with Most Claims",
#             "Q10: Average Food Claimed per Receiver",
#             "Q11: Most Claimed Meal Type",
#             "Q12: City with Highest Claims",
#             "Q13: Food Type Claimed the Most",
#             "Q14: Receiver Type vs Food Type Preference",
#             "Q15: Provider-wise Average Donation"
#         )
#     )

#     df = None

#     if query == "Q1: Total Food Available":
#         df = pd.read_sql("SELECT SUM(Quantity) AS total_food_available FROM food_listings", conn)

#     elif query == "Q2: Providers per City":
#         df = pd.read_sql("SELECT City, COUNT(*) AS provider_count FROM food_providers GROUP BY City", conn)

#     elif query == "Q3: Receivers per City":
#         df = pd.read_sql("SELECT City, COUNT(*) AS receiver_count FROM food_receivers GROUP BY City", conn)

#     elif query == "Q4: Provider-wise Total Food Donated":
#         df = pd.read_sql("""
#             SELECT p.Name, SUM(f.Quantity) AS total_food
#             FROM food_listings f
#             JOIN food_providers p ON f.Provider_ID = p.Provider_ID
#             GROUP BY p.Name
#         """, conn)

#     elif query == "Q5: Average Food Provided by Each Provider":
#         df = pd.read_sql("""
#             SELECT p.Name, AVG(f.Quantity) AS avg_food
#             FROM food_listings f
#             JOIN food_providers p ON f.Provider_ID = p.Provider_ID
#             GROUP BY p.Name
#         """, conn)

#     elif query == "Q6: City with Highest Food Listings":
#         df = pd.read_sql("""
#             SELECT Location, COUNT(*) AS listing_count
#             FROM food_listings
#             GROUP BY Location
#             ORDER BY listing_count DESC
#             LIMIT 1
#         """, conn)

#     elif query == "Q7: Most Common Food Type":
#         df = pd.read_sql("""
#             SELECT Food_Type, COUNT(*) AS count
#             FROM food_listings
#             GROUP BY Food_Type
#             ORDER BY count DESC
#         """, conn)

#     elif query == "Q8: Claims per Food Item":
#         df = pd.read_sql("""
#             SELECT f.Food_Name, COUNT(c.Claim_ID) AS total_claims
#             FROM claims c
#             JOIN food_listings f ON c.Food_ID = f.Food_ID
#             GROUP BY f.Food_Name
#         """, conn)

#     elif query == "Q9: Provider with Most Claims":
#         df = pd.read_sql("""
#             SELECT p.Name, COUNT(c.Claim_ID) AS claim_count
#             FROM claims c
#             JOIN food_listings f ON c.Food_ID = f.Food_ID
#             JOIN food_providers p ON f.Provider_ID = p.Provider_ID
#             GROUP BY p.Name
#             ORDER BY claim_count DESC
#             LIMIT 1
#         """, conn)

#     elif query == "Q10: Average Food Claimed per Receiver":
#         df = pd.read_sql("""
#             SELECT r.Name, AVG(f.Quantity) AS avg_quantity
#             FROM claims c
#             JOIN food_listings f ON c.Food_ID = f.Food_ID
#             JOIN food_receivers r ON c.Receiver_ID = r.Receiver_ID
#             GROUP BY r.Name
#         """, conn)

#     elif query == "Q11: Most Claimed Meal Type":
#         df = pd.read_sql("""
#             SELECT f.Meal_Type, COUNT(*) AS claim_count
#             FROM claims c
#             JOIN food_listings f ON c.Food_ID = f.Food_ID
#             GROUP BY f.Meal_Type
#             ORDER BY claim_count DESC
#         """, conn)

#     elif query == "Q12: City with Highest Claims":
#         df = pd.read_sql("""
#             SELECT f.Location, COUNT(*) AS total_claims
#             FROM claims c
#             JOIN food_listings f ON c.Food_ID = f.Food_ID
#             GROUP BY f.Location
#             ORDER BY total_claims DESC
#             LIMIT 1
#         """, conn)

#     elif query == "Q13: Food Type Claimed the Most":
#         df = pd.read_sql("""
#             SELECT f.Food_Type, COUNT(*) AS total_claims
#             FROM claims c
#             JOIN food_listings f ON c.Food_ID = f.Food_ID
#             GROUP BY f.Food_Type
#             ORDER BY total_claims DESC
#             LIMIT 1
#         """, conn)

#     elif query == "Q14: Receiver Type vs Food Type Preference":
#         df = pd.read_sql("""
#             SELECT r.Type AS receiver_type, f.Food_Type, COUNT(*) AS claims_count
#             FROM claims c
#             JOIN food_listings f ON c.Food_ID = f.Food_ID
#             JOIN food_receivers r ON c.Receiver_ID = r.Receiver_ID
#             GROUP BY r.Type, f.Food_Type
#             ORDER BY claims_count DESC
#         """, conn)

#     elif query == "Q15: Provider-wise Average Donation":
#         df = pd.read_sql("""
#             SELECT p.Name, AVG(f.Quantity) AS avg_donation
#             FROM food_listings f
#             JOIN food_providers p ON f.Provider_ID = p.Provider_ID
#             GROUP BY p.Name
#         """, conn)

#     if df is not None:
#         st.dataframe(df)
#         if len(df.columns) == 2:
#             st.bar_chart(df.set_index(df.columns[0]))


# # ==========================================================
# # 2️⃣ FILTER FOOD DONATIONS
# # ==========================================================

# elif menu == "Filter Food Donations":

#     st.subheader("Filter Food Listings")

#     city_list = pd.read_sql("SELECT DISTINCT Location FROM food_listings", conn)["Location"]
#     food_type_list = pd.read_sql("SELECT DISTINCT Food_Type FROM food_listings", conn)["Food_Type"]

#     selected_city = st.selectbox("Select City", city_list)
#     selected_food_type = st.selectbox("Select Food Type", food_type_list)

#     filtered_df = pd.read_sql("""
#         SELECT Food_Name, Quantity, Expiry_Date, Location, Food_Type
#         FROM food_listings
#         WHERE Location = ? AND Food_Type = ?
#     """, conn, params=(selected_city, selected_food_type))

#     st.dataframe(filtered_df)


# # ==========================================================
# # 3️⃣ CRUD OPERATIONS
# # ==========================================================

# elif menu == "Manage Food (CRUD)":

#     st.subheader("Manage Food Listings")

#     operation = st.selectbox("Choose Operation", ["Add", "Update Quantity", "Delete"])

#     if operation == "Add":
#         food_name = st.text_input("Food Name")
#         quantity = st.number_input("Quantity", min_value=1)
#         expiry_date = st.date_input("Expiry Date")
#         provider_id = st.number_input("Provider ID", min_value=1)
#         provider_type = st.text_input("Provider Type")
#         location = st.text_input("Location")
#         food_type = st.text_input("Food Type")
#         meal_type = st.text_input("Meal Type")

#         if st.button("Add Food"):
#             conn.execute("""
#                 INSERT INTO food_listings 
#                 (Food_Name, Quantity, Expiry_Date, Provider_ID, Provider_Type, Location, Food_Type, Meal_Type)
#                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#             """, (food_name, quantity, expiry_date, provider_id, provider_type, location, food_type, meal_type))
#             conn.commit()
#             st.success("Food Added Successfully!")

#     elif operation == "Update Quantity":
#         food_id = st.number_input("Food ID", min_value=1)
#         new_quantity = st.number_input("New Quantity", min_value=1)

#         if st.button("Update"):
#             conn.execute("UPDATE food_listings SET Quantity=? WHERE Food_ID=?", (new_quantity, food_id))
#             conn.commit()
#             st.success("Updated Successfully!")

#     elif operation == "Delete":
#         food_id = st.number_input("Food ID", min_value=1)

#         if st.button("Delete"):
#             conn.execute("DELETE FROM food_listings WHERE Food_ID=?", (food_id,))
#             conn.commit()
#             st.success("Deleted Successfully!")


# # ==========================================================
# # 4️⃣ CONTACT DIRECTORY
# # ==========================================================

# elif menu == "Contact Directory":

#     st.subheader("Food Providers Contact")
#     providers = pd.read_sql("SELECT Name, City, Contact FROM food_providers", conn)
#     st.dataframe(providers)

#     st.subheader("Food Receivers Contact")
#     receivers = pd.read_sql("SELECT Name, City, Contact FROM food_receivers", conn)
#     st.dataframe(receivers)


# conn.close()

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

# ── QUERIES (UNCHANGED) ──
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