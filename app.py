# IMPROVEMTS
# Faster plot rendering DONE
# More Graph rendering ways DONE
# More network parameters: Centrality
# One more standard plot

import os
import streamlit as st
# import and libraries
import base64
import pandas as pd

st.set_page_config(page_title='Network analysis', layout='wide',
                   initial_sidebar_state='auto')

st.markdown(
    """
    <style>
    .logo-text {
        font-weight:700 !important;
        font-size:50px !important;
        float: right;
        margin-right: 13rem;
    }
    .stApp {
        # background-color: #EA5455;
        # background-color: aliceblue;
        # background-image: linear-gradient(to bottom right, #FEB692, #EA5455);
        background-image: linear-gradient(to bottom right, #ABCDFF, #0396FF);
    }
    .css-18e3th9 {
        width: 70%;
        padding: 2rem;
        text-align: center;
    }
    .css-17z2rne  {
        color: #000000;
    }
    .link {
        text-decoration: none !important;
        color: #fff !important;
        border-radius: 0.25rem;
        padding: 5px;
        background-color: black;
    }
    a.link:hover {
        color: #f00 !important;
        border: 1px solid #f00;
    }
    .intro {
        text-align: justify;
        color: black;
    }
    .stDataFrame {
        background-color: #71458c;
    }

    .css-v37k9u {
        color: black;
    }
    .css-ltfnpr {
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" width="140px" height="140px" src="data:image/png;base64,{base64.b64encode(open("assets/logo_0.png", "rb").read()).decode()}">
        <h1 class="logo-text"">RV College of Engineering<br><h5><small>(Autonomous Institution Affiliated to Visvesvaraya Technological University, Belagavi)</small></h5></h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("DEPARTMENT OF MASTER OF COMPUTER APPLICATIONS  \nBengaluru- 560059")


st.markdown("""<hr>""",
            unsafe_allow_html=True)


# proportions of values in non numeric

all_files = os.listdir("./analysis")
csv_files = list(filter(lambda f: f.endswith('.csv'), all_files))

for col in csv_files:
    st.write(f"Summary of {col} column")
    df = pd.read_csv("./analysis/" + col)
    st.dataframe(df)
    print('\n')

# histogram
st.image("./analysis/hist.png")

# # correlation matrix

st.image("./analysis/correlation_matrix.png")

# Network Graph
st.image("./analysis/Graph (3).png", caption="Kamada Kawai Graph model")
st.write("Force-directed graph algorithms are a class of algorithms for visual graph alignment. Their purpose is to position the nodes of a graph in two-dimensional or three-dimensional space so that all the edges are of more or less equal length and there are as few crossing edges as possible, by assigning forces among the set of edges and the set of nodes, based on their relative positions, and then using these forces either to simulate the motion of the edges and nodes or to minimize their energy.")
st.write("The Kamada-Kawai method assumes that the n vertices in an on-screen graph are connected by springs. The graph becomes a dynamical system that tries to reach a minimum-energy state, where springs are, as much as possible, not stretched or compressed overmuch from their “relaxed-state length”.")
