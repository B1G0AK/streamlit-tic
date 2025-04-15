import streamlit as st

st.title("Foreign Flow Watch: Treasury TIC Dashboard")

st.markdown("""
Track foreign flows into U.S. Treasurys with live data signals.

- **Last TIC Release:** [TIC Data](https://home.treasury.gov/data/treasury-international-capital-tic-system)
- **Latest Month Analyzed:** February 2025
- **Next Expected Release:** Mid-May 2025
""")

st.header("Major Foreign Holders (Top 5)")
st.line_chart({
    'China': [1050, 1042, 1036, 1024],
    'Japan': [1150, 1147, 1143, 1138],
    'UK': [690, 715, 702, 698],
    'Luxembourg': [320, 324, 329, 335],
    'Cayman Islands': [280, 276, 272, 266]
})

st.header("Net Monthly Treasury Purchases")
st.bar_chart({
    'China': [-12.4],
    'Japan': [-2.1],
    'Cayman Islands': [-6.8],
    'UK': [-4.3],
    'Luxembourg': [+6.0]
})

st.header("Auction Participation – 10Y Benchmark")
st.markdown("""
- **Indirects:** 72% (↑ from 61%)
- **Primary Dealers:** 21%
- **Directs:** 7%
""")

st.header("Market Context")
st.markdown("""
- **MOVE Index:** 132  
- **DXY:** Holding ~103  
- **Signal:** Market is hedging the hell out of something. Watch for rollover pressure.
""")