import streamlit as st
import sqlite3
import pandas as pd

st.title("Food Wastage Management System")

# Connect to SQLite database
conn = sqlite3.connect("food_waste.db")

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

#Q1: Total Food Available
if query == "Q1: Total Food Available":
    q1_df = pd.read_sql("""
        SELECT SUM(Quantity) AS total_food_available
        FROM food_listings
    """, conn)
    st.dataframe(q1_df)

#Q2: Providers per City
if query == "Q2: Providers per City":
    q2_df = pd.read_sql("""
        SELECT City, COUNT(*) AS provider_count
        FROM food_providers
        GROUP BY City
    """, conn)
    st.dataframe(q2_df)

#Q3: Receivers per City
if query == "Q3: Receivers per City":
    df = pd.read_sql("""
        SELECT City, COUNT(*) AS receiver_count
        FROM food_receivers
        GROUP BY City
    """, conn)
    st.dataframe(df)

#Q4: Provider-wise Total Food Donated
if query == "Q4: Provider-wise Total Food Donated":
    df = pd.read_sql("""
        SELECT p.Name, SUM(f.Quantity) AS total_food
        FROM food_listings f
        JOIN food_providers p
        ON f.Provider_ID = p.Provider_ID
        GROUP BY p.Name
    """, conn)
    st.dataframe(df)


#Q5: Average Food Provided by Each Provider
if query == "Q5: Average Food Provided by Each Provider":
    df = pd.read_sql("""
        SELECT p.Name, AVG(f.Quantity) AS avg_food
        FROM food_listings f
        JOIN food_providers p
        ON f.Provider_ID = p.Provider_ID
        GROUP BY p.Name
    """, conn)
    st.dataframe(df)

#Q6: City with Highest Food Listings
if query == "Q6: City with Highest Food Listings":
    df = pd.read_sql("""
        SELECT Location, COUNT(*) AS listing_count
        FROM food_listings
        GROUP BY Location
        ORDER BY listing_count DESC
        LIMIT 1
    """, conn)
    st.dataframe(df)
       
        
#Q7: Most Common Food Type
if query == "Q7: Most Common Food Type":
    df = pd.read_sql("""
        SELECT Food_Type, COUNT(*) AS count
        FROM food_listings
        GROUP BY Food_Type
        ORDER BY count DESC
    """, conn)
    st.dataframe(df)

 
#Q8: Claims per Food Item
if query == "Q8: Claims per Food Item":
    df = pd.read_sql("""
        SELECT f.Food_Name, COUNT(c.Claim_ID) AS total_claims
        FROM claims c
        JOIN food_listings f
        ON c.Food_ID = f.Food_ID
        GROUP BY f.Food_Name
    """, conn)
    st.dataframe(df)

#Q9: Provider with Most Claims
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

#Q10: Average Food Claimed per Receiver
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

#Q11: Most Claimed Meal Type
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

#Q12: City with Highest Claims
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

#Q13: Food Type Claimed the Most
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

#Q14: Receiver Type vs Food Type Preference
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



#Q15: Provider-wise Average Donation
if query == "Q15: Provider-wise Average Donation":
    df = pd.read_sql("""
        SELECT p.Name, AVG(f.Quantity) AS avg_donation
        FROM food_listings f
        JOIN food_providers p
        ON f.Provider_ID = p.Provider_ID
        GROUP BY p.Name
    """, conn)
    st.dataframe(df)
